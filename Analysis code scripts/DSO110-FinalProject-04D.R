# DSO110 - Data Science Final Project
  # File 4-D
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found in states where there are higher rates 
  # of crime overall

# H0: Arrests for crime overall do not predict arrests for trafficking crimes 
  # within the same state
# H1: Arrests for crime overall do predict arrests for trafficking crimes within
  # the same state

# IV's:
  # All crime arrests
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
traffickCrimeState_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, State, TotalAll, TotalTraffick)

View(traffickCrimeState_2013to2021)
# 1,386 entries, 4 total columns


  # Drop non-total rows
traffickCrimeState_2013to2021R = traffickCrimeState_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickCrimeState_2013to2021R)
# 459 entries, 4 total columns
  # Sample size still validated


  # Drop age column
traffickCrimeState_2013to2021R = subset(
  traffickCrimeState_2013to2021R, select = -(Age))

View(traffickCrimeState_2013to2021R)
# 459 entries, 3 total columns



# Create multiple linear regression models ----

  # With all IV's
traffickCrimeStateLmAllIVs = lm(TotalTraffick ~ ., 
                                data = traffickCrimeState_2013to2021R)
# Success

  # With no IV's
traffickCrimeStateLmNoIVs = lm(TotalTraffick ~ 1, 
                               data = traffickCrimeState_2013to2021R)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCrimeStateLmAllIVs, direction = 'backward')
# Kept both IV's

  # Forward selection
step(traffickCrimeStateLmNoIVs, direction = 'forward', 
     scope = formula(traffickCrimeStateLmAllIVs))
# Kept both IV's
  # Glad it's aligned with BE
  # Added state first, implying it has the strongest impact

  # Hybrid selection
step(traffickCrimeStateLmNoIVs, direction = 'both', 
     scope = formula(traffickCrimeStateLmAllIVs))
# Kept both IV's
  # Added variables in the same order as FS model
  # Glad all three are aligned!



# Analyze model ----
traffickCrimeStateLm = lm(formula = TotalTraffick ~ TotalAll * State, 
    data = traffickCrimeState_2013to2021R)

