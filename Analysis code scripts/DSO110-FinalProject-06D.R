# DSO110 - Data Science Final Project
  # File 6-D
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported suicides are more likely to 
  # be found in states where there are higher rates of arrests for human 
  # trafficking crimes

# H0: Arrests for trafficking crimes do not predict suicides within the same 
  # state
# H1: Arrests for trafficking crimes do predict suicides within the same state

# IV's:
  # Trafficking crime arrests
  # State
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
suicideTraffickState_2013to2021 = crimeSuicide_2013to2021 %>% 
  select(Age, State, TotalSuicide, TotalTraffick)

View(suicideTraffickState_2013to2021)
# 3,021 entries, 4 total columns


  # Drop non-total rows
suicideTraffickState_2013to2021R = suicideTraffickState_2013to2021 %>%
  filter(Age == 'Total all ages')

View(suicideTraffickState_2013to2021R)
# 459 entries, 4 total columns
  # Sample size still validated


  # Drop age column
suicideTraffickState_2013to2021R = subset(
  suicideTraffickState_2013to2021R, select = -(Age))

View(suicideTraffickState_2013to2021R)
# 459 entries, 3 total columns



# Create multiple linear regression models ----

  # With all IV's
suicideTraffickStateLmAllIVs = lm(TotalSuicide ~ ., 
                                data = suicideTraffickState_2013to2021R)
# Success

  # With no IV's
