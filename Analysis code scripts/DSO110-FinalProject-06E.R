# DSO110 - Data Science Final Project
  # File 6-E
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported suicides are more likely to 
  # be found for years where there are higher rates of arrests for human 
  # trafficking crimes

# H0: Arrests for trafficking crimes do not predict suicides within the same 
  # year
# H1: Arrests for trafficking crimes do predict suicides within the same year

# IV's:
  # Trafficking crime arrests
  # Year
# DV: Suicides


# Import packages ----
library(dplyr)
library(ggplot2)
library(IDPmisc)


# Import and preview data ----
crimeSuicide_2013to2021 = read.csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/crimeSuicide_2013to2021.csv')

View(crimeSuicide_2013to2021)
# 3,021 entries, 43 total columns
  # Sample size is validated for now...
  # Lots of 0 values



# Wrangling ----

  # Subset data to only keep columns I'll use
suicideTraffickYear_2013to2021 = crimeSuicide_2013to2021 %>% 
  select(Age, TotalSuicide, TotalTraffick, Year)

View(suicideTraffickYear_2013to2021)
# 3,021 entries, 4 total columns


  # Drop non-total rows
suicideTraffickYear_2013to2021R = suicideTraffickYear_2013to2021 %>%
  filter(Age == 'Total all ages')

View(suicideTraffickYear_2013to2021R)
# 459 entries, 4 total columns
  # Sample size still validated


  # Drop age column
suicideTraffickYear_2013to2021R = subset(
  suicideTraffickYear_2013to2021R, select = -(Age))

View(suicideTraffickYear_2013to2021R)
# 459 entries, 3 total columns



# Create multiple linear regression models ----

  # With all IV's
suicideTraffickYearLmAllIVs = lm(TotalSuicide ~ ., 
                                data = suicideTraffickYear_2013to2021R)
# Success

  # With no IV's
