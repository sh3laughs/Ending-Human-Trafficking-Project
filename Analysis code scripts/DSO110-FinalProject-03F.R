# DSO110 - Data Science Final Project
  # File 3-F
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found for an age bracket where there are 
  # higher rates of reported non-trafficking sex crime arrests

# H0: Arrests for non-trafficking sex crimes do not predict arrests for 
  # trafficking crimes within the same age bracket
# H1: Arrests for non-trafficking sex crimes effect do predict arrests for 
  # trafficking crimes within the same age bracket

# IV's:
  # Rape arrests
  # Non-trafficking sex arrests
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
traffickNonTraffickSexAge_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, Rape, Sex, TotalTraffick)

View(traffickNonTraffickSexAge_2013to2021)
# 1,386 entries, 4 total columns


  # Drop total age rows
traffickNonTraffickSexAge_2013to2021R = traffickNonTraffickSexAge_2013to2021 %>%
  filter(Age != 'Total all ages')

View(traffickNonTraffickSexAge_2013to2021R)
# 927 entries, 4 total columns
  # Sample size still validated



# Create multiple linear regression models ----

  # With all IV's
traffickNonTraffickSexAgeLmAllIVs = lm(
  TotalTraffick ~ ., data = traffickNonTraffickSexAge_2013to2021R)
# Success

  # With no IV's
traffickNonTraffickSexAgeLmNoIVs = lm(
  TotalTraffick ~ 1, data = traffickNonTraffickSexAge_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickNonTraffickSexAgeLmAllIVs, direction = 'backward')
# Removed age... that's not useful for this analysis...

  # Forward selection
step(traffickNonTraffickSexAgeLmNoIVs, direction = 'forward', 
     scope = formula(traffickNonTraffickSexAgeLmAllIVs))
# Removed age
  # This time, I'm not glad it's aligned with BE ;)
  # Added rape first, implying it has the strongest impact, then sex - this 
  # aligns with other analyses that find rape more significant than other 
  # non-trafficking sex crimes

  # Hybrid selection
step(traffickNonTraffickSexAgeLmNoIVs, direction = 'both', 
     scope = formula(traffickNonTraffickSexAgeLmAllIVs))
# Removed age
  # Added variables in the same order as FS model
  # Glad all three are aligned!


# Note: Because the goal of this analysis is to determine impact of age, I will
  # not analyze the model without age - will move forward with some 
  # transformation



# Re-wrangling to better meet assumptions ----

  # Transform DV
traffickNonTraffickSexAge_2013to2021R$TotalTraffickLog = log(
  traffickNonTraffickSexAge_2013to2021R$TotalTraffick)

View(traffickNonTraffickSexAge_2013to2021R)
# 927 entries, 5 total columns
  # Lots of infinite values

      # Drop NA's
traffickNonTraffickSexAge_2013to2021R = NaRV.omit(
  traffickNonTraffickSexAge_2013to2021R)

View(traffickNonTraffickSexAge_2013to2021R)
# 363 entries, 5 total columns
  # Sample size still validated

      # Drop original column
traffickNonTraffickSexAge_2013to2021R = subset(
  traffickNonTraffickSexAge_2013to2021R, select = -(TotalTraffick))

View(traffickNonTraffickSexAge_2013to2021R)
# 363 entries, 4 total columns


  # Drop outliers

    # Create a model with all variables to test look for outliers
traffickNonTraffickSexAgeLm = lm(formula = TotalTraffickLog ~ Rape * Sex * Age, 
                                 data = traffickNonTraffickSexAge_2013to2021R)

    # Leverage