suicideTraffickStateLmNoIVs = lm(TotalSuicide ~ 1, 
                               data = suicideTraffickState_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(suicideTraffickStateLmAllIVs, direction = 'backward')
# Kept both IV's

  # Forward selection
step(suicideTraffickStateLmNoIVs, direction = 'forward', 
     scope = formula(suicideTraffickStateLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added state first, implying it has the strongest impact

  # Hybrid selection
step(suicideTraffickStateLmNoIVs, direction = 'both', 
     scope = formula(suicideTraffickStateLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model ----
suicideTraffickStateLm = lm(formula = TotalSuicide ~ TotalTraffick * State, 
    data = suicideTraffickState_2013to2021R)

summary(suicideTraffickStateLm)
# Residuals:
#      Min       1Q   Median       3Q      Max 
# -2260.47   -53.70    16.35   104.99  1024.79 
# Coefficients:
#                                     Estimate Std. Error t value Pr(>|t|)    
# (Intercept)                        1.447e+03  1.159e+02  12.484  < 2e-16 ***
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 320.6 on 357 degrees of freedom
# Multiple R-squared:  0.9648,	Adjusted R-squared:  0.9549 
# F-statistic:    97 on 101 and 357 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
  # What it determined is that there is a significant difference in the 
  # predictive abilities of trafficking crime arrests by state
  # It also found some states more significant on their own



# Re-wrangling to better meet assumptions ----

  # Transform DV
suicideTraffickState_2013to2021R$TotalSuicideLog = log(
  suicideTraffickState_2013to2021R$TotalSuicide)

View(suicideTraffickState_2013to2021R)
# 459 entries, 4 total columns
  # Some infinite values

      # Drop NA's
suicideTraffickState_2013to2021R = NaRV.omit(
  suicideTraffickState_2013to2021R)

View(suicideTraffickState_2013to2021R)
# 457 entries, 4 total columns
  # Sample size still validated

      # Drop original column
suicideTraffickState_2013to2021R = subset(
  suicideTraffickState_2013to2021R, select = -(TotalSuicide))

View(suicideTraffickState_2013to2021R)
# 457 entries, 3 total columns


  # Drop outliers

    # Leverage
CookD(suicideTraffickStateLm, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers: 9, 45, 135

    # Distance
car::outlierTest(suicideTraffickStateLm)
# Distance outliers: 387, 45, 81, 37
  # So 45 is influential

    # Influential
summary(influence.measures(suicideTraffickStateLm))
# This determined several rows have low significance - none more influential
  # than that, though don't include any identified above - the ones 
  # identified are rows:
  # 9, 13, 15, 23, 31, 37, 42, 43, 44


    # Remove outliers
suicideTraffickStateNoOutliers = suicideTraffickState_2013to2021R[-c(
  9, 45, 135, 387, 81, 37, 9, 13, 15, 23, 31, 37, 42, 43, 44),]

View(suicideTraffickStateNoOutliers)
# 444 entries, 3 total columns
  # Sample size still validated



# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
suicideTraffickStateNoOutliersLmAllIVs = lm(
  TotalSuicideLog ~ ., data = suicideTraffickStateNoOutliers)
# Success

  # With no IV's
suicideTraffickStateNoOutliersLmNoIVs = lm(
  TotalSuicideLog ~ 1, data = suicideTraffickStateNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(suicideTraffickStateNoOutliersLmAllIVs, direction = 'backward')
# Removed trafficking arrests.. uh oh

  # Forward selection
step(suicideTraffickStateNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(suicideTraffickStateNoOutliersLmAllIVs))
# Also removed trafficking arrests
  # Nog glad it's aligned with BE ;)

  # Hybrid selection
step(suicideTraffickStateNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(suicideTraffickStateNoOutliersLmAllIVs))
# Also removed trafficking arrests
  # Glad all three are aligned!


# Note: Because the goal of this analysis was to determine whether state 
# influences the impact of trafficking arrests in predicting suicides, I am 
# going to create and analyze a model without both IV's in spite of these 
# results


# Analyze model without outliers ----
suicideTraffickStateNoOutliersLm = lm(
  formula = TotalSuicideLog ~ TotalTraffick * State, 
  data = suicideTraffickStateNoOutliers)

summary(suicideTraffickStateNoOutliersLm)
# Residuals:
#      Min       1Q   Median       3Q      Max 
# -0.58634 -0.05154  0.02945  0.10819  0.32128 
# Coefficients:
#                                     Estimate Std. Error t value Pr(>|t|)    
# (Intercept)                        7.247e+00  7.402e-02  97.911  < 2e-16 ***
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 0.1864 on 342 degrees of freedom
# Multiple R-squared:  0.9716,	Adjusted R-squared:  0.9632 
# F-statistic: 115.9 on 101 and 342 DF,  p-value: < 2.2e-16
  # Though the model overall is significant, it did not find a significant 
  # difference in the impact of trafficking crime arrests based on state; accept 
  # the null and reject the alternative hypothesis



# Test assumptions post hoc ----

  # Linearity

    # With outliers
ggplot(suicideTraffickState_2013to2021R, 
       aes(x = TotalSuicideLog, y = TotalTraffick, State)) +
  geom_point() + 
  labs(x = 'Suicide', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(suicideTraffickStateNoOutliers, 
       aes(x = TotalSuicideLog, y = TotalTraffick, State)) +
  geom_point() + 
  labs(x = 'Suicide', y = 'Trafficking Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Pretty much identical to the version with outliers


  # Homoscedasticity

    # With outliers
lmtest::bptest(suicideTraffickStateLm)
# 	studentized Breusch-Pagan test
# data:  suicideTraffickStateLm
# BP = 204.18, df = 101, p-value = 5.705e-09
  # This p value below 0.05 violates the assumption of homoscedasticity


    # Without outliers
lmtest::bptest(suicideTraffickStateNoOutliersLm)
# 	studentized Breusch-Pagan test
# data:  suicideTraffickStateNoOutliersLm
# BP = 81.177, df = 101, p-value = 0.9265
  # This p value above 0.05 validates the assumption of homoscedasticity



# Summary ----
# The relationship between suicides, trafficking crime arrests, and state is not 
# linear or homoscedastic, which means the results of a stepwise multiple linear 
# regression model cannot be fully tested. That said, with outliers this model 
# determined that the ability of trafficking crime arrests to predict suicides 
# does vary significantly by state and without outliers they do not.