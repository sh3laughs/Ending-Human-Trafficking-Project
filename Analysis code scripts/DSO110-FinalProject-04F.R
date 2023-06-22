# DSO110 - Data Science Final Project
  # File 4-F
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found for age brackets where there are higher 
  # rates of crime overall

# H0: Arrests for crime overall do not predict arrests for trafficking crimes 
  # within the same age bracket
# H1: Arrests for crime overall do predict arrests for trafficking crimes within
  # the same age bracket

# IV's:
  # All crime arrests
  # Age
# DV: Trafficking arrests


# Import packages ----
library(dplyr)
library(ggplot2)
library(IDPmisc)
library(predictmeans)

# Import and preview data ----
traffickingCrime_2013to2021 = read.csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/traffickingAllCrimes_2013to2021.csv')

View(traffickingCrime_2013to2021)
# 1,386 entries, 41 total columns
  # Sample size is validated for now...
  # Lots of 0 values



# Wrangling ----

  # Subset data to only keep columns I'll use
traffickCrimeAge_2013to2021R = traffickingCrime_2013to2021 %>% 
  select(Age, TotalAll, TotalTraffick)

View(traffickCrimeAge_2013to2021R)
# 1,386 entries, 3 total columns


  # Drop total age rows
traffickCrimeAge_2013to2021R = traffickCrimeAge_2013to2021R %>%
  filter(Age != 'Total all ages')

View(traffickCrimeAge_2013to2021R)
# 927 entries, 3 total columns
  # Sample size still validated



# Create multiple linear regression models ----

  # With all IV's
traffickCrimeAgeLmAllIVs = lm(TotalTraffick ~ ., 
                                data = traffickCrimeAge_2013to2021R)
# Success

  # With no IV's
traffickCrimeAgeLmNoIVs = lm(TotalTraffick ~ 1, 
                               data = traffickCrimeAge_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCrimeAgeLmAllIVs, direction = 'backward')
# Kept both IV's

  # Forward selection
