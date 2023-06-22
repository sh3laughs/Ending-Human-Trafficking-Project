# DSO110 - Data Science Final Project
  # File 3-B
  # Analysis: Polynomial linear regression

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found where there are higher rates of reported 
  # non-trafficking sex crime arrests

# H0: Arrests for non-trafficking sex crimes do not predict arrests for 
  # trafficking crimes
# H1: Arrests for non-trafficking sex crimes effect do predict arrests for 
  # trafficking crimes

# IV's:
  # Rape arrests
  # Non-trafficking sex arrests
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
traffickNonTraffickSex_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, Rape, Sex, TotalTraffick)

View(traffickNonTraffickSex_2013to2021)
# 1,386 entries, 4 total columns


  # Drop non-total rows
traffickNonTraffickSex_2013to2021R = traffickNonTraffickSex_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickNonTraffickSex_2013to2021R)
# 459 entries, 4 total columns
  # Sample size still validated


  # Drop age column
traffickNonTraffickSex_2013to2021R = subset(
  traffickNonTraffickSex_2013to2021R, select = -(Age))

View(traffickNonTraffickSex_2013to2021R)
# 459 entries, 3 total columns


  # Transform DV
traffickNonTraffickSex_2013to2021R$TotalTraffickLog = log(
  traffickNonTraffickSex_2013to2021R$TotalTraffick)

View(traffickNonTraffickSex_2013to2021R)
# 459 entries, 4 total columns
  # Lots of infinite values

      # Drop NA's
traffickNonTraffickSex_2013to2021R = NaRV.omit(
  traffickNonTraffickSex_2013to2021R)

View(traffickNonTraffickSex_2013to2021R)
# 293 entries, 4 total columns
  # Sample size still validated


  # Drop outliers
traffickNonTraffickSexNoOutliers = traffickNonTraffickSex_2013to2021R[-c(
  37, 38, 39, 40, 41, 42, 43, 44, 74, 76, 78, 79, 80, 380, 381, 382, 383, 384, 
  385, 386, 387, 286, 431),]

View(traffickNonTraffickSexNoOutliers)
# 279 entries, 4 total columns
  # Sample size still validated



# Create polynomial regression models ----

  # Cubic

    # With outliers
traffickNonTraffickPoly3Lm = lm(TotalTraffickLog ~ poly(Rape + Sex, 3), 
                    data = traffickNonTraffickSex_2013to2021R)

summary(traffickNonTraffickPoly3Lm)
# Multiple R-squared:  0.3641,	Adjusted R-squared:  0.3575 
# F-statistic: 55.17 on 3 and 289 DF,  p-value: < 2.2e-16
  # About a 2% increase in explanation of variance from the adj. R squared in
  # the simple regression model with outliers


    # Without outliers
traffickNonTraffickPoly3LmNoOutliers = lm(
  TotalTraffickLog ~ poly(Rape + Sex, 3), 
  data = traffickNonTraffickSexNoOutliers)

summary(traffickNonTraffickPoly3LmNoOutliers)
# Multiple R-squared:  0.374,	Adjusted R-squared:  0.3671 
# F-statistic: 54.76 on 3 and 275 DF,  p-value: < 2.2e-16
  # About a 3% increase in explanation of variance from the adj. R squared in 
    # the simple regression model without outliers


  # Quadratic

    # With outliers
traffickNonTraffickPoly4Lm = lm(TotalTraffickLog ~ poly(Rape + Sex, 4), 
                    data = traffickNonTraffickSex_2013to2021R)

summary(traffickNonTraffickPoly4Lm)
# Multiple R-squared:  0.3684,	Adjusted R-squared:  0.3596 
# F-statistic:    42 on 4 and 288 DF,  p-value: < 2.2e-16
  # Only a fractional difference in results from cubic


    # Without outliers
traffickNonTraffickPoly4LmNoOutliers = lm(
  TotalTraffickLog ~ poly(Rape + Sex, 4), 
  data = traffickNonTraffickSexNoOutliers)

summary(traffickNonTraffickPoly4LmNoOutliers)
# Multiple R-squared:  0.3781,	Adjusted R-squared:  0.369 
# F-statistic: 41.64 on 4 and 274 DF,  p-value: < 2.2e-16
  # Only a fractional difference in results from cubic



# Plot of the data ----
  
  # With outliers - cubic
ggplot(traffickNonTraffickSex_2013to2021R, 
       aes(x = TotalTraffickLog, y = Rape + Sex)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-trafficking Sex Crimes') +
  theme_minimal() +
  stat_smooth(
    method = 'lm', formula = y ~ poly(x, 3), se = FALSE, color = 'red')
# U-ish line with mildly linear data + outliers

  # With outliers - quadratic
ggplot(traffickNonTraffickSex_2013to2021R, 
       aes(x = TotalTraffickLog, y = Rape + Sex)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-trafficking Sex Crimes') +
  theme_minimal() +
  stat_smooth(
    method = 'lm', formula = y ~ poly(x, 4), se = FALSE, color = 'red')
# M-ish line with mostly linear data, still some outliers

  # Without outliers - cubic
ggplot(traffickNonTraffickSexNoOutliers, 
       aes(x = TotalTraffickLog, y = Rape + Sex)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-trafficking Sex Crimes') +
  theme_minimal() +
  stat_smooth(
    method = 'lm', formula = y ~ poly(x, 3), se = FALSE, color = 'red')
# U-ish line with mostly linear data, still some outliers

  # Without outliers - quadratic
ggplot(traffickNonTraffickSexNoOutliers, 
       aes(x = TotalTraffickLog, y = Rape + Sex)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-trafficking Sex Crimes') +
  theme_minimal() +
  stat_smooth(
    method = 'lm', formula = y ~ poly(x, 4), se = FALSE, color = 'red')
# M-ish line with mostly linear data, still some outliers



# Summary ----
# The relationship between trafficking arrests and non-trafficking sex crime
# arrests is not linear, which means the results of a polynomial linear 
# regression model cannot be fully tested. That said, with and without outliers, 
# the cubic model shows that together rape and non-trafficking sex crime 
# arrests predict approximately 36% of the variance in trafficking arrests and 
# the quadratic model shows that together rape and non-trafficking sex crime 
# arrests predict approximately 37% of the variance in trafficking arrests. 
# Further analysis will be completed to # validate this model's results.