summary(traffickCrimeStateLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -7498.3  -251.4   -28.1   194.7 11365.3 
# Coefficients:
#                                Estimate Std. Error t value Pr(>|t|)    
# (Intercept)                   1.914e+02  8.861e+02   0.216  0.82908   
# ...
# StateFLORIDA                  4.834e+03  1.914e+03   2.526  0.01198 *  
# StateGEORGIA                  1.060e+04  1.902e+03   5.570 5.02e-08 ***
# ...
# StateMINNESOTA                1.690e+04  6.654e+03   2.539  0.01153 *  
# ...
# StateTENNESSEE                1.019e+04  4.670e+03   2.182  0.02979 *  
# StateTEXAS                    7.124e+04  3.330e+03  21.392  < 2e-16 ***
# StateUTAH                     1.198e+04  4.273e+03   2.805  0.00531 ** 
# ...
# StateVIRGINIA                 9.930e+03  4.130e+03   2.405  0.01670 *  
# StateWASHINGTON               1.195e+04  4.837e+03   2.471  0.01394 *  
# ...
# StateWISCONSIN                1.396e+04  3.494e+03   3.997 7.80e-05 ***
# ...
# TotalAll:StateGEORGIA        -3.721e-02  1.184e-02  -3.142  0.00182 ** 
# ...
# TotalAll:StateLOUISIANA       4.860e-02  1.967e-02   2.471  0.01394 *  
# ...
# TotalAll:StateTEXAS          -6.910e-02  1.008e-02  -6.855 3.14e-11 ***
# TotalAll:StateUTAH           -1.006e-01  4.083e-02  -2.463  0.01426 *  
# ...
# TotalAll:StateWASHINGTON     -5.880e-02  2.959e-02  -1.987  0.04766 *  
# ...
# TotalAll:StateWISCONSIN      -4.354e-02  1.650e-02  -2.639  0.00868 ** 
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1846 on 357 degrees of freedom
# Multiple R-squared:  0.8299,	Adjusted R-squared:  0.7818 
# F-statistic: 17.25 on 101 and 357 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
  # What it determined is that there is a significant difference in the 
  # predictive abilities of total crime arrests by state
  # It also found some states more significant on their own



# Re-wrangling to better meet assumptions ----

  # Transform DV
traffickCrimeState_2013to2021R$TotalTraffickLog = log(
  traffickCrimeState_2013to2021R$TotalTraffick)

View(traffickCrimeState_2013to2021R)
# 459 entries, 4 total columns
  # Lots of infinite values

      # Drop NA's
traffickCrimeState_2013to2021R = NaRV.omit(traffickCrimeState_2013to2021R)

View(traffickCrimeState_2013to2021R)
# 293 entries, 4 total columns
  # Sample size still validated

      # Drop original column
traffickCrimeState_2013to2021R = subset(
  traffickCrimeState_2013to2021R, select = -(TotalTraffick))

View(traffickCrimeState_2013to2021R)
# 293 entries, 3 total columns


  # Drop outliers

    # Leverage
CookD(traffickCrimeStateLm, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers on rows 45, 81, 206

    # Distance
car::outlierTest(traffickCrimeStateLm)
# Distance outliers: 81, 80, 252, 247, 244, 245, 379, 248, 202, 89

    # Influential
summary(influence.measures(traffickCrimeStateLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include one identified above - the ones 
  # identified are rows:
  # 4, 18, 27, 28, 35, 36, 45, 53, 54


    # Remove outliers
traffickCrimeStateNoOutliers = traffickCrimeState_2013to2021R[-c(
  45, 81, 206, 81, 80, 252, 247, 244, 245, 379, 248, 202, 89, 4, 18, 27, 28, 35, 
  36, 53, 54),]

View(traffickCrimeStateNoOutliers)
# 274 entries, 3 total columns
  # Sample size still validated



# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
traffickCrimeStateNoOutliersLmAllIVs = lm(
  TotalTraffickLog ~ ., data = traffickCrimeStateNoOutliers)
# Success

  # With no IV's
traffickCrimeStateNoOutliersLmNoIVs = lm(
  TotalTraffickLog ~ 1, data = traffickCrimeStateNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCrimeStateNoOutliersLmAllIVs, direction = 'backward')
# Removed all crime - uh oh...

  # Forward selection
step(traffickCrimeStateNoOutliersLmNoIVs, direction = 'forward', 
     scope = formula(traffickCrimeStateNoOutliersLmAllIVs))
# Removed all crime

  # Hybrid selection
step(traffickCrimeStateNoOutliersLmNoIVs, direction = 'both', 
     scope = formula(traffickCrimeStateNoOutliersLmAllIVs))
# Removed all crime


# Note: Because the goal of this analysis was to determine whether state 
# influences the impact of crime arrests overall in predicting trafficking 
# arrests, I am going to create and analyze a model without both IV's in spite 
# of these results


# Analyze model without outliers ----
traffickCrimeStateNoOutliersLm = lm(
  formula = TotalTraffickLog ~ TotalAll * State, 
  data = traffickCrimeStateNoOutliers)

summary(traffickCrimeStateNoOutliersLm)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -2.9242 -0.2813  0.0084  0.3960  1.9046 
# Coefficients: (1 not defined because of singularities)
#                                Estimate Std. Error t value Pr(>|t|)    
# (Intercept)                   4.253e+00  6.351e-01   6.697 2.87e-10 ***
# TotalAll                      5.543e-05  2.271e-05   2.440 0.015686 *  
# ...
# StateCOLORADO                 6.146e+00  2.088e+00   2.944 0.003686 ** 
# ...
# StateFLORIDA                  7.582e+00  3.546e+00   2.138 0.033901 *  
# StateGEORGIA                  6.623e+00  1.326e+00   4.994 1.44e-06 ***
# ...
# StateILLINOIS                 3.320e+00  1.072e+00   3.098 0.002278 ** 
# StateINDIANA                  6.204e+00  1.523e+00   4.073 7.06e-05 ***
# StateIOWA                    -4.924e+00  1.870e+00  -2.633 0.009220 ** 
# ...
# StateMARYLAND                 2.032e+00  9.297e-01   2.185 0.030197 *  
# StateMASSACHUSETTS            7.312e+00  2.160e+00   3.385 0.000880 ***
# StateMICHIGAN                 7.210e+00  1.906e+00   3.782 0.000214 ***
# ...
# StateMISSOURI                 5.468e+00  1.385e+00   3.947 0.000115 ***
# ...
# StateNEW MEXICO               2.452e+00  1.237e+00   1.982 0.049103 *  
# ...
# StateOHIO                     6.856e+00  1.854e+00   3.699 0.000291 ***
# ...
# StateTENNESSEE                6.947e+00  2.230e+00   3.115 0.002152 ** 
# StateTEXAS                    7.348e+00  2.302e+00   3.193 0.001676 ** 
# ...
# StateVIRGINIA                 7.590e+00  2.745e+00   2.766 0.006299 ** 
# StateWASHINGTON               1.061e+01  2.306e+00   4.601 8.09e-06 ***
# ...
# StateWEST VIRGINIA            5.926e+00  2.400e+00   2.469 0.014518 *  
# StateWISCONSIN                7.965e+00  1.874e+00   4.249 3.50e-05 ***
# ...
# TotalAll:StateCALIFORNIA     -5.257e-05  2.273e-05  -2.313 0.021913 *  
# TotalAll:StateCOLORADO       -6.959e-05  2.489e-05  -2.796 0.005755 ** 
# ...
# TotalAll:StateFLORIDA        -5.969e-05  2.336e-05  -2.555 0.011465 *  
# TotalAll:StateGEORGIA        -7.828e-05  2.415e-05  -3.242 0.001426 ** 
# TotalAll:StateHAWAII         -7.085e-05  3.552e-05  -1.995 0.047611 *  
# ...
# TotalAll:StateILLINOIS       -5.399e-05  2.527e-05  -2.136 0.034067 *  
# TotalAll:StateINDIANA        -8.909e-05  2.570e-05  -3.467 0.000664 ***
# ...
# TotalAll:StateMARYLAND       -5.123e-05  2.326e-05  -2.203 0.028931 *  
# TotalAll:StateMASSACHUSETTS  -1.003e-04  3.023e-05  -3.317 0.001108 ** 
# TotalAll:StateMICHIGAN       -7.675e-05  2.412e-05  -3.182 0.001731 ** 
# ...
# TotalAll:StateMISSOURI       -6.874e-05  2.345e-05  -2.931 0.003830 ** 
# ...
# TotalAll:StateNEW JERSEY     -5.531e-05  2.318e-05  -2.386 0.018103 *  
# TotalAll:StateNEW MEXICO     -6.838e-05  3.066e-05  -2.230 0.027033 *  
# TotalAll:StateNEW YORK       -6.302e-05  2.369e-05  -2.660 0.008550 ** 
# ...
# TotalAll:StateOHIO           -8.264e-05  2.430e-05  -3.401 0.000833 ***
# ...
# TotalAll:StateSOUTH CAROLINA -6.307e-05  3.164e-05  -1.994 0.047778 *  
# ...
# TotalAll:StateTENNESSEE      -6.596e-05  2.365e-05  -2.790 0.005869 ** 
# TotalAll:StateTEXAS          -5.778e-05  2.290e-05  -2.523 0.012537 *  
# ...
# TotalAll:StateVIRGINIA       -7.403e-05  2.534e-05  -2.922 0.003947 ** 
# TotalAll:StateWASHINGTON     -1.028e-04  2.623e-05  -3.917 0.000129 ***
# ...
# TotalAll:StateWEST VIRGINIA  -1.895e-04  9.409e-05  -2.014 0.045559 *  
# TotalAll:StateWISCONSIN      -7.435e-05  2.390e-05  -3.110 0.002186 ** 
# TotalAll:StateWYOMING        -1.280e-04  6.237e-05  -2.051 0.041740 *  
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 0.8607 on 173 degrees of freedom
# Multiple R-squared:  0.8152,	Adjusted R-squared:  0.7084 
# F-statistic: 7.631 on 100 and 173 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
  # What it determined is that there is a significant difference in the 
  # predictive abilities of total crime arrests by state
  # It also found some states more significant on their own



# Test assumptions post hoc on data ----

  # Linearity

    # With outliers
ggplot(traffickCrimeState_2013to2021, aes(
  x = TotalTraffickLog, y = TotalAll, State)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'All Crimes by State') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear with outliers

    # Without outliers
ggplot(traffickCrimeStateNoOutliers, aes(
  x = TotalTraffickLog, y = TotalAll, State)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'All Crimes by State') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Almost identical results to version with outliers


  # Homoscedasticity

    # With outliers
lmtest::bptest(traffickCrimeStateLm)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeStateLmBE
# BP = 286.3, df = 101, p-value < 2.2e-16
  # This p value below 0.05 violates the assumption of homoscedasticity

    # Without outliers
lmtest::bptest(traffickCrimeStateNoOutliersLm)
# 	studentized Breusch-Pagan test
# data:  traffickCrimeStateNoOutliersLm
# BP = 115.18, df = 100, p-value = 0.1423
  # This p value above 0.05 validates the assumption of homoscedasticity



# Summary ----
# The relationship between trafficking arrests, overall crime arrests, and state 
# is only mildly linear and with outliers is not homoscedastic (without outliers
# it is), which means the results of a stepwise multiple linear regression model 
# cannot be fully tested. That said, with and without outliers this model 
# determined that the ability of overall crime arrests to predict trafficking 
# crime arrests does vary significantly by state.