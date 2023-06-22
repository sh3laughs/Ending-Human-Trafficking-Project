# DSO110 - Data Science Final Project
  # File 6-F
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported suicides are more likely to 
  # be found for age brackets where there are higher rates of arrests for human 
  # trafficking crimes

# H0: Arrests for trafficking crimes do not predict suicides within the same 
  # age bracket
# H1: Arrests for trafficking crimes do predict suicides within the same age 
  # bracket

# IV's:
  # Trafficking crime arrests
  # Age
# DV: Suicides


# Import packages ----
library(dplyr)
library(ggplot2)
library(IDPmisc)
library(predictmeans)


# Import and preview data ----
crimeSuicide_2013to2021 = read.csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/crimeSuicide_2013to2021.csv')

View(crimeSuicide_2013to2021)
# 3,021 entries, 43 total columns
  # Sample size is validated for now...
  # Lots of 0 values



# Wrangling ----

  # Subset data to only keep columns I'll use
suicideTraffickAge_2013to2021 = crimeSuicide_2013to2021 %>% 
  select(Age, TotalSuicide, TotalTraffick)

View(suicideTraffickAge_2013to2021)
# 3,021 entries, 3 total columns


  # Drop total age rows
suicideTraffickAge_2013to2021R = suicideTraffickAge_2013to2021 %>%
  filter(Age != 'Total all ages')

View(suicideTraffickAge_2013to2021R)
# 2,562 entries, 4 total columns
  # Sample size still validated



# Create multiple linear regression models ----

  # With all IV's
suicideTraffickAgeLmAllIVs = lm(TotalSuicide ~ ., 
                                data = suicideTraffickAge_2013to2021R)
# Success

  # With no IV's