suicideTraffickYearLmNoIVs = lm(TotalSuicide ~ 1, 
                               data = suicideTraffickYear_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(suicideTraffickYearLmAllIVs, direction = 'backward')
# Kept both IV's

  # Forward selection
step(suicideTraffickYearLmNoIVs, direction = 'forward', 
     scope = formula(suicideTraffickYearLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added trafficking crime arrests first, implying they have the strongest 
  # impact

  # Hybrid selection
step(suicideTraffickYearLmNoIVs, direction = 'both', 
     scope = formula(suicideTraffickYearLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model ----
suicideTraffickYearLm = lm(formula = TotalSuicide ~ TotalTraffick * Year, 
    data = suicideTraffickYear_2013to2021R)

summary(suicideTraffickYearLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -4961.0  -757.4  -280.7   435.7  5950.9 
# Coefficients:
#                      Estimate Std. Error t value Pr(>|t|)    
# (Intercept)         9.468e+04  4.798e+04   1.973   0.0491 *  
# TotalTraffick       7.404e+01  1.331e+01   5.563 4.54e-08 ***
# Year               -4.637e+01  2.379e+01  -1.949   0.0519 .  
# TotalTraffick:Year -3.658e-02  6.594e-03  -5.546 4.95e-08 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1225 on 455 degrees of freedom
# Multiple R-squared:  0.3455,	Adjusted R-squared:  0.3412 
# F-statistic: 80.08 on 3 and 455 DF,  p-value: < 2.2e-16
  # This determined that trafficking crime arrests is a significant predictor 
  # on its own, and that trafficking arrests' ability to predict suicides is 
  # also significantly different by year; reject the null and accept the 
  # alternative hypothesis
  # It did not find year to have a significant impact on its own



# Re-wrangling to better meet assumptions ----

  # Transform DV
suicideTraffickYear_2013to2021R$TotalSuicideLog = log(
  suicideTraffickYear_2013to2021R$TotalSuicide)

View(suicideTraffickYear_2013to2021R)
# 459 entries, 4 total columns
  # Some infinite values

      # Drop NA's
suicideTraffickYear_2013to2021R = NaRV.omit(suicideTraffickYear_2013to2021R)

View(suicideTraffickYear_2013to2021R)
# 457 entries, 4 total columns
  # Sample size still validated

      # Drop original column
suicideTraffickYear_2013to2021R = subset(
  suicideTraffickYear_2013to2021R, select = -(TotalSuicide))

View(suicideTraffickYear_2013to2021R)
# 457 entries, 3 total columns


  # Drop outliers

    # Leverage
suicideTraffickYearLmR = lm(formula = TotalSuicideLog ~ TotalTraffick * Year, 
    data = suicideTraffickYear_2013to2021R)

suicideTraffickYearLev = hat(model.matrix(suicideTraffickYearLmR))

plot(suicideTraffickYearLev)

suicideTraffickYear_2013to2021R[suicideTraffickYearLev > .2,]
# Leverage outliers: 386, 387

    # Distance
car::outlierTest(suicideTraffickYearLm)
# Distance outliers: 43, 44, 42, 246, 41

    # Influential
summary(influence.measures(suicideTraffickYearLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include the outliers identified above - 
  # the ones identified are rows:
  # 37, 38, 39, 40, 41, 42, 43, 44, 45, 73, 75, 77, 78, 79, 80, 89, 90, 201, 
  # 202, 203, 246, 249, 251, 252, 379, 380, 381, 382, 383, 384, 385, 386, 387


    # Remove outliers
suicideTraffickYearNoOutliers = suicideTraffickYear_2013to2021R[-c(
  37, 38, 39, 40, 41, 42, 43, 44, 45, 73, 75, 77, 78, 79, 80, 89, 90, 201, 202, 
  203, 246, 249, 251, 252, 379, 380, 381, 382, 383, 384, 385, 386, 387),]

View(suicideTraffickYearNoOutliers)
# 424 entries, 3 total columns
  # Sample size still validated



# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
suicideTraffickYearNoOutliersLmAllIVs = lm(
  TotalSuicideLog ~ ., data = suicideTraffickYearNoOutliers)
# Success

  # With no IV's
suicideTraffickYearNoOutliersLmNoIVs = lm(
  TotalSuicideLog ~ 1, data = suicideTraffickYearNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(suicideTraffickYearNoOutliersLmAllIVs, direction = 'backward')
# Kept both IV's

  # Forward selection
step(suicideTraffickYearNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(suicideTraffickYearNoOutliersLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added trafficking crimes first, implying they have the strongest impact

  # Hybrid selection
step(suicideTraffickYearNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(suicideTraffickYearNoOutliersLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model without outliers ----
suicideTraffickYearNoOutliersLm = lm(
  formula = TotalSuicideLog ~ TotalTraffick * Year, 
  data = suicideTraffickYearNoOutliers)

summary(suicideTraffickYearNoOutliersLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -2.9725 -0.5472  0.1301  0.6493  1.9975 
# Coefficients:
#                      Estimate Std. Error t value Pr(>|t|)   
# (Intercept)         1.226e+02  3.803e+01   3.225  0.00136 **
# TotalTraffick      -2.025e-03  1.870e-02  -0.108  0.91385   
# Year               -5.749e-02  1.886e-02  -3.049  0.00244 **
# TotalTraffick:Year  1.075e-06  9.269e-06   0.116  0.90775   
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 0.8762 on 420 degrees of freedom
# Multiple R-squared:  0.09217,	Adjusted R-squared:  0.08569 
# F-statistic: 14.21 on 3 and 420 DF,  p-value: 7.713e-09
  # This ended up with results opposite of the model with outliers - that year
  # has a significant impact on its own, but trafficking crime arrests to not
  # have a predictive ability over suicides on their own or by year; accept the
  # null and reject the alternative hypothesis



# Test assumptions post hoc ----

  # Linearity

    # With outliers
ggplot(suicideTraffickYear_2013to2021R, 
       aes(x = TotalSuicideLog, y = TotalTraffick, Year)) +
  geom_point() + 
  labs(x = 'Suicide', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(suicideTraffickYearNoOutliers, aes(x = TotalSuicideLog, y = TotalTraffick, Year)) +
  geom_point() + 
  labs(x = 'Suicide', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# This seems worse - likely due to zooming in, per se, on the data and showing
  # it's more spread out than I thought previously 


  # Homoscedasticity

    # With outliers
lmtest::bptest(suicideTraffickYearLm)
# 	studentized Breusch-Pagan test
# data:  suicideTraffickYearLm
# BP = 38.94, df = 3, p-value = 1.788e-08
  # This p value below 0.05 violates the assumption of homoscedasticity


    # Without outliers
lmtest::bptest(suicideTraffickYearNoOutliersLm)
# 	studentized Breusch-Pagan test
# data:  suicideTraffickYearNoOutliersLm
# BP = 4.5626, df = 3, p-value = 0.2068
  # This p value above 0.05 validates the assumption of homoscedasticity



# Summary ----
# The relationship between suicides, trafficking crime arrests, and year is only 
# mildly linear and with outliers is not homoscedastic (without outliers it is), 
# which means the results of a stepwise multiple linear regression model cannot 
# be fully tested. That said, with outliers this model determined that the 
# ability of trafficking crime arrests to predict suicides does vary 
# significantly by year and without outliers it does not.