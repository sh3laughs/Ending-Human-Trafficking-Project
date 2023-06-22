# DSO110 - Data Science Final Project
  # File 5
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether there are any other correlations between reported 
  # non-trafficking arrests and trafficking crime arrests in the FBI data

# H0: No non-trafficking crime arrests predict arrests for trafficking crimes
# H1: Arrests for one or more non-trafficking crimes predict arrests for 
  # trafficking crimes

# IV: 
  # Before testing: TBD
  # After testing: All crimes other than burglary
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

  # Subset to only include crime data (without total categories)
traffickCrime_2013to2021 = traffickingCrime_2013to2021 %>% select(
  Age, TotalTraffick, Rape, Sex, AggravatedAssault, AllOther, Arson, Assault, 
  Burglary, CarTheft, CurfewLoitering, DisorderlyConduct, DrugAbuse, 
  Drunkenness, DUI, Embezzlement, FamilyChildren, ForgeryCounterfeit, Fraud, 
  Gambling, Larceny, LiquorLaws, MurderManslaughter, Robbery, StolenProperty, 
  Suspicion, Vagrancy, Vandalism, Weapons)

View(traffickCrime_2013to2021)
# 1,386 entries, 29 total columns


  # Drop non-total rows
traffickCrime_2013to2021R = traffickCrime_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickCrime_2013to2021R)
# 459 entries, 29 total columns
  # Sample size still validated


  # Drop age column
traffickCrime_2013to2021R = subset(
  traffickCrime_2013to2021R, select = -(Age))

View(traffickCrime_2013to2021R)
# 459 entries, 28 total columns



# Create multiple linear regression models ----

  # With all IV's
traffickCrimeLmAllIVs = lm(TotalTraffick ~ ., data = traffickCrime_2013to2021R)
# Success

  # With no IV's
traffickCrimeLmNoIVs = lm(TotalTraffick ~ 1, data = traffickCrime_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCrimeLmAllIVs, direction = 'backward')
# Removed liquor laws, burglary, fraud, vandalism, car theft, suspicion, 
# gambling, curfew / loitering, drunkenness, aggravated assault, all other, and,
# weapons - in that order

  # Forward selection
step(traffickCrimeLmNoIVs, direction = 'forward', scope = formula(
  traffickCrimeLmAllIVs))
# Removed drunkenness, all other, aggravated assault, car theft, gambling, 
  # suspicious, liquor laws, burglary, vandalism, fraud, curfew / loitering
  # Aligned with backward elimination other than keeping weapons - which is 
  # interesting b/c it was the last crime removed in BE model and first added 
  # after sex crimes in this one
  # Also noteworthy that rape and non-trafficking sex crime arrests were the 
  # first two crimes to be added, based on impact, implying they are the 
  # strongest predictors of trafficking crime arrests

  # Hybrid selection
step(traffickCrimeLmNoIVs, direction = 'both', scope = formula(
  traffickCrimeLmAllIVs))
# Removed weapons, drunkenness, gambling, aggravated assault, burglary, car
  # theft, suspicion, all other, liquor laws, curfew / loitering, fraud, and
  # vandalism
  # Aligned with BE
  # Like forward selection, rape and non-trafficking sex crime arrests were
  # added first



# Analyze models ----

  # Backward elimination
traffickCrimeLmBE = lm(
  formula = TotalTraffick ~ Rape + Sex + Arson + Assault + DisorderlyConduct + 
    DrugAbuse + DUI + Embezzlement + FamilyChildren + ForgeryCounterfeit + 
    Larceny + MurderManslaughter + Robbery + StolenProperty + 
    Vagrancy, data = traffickCrime_2013to2021R)

summary(traffickCrimeLmBE)
# Residuals:
#      Min       1Q   Median       3Q      Max 
# -10088.6   -988.8   -232.1    479.8  12875.2 
# Coefficients:
#                      Estimate Std. Error t value Pr(>|t|)    
# (Intercept)        -186.57962  186.19271  -1.002  0.31685    
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 2317 on 443 degrees of freedom
# Multiple R-squared:  0.6677,	Adjusted R-squared:  0.6565 
# F-statistic: 59.35 on 15 and 443 DF,  p-value: < 2.2e-16
  # All crimes' arrests other than arson  are individually significant with 
    # varying degrees of significance, and together have high significance and 
    # explain ~66% of the variance in trafficking crime arrests; reject the null 
    # and accept the alternative hypothesis

    # With high significance, a one unit increase in:
# Rape arrests predict a 6.40692 increase in trafficking crime arrests
# Assault arrests predict a 0.16357 increase in trafficking crime arrests
# DUI arrests predict a 0.10800 increase in trafficking crime arrests
# Embezzlement arrests predict a 4.21867 decrease in trafficking crime arrests
# Larceny arrests predict a 0.15752 decrease in trafficking crime arrests
# MurderManslaughter arrests predict a 11.40444 increase in trafficking crime 
  # arrests
# Robbery arrests predict a 1.30514 decrease in trafficking crime arrests
# StolenProperty arrests predict a 0.62772 decrease in trafficking crime arrests
# Vagrancy arrests predict a 1.57516 increase in trafficking crime arrests

    # With moderate significance, a one unit increase in:
# Sex arrests predict a 1.03199 decrease in trafficking crime arrests
# DisorderlyConduct arrests predict a 0.07114 decrease in trafficking crime 
  # arrests
# FamilyChildren arrests predict a 0.29609 increase in trafficking crime arrests
# ForgeryCounterfeit arrests predict a 0.99098 increase in trafficking crime 
  # arrests

    # With low significance, a one unit increase in:
# DrugAbuse arrests predict a 0.04023 decrease in trafficking crime arrests

    # There is no significant impact from:
# Arson


  # Forward selection
traffickCrimeLmFS = lm(
  formula = TotalTraffick ~ Rape + Sex + Weapons + Robbery + 
    Vagrancy + Assault + Embezzlement + Larceny + ForgeryCounterfeit + 
    MurderManslaughter + StolenProperty + DUI + Arson + FamilyChildren + 
    DisorderlyConduct + DrugAbuse, data = traffickCrime_2013to2021R)

summary(traffickCrimeLmFS)
# Residuals:
#      Min       1Q   Median       3Q      Max 
# -10283.9   -997.9   -223.9    458.9  12825.8 
# Coefficients:
#                      Estimate Std. Error t value Pr(>|t|)    
# (Intercept)        -161.66695  188.96117  -0.856  0.39271 
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 2318 on 442 degrees of freedom
# Multiple R-squared:  0.6682,	Adjusted R-squared:  0.6562 
# F-statistic: 55.63 on 16 and 442 DF,  p-value: < 2.2e-16
  # Most variables are individually significant with varying degrees of 
    # significance, and together have high significance and explain ~66% of the 
    # variance in trafficking crime arrests; reject the null and accept the 
    # alternative hypothesis
    # The stats are similar to BE model

    # With high significance, a one unit increase in:
# Rape arrests predict a 6.33253 increase in trafficking crime arrests
# Robbery arrests predict a 1.27904 decrease in trafficking crime arrests
# Vagrancy arrests predict a 1.55918 increase in trafficking crime arrests
# Assault arrests predict a 0.15706 increase in trafficking crime arrests
# Embezzlement arrests predict a 4.16919 decrease in trafficking crime arrests
# Larceny arrests predict a 0.14654 decrease in trafficking crime arrests
# MurderManslaughter arrests predict a 10.53708 increase in trafficking crime 
  # arrests
# StolenProperty arrests predict a 0.62889 decrease in trafficking crime arrests
# DUI arrests predict a 0.10010 increase in trafficking crime arrests

    # With moderate significance, a one unit increase in:
# Sex arrests predict a 1.08349 decrease in trafficking crime arrests
# ForgeryCounterfeit arrests predict a 1.02668 increase in trafficking crime 
  # arrests
# FamilyChildren arrests predict a 0.29010 increase in trafficking crime arrests
# DisorderlyConduct arrests predict a 0.07154 decrease in trafficking crime 
  # arrests
# DrugAbuse arrests predict a 0.04211 decrease in trafficking crime arrests

    # There is no significant impact from:
# Weapons
# Arson


  # Hybrid selection
traffickCrimeLmHS = lm(
  formula = TotalTraffick ~ Rape + Sex + Robbery + Vagrancy + 
    Assault + Embezzlement + Larceny + ForgeryCounterfeit + MurderManslaughter + 
    StolenProperty + DUI + Arson + FamilyChildren + DisorderlyConduct + 
    DrugAbuse, data = traffickCrime_2013to2021R)

summary(traffickCrimeLmHS)
# Results are identical to BE model, as expected (though listed in different 
  # order ;)



# Re-wrangling to better meet assumptions ----

  # Transform DV
traffickCrime_2013to2021R$TotalTraffickLog = log(
  traffickCrime_2013to2021R$TotalTraffick)

View(traffickCrime_2013to2021R)
# 459 entries, 29 total columns
  # Lots of infinite values

      # Drop NA's
traffickCrime_2013to2021R = NaRV.omit(traffickCrime_2013to2021R)

