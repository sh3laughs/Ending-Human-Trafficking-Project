# DSO110 - Data Science Final Project
  # File 4-A
  # Analysis: Simple linear regression

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found where there are higher rates of crime 
  # overall

# H0: Overall crime arrests do not predict arrests for trafficking crimes
# H1: Overall crime arrests do predict arrests for trafficking crimes

# IV: All crime arrests
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
traffickCrime_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, TotalAll, TotalTraffick)

View(traffickCrime_2013to2021)
# 1,386 entries, 2 total columns


  # Drop non-total rows
traffickCrime_2013to2021R = traffickCrime_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickCrime_2013to2021R)
# 459 entries, 3 total columns
  # Sample size still validated


  # Drop age column
traffickCrime_2013to2021R = subset(
  traffickCrime_2013to2021R, select = -(Age))

View(traffickCrime_2013to2021R)
# 459 entries, 2 total columns


  # Transform DV
traffickCrime_2013to2021R$TotalTraffickLog = log(
  traffickCrime_2013to2021R$TotalTraffick)

View(traffickCrime_2013to2021R)
# 459 entries, 3 total columns
  # Lots of infinite values

      # Drop NA's
traffickCrime_2013to2021R = NaRV.omit(traffickCrime_2013to2021R)

View(traffickCrime_2013to2021R)
# 293 entries, 3 total columns
  # Sample size still validated



# Test assumptions ----

  # Linearity ----
ggplot(traffickCrime_2013to2021R, aes(x = TotalTraffickLog, y = TotalAll)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'All Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with some outliers


  # Homoscedasticity ----
traffickCrimeLm = lm(TotalTraffickLog ~ TotalAll, 
                     data = traffickCrime_2013to2021R)

    # Breusch Pagan Homoscedasticity test
lmtest::bptest(traffickCrimeLm)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeLm
# BP = 0.0072129, df = 1, p-value = 0.9323
  # This p value above 0.05 validates this assumption


  # Outliers ----

    # Leverage
CookD(traffickCrimeLm, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers on rows 37, 38, 39

    # Distance
car::outlierTest(traffickCrimeLm)
# No Studentized residuals with Bonferroni p < 0.05
# Largest |rstudent|:
#      rstudent unadjusted p-value Bonferroni p
# 431 -2.955326          0.0033797      0.99026
  # Distance outlier: 431

    # Influential
summary(influence.measures(traffickCrimeLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include those identified above - the ones 
  # identified are rows:
  # 18, 37, 38, 39, 40, 41, 42, 43, 44, 74, 76, 78, 79, 202, 246, 251, 252, 380, 
  # 381, 382, 383, 384, 431


    # Remove outliers
traffickCrime_2013to2021NoOutliers = traffickCrime_2013to2021R[-c(
  18, 37, 38, 39, 40, 41, 42, 43, 44, 74, 76, 78, 79, 202, 246, 251, 252, 380, 
  381, 382, 383, 384, 431),]

View(traffickCrime_2013to2021NoOutliers)
# 276 entries, 3 total columns
  # Sample size still validated



# Create new model without outliers ----
traffickCrimeLmNoOutliers = lm(
  TotalTraffickLog ~ TotalAll, data = traffickCrime_2013to2021NoOutliers)


# Re-test assumptions ----

  # Normality
ggplot(traffickCrime_2013to2021NoOutliers, 
       aes(x = TotalTraffickLog, y = TotalAll)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'All Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Not a big difference... it still looks like there's a batch of outliers...


  # Homoscedasticity
lmtest::bptest(traffickCrimeLmNoOutliers)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeLmNoOutliers
# BP = 0.060564, df = 1, p-value = 0.8056
  # This p value above 0.05 validates the assumption of homoscedasticity



# Analyze ----

  # With outliers
summary(traffickCrimeLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -4.0300 -1.0980  0.0104  1.0940  3.0481 
# Coefficients:
#              Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 6.094e+00  1.029e-01   59.24   <2e-16 ***
# TotalAll    3.827e-06  3.758e-07   10.18   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.385 on 291 degrees of freedom
# Multiple R-squared:  0.2627,	Adjusted R-squared:  0.2602 
# F-statistic: 103.7 on 1 and 291 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # This means that total crime arrests do predict trafficking arrests
    # Total crime arrests explain ~26% of the variance in trafficking arrests


  # Without outliers
summary(traffickCrimeLmNoOutliers)
# Residuals:
# -3.9676 -1.1544  0.0096  1.0918  3.1095 
# Coefficients:
#              Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 6.031e+00  1.057e-01   57.07   <2e-16 ***
# TotalAll    3.837e-06  3.787e-07   10.13   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.386 on 274 degrees of freedom
# Multiple R-squared:  0.2725,	Adjusted R-squared:  0.2699 
# F-statistic: 102.6 on 1 and 274 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # This means that total crime arrests do predict trafficking arrests
    # Total crime arrests explain ~27% of the variance in trafficking arrests



# Summary ----
# The relationship between trafficking arrests and total crime arrests is only 
# mildly linear, which means the results of a linear regression model cannot be 
# fully tested. That said, with outliers this model shows that total crime 
# arrests predict approximately 26% of the variance in trafficking arrests and
# without outliers they predict 27%. Further analysis will be completed to 
# validate this model's results.