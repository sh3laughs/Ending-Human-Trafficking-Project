# DSO110 - Data Science Final Project
  # File 4-B
  # Analysis: Polynomial linear regression

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


  # Drop outliers
traffickCrime_2013to2021NoOutliers = traffickCrime_2013to2021R[-c(
  18, 37, 38, 39, 40, 41, 42, 43, 44, 74, 76, 78, 79, 202, 246, 251, 252, 380, 
  381, 382, 383, 384, 431),]

View(traffickCrime_2013to2021NoOutliers)
# 276 entries, 3 total columns
  # Sample size still validated



# Create polynomial regression models ----

  # Cubic

    # With outliers
traffickCrimePoly3Lm = lm(TotalTraffickLog ~ poly(TotalAll, 3), 
                    data = traffickCrime_2013to2021R)

summary(traffickCrimePoly3Lm)
# Multiple R-squared:  0.341,	Adjusted R-squared:  0.3342 
# F-statistic: 49.85 on 3 and 289 DF,  p-value: < 2.2e-16
  # About a 7% increase in explanation of variance from the adj. R squared in
  # the simple regression model with outliers


    # Without outliers
traffickCrimePoly3LmNoOutliers = lm(TotalTraffickLog ~ poly(TotalAll, 3), 
                    data = traffickCrime_2013to2021NoOutliers)

summary(traffickCrimePoly3LmNoOutliers)
# Multiple R-squared:  0.3503,	Adjusted R-squared:  0.3432 
# F-statistic:  48.9 on 3 and 272 DF,  p-value: < 2.2e-16
  # About a 7% increase in explanation of variance from the adj. R squared in
  # the simple regression model without outliers


  # Quadratic

    # With outliers
traffickCrimePoly4Lm = lm(TotalTraffickLog ~ poly(TotalAll, 4), 
                    data = traffickCrime_2013to2021R)

summary(traffickCrimePoly4Lm)
# Multiple R-squared:  0.3522,	Adjusted R-squared:  0.3432 
# F-statistic: 39.14 on 4 and 288 DF,  p-value: < 2.2e-16
  # About a 1% increase in explanation of variance from cubic


    # Without outliers
traffickCrimePoly4LmNoOutliers = lm(TotalTraffickLog ~ poly(TotalAll, 4), 
                    data = traffickCrime_2013to2021NoOutliers)

summary(traffickCrimePoly4LmNoOutliers)
# Multiple R-squared:  0.3638,	Adjusted R-squared:  0.3544 
# F-statistic: 38.74 on 4 and 271 DF,  p-value: < 2.2e-16
  # About a 1% increase in explanation of variance from cubic



# Plot of the data ----
  
  # With outliers - cubic
ggplot(traffickCrime_2013to2021R, 
       aes(x = TotalTraffickLog, y = TotalAll)) +
  geom_point() + 
  labs(x = "Trafficking Crimes", y = "All Crimes") +
  theme_minimal() +
  stat_smooth(
    method = "lm", formula = y ~ poly(x, 3), se = FALSE, color = "red")
# Upwards sloped line with moderately linear data + outliers

  # With outliers - quadratic
ggplot(traffickCrime_2013to2021R, 
       aes(x = TotalTraffickLog, y = TotalAll)) +
  geom_point() + 
  labs(x = "Trafficking Crimes", y = "All Crimes") +
  theme_minimal() +
  stat_smooth(
    method = "lm", formula = y ~ poly(x, 4), se = FALSE, color = "red")
# M-ish line with mostly linear data, still some outliers

  # Without outliers - cubic
ggplot(traffickCrime_2013to2021NoOutliers, 
       aes(x = TotalTraffickLog, y = TotalAll)) +
  geom_point() + 
  labs(x = "Trafficking Crimes", y = "All Crimes") +
  theme_minimal() +
  stat_smooth(
    method = "lm", formula = y ~ poly(x, 3), se = FALSE, color = "red")
# Almost identical to version with outliers

  # Without outliers - quadratic
ggplot(traffickCrime_2013to2021NoOutliers, 
       aes(x = TotalTraffickLog, y = TotalAll)) +
  geom_point() + 
  labs(x = "Trafficking Crimes", y = "All Crimes") +
  theme_minimal() +
  stat_smooth(
    method = "lm", formula = y ~ poly(x, 4), se = FALSE, color = "red")
# Almost identical to version with outliers



# Summary ----
# The relationship between trafficking arrests and total crime arrests is only 
# mildly linear, which means the results of a polynomial linear regression model 
# cannot be fully tested. That said, these are the results found for the percent 
# of variance in trafficking arrests that total crime arrests' predict:
  # With outliers
    # Cubic: 33%
    # Quadratic: 34%
  # Without outliers
    # Cubic: 34%
    # Quadratic: 35%
# Further analysis will be completed to validate this model's results.