suicideTraffickAgeLmNoIVs = lm(TotalSuicide ~ 1, 
                               data = suicideTraffickAge_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(suicideTraffickAgeLmAllIVs, direction = 'backward')
# Kept both IV's

  # Forward selection
step(suicideTraffickAgeLmNoIVs, direction = 'forward', 
     scope = formula(suicideTraffickAgeLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added trafficking crimes first, implying they have the strongest impact

  # Hybrid selection
step(suicideTraffickAgeLmNoIVs, direction = 'both', 
     scope = formula(suicideTraffickAgeLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model ----
suicideTraffickAgeLm = lm(formula = TotalSuicide ~ TotalTraffick * Age, 
    data = suicideTraffickAge_2013to2021R)

summary(suicideTraffickAgeLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -1967.8  -208.8  -105.2    10.4  3915.6 
# Coefficients:
#                             Estimate Std. Error t value Pr(>|t|)    
# (Intercept)                248.79124   11.58970  21.467   <2e-16 ***
# TotalTraffick                0.05099    0.00279  18.275   <2e-16 ***
# AgeUnder 18               -223.24569   25.63338  -8.709   <2e-16 ***
# TotalTraffick:AgeUnder 18   -0.03296    0.08360  -0.394    0.693    
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 484.7 on 2558 degrees of freedom
# Multiple R-squared:  0.1601,	Adjusted R-squared:  0.1591 
# F-statistic: 162.5 on 3 and 2558 DF,  p-value: < 2.2e-16
  # Though the model is significant, it determined that the predictive ability  
  # of trafficking crime is not significantly different by age; accept the null 
  # and reject the alternative hypothesis
  # It did find trafficking crime and the minors age bracket each to be 
  # significant on their own



# Re-wrangling to better meet assumptions ----

  # Transform DV
suicideTraffickAge_2013to2021R$TotalSuicideLog = log(
  suicideTraffickAge_2013to2021R$TotalSuicide)

View(suicideTraffickAge_2013to2021R)
# 2,562 entries, 4 total columns
  # Some infinite values

      # Drop NA's
suicideTraffickAge_2013to2021R = NaRV.omit(suicideTraffickAge_2013to2021R)

View(suicideTraffickAge_2013to2021R)
# 2,375 entries, 4 total columns
  # Sample size still validated

      # Drop original column
suicideTraffickAge_2013to2021R = subset(
  suicideTraffickAge_2013to2021R, select = -(TotalSuicide))

View(suicideTraffickAge_2013to2021R)
# 2,375 entries, 3 total columns


  # Drop outliers

    # Leverage
CookD(suicideTraffickAgeLm, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers: 2175, 2181, 2184

    # Distance
car::outlierTest(suicideTraffickAgeLm)
# Distance outliers: 260, 265, 271, 276, 249, 254, 282, 287, 238, 243

    # Influential
options(max.print = 5000)

summary(influence.measures(suicideTraffickAgeLm))
# This determined several rows have low significance - none more influential
  # than that, and does include the ones identified above - the ones 
  # identified are rows:
  # 117, 147, 205, 210, 216, 221, 227, 232, 238, 243, 249, 254, 260, 261, 265, 
  # 266, 271, 272, 276, 277, 282, 283, 287, 288, 443, 449, 455, 456, 461, 467, 
  # 468, 473, 474, 479, 482, 483, 484, 485, 486, 499, 505, 511, 517, 523, 529, 
  # 536, 537, 643, 655, 661, 667, 673, 679, 685, 1007, 1013, 1019, 1093, 1099, 
  # 1105, 1111, 1117, 1123, 1129, 1135, 1158, 1159, 1160, 1161, 1162, 1402, 
  # 1403, 1404, 1405, 1406, 1407, 1420, 1421, 1422, 1423, 1424, 1429, 1432, 
  # 1433, 1434, 1435, 1436, 1437, 1438, 1593, 1599, 1605, 1611, 1617, 1623, 
  # 1629, 1635, 1643, 1649, 1655, 1661, 1667, 1673, 1743, 1749, 1755, 1761, 
  # 1767, 1773, 1779, 1785, 1819, 1893, 1899, 1905, 1911, 1917, 1923, 1929, 
  # 1935, 2139, 2141, 2143, 2145, 2146, 2148, 2149, 2150, 2151, 2152, 2154, 
  # 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 
  # 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 
  # 2179, 2180, 2181, 2182, 2183, 2184


    # Remove outliers
suicideTraffickAgeNoOutliers = suicideTraffickAge_2013to2021R[-c(
  2134117, 147, 205, 210, 216, 221, 227, 232, 238, 243, 249, 254, 260, 261, 265, 
  266, 271, 272, 276, 277, 282, 283, 287, 288, 443, 449, 455, 456, 461, 467,
  468, 473, 474, 479, 482, 483, 484, 485, 486, 499, 505, 511, 517, 523, 529,
  536, 537, 643, 655, 661, 667, 673, 679, 685, 1007, 1013, 1019, 1093, 1099,
  1105, 1111, 1117, 1123, 1129, 1135, 1158, 1159, 1160, 1161, 1162, 1402,
  1403, 1404, 1405, 1406, 1407, 1420, 1421, 1422, 1423, 1424, 1429, 1432,
  1433, 1434, 1435, 1436, 1437, 1438, 1593, 1599, 1605, 1611, 1617, 1623,
  1629, 1635, 1643, 1649, 1655, 1661, 1667, 1673, 1743, 1749, 1755, 1761,
  1767, 1773, 1779, 1785, 1819, 1893, 1899, 1905, 1911, 1917, 1923, 1929,
  1935, 2139, 2141, 2143, 2145, 2146, 2148, 2149, 2150, 2151, 2152, 2154,
  2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166,
  2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178,
  2179, 2180, 2181, 2182, 2183, 2184),]

View(suicideTraffickAgeNoOutliers)
# 2,215 entries, 3 total columns
  # Sample size still validated



# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
suicideTraffickAgeNoOutliersLmAllIVs = lm(
  TotalSuicideLog ~ ., data = suicideTraffickAgeNoOutliers)
# Success

  # With no IV's
suicideTraffickAgeNoOutliersLmNoIVs = lm(
  TotalSuicideLog ~ 1, data = suicideTraffickAgeNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(suicideTraffickAgeNoOutliersLmAllIVs, direction = 'backward')
# Kept both IV's

  # Forward selection
step(suicideTraffickAgeNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(suicideTraffickAgeNoOutliersLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added age first, implying it has the strongest impact

  # Hybrid selection
step(suicideTraffickAgeNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(suicideTraffickAgeNoOutliersLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model without outliers ----
suicideTraffickAgeNoOutliersLm = lm(
  formula = TotalSuicideLog ~ TotalTraffick * Age, 
  data = suicideTraffickAgeNoOutliers)

summary(suicideTraffickAgeNoOutliersLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -2.6386 -0.7196 -0.0427  0.6708  3.2326 
# Coefficients:
#                             Estimate Std. Error t value Pr(>|t|)    
# (Intercept)                4.847e+00  2.730e-02 177.530   <2e-16 ***
# TotalTraffick              1.091e-04  6.598e-06  16.533   <2e-16 ***
# AgeUnder 18               -1.460e+00  6.975e-02 -20.927   <2e-16 ***
# TotalTraffick:AgeUnder 18  6.655e-05  1.932e-04   0.344    0.731    
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.094 on 2211 degrees of freedom
# Multiple R-squared:  0.2774,	Adjusted R-squared:  0.2765 
# F-statistic:   283 on 3 and 2211 DF,  p-value: < 2.2e-16
  # Though the model is significant, it determined that the predictive ability  
  # of trafficking crime is not significantly different by age; accept the null 
  # and reject the alternative hypothesis
  # It did find trafficking crime and the minors age bracket each to be 
  # significant on their own



# Test assumptions post hoc ----

  # Linearity

    # With outliers
ggplot(suicideTraffickAge_2013to2021R, 
       aes(x = TotalSuicideLog, y = TotalTraffick, Age)) +
  geom_point() + 
  labs(x = 'Suicide', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Only mildly linear, with outliers

    # Without outliers
ggplot(suicideTraffickAgeNoOutliers, aes(x = TotalSuicideLog, y = TotalTraffick, Age)) +
  geom_point() + 
  labs(x = 'Suicide', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# This seems worse - likely due to zooming in, per se, on the data and showing
  # it's more spread out than I thought previously 


  # Homoscedasticity

    # With outliers
lmtest::bptest(suicideTraffickAgeLm)
# 	studentized Breusch-Pagan test
# data:  suicideTraffickAgeLm
# BP = 187.57, df = 3, p-value < 2.2e-16
  # This p value below 0.05 violates the assumption of homoscedasticity


    # Without outliers
lmtest::bptest(suicideTraffickAgeNoOutliersLm)
# 	studentized Breusch-Pagan test
# data:  suicideTraffickAgeNoOutliersLm
# BP = 84.46, df = 3, p-value < 2.2e-16
  # This p value below 0.05 violates the assumption of homoscedasticity



# Summary ----
# The relationship between suicides, trafficking crime arrests, and age is only 
# mildly linear and is not homoscedastic, which means the results of a stepwise 
# multiple linear regression model cannot be fully tested. That said, with 
# and without outliers this model determined that the ability of trafficking 
# crime arrests to predict suicides does not vary significantly by age.