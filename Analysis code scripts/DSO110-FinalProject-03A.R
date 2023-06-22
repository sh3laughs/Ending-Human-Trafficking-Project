# DSO110 - Data Science Final Project
  # File 3-A
  # Analysis: Simple linear regression

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
library(predictmeans)


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
traffickNonTraffickSex_2013to2021 = traffickNonTraffickSex_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickNonTraffickSex_2013to2021)
# 459 entries, 4 total columns
  # Sample size still validated


  # Drop age column
traffickNonTraffickSex_2013to2021 = subset(
  traffickNonTraffickSex_2013to2021, select = -(Age))

View(traffickNonTraffickSex_2013to2021)
# 459 entries, 3 total columns



# Test assumptions ----

  # Linearity for each potential IV ----

    # Rape
ggplot(traffickNonTraffickSex_2013to2021, aes(x = TotalTraffick, y = Rape)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Rape') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Not linear

      # Transform DV
traffickNonTraffickSex_2013to2021$TotalTraffickLog = log(
  traffickNonTraffickSex_2013to2021$TotalTraffick)

View(traffickNonTraffickSex_2013to2021)
# 459 entries, 4 total columns
  # Lots of infinite values

      # Drop NA's
traffickNonTraffickSex_2013to2021R = NaRV.omit(
  traffickNonTraffickSex_2013to2021)

View(traffickNonTraffickSex_2013to2021R)
# 293 entries, 4 total columns
  # Sample size still validated

      # Check distribution again
ggplot(traffickNonTraffickSex_2013to2021R, aes(x = TotalTraffickLog, 
                                               y = Rape)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Rape') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Decently linear... but a batch of outliers


    # Non-trafficking, non-rape sex crimes
ggplot(traffickNonTraffickSex_2013to2021, aes(x = TotalTraffick, 
                                               y = Sex)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Sex Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Not linear

        # Check distribution with transformed DV
ggplot(traffickNonTraffickSex_2013to2021R, aes(x = TotalTraffickLog, 
                                               y = Sex)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Sex Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Pretty linear, with a batch of outliers


  # Homoscedasticity ----

    # Linear regression model
traffickNonTraffickLm = lm(TotalTraffickLog ~ Rape + Sex, 
                    data = traffickNonTraffickSex_2013to2021R)

      # Breusch Pagan Homoscedasticity test
lmtest::bptest(traffickNonTraffickLm)
# 	studentized Breusch-Pagan test
# data:  traffickNonTraffickLm
# BP = 1.8786, df = 2, p-value = 0.3909
  # This p value below 0.05 violates this assumption

      # Transform
traffickNonTraffickBc = caret::BoxCoxTrans(
  traffickNonTraffickSex_2013to2021R$TotalTraffickLog)

traffickNonTraffickSex_2013to2021R = cbind(
  traffickNonTraffickSex_2013to2021R, 
  TotalTraffickR = predict(traffickNonTraffickBc, 
                           traffickNonTraffickSex_2013to2021R$TotalTraffickLog))
						
traffickNonTraffickLmR = lm(TotalTraffickR ~ Rape + Sex, 
                    data = traffickNonTraffickSex_2013to2021R)

lmtest::bptest(traffickNonTraffickLmR)
# 	studentized Breusch-Pagan test
# data:  traffickNonTraffickLmR
# BP = 1.8786, df = 2, p-value = 0.3909
  # No change in results... will check again after removing outliers, since
  # there clearly are some



  # Outliers ----

    # Leverage
CookD(traffickNonTraffickLm, group = NULL, idn = 3, newwd = FALSE)
# Leverage outliers on rows 37, 42, 286


    # Distance
car::outlierTest(traffickNonTraffickLm)
# No Studentized residuals with Bonferroni p < 0.05
# Largest |rstudent|:
#        rstudent unadjusted p-value Bonferroni p
#   431 -3.012738          0.0028182      0.82574
  # 431 is distance


    # Influential
summary(influence.measures(traffickNonTraffickLm))
# This determined several rows have low significance - none more influential
  # than that, though they do include some identified above - the ones 
  # identified are rows:
  # 37, 38, 39, 40, 41, 42, 43, 44, 74, 76, 78, 79, 80, 380, 381, 382, 383, 384, 
  # 385, 386, 387


    # Drop outliers
traffickNonTraffickSexNoOutliers = traffickNonTraffickSex_2013to2021R[-c(
  37, 38, 39, 40, 41, 42, 43, 44, 74, 76, 78, 79, 80, 380, 381, 382, 383, 384, 
  385, 386, 387, 286, 431),]

View(traffickNonTraffickSexNoOutliers)
# 279 entries, 5 total columns
  # Sample size still validated



# Create new model without outliers ----
traffickNonTraffickLmNoOutliers = lm(
  TotalTraffickLog ~ Rape + Sex, 
  data = traffickNonTraffickSexNoOutliers)



# Re-test assumptions ----

  # Normality
ggplot(traffickNonTraffickSexNoOutliers, 
       aes(x = TotalTraffickLog, y = Rape + Sex)) +
  geom_point() + 
  labs(x = 'Trafficking Crimes', y = 'Non-trafficking Sex Crimes') +
  theme_minimal() +
  stat_smooth(method = 'lm', formula = y ~ x, se = FALSE, color = 'red')
# Not a big difference... it still looks like there's a batch of outliers...


  # Homoscedasticity
lmtest::bptest(traffickNonTraffickLmNoOutliers)
# 	studentized Breusch-Pagan test
# data:  traffickNonTraffickLmNoOutliers
# BP = 1.7234, df = 2, p-value = 0.4224
  # This p value below 0.05 still violates the assumption of homoscedasticity -
  # even worse, actually



# Analyze ----

  # With outliers
summary(traffickNonTraffickLm)
# Residuals:
# -3.8895 -0.9820 -0.0190  0.9985  2.9529 
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)    
# (Intercept)  5.970e+00  9.942e-02  60.042   <2e-16 ***
# Rape         2.418e-03  2.662e-04   9.084   <2e-16 ***
# Sex         -2.639e-04  8.965e-05  -2.944   0.0035 ** 
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.313 on 290 degrees of freedom
# Multiple R-squared:  0.3404,	Adjusted R-squared:  0.3359 
# F-statistic: 74.84 on 2 and 290 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # This means that non-trafficking sex crime arrests do predict trafficking 
    # arrests
    # Together rape and non-trafficking sex crime arrests explain ~34% of the 
    # variance in trafficking arrests
    # Rape arrests are a highly significant predictor and non-trafficking sex 
    # crime arrests predictions have moderate significance


  # Without outliers
summary(traffickNonTraffickLmNoOutliers)
# Residuals:
#    Min     1Q Median     3Q    Max 
# -3.849 -1.008 -0.032  1.033  2.991 
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)    
# (Intercept)  5.929e+00  1.022e-01  58.013  < 2e-16 ***
# Rape         2.390e-03  2.710e-04   8.816  < 2e-16 ***
# Sex         -2.490e-04  9.106e-05  -2.734  0.00665 ** 
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.325 on 276 degrees of freedom
# Multiple R-squared:  0.3451,	Adjusted R-squared:  0.3404 
# F-statistic: 72.73 on 2 and 276 DF,  p-value: < 2.2e-16
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # This means that non-trafficking sex crime arrests do predict trafficking 
    # arrests
    # Together rape and non-trafficking sex crime arrests explain ~34% of the 
    # variance in trafficking arrests
    # Rape arrests are a highly significant predictor and non-trafficking sex 
    # crime arrests predictions have moderate significance



# Summary ----
# The relationship between trafficking arrests and non-trafficking sex crime
# arrests is only mildly linear, which means the results of a linear regression 
# model cannot be fully tested. That said, with and without outliers, this 
# model shows that non-trafficking sex crime arrests predict approximately 34% 
# of the variance in trafficking arrests. Rape is a highly significant predictor
# and other non-trafficking sex crimes predict with moderate significance. 
# Further analysis will be completed to validate this model's results.