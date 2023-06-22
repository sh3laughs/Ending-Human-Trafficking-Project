# DSO110 - Data Science Final Project
  # File 6-A
  # Analysis: Simple linear regression

# Goal: Determine whether higher rates of reported suicides are more likely to 
  # be found where there are higher rates of arrests for human trafficking 
  # crimes

# H0: Trafficking crimes arrests do not predict suicide rates
# H1: Trafficking crimes arrests do predict suicide rates

# IV: Trafficking arrests
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
suicideTraffick_2013to2021 = crimeSuicide_2013to2021 %>% 
  select(Age, TotalSuicide, TotalTraffick)

View(suicideTraffick_2013to2021)
# 3,021 entries, 3 total columns


  # Drop non-total rows
suicideTraffick_2013to2021R = suicideTraffick_2013to2021 %>%
  filter(Age == 'Total all ages')

View(suicideTraffick_2013to2021R)
# 459 entries, 3 total columns
  # Sample size still validated


  # Drop age column
suicideTraffick_2013to2021R = subset(
  suicideTraffick_2013to2021R, select = -(Age))

View(suicideTraffick_2013to2021R)
# 459 entries, 2 total columns



# Test assumptions ----

  # Linearity ----
ggplot(suicideTraffick_2013to2021R, aes(x = TotalSuicide, y = TotalTraffick)) +
  geom_point() + 
  labs(x = 'Suicides', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Only barely linear

    # Transform DV
suicideTraffick_2013to2021R$TotalSuicideSqrt = sqrt(
  suicideTraffick_2013to2021R$TotalSuicide)

View(suicideTraffick_2013to2021R)
# 459 entries, 3 total columns

      # Check distribution again
ggplot(suicideTraffick_2013to2021R, 
       aes(x = TotalSuicideSqrt, y = TotalTraffick)) +
  geom_point() + 
  labs(x = 'Suicides', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Better, but still not linear

    # Transform again
suicideTraffick_2013to2021R$TotalSuicideLog = log(
  suicideTraffick_2013to2021R$TotalSuicide)

View(suicideTraffick_2013to2021R)
# 459 entries, 4 total columns
  # Some infinite values

      # Drop NA's
suicideTraffick_2013to2021R = NaRV.omit(
  suicideTraffick_2013to2021R)

View(suicideTraffick_2013to2021R)
# 457 entries, 4 total columns
  # Sample size still validated

      # Check distribution again
ggplot(suicideTraffick_2013to2021R, 
       aes(x = TotalSuicideLog, y = TotalTraffick)) +
  geom_point() + 
  labs(x = 'Suicides', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Best so far - decently linear with some outliers


  # Homoscedasticity ----
suicideTraffickLm = lm(TotalSuicideLog ~ TotalTraffick, 
                     data = suicideTraffick_2013to2021R)

    # Breusch Pagan Homoscedasticity test
lmtest::bptest(suicideTraffickLm)
# 	studentized Breusch-Pagan test
# data:  traffickSuicideLm
# BP = 0.34174, df = 1, p-value = 0.5588
  # This p value above 0.05 validates this assumption


  # Outliers ----

    # Leverage
CookD(suicideTraffickLm, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers: 385, 386, 387

    # Distance
car::outlierTest(suicideTraffickLm)
# No Studentized residuals with Bonferroni p < 0.05
# Largest |rstudent|:
#      rstudent unadjusted p-value Bonferroni p
# 431 -3.221359          0.0013675      0.62497
   # 431 is a distance outlier

    # Influential
summary(influence.measures(suicideTraffickLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include the outliers identified above - 
  # the ones identified are rows:
  # 80, 89, 90, 202, 203, 205, 246, 249, 250, 251, 252, 351, 380, 381, 382, 383, 
  # 384, 385, 386, 387, 424, 425, 426, 427, 428, 429, 430, 431

      # Remove outliers
suicideTraffickNoOutliers = suicideTraffick_2013to2021R[-c(
  385, 386, 387, 431, 80, 89, 90, 202, 203, 205, 246, 249, 250, 251, 252, 351, 
  380, 381, 382, 383, 384, 424, 425, 426, 427, 428, 429, 430),]

View(suicideTraffickNoOutliers)
# 429 entries, 4 total columns
  # Sample size still validated



# Create new model without outliers ----
suicideTraffickLmNoOutliers = lm(
  TotalSuicideLog ~ TotalTraffick, data = suicideTraffickNoOutliers)



# Re-test assumptions ----

  # Normality
ggplot(suicideTraffickNoOutliers, 
       aes(x = TotalSuicideLog, y = TotalTraffick)) +
  geom_point() + 
  labs(x = 'Suicides', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Not a big difference... it still looks like there are outliers...

  # Homoscedasticity
lmtest::bptest(suicideTraffickLmNoOutliers)
# 	studentized Breusch-Pagan test
# data:  suicideTraffickLmNoOutliers
# BP = 0.037227, df = 1, p-value = 0.847
  # This p value above 0.05 still validates the assumption of homoscedasticity



# Analyze ----

  # With outliers
summary(suicideTraffickLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -2.8853 -0.6245  0.1290  0.6583  1.9161 
# Coefficients:
#                Estimate Std. Error t value Pr(>|t|)    
# (Intercept)   6.756e+00  4.608e-02 146.620   <2e-16 ***
# TotalTraffick 9.532e-05  1.071e-05   8.897   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 0.906 on 455 degrees of freedom
# Multiple R-squared:  0.1482,	Adjusted R-squared:  0.1463 
# F-statistic: 79.16 on 1 and 455 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # This means that trafficking arrests do predict suicides
    # Suicides explain ~15% of the variance in trafficking arrests

  # Without outliers
summary(suicideTraffickLmNoOutliers)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -2.8167 -0.6150  0.1244  0.5850  1.9233 
# Coefficients:
#                Estimate Std. Error t value Pr(>|t|)    
# (Intercept)   6.749e+00  4.610e-02   146.4  < 2e-16 ***
# TotalTraffick 1.493e-04  1.757e-05     8.5 3.22e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 0.8449 on 427 degrees of freedom
# Multiple R-squared:  0.1447,	Adjusted R-squared:  0.1427 
# F-statistic: 72.24 on 1 and 427 DF,  p-value: 3.216e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # This means that trafficking arrests do predict suicides
    # Suicides explain ~14% of the variance in trafficking arrests



# Summary ----
# The relationship between suicides and trafficking crime arrests is only mildly
# linear, which means the results of a linear regression model cannot be fully 
# tested. That said, with outliers this model shows that trafficking crime 
# arrests predict approximately 15% of the variance in suicides and without 
# outliers they predict about 14%. Further analysis will be completed to 
# validate this model's results.