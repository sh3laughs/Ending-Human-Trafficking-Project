# DSO110 - Data Science Final Project
  # File 3-E
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found in years where there are higher rates 
  # of reported non-trafficking sex crime arrests

# H0: Arrests for non-trafficking sex crimes do not predict arrests for 
  # trafficking crimes within the same year
# H1: Arrests for non-trafficking sex crimes effect do predict arrests for 
  # trafficking crimes within the same year

# IV's:
  # Rape arrests
  # Non-trafficking sex arrests
  # Year
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
traffickNonTraffickSexYear_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, Rape, Sex, TotalTraffick, Year)

View(traffickNonTraffickSexYear_2013to2021)
# 1,386 entries, 5 total columns


  # Drop non-total rows
traffickNonTraffickSexYear_2013to2021R = traffickNonTraffickSexYear_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickNonTraffickSexYear_2013to2021R)
# 459 entries, 5 total columns
  # Sample size still validated


  # Drop age column
traffickNonTraffickSexYear_2013to2021R = subset(
  traffickNonTraffickSexYear_2013to2021R, select = -(Age))

View(traffickNonTraffickSexYear_2013to2021R)
# 459 entries, 4 total columns


  # Remove rows with all 0's
traffickNonTraffickSexYear_2013to2021R = 
  traffickNonTraffickSexYear_2013to2021R[rowSums(
    traffickNonTraffickSexYear_2013to2021R[, -which(names(
      traffickNonTraffickSexYear_2013to2021R) == 'Year')] != 0) > 0, ]

View(traffickNonTraffickSexYear_2013to2021R)
# 459 entries, 4 total columns
  # Sample size validated



# Create multiple linear regression models ----

  # With all IV's
traffickNonTraffickSexYearLmAllIVs = lm(
  TotalTraffick ~ ., data = traffickNonTraffickSexYear_2013to2021R)
# Success

  # With no IV's
traffickNonTraffickSexYearLmNoIVs = lm(
  TotalTraffick ~ 1, data = traffickNonTraffickSexYear_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickNonTraffickSexYearLmAllIVs, direction = 'backward')
# Kept all three IV's

  # Forward selection
step(traffickNonTraffickSexYearLmNoIVs, direction = 'forward', 
     scope = formula(traffickNonTraffickSexYearLmAllIVs))
# Kept all three IV's
  # Glad it's aligned with BE
  # Added rape first, implying it has the strongest impact, then sex - this 
  # aligns with other analyses that find rape more significant than other 
  # non-trafficking sex crimes

  # Hybrid selection
step(traffickNonTraffickSexYearLmNoIVs, direction = 'both', 
     scope = formula(traffickNonTraffickSexYearLmAllIVs))
# Kept all three IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model ----
traffickNonTraffickSexYearLm = lm(
  formula = TotalTraffick ~ Rape * Sex * Year, 
    data = traffickNonTraffickSexYear_2013to2021R)

summary(traffickNonTraffickSexYearLm)
# Residuals:
#      Min       1Q   Median       3Q      Max 
# -10359.0   -651.1   -118.7    225.2  13174.8 
# Coefficients:
#                 Estimate Std. Error t value Pr(>|t|)    
# (Intercept)    1.743e+05  1.418e+05   1.229  0.21959    
# Rape          -4.474e+03  3.707e+02 -12.071  < 2e-16 ***
# Sex            8.374e+02  2.796e+02   2.995  0.00289 ** 
# Year          -8.655e+01  7.031e+01  -1.231  0.21894    
# Rape:Sex       2.397e-01  1.328e-01   1.805  0.07171 .  
# Rape:Year      2.222e+00  1.838e-01  12.092  < 2e-16 ***
# Sex:Year      -4.159e-01  1.387e-01  -2.998  0.00287 ** 
# Rape:Sex:Year -1.188e-04  6.588e-05  -1.804  0.07197 .  
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 2586 on 448 degrees of freedom
# Multiple R-squared:  0.5808,	Adjusted R-squared:  0.5743 
# F-statistic: 88.68 on 7 and 448 DF,  p-value: < 2.2e-16
  # Super interesting - this determined that rape and sex are each significant
  # predictors on their own, and that on their own there are also significant
  # differences by year; reject the null and accept the alternative hypothesis
  # Also interesting that it did not find their combined impact significant, at
  # all or by year, and it did find significance by year
  # Incredibly interesting how results vary so much by analysis - and makes 
  # the importance of multiple analyses even more clear



# Re-wrangling to better meet assumptions ----

  # Transform DV
traffickNonTraffickSexYear_2013to2021R$TotalTraffickLog = log(
  traffickNonTraffickSexYear_2013to2021R$TotalTraffick)

View(traffickNonTraffickSexYear_2013to2021R)
# 456 entries, 5 total columns
  # Lots of infinite values

      # Drop NA's
traffickNonTraffickSexYear_2013to2021R = NaRV.omit(
  traffickNonTraffickSexYear_2013to2021R)

View(traffickNonTraffickSexYear_2013to2021R)
# 293 entries, 5 total columns
  # Sample size still validated

      # Drop original column
traffickNonTraffickSexYear_2013to2021R = subset(
  traffickNonTraffickSexYear_2013to2021R, select = -(TotalTraffick))

View(traffickNonTraffickSexYear_2013to2021R)
# 293 entries, 4 total columns


  # Drop outliers
    # Leverage
traffickNonTraffickSexYearLev = hat(
  model.matrix(traffickNonTraffickSexYearLm))

plot(traffickNonTraffickSexYearLev)

traffickNonTraffickSexYear_2013to2021R[traffickNonTraffickSexYearLev > .2,]
# Leverage outliers: 51, 52, 53, 59, 60, 61


    # Distance
car::outlierTest(traffickNonTraffickSexYearLm)
# Distance outliers: 386, 246, 202, 249, 381, 251, 385, 77, 387, 252


    # Influential
summary(influence.measures(traffickNonTraffickSexYearLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include some identified above - the ones 
  # identified are rows:
  # 19, 23, 26, 37, 38, 39, 40, 41, 42, 43, 44, 73, 74, 75, 77, 78, 79, 80, 82, 
  # 83, 84, 85, 86, 87, 89, 90, 157, 195, 197, 198, 202, 203, 246, 249, 250, 
  # 251, 252, 280, 286, 287, 334, 338, 339, 379, 380, 381, 382, 383, 384, 385, 
  # 386, 387, 442


    # Remove outliers
traffickNonTraffickSexYearNoOutliers = 
  traffickNonTraffickSexYear_2013to2021R[-c(
    51, 52, 53, 59, 60, 61, 386, 246, 202, 249, 381, 251, 385, 77, 387, 252, 19,
    23, 26, 37, 38, 39, 40, 41, 42, 43, 44, 73, 74, 75, 77, 78, 79, 80, 82, 
    83, 84, 85, 86, 87, 89, 90, 157, 195, 197, 198, 203, 250, 251, 252, 280, 
    286, 287, 334, 338, 339, 379, 380, 382, 383, 384, 387, 442),]

View(traffickNonTraffickSexYearNoOutliers)
# 247 entries, 4 total columns
  # Sample size still validated




# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
traffickNonTraffickSexYearNoOutliersLmAllIVs = lm(
  TotalTraffickLog ~ ., data = traffickNonTraffickSexYearNoOutliers)
# Success

  # With no IV's
traffickNonTraffickSexYearNoOutliersLmNoIVs = lm(
  TotalTraffickLog ~ 1, data = traffickNonTraffickSexYearNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickNonTraffickSexYearNoOutliersLmAllIVs, direction = 'backward')
# Kept all three IV's again - hurray

  # Forward selection
step(traffickNonTraffickSexYearNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(traffickNonTraffickSexYearNoOutliersLmAllIVs))
# Removed year
  # Added rape first again

  # Hybrid selection
step(traffickNonTraffickSexYearNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(traffickNonTraffickSexYearNoOutliersLmAllIVs))
# Identical results to FS option - so two of the three options without outliers 
  # are the same



# Analyze model without outliers ----
traffickNonTraffickSexYearNoOutliersLm = lm(
  formula = TotalTraffickLog ~ Rape * Sex * Year, 
    data = traffickNonTraffickSexYearNoOutliers)

summary(traffickNonTraffickSexYearNoOutliersLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -4.8426 -0.7969 -0.0354  0.8878  3.2552 
# Coefficients:
#                 Estimate Std. Error t value Pr(>|t|)  
# (Intercept)   -1.989e+02  1.177e+02  -1.690   0.0924 .
# Rape          -2.449e-01  2.552e-01  -0.960   0.3383  
# Sex           -3.361e-01  1.823e-01  -1.843   0.0665 .
# Year           1.012e-01  5.831e-02   1.736   0.0839 .
# Rape:Sex       2.165e-04  8.733e-05   2.479   0.0139 *
# Rape:Year      1.226e-04  1.265e-04   0.969   0.3335  
# Sex:Year       1.671e-04  9.043e-05   1.848   0.0658 .
# Rape:Sex:Year -1.076e-07  4.331e-08  -2.485   0.0136 *
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.221 on 239 degrees of freedom
# Multiple R-squared:  0.4652,	Adjusted R-squared:  0.4495 
# F-statistic:  29.7 on 7 and 239 DF,  p-value: < 2.2e-16
  # This again determined that the combined effect of rape and other 
  # non-trafficking sex crime arrests is a significant predictors and that there
  # are differences by year for their combined effect; reject the null and 
  # accept the alternative hypothesis
  # It did not find significance for these arrests on their own, or for year on
  # its own



# Test assumptions post hoc ----

  # Linearity

    # With outliers
ggplot(traffickNonTraffickSexYear_2013to2021R, aes(
  x = TotalTraffickLog, y = Rape + Sex + Year)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-Trafficking Sex Crimes by Year') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(traffickNonTraffickSexYearNoOutliers, aes(
  x = TotalTraffickLog, y = Rape + Sex + Year)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-Trafficking Sex Crimes by Year') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Almost identical to version with outliers


  # Homoscedasticity

    # With outliers
lmtest::bptest(traffickNonTraffickSexYearLm)
# 	studentized Breusch-Pagan test
# data:  traffickNonTraffickSexYearLm
# BP = 133.9, df = 7, p-value < 2.2e-16
  # This p value below 0.05 violates the assumption of homoscedasticity


    # Without outliers
lmtest::bptest(traffickNonTraffickSexYearNoOutliersLm)
# 	studentized Breusch-Pagan test
# data:  traffickNonTraffickSexYearNoOutliersLm
# BP = 12.254, df = 7, p-value = 0.09251
  # This p value above 0.05 validates the assumption of homoscedasticity



# Summary ----
# The relationship between trafficking arrests, non-trafficking sex crime
# arrests, and year is only mildly linear and with outliers is not 
# homoscedastic, which means the results of a stepwise multiple linear 
# regression model cannot be fully tested. That said, with and without outliers, 
# this model determined that the ability of non-trafficking sex crime arrests to 
# predict trafficking arrests does vary significantly by year.