CookD(traffickNonTraffickSexAgeLm, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers: 73, 76, 97


    # Distance
car::outlierTest(traffickNonTraffickSexAgeLm)
# Distance outliers: 581


    # Influential
summary(influence.measures(traffickNonTraffickSexAgeLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include the ones identified above - the ones 
  # identified are rows:
  # 36, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
  # 91, 92, 93, 94, 97, 168, 187, 360, 391, 502, 513, 581, 583, 600, 629, 631, 
  # 704, 768, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 
  # 839, 841, 871, 888, 898, 918


    # Remove outliers
traffickNonTraffickSexAgeNoOutliers = traffickNonTraffickSexAge_2013to2021R[-c(
  36, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
  91, 92, 93, 94, 97, 168, 187, 360, 391, 502, 513, 581, 583, 600, 629, 631,
  704, 768, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783,
  839, 841, 871, 888, 898, 918),]

View(traffickNonTraffickSexAgeNoOutliers)
# 336 entries, 4 total columns
  # Sample size still validated



# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
traffickNonTraffickSexAgeNoOutliersLmAllIVs = lm(
  TotalTraffickLog ~ ., data = traffickNonTraffickSexAgeNoOutliers)
# Success

  # With no IV's
traffickNonTraffickSexAgeNoOutliersLmNoIVs = lm(
  TotalTraffickLog ~ 1, data = traffickNonTraffickSexAgeNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickNonTraffickSexAgeNoOutliersLmAllIVs, direction = 'backward')
# Kept all three IV's - hurray

  # Forward selection
step(traffickNonTraffickSexAgeNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(traffickNonTraffickSexAgeNoOutliersLmAllIVs))
# Kept all three IV's
  # Added rape first again, and age second, which is interesting

  # Hybrid selection
step(traffickNonTraffickSexAgeNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(traffickNonTraffickSexAgeNoOutliersLmAllIVs))
# Identical results to FS option
  # Glad all three models are aligned



# Analyze model without outliers ----
traffickNonTraffickSexAgeNoOutliersLm = lm(
  formula = TotalTraffickLog ~ Rape * Sex * Age, 
    data = traffickNonTraffickSexAgeNoOutliers)

summary(traffickNonTraffickSexAgeNoOutliersLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -4.2934 -0.7863 -0.0151  0.9255  3.9692 
# Coefficients:
#                        Estimate Std. Error t value Pr(>|t|)    
# (Intercept)           5.676e+00  1.189e-01  47.751  < 2e-16 ***
# Rape                  3.012e-03  3.270e-04   9.211  < 2e-16 ***
# Sex                   6.795e-04  2.274e-04   2.988  0.00302 ** 
# AgeUnder 18          -1.698e+00  3.408e-01  -4.983 1.02e-06 ***
# Rape:Sex             -5.136e-07  1.043e-07  -4.926 1.34e-06 ***
# Rape:AgeUnder 18      5.666e-03  2.658e-03   2.132  0.03379 *  
# Sex:AgeUnder 18      -4.332e-05  1.444e-03  -0.030  0.97608    
# Rape:Sex:AgeUnder 18 -9.590e-06  6.606e-06  -1.452  0.14756    
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.262 on 328 degrees of freedom
# Multiple R-squared:  0.4952,	Adjusted R-squared:  0.4844 
# F-statistic: 45.97 on 7 and 328 DF,  p-value: < 2.2e-16
  # Though the model overall is significant, it did not find a significant 
  # difference in the impact of non-trafficking sex crime arrests based on 
  # age; accept the null and reject the alternative hypothesis
  # It did find significance in Under 18 age bracket, rape, sex, and rape and
  # sex together on their own, which is interesting - and there is a low 
  # significant difference in rape's impact for minors



# Test assumptions post hoc ----

  # Linearity

    # With outliers
ggplot(traffickNonTraffickSexAge_2013to2021R, aes(
  x = TotalTraffickLog, y = Rape, Sex, Age)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-Trafficking Sex Crimes by Age') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(traffickNonTraffickSexAgeNoOutliers, aes(
  x = TotalTraffickLog, y = Rape, Sex, Age)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-Trafficking Sex Crimes by Age') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Pretty much identical results to version with outliers


  # Homoscedasticity

    # With outliers
lmtest::bptest(traffickNonTraffickSexAgeLm)
# 	studentized Breusch-Pagan test
# data:  traffickNonTraffickSexAgeLm
# BP = 9.9939, df = 7, p-value = 0.1889
  # This p value above 0.05 validates the assumption of homoscedasticity

    # Without outliers
lmtest::bptest(traffickNonTraffickSexAgeNoOutliersLm)
# 	studentized Breusch-Pagan test
# data:  traffickNonTraffickSexAgeNoOutliersLm
# BP = 8.4728, df = 7, p-value = 0.2927
  # This p value above 0.05 validates the assumption of homoscedasticity


# Summary ----
# The relationship between trafficking arrests, non-trafficking sex crime
# arrests, and age is only mildly linear, which means the results of a stepwise 
# multiple linear regression model cannot be fully tested. That said, with and
# without outliers, this model determined that the ability of non-trafficking 
# sex crime arrests to predict trafficking arrests does not vary significantly 
# by age, though without outliers there is a significant difference in rape 
# arrests' ability to predict trafficking arrests for minors.