step(traffickCrimeAgeLmNoIVs, direction = 'forward', 
     scope = formula(traffickCrimeAgeLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added total crime first, implying it's most significant

  # Hybrid selection
step(traffickCrimeAgeLmNoIVs, direction = 'both', 
     scope = formula(traffickCrimeAgeLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!


# Analyze model ----
traffickCrimeAgeLm = lm(
  formula = TotalTraffick ~ TotalAll * Age, data = traffickCrimeAge_2013to2021R)

summary(traffickCrimeAgeLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -7857.4  -554.4   -39.2   -12.3 29016.8 
# Coefficients:
#                        Estimate Std. Error t value Pr(>|t|)    
# (Intercept)           3.088e+02  1.410e+02   2.190   0.0288 *  
# TotalAll              8.924e-03  5.253e-04  16.989   <2e-16 ***
# AgeUnder 18          -3.010e+02  2.052e+02  -1.466   0.1429    
# TotalAll:AgeUnder 18 -6.387e-03  7.739e-03  -0.825   0.4094    
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 2433 on 923 degrees of freedom
# Multiple R-squared:  0.3043,	Adjusted R-squared:  0.302 
# F-statistic: 134.5 on 3 and 923 DF,  p-value: < 2.2e-16
  # Though the model is significant, it determined that the ability of overall 
  # crime is not significantly different by age; accept the null and reject the 
  # alternative hypothesis
  # It did find overall crime to be significant on its own



# Re-wrangling to better meet assumptions ----

  # Transform DV
traffickCrimeAge_2013to2021R$TotalTraffickLog = log(
  traffickCrimeAge_2013to2021R$TotalTraffick)

View(traffickCrimeAge_2013to2021R)
# 927 entries, 4 total columns
  # Lots of infinite values

      # Drop NA's
traffickCrimeAge_2013to2021R = NaRV.omit(traffickCrimeAge_2013to2021R)

View(traffickCrimeAge_2013to2021R)
# 363 entries, 4 total columns
  # Sample size still validated

      # Drop original column
traffickCrimeAge_2013to2021R = subset(
  traffickCrimeAge_2013to2021R, select = -(TotalTraffick))

View(traffickCrimeAge_2013to2021R)
# 363 entries, 3 total columns


  # Drop outliers

    # Leverage
CookD(traffickCrimeAgeLm, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers: 779, 781, 783


    # Distance
car::outlierTest(traffickCrimeAgeLm)
# Distance outliers: 783, 781, 779, 777, 775, 413, 501, 511, 513, 507
  # So 779, 781, and 783 are influential


    # Influential
summary(influence.measures(traffickCrimeAgeLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include the ones identified above - the ones 
  # identified are rows:
  # 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 
  # 92, 93, 95, 96, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 
  # 166, 167, 169, 187, 189, 323, 411, 413, 415, 417, 419, 501, 507, 509, 511, 
  # 513, 676, 678, 680, 682, 684, 766, 767, 768, 769, 770, 771, 772, 773, 774, 
  # 775, 776, 777, 778, 779, 781, 783, 892, 894, 896, 898, 900


    # Remove outliers
traffickCrimeAgeNoOutliers = traffickCrimeAge_2013to2021R[-c(
  73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 
  92, 93, 95, 96, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165,
  166, 167, 169, 187, 189, 323, 411, 413, 415, 417, 419, 501, 507, 509, 511,
  513, 676, 678, 680, 682, 684, 766, 767, 768, 769, 770, 771, 772, 773, 774,
  775, 776, 777, 778, 779, 781, 783, 892, 894, 896, 898, 900),]

View(traffickCrimeAgeNoOutliers)
# 322 entries, 3 total columns
  # Sample size still validated


# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
traffickCrimeAgeNoOutliersLmAllIVs = lm(
  TotalTraffickLog ~ ., data = traffickCrimeAgeNoOutliers)
# Success

  # With no IV's
traffickCrimeAgeNoOutliersLmNoIVs = lm(
  TotalTraffickLog ~ 1, data = traffickCrimeAgeNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCrimeAgeNoOutliersLmAllIVs, direction = 'backward')
# Kept both IV's - hurray!

  # Forward selection
step(traffickCrimeAgeNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(traffickCrimeAgeNoOutliersLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added overall crime first, implying it has the strongest impact

  # Hybrid selection
step(traffickCrimeAgeNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(traffickCrimeAgeNoOutliersLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model without outliers ----
traffickCrimeAgeNoOutliersLm = lm(formula = TotalTraffickLog ~ TotalAll * Age, 
  data = traffickCrimeAgeNoOutliers)

summary(traffickCrimeAgeNoOutliersLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -4.3820 -0.8894 -0.1256  1.0726  3.9060 
# Coefficients:
#                        Estimate Std. Error t value Pr(>|t|)    
# (Intercept)           6.138e+00  1.032e-01  59.477  < 2e-16 ***
# TotalAll              3.456e-06  3.377e-07  10.237  < 2e-16 ***
# AgeUnder 18          -1.835e+00  2.999e-01  -6.119 2.77e-09 ***
# TotalAll:AgeUnder 18  1.145e-05  8.396e-06   1.364    0.174    
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.376 on 318 degrees of freedom
# Multiple R-squared:  0.3978,	Adjusted R-squared:  0.3921 
# F-statistic: 70.02 on 3 and 318 DF,  p-value: < 2.2e-16
  # Though the model is significant, it determined that the ability of overall 
  # crime is not significantly different by age; accept the null and reject the 
  # alternative hypothesis
  # It did find overall crime and the minors age bracket each to be significant 
  # on their own



# Test assumptions post hoc ----

  # Linearity

    # With outliers
ggplot(traffickCrimeAge_2013to2021R, aes(
  x = TotalTraffickLog, y = TotalAll, Age)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'All Crimes by Age') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(traffickCrimeAgeNoOutliers, aes(
  x = TotalTraffickLog, y = TotalAll, Age)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'All Crimes by Age') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Pretty much identical to version with outliers


  # Homoscedasticity

    # With outliers
lmtest::bptest(traffickCrimeAgeLm)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeAgeLm
# BP = 753.958, df = 3, p-value = 1.145e-11
  # This p value below 0.05 violates the assumption of homoscedasticity


    # Without outliers
lmtest::bptest(traffickCrimeAgeNoOutliersLm)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeAgeNoOutliersLm
# BP = 1.9237, df = 3, p-value = 0.5884
  # This p value above 0.05 validates the assumption of homoscedasticity



# Summary ----
# The relationship between trafficking arrests, overall crime arrests, and age 
# is only mildly linear, which means the results of a stepwise multiple linear 
# regression model cannot be fully tested. That said, with and without outliers, 
# this model determined that the ability of overall crime arrests to predict 
# trafficking arrests does not vary significantly by age.