View(traffickCrime_2013to2021R)
# 293 entries, 29 total columns
  # Sample size still validated

      # Drop original column
traffickCrime_2013to2021R = subset(
  traffickCrime_2013to2021R, select = -(TotalTraffick))

View(traffickCrime_2013to2021R)
# 293 entries, 28 total columns


  # Drop outliers - using FS model, per more variables retained

    # Leverage
CookD(traffickCrimeLmFS, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers: 37, 379, 385


    # Distance
car::outlierTest(traffickCrimeLmFS)
# Distance outliers: 202, 246, 379, 385, 251, 37, 386, 252


    # Influential
summary(influence.measures(traffickCrimeLmFS))
# This determined several rows have low significance - none more influential
  # than that, though they do include some identified above - the ones 
  # identified are rows:
  # 23, 24, 37, 38, 39, 40, 41, 42, 43, 44, 73, 74, 75, 76, 77, 78, 79, 80, 82, 
  # 83, 89, 109, 114, 157, 197, 198, 202, 203, 204, 205, 207, 246, 249, 250, 
  # 251, 252, 262, 263, 264, 265, 266, 267, 268, 271, 274, 289, 290


    # Remove outliers
traffickCrimeNoOutliers = traffickCrime_2013to2021R[-c(
  202, 246, 379, 385, 251, 37, 386, 252, 23, 24, 38, 39, 40, 41, 42, 43, 44, 73, 
  74, 75, 76, 77, 78, 79, 80, 82, 83, 89, 109, 114, 157, 197, 198, 203, 204, 
  205, 207, 249, 250, 262, 263, 264, 265, 266, 267, 268, 271, 274, 289, 290),]

View(traffickCrimeNoOutliers)
# 246 entries, 28 total columns
  # Sample size still validated



# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
traffickCrimeNoOutliersLmAllIVs = lm(
  TotalTraffickLog ~ ., data = traffickCrimeNoOutliers)
# Success

  # With no IV's
traffickCrimeNoOutliersLmNoIVs = lm(
  TotalTraffickLog ~ 1, data = traffickCrimeNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCrimeNoOutliersLmAllIVs, direction = 'backward')
# Removed vandalism, car theft, robbery, aggravated assault, sex, family 
  # children, liquor laws, disorderly conduct, vagrancy, weapons, assault, 
  # curfew / loitering, DUI, arson - in that order
  # Interesting that this is similar to but different from the model with 
  # outliers

  # Forward selection
step(traffickCrimeNoOutliersLmNoIVs, direction = 'forward', scope = formula(
  traffickCrimeNoOutliersLmAllIVs))
# Removed everything other than rape, drug abuse, murder / manslaughter, 
  # forgery / counterfeit, all other, and gambling
  # This is more noticeably different from both BE model w/o outliers and FS
  # model with outliers
  # Also noteworthy that rape is just as significant in this model, though other
  # non-trafficking sex crimes were removed


  # Hybrid selection
step(traffickCrimeNoOutliersLmNoIVs, direction = 'both', scope = formula(
  traffickCrimeNoOutliersLmAllIVs))
# Identical to the FS model - so that's good



# Analyze models without outliers ----

  # Backward elimination
traffickCrimeNoOutliersLmBE = lm(
  formula = TotalTraffickLog ~ Rape + AllOther + Burglary + 
    DrugAbuse + Drunkenness + Embezzlement + ForgeryCounterfeit + 
    Fraud + Gambling + Larceny + MurderManslaughter + StolenProperty + 
    Suspicion, data = traffickCrimeNoOutliers)

summary(traffickCrimeNoOutliersLmBE)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -3.3775 -0.7258  0.0372  0.8286  2.6517 
# Coefficients:
#                      Estimate Std. Error t value Pr(>|t|)    
# (Intercept)         5.435e+00  1.290e-01  42.149  < 2e-16 ***
# ... 
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.183 on 232 degrees of freedom
# Multiple R-squared:   0.51,	Adjusted R-squared:  0.4826 
# F-statistic: 18.58 on 13 and 232 DF,  p-value: < 2.2e-16
  # Most variables are individually significant with varying degrees of 
    # significance, and together have high significance and explain ~48% of the 
    # variance in trafficking crime arrests; reject the null and accept the 
    # alternative hypothesis

    # With high significance, a one unit increase in:
# Rape arrests predict a 2.146e-03 increase in trafficking crime arrests
# DrugAbuse arrests predict a 7.198e-05 decrease in trafficking crime arrests
# MurderManslaughter arrests predict a 4.828e-03 increase in trafficking crime 
  # arrests

    # With moderate significance, a one unit increase in:
# Fraud arrests predict a 3.604e-04 increase in trafficking crime arrests

    # With low significance, a one unit increase in:
# AllOther arrests predict a 9.948e-06 increase in trafficking crime arrests
# Embezzlement arrests predict a 1.036e-03 decrease in trafficking crime arrests
# Gambling arrests predict a 2.794e-03 decrease in trafficking crime arrests
# StolenProperty arrests predict a 2.163e-04 increase in trafficking crime 
  # arrests

    # There is no significant impact from:
# Burglary
# Drunkenness
# ForgeryCounterfeit
# Larceny
# Suspicion



  # Forward selection
traffickCrimeNoOutliersLmFS = lm(
  formula = TotalTraffickLog ~ Rape + Sex + CurfewLoitering + 
    MurderManslaughter + Burglary + Fraud + Vagrancy + CarTheft + 
    Gambling + AggravatedAssault + Assault + DUI + Robbery + 
    FamilyChildren, data = traffickCrimeNoOutliers)

summary(traffickCrimeNoOutliersLmFS)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -3.5590 -0.8724 -0.0105  0.9263  2.9458 
# Coefficients:
#                      Estimate Std. Error t value Pr(>|t|)    
# (Intercept)         5.643e+00  1.294e-01  43.601  < 2e-16 ***
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.264 on 231 degrees of freedom
# Multiple R-squared:  0.443,	Adjusted R-squared:  0.4092 
# F-statistic: 13.12 on 14 and 231 DF,  p-value: < 2.2e-16
  # Only a few variables are individually significant with varying degrees of 
    # significance, though together all have high significance and explain ~41% 
    # of the variance in trafficking crime arrests; reject the null and accept 
    # the alternative hypothesis

    # With moderate significance, a one unit increase in:
# MurderManslaughter arrests predict a 3.199e-03 increase in trafficking crime 

    # With low significance, a one unit increase in:
# Vagrancy arrests predict a 4.081e-04 increase in trafficking crime 
# Gambling arrests predict a 3.795e-03 decrease in trafficking crime 

    # There is no significant impact from:
# Rape
  # This is surprising.. if not suspicious!
# Sex
  # This is also surprising
# CurfewLoitering
# Burglary
# Fraud
# CarTheft
# AggravatedAssault
# Assault
# DUI
# Robbery
# FamilyChildren



# Test assumptions post hoc----

  # Linearity

    # With outliers
ggplot(traffickCrime_2013to2021R, aes(
  x = TotalTraffickLog, y = Rape + Sex + Vagrancy + Weapons + 
    StolenProperty + Robbery + Assault + Embezzlement + MurderManslaughter + 
    Larceny + DUI + ForgeryCounterfeit + Arson + FamilyChildren + 
    DisorderlyConduct + DrugAbuse + Vandalism + CarTheft + Suspicion + 
    AggravatedAssault + LiquorLaws + AllOther + CurfewLoitering + Gambling + 
    Drunkenness)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(traffickCrimeNoOutliers, aes(
  x = TotalTraffickLog, y = Rape + CarTheft + Arson + DUI + 
    Embezzlement + Larceny + Vandalism + Suspicion + StolenProperty + 
    Fraud + DrugAbuse + Weapons + AggravatedAssault + DisorderlyConduct + 
    ForgeryCounterfeit + Assault + MurderManslaughter + Drunkenness + 
    Sex + LiquorLaws + Gambling + Robbery + FamilyChildren + 
    AllOther + Vagrancy + CurfewLoitering)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Very similar to version with outliers 


  # Homoscedasticity

    # With outliers
lmtest::bptest(traffickCrimeLmBE)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeLmBE
# BP = 72.586, df = 15, p-value = 1.54e-09
  # This p value below 0.05 violates the assumption of homoscedasticity


    # Without outliers
lmtest::bptest(traffickCrimeNoOutliersLmBE)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeNoOutliersLmBE
# BP = 10.804, df = 13, p-value = 0.6272
  # This p value above 0.05 validates the assumption of homoscedasticity



# Summary ----
# The relationship between trafficking arrests and non-trafficking crime 
# arrests is not linear and with outliers is not homoscedastic (without outliers
# it is), which means the results of a stepwise multiple linear regression model 
# cannot be fully tested. That said, with outliers, this model shows that 
# non-trafficking crime arrests predict approximately 66% of the variance in 
# trafficking arrests and without outliers they predict about 44%. Strongest
# individual crime predictors are
  # With outliers: Rape, Assault, DUI, Embezzlement, Larceny, 
    # MurderManslaughter, Robbery, StolenProperty, Vagrancy
  # Without outliers: MurderManslaughter
# Further analysis will be completed to validate this model's results.