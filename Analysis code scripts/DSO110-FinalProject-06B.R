# DSO110 - Data Science Final Project
  # File 6-B
  # Analysis: Polynomial linear regression

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


  # Transform DV
suicideTraffick_2013to2021R$TotalSuicideLog = log(
  suicideTraffick_2013to2021R$TotalSuicide)

View(suicideTraffick_2013to2021R)
# 459 entries, 3 total columns
  # Some infinite values

      # Drop NA's
suicideTraffick_2013to2021R = NaRV.omit(
  suicideTraffick_2013to2021R)

View(suicideTraffick_2013to2021R)
# 457 entries, 3 total columns
  # Sample size still validated


  # Drop outliers
suicideTraffickNoOutliers = suicideTraffick_2013to2021R[-c(
  385, 386, 387, 431, 80, 89, 90, 202, 203, 205, 246, 249, 250, 251, 252, 351, 
  380, 381, 382, 383, 384, 424, 425, 426, 427, 428, 429, 430),]

View(suicideTraffickNoOutliers)
# 429 entries, 3 total columns
  # Sample size still validated



# Create polynomial regression models ----

  # Cubic

    # With outliers
suicideTraffickPoly3Lm = lm(TotalSuicideLog ~ poly(TotalTraffick, 3),
                            data = suicideTraffick_2013to2021R)

summary(suicideTraffickPoly3Lm)
# Multiple R-squared:  0.1969,	Adjusted R-squared:  0.1916 
# F-statistic: 37.02 on 3 and 453 DF,  p-value: < 2.2e-16
  # About a 4% increase in explanation of variance from the adj. R squared in 
  # the simple regression model with outliers

    # Without outliers
suicideTraffickPoly3LmNoOutliers = lm(TotalSuicideLog ~ poly(TotalTraffick, 3),
                            data = suicideTraffickNoOutliers)

summary(suicideTraffickPoly3LmNoOutliers)
# Multiple R-squared:  0.1773,	Adjusted R-squared:  0.1715 
# F-statistic: 30.53 on 3 and 425 DF,  p-value: < 2.2e-16
  # About a 3% increase in explanation of variance from the adj. R squared in 
  # the simple regression model with outliers


  # Quadratic

    # With outliers
suicideTraffickPoly4Lm = lm(TotalSuicideLog ~ poly(TotalTraffick, 4),
                            data = suicideTraffick_2013to2021R)

summary(suicideTraffickPoly4Lm)
# Multiple R-squared:  0.207,	Adjusted R-squared:    0.2 
# F-statistic:  29.5 on 4 and 452 DF,  p-value: < 2.2e-16
  # About a 1% increase in explanation of variance from the adj. R squared in
  # the cubic model

    # Without outliers
suicideTraffickPoly4LmNoOutliers = lm(TotalSuicideLog ~ poly(TotalTraffick, 4),
                            data = suicideTraffickNoOutliers)

summary(suicideTraffickPoly4LmNoOutliers)
# Multiple R-squared:  0.1817,	Adjusted R-squared:  0.174 
# F-statistic: 23.54 on 4 and 424 DF,  p-value: < 2.2e-16
  # Only a fractional difference in results from the adj. R squared in the 
  # cubic model



# Plot of the data ----
  
  # With outliers - cubic
ggplot(suicideTraffick_2013to2021R, 
       aes(x = TotalSuicideLog, y = TotalTraffick)) +
  geom_point() + 
  labs(x = 'Suicides', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(
    method = 'lm', formula = y ~ poly(x, 3), se = FALSE, color = 'red')
# Mildly upwards curved s-ish line with very mildly linear data + outliers

  # With outliers - quadratic
ggplot(suicideTraffick_2013to2021R, 
       aes(x = TotalSuicideLog, y = TotalTraffick)) +
  geom_point() + 
  labs(x = 'Suicides', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(
    method = 'lm', formula = y ~ poly(x, 4), se = FALSE, color = 'red')
# Slightly upwards curved w-ish line with very mildly linear data + outliers

  # Without outliers - cubic
ggplot(suicideTraffickNoOutliers, aes(x = TotalSuicideLog, y = TotalTraffick)) +
  geom_point() + 
  labs(x = 'Suicides', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(
    method = 'lm', formula = y ~ poly(x, 3), se = FALSE, color = 'red')
# Pretty much the same as the version with outliers

  # Without outliers - quadratic
ggplot(suicideTraffickNoOutliers, aes(x = TotalSuicideLog, y = TotalTraffick)) +
  geom_point() + 
  labs(x = 'Suicides', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(
    method = 'lm', formula = y ~ poly(x, 4), se = FALSE, color = 'red')
# Similar to the version with outliers



# Summary ----
# The relationship between suicides and trafficking crime arrests is not linear, 
# which means the results of a linear regression model cannot be fully tested. 
# That said, these are the results found for the percent of variance in suicides
# that trafficking crime arrests' predict:
  # With outliers
    # Cubic: 19%
    # Quadratic: 17%
  # Without outliers
    # Cubic: 20%
    # Quadratic: 17%
# Further analysis will be completed to validate this model's results.