# DSO110 - Data Science Final Project
  # File 3-D
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found in states  where there are higher rates 
  # of reported non-trafficking sex crime arrests

# H0: Arrests for non-trafficking sex crimes do not predict arrests for 
  # trafficking crimes within the same state
# H1: Arrests for non-trafficking sex crimes effect do predict arrests for 
  # trafficking crimes within the same state

# IV's:
  # Rape arrests
  # Non-trafficking sex arrests
  # State
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
traffickNonTraffickSexState_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, Rape, Sex, State, TotalTraffick)

View(traffickNonTraffickSexState_2013to2021)
# 1,386 entries, 5 total columns


  # Drop non-total rows
traffickNonTraffickSexState_2013to2021R = traffickNonTraffickSexState_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickNonTraffickSexState_2013to2021R)
# 459 entries, 5 total columns
  # Sample size still validated


  # Drop age column
traffickNonTraffickSexState_2013to2021R = subset(
  traffickNonTraffickSexState_2013to2021R, select = -(Age))

View(traffickNonTraffickSexState_2013to2021R)
# 459 entries, 4 total columns


  # Remove rows with all 0's
traffickNonTraffickSexState_2013to2021R = 
  traffickNonTraffickSexState_2013to2021R[rowSums(
    traffickNonTraffickSexState_2013to2021R[, -which(names(
      traffickNonTraffickSexState_2013to2021R) == 'State')] != 0) > 0, ]

View(traffickNonTraffickSexState_2013to2021R)
# 456 entries, 4 total columns
  # Sample size validated



# Create multiple linear regression models ----

  # With all IV's
traffickNonTraffickSexStateLmAllIVs = lm(
  TotalTraffick ~ ., data = traffickNonTraffickSexState_2013to2021R)
# Success

  # With no IV's
traffickNonTraffickSexStateLmNoIVs = lm(
  TotalTraffick ~ 1, data = traffickNonTraffickSexState_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickNonTraffickSexStateLmAllIVs, direction = 'backward')
# Kept all three IV's

  # Forward selection
step(traffickNonTraffickSexStateLmNoIVs, direction = 'forward', 
     scope = formula(traffickNonTraffickSexStateLmAllIVs))
# Kept all three IV's
  # Glad it's aligned with BE
  # Added state first, implying it has the strongest impact, then rape, then
  # sex - this aligns with other analyses that find rape more significant than
  # other non-trafficking sex crimes

  # Hybrid selection
step(traffickNonTraffickSexStateLmNoIVs, direction = 'both', 
     scope = formula(traffickNonTraffickSexStateLmAllIVs))
# Kept all three IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model ----
traffickNonTraffickSexStateLm = lm(
  formula = TotalTraffick ~ Rape * Sex * State, 
    data = traffickNonTraffickSexState_2013to2021R)

options(max.print = 2000)

summary(traffickNonTraffickSexStateLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -8277.3  -180.3    -6.0   135.1  9473.0 
# Coefficients:
#                                Estimate Std. Error t value Pr(>|t|)      
# (Intercept)                   1.694e+02  7.209e+02   0.235 0.814432
# ...
# StateNEVADA                  -6.447e+04  1.667e+04  -3.868 0.000140 ***
# ...
# StateTEXAS                    5.877e+04  1.714e+04   3.430 0.000706 ***
# ...
# Rape:StateNEVADA              2.422e+02  5.510e+01   4.396 1.63e-05 ***
# ...
# Sex:StateNEVADA               4.684e+01  2.257e+01   2.076 0.038931 *
# ...
# Rape:Sex:StateNEVADA         -1.654e-01  5.847e-02  -2.829 0.005046 **
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1491 on 252 degrees of freedom
# Multiple R-squared:  0.9217,	Adjusted R-squared:  0.8586 
# F-statistic: 14.61 on 203 and 252 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
  # What it determined is that there is a significant difference in the 
  # predictive abilities of rape, other non-trafficking sex crimes, and their 
  # combined effect for Nevada than all other states



# Re-wrangling to better meet assumptions ----

  # Transform DV
traffickNonTraffickSexState_2013to2021R$TotalTraffickLog = log(
  traffickNonTraffickSexState_2013to2021R$TotalTraffick)

View(traffickNonTraffickSexState_2013to2021R)
# 456 entries, 5 total columns
  # Lots of infinite values

      # Drop NA's
traffickNonTraffickSexState_2013to2021R = NaRV.omit(
  traffickNonTraffickSexState_2013to2021R)

View(traffickNonTraffickSexState_2013to2021R)
# 293 entries, 5 total columns
  # Sample size still validated

      # Drop original column
traffickNonTraffickSexState_2013to2021R = subset(
  traffickNonTraffickSexState_2013to2021R, select = -(TotalTraffick))

View(traffickNonTraffickSexState_2013to2021R)
# 293 entries, 4 total columns


  # Drop outliers

    # Find leverage
traffickNonTraffickSexStateLev = hat(
  model.matrix(traffickNonTraffickSexStateLm))

plot(traffickNonTraffickSexStateLev)

traffickNonTraffickSexState_2013to2021R[traffickNonTraffickSexStateLev > .2,]
# This found a ton...


    # Distance
car::outlierTest(traffickNonTraffickSexStateLm)
#      rstudent unadjusted p-value Bonferroni p
# 80   7.730246         2.5884e-13   1.1803e-10
# 202  6.913274         3.9001e-11   1.7785e-08
# 248 -6.496536         4.3848e-10   1.9995e-07
# 77  -5.166130         4.8738e-07   2.2225e-04
# 199 -4.224411         3.3543e-05   1.5296e-02
  # Distance outliers: 80, 202, 248, 77, 199


    # Influential
summary(influence.measures(traffickNonTraffickSexStateLm))
# This determined several rows have low significance - none more influential
  # than that, 6 seemed to be most significant, but overall it found:
  # 3, 4, 6, 11, 13, 15, 17, 18, 19


    # Remove outliers
traffickNonTraffickSexStateNoOutliers = traffickNonTraffickSexState_2013to2021R[-c(
  80, 202, 248, 77, 199, 3, 4, 6, 11, 13, 15, 17, 18, 19),]

View(traffickNonTraffickSexStateNoOutliers)
# 279 entries, 4 total columns
  # Sample size still validated



# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
traffickNonTraffickSexStateNoOutliersLmAllIVs = lm(
  TotalTraffickLog ~ ., data = traffickNonTraffickSexStateNoOutliers)
# Success

  # With no IV's
traffickNonTraffickSexStateNoOutliersLmNoIVs = lm(
  TotalTraffickLog ~ 1, data = traffickNonTraffickSexStateNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickNonTraffickSexStateNoOutliersLmAllIVs, direction = 'backward')
# Kept all three IV's again

  # Forward selection
step(traffickNonTraffickSexStateNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(traffickNonTraffickSexStateNoOutliersLmAllIVs))
# Kept all three IV's again
  # Also added state first, again

  # Hybrid selection
step(traffickNonTraffickSexStateNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(traffickNonTraffickSexStateNoOutliersLmAllIVs))
# Results identical to FS



# Analyze model without outliers ----
traffickNonTraffickSexStateNoOutliersLm = lm(
  formula = TotalTraffickLog ~ Rape * Sex * State, 
  data = traffickNonTraffickSexStateNoOutliers)

summary(traffickNonTraffickSexStateNoOutliersLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -1.8645 -0.1185  0.0000  0.1375  1.5923 
# Coefficients: (15 not defined because of singularities)
#                                Estimate Std. Error t value Pr(>|t|)    
# (Intercept)                   3.871e+00  7.122e-01   5.436 4.63e-07 ***
# ...
# StateKENTUCKY                     -1.282e+02  3.780e+01  -3.390  0.00104 **
# ...
# StateMARYLAND                       5.402e+00  2.133e+00   2.532  0.01307 *
# ...
# StateSOUTH DAKOTA                   1.713e+01  8.395e+00   2.040  0.04426 *  
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 0.7122 on 90 degrees of freedom
# Multiple R-squared:  0.9383,	Adjusted R-squared:  0.8095 
# F-statistic: 7.285 on 188 and 90 DF,  p-value: < 2.2e-16
  # Though the model overall is significant, it did not find a significant 
  # difference in the impact of non-trafficking sex crime arrests based on 
  # state; accept the null and reject the alternative hypothesis
  # In fact, it only found an impact from a few specific states (included in
  # results truncated above), not from non-trafficking sex crime arrests without 
  # state, which is interesting, since different from results above



# Test assumptions post hoc on data ----

  # Linearity

    # With outliers
ggplot(traffickNonTraffickSexState_2013to2021R, aes(
  x = TotalTraffickLog, y = Rape, Sex, State)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-Trafficking Sex Crimes by State') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(traffickNonTraffickSexStateNoOutliers, aes(
  x = TotalTraffickLog, y = Rape, Sex, State)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-Trafficking Sex Crimes by State') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Pretty much identical to the version with outliers...


  # Homoscedasticity

    # With outliers
lmtest::bptest(traffickNonTraffickSexStateLm)
# 	studentized Breusch-Pagan test
# data:  traffickNonTraffickSexStateLm
# BP = 177.71, df = 203, p-value = 0.8994
  # This p value above 0.05 validates the assumption of homoscedasticity

    # With outliers
lmtest::bptest(traffickNonTraffickSexStateNoOutliersLm)
# data:  traffickNonTraffickSexStateNoOutliersLm
# BP = 186.05, df = 188, p-value = 0.5265
  # This p value above 0.05 validates the assumption of homoscedasticity



# Summary ----
# The relationship between trafficking arrests, non-trafficking sex crime
# arrests, and state is only mildly linear, which means the results of a 
# stepwise multiple linear regression model cannot be fully tested. That said, 
# with outliers this model determined that the ability of non-trafficking sex 
# crime arrests to predict trafficking crime arrests does vary by state, and 
# without outliers it does not.