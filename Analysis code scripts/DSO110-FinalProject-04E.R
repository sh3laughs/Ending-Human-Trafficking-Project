# DSO110 - Data Science Final Project
  # File 4-E
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found in years where there are higher rates 
  # of crime overall

# H0: Arrests for crime overall do not predict arrests for trafficking crimes 
  # within the same year
# H1: Arrests for crime overall do predict arrests for trafficking crimes within
  # the same year

# IV's:
  # All crime arrests
  # State
# DV: Trafficking arrests


# Import packages ----
library(dplyr)
library(ggplot2)
library(IDPmisc)


# Import and preview data ----
traffickingCrime_2013to2021 = read.csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/traffickingAllCrimes_2013to2021.csv')

View(traffickingCrime_2013to2021)
# 1,386 entries, 41 total columns
  # Sample size is validated for now...
  # Lots of 0 values



# Wrangling ----

  # Subset data to only keep columns I'll use
traffickCrimeYear_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, TotalAll, TotalTraffick, Year)

View(traffickCrimeYear_2013to2021)
# 1,386 entries, 3 total columns


  # Drop non-total rows
traffickCrimeYear_2013to2021R = traffickCrimeYear_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickCrimeYear_2013to2021R)
# 459 entries, 4 total columns
  # Sample size still validated


  # Drop age column
traffickCrimeYear_2013to2021R = subset(
  traffickCrimeYear_2013to2021R, select = -(Age))

View(traffickCrimeYear_2013to2021R)
# 459 entries, 3 total columns



# Create multiple linear regression models ----

  # With all IV's
traffickCrimeYearLmAllIVs = lm(TotalTraffick ~ ., 
                                data = traffickCrimeYear_2013to2021R)
# Success

  # With no IV's
traffickCrimeYearLmNoIVs = lm(TotalTraffick ~ 1, 
                               data = traffickCrimeYear_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCrimeYearLmAllIVs, direction = 'backward')
# Kept both IV's

  # Forward selection
step(traffickCrimeYearLmNoIVs, direction = 'forward', 
     scope = formula(traffickCrimeYearLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added overall crime first, implying it has the strongest impact

  # Hybrid selection
step(traffickCrimeYearLmNoIVs, direction = 'both', 
     scope = formula(traffickCrimeYearLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model ----
traffickCrimeYearLm = lm(formula = TotalTraffick ~ TotalAll * Year, 
    data = traffickCrimeYear_2013to2021)

summary(traffickCrimeYearLm)
# Residuals:
#      Min       1Q   Median       3Q      Max 
# -10882.8   -579.7   -203.7    173.1  24032.8 
# Coefficients:
#                 Estimate Std. Error t value Pr(>|t|)    
# (Intercept)   -1.966e+05  6.365e+04  -3.089  0.00205 ** 
# TotalAll      -4.058e+00  3.361e-01 -12.072  < 2e-16 ***
# Year           9.747e+01  3.156e+01   3.088  0.00205 ** 
# TotalAll:Year  2.018e-03  1.667e-04  12.101  < 2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 2599 on 1382 degrees of freedom
# Multiple R-squared:  0.3857,	Adjusted R-squared:  0.3843 
# F-statistic: 289.2 on 3 and 1382 DF,  p-value: < 2.2e-16
  # This determined that overall crime and year are significant predictors on 
  # their own, and that overall crime is also significantly different by year; 
  # reject the null and accept the alternative hypothesis



# Re-wrangling to better meet assumptions ----

  # Transform DV
traffickCrimeYear_2013to2021R$TotalTraffickLog = log(
  traffickCrimeYear_2013to2021R$TotalTraffick)

View(traffickCrimeYear_2013to2021R)
# 459 entries, 4 total columns
  # Lots of infinite values

      # Drop NA's
traffickCrimeYear_2013to2021R = NaRV.omit(
  traffickCrimeYear_2013to2021R)

View(traffickCrimeYear_2013to2021R)
# 293 entries, 4 total columns
  # Sample size still validated

      # Drop original column
traffickCrimeYear_2013to2021R = subset(
  traffickCrimeYear_2013to2021R, select = -(TotalTraffick))

View(traffickCrimeYear_2013to2021R)
# 293 entries, 3 total columns


  # Drop outliers

    # Leverage
traffickCrimeYearLev = hat(model.matrix(traffickCrimeYearLm))

plot(traffickCrimeYearLev)

traffickCrimeYear_2013to2021[traffickCrimeYearLev > .2,]
# No leverage outliers found


    # Distance
car::outlierTest(traffickCrimeYearLm)
# Distance outliers: 1169, 1166, 1170, 1167, 1164, 1163, 615, 747, 746, 614

    # Influential
summary(influence.measures(traffickCrimeYearLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include those identified above - the ones 
  # identified are rows:
  # 110, 111, 112, 114, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 128, 
  # 130, 131, 132, 134, 135, 136, 138, 139, 140, 227, 228, 230, 231, 233, 234, 
  # 236, 237, 239, 240, 242, 243, 245, 246, 248, 249, 275, 276, 278, 279, 479, 
  # 480, 611, 612, 614, 615, 617, 618, 620, 621, 623, 624, 746, 747, 755, 756, 
  # 758, 759, 761, 762, 764, 765, 875, 876, 1010, 1118, 1145, 1146, 1148, 1149, 
  # 1151, 1152, 1154, 1155, 1157, 1158, 1160, 1161, 1163, 1164, 1166, 1167, 
  # 1169, 1170


    # Remove outliers
traffickCrimeYearNoOutliers = traffickCrimeYear_2013to2021R[-c(
  110, 111, 112, 114, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 128, 
  130, 131, 132, 134, 135, 136, 138, 139, 140, 227, 228, 230, 231, 233, 234,
  236, 237, 239, 240, 242, 243, 245, 246, 248, 249, 275, 276, 278, 279, 479,
  480, 611, 612, 614, 615, 617, 618, 620, 621, 623, 624, 746, 747, 755, 756,
  758, 759, 761, 762, 764, 765, 875, 876, 1010, 1118, 1145, 1146, 1148, 1149,
  1151, 1152, 1154, 1155, 1157, 1158, 1160, 1161, 1163, 1164, 1166, 1167,
  1169, 1170),]

View(traffickCrimeYearNoOutliers)
# 249 entries, 3 total columns
  # Sample size still validated


# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
traffickCrimeYearNoOutliersLmAllIVs = lm(
  TotalTraffickLog ~ ., data = traffickCrimeYearNoOutliers)
# Success

  # With no IV's
traffickCrimeYearNoOutliersLmNoIVs = lm(
  TotalTraffickLog ~ 1, data = traffickCrimeYearNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCrimeYearNoOutliersLmAllIVs, direction = 'backward')
# Kept both IV's again - hurray!

  # Forward selection
step(traffickCrimeYearNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(traffickCrimeYearNoOutliersLmAllIVs))
# Kept both IV's again
  # Glad it's aligned with BE
  # Added overall crime first again, too, implying it has the strongest impact

  # Hybrid selection
step(traffickCrimeYearNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(traffickCrimeYearNoOutliersLmAllIVs))
# Kept both IV's again
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model without outliers ----
traffickCrimeYearNoOutliersLm = lm(
  formula = TotalTraffickLog ~ TotalAll * Year, 
  data = traffickCrimeYearNoOutliers)

summary(traffickCrimeYearNoOutliersLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -4.0902 -0.9453  0.0588  0.9624  3.5361 
# Coefficients:
#                 Estimate Std. Error t value Pr(>|t|)  
# (Intercept)   -2.148e+02  9.587e+01  -2.241   0.0260 *
# TotalAll      -8.012e-04  3.361e-04  -2.384   0.0179 *
# Year           1.094e-01  4.750e-02   2.303   0.0221 *
# TotalAll:Year  3.993e-07  1.667e-07   2.396   0.0173 *
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.297 on 245 degrees of freedom
# Multiple R-squared:  0.3169,	Adjusted R-squared:  0.3085 
# F-statistic: 37.88 on 3 and 245 DF,  p-value: < 2.2e-16
  # This determined that overall crime and year are each significant predictors 
  # on their own, and that overall crime is also significantly different by 
  # year; reject the null and accept the alternative hypothesis



# Test assumptions post hoc ----

  # Linearity

    # With outliers
ggplot(traffickCrimeYear_2013to2021R, aes(
  x = TotalTraffickLog, y = TotalAll + Year)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'All Crimes by Year') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(traffickCrimeYearNoOutliers, aes(
  x = TotalTraffickLog, y = TotalAll + Year)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'All Crimes by Year') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Nearly identical to version with outliers


  # Homoscedasticity

    # With outliers
lmtest::bptest(traffickCrimeYearLm)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeYearLm
# BP = 335.93, df = 3, p-value < 2.2e-16
  # This p value below 0.05 violates the assumption of homoscedasticity


    # Without outliers
lmtest::bptest(traffickCrimeYearNoOutliersLm)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeYearNoOutliersLm
# BP = 4.249, df = 3, p-value = 0.2358
  # This p value above 0.05 validates the assumption of homoscedasticity



# Summary ----
# The relationship between trafficking arrests, overall crime arrests, and year 
# is only mildly linear and with outliers is not homoscedastic (without outlier
# it is), which means the results of a stepwise multiple linear regression model 
# cannot be fully tested. That said, with and without outliers, this model 
# determined that the ability of overall crime arrests to predict trafficking 
# arrests does vary significantly by year.