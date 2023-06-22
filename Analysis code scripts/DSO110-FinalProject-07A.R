# DSO110 - Data Science Final Project
  # File 7A
  # Analysis: Stepwise multiple linear regression model

# Goal: Determine what the leading, contributing demographic factors to people 
  # being trafficked are, according to US census and FBI crime data for 2013- 
  # 2021

# H0: No census demographics predict arrests for trafficking crimes
# H1: One or more census demographics predict arrests for trafficking crimes

# IV: 
  # Before testing: TBD
  # After testing: TotalPopulation, AgeUnder, and TotalHouseholds
# DV: Trafficking arrests


# Import packages ----
library(dplyr)
library(ggplot2)
library(IDPmisc)
library(predictmeans)


# Import and preview data ----
allData_2013to2021 = read.csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/allData_2013to2021.csv')

View(allData_2013to2021)
# 92,593 entries, 51 total columns
  # Sample size is validated for now...
  # Lots of 0 values



# Wrangling ----

  # Subset to only include trafficking and census
traffickCensus_2013to2021 = allData_2013to2021 %>% select(
  TotalTraffick, TotalPopulation, Age, AgeDetail, TotalHouseholds, Computer, 
  Education, Employment, Gender, IncomeInPast12Months, Internet, Poverty)

View(traffickCensus_2013to2021)
# 92,593 entries, 12 total columns



# Create multiple linear regression models ----

  # With all IV's
traffickCensusLmAllIVs = lm(
  TotalTraffick ~ ., data = traffickCensus_2013to2021)

# Success

  # With no IV's
traffickCensusLmNoIVs = lm(TotalTraffick ~ 1, data = traffickCensus_2013to2021)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCensusLmAllIVs, direction = 'backward')
# No variables removed!

  # Forward selection
step(traffickCensusLmNoIVs, direction = 'forward', scope = formula(
  traffickCensusLmAllIVs))
# No variables removed
  # Nice that this is aligned with backward elimination
  # Age detail was added first, implying it is most significant

  # Hybrid selection
step(traffickCensusLmNoIVs, direction = 'both', scope = formula(
  traffickCensusLmAllIVs))
# No variables removed
  # Added variables in same order as FS
  # Love that all three approaches are aligned



# Analyze model ----
traffickCensusLm = lm(
  formula = TotalTraffick ~ TotalPopulation + Age + AgeDetail + 
    TotalHouseholds + Computer + Education + Employment + Gender + 
    IncomeInPast12Months + Internet + Poverty, data = traffickCensus_2013to2021)

summary(traffickCensusLm)
# Residuals:
#    Min     1Q Median     3Q    Max 
# -15804  -1283    -98    138  33636 
# Coefficients:
#                       Estimate
# (Intercept)           3.051e+03
# ...
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 2882 on 92520 degrees of freedom
# Multiple R-squared:  0.1391,	Adjusted R-squared:  0.1384 
# F-statistic: 207.6 on 72 and 92520 DF,  p-value: < 2.2e-16
  # Most variables are individually significant, and together all are 
    # significant and explain ~14% of the variance in trafficking crime arrests; 
    # reject the null and accept the alternative hypothesis

    # With high significance, a one unit increase in:
# TotalPopulation	 predicts a 	3.84E-04	 decrease in trafficking arrests
# AgeTotal all ages	 predicts a 	-2.05E+03	 decrease in trafficking arrests
# AgeUnder 18	 predicts a 	-3.04E+03	 decrease in trafficking arrests
# AgeDetail18 to 24	 predicts a 	-1.46E+03	 decrease in trafficking arrests
# AgeDetail18 to 64	 predicts a 	-1.67E+03	 decrease in trafficking arrests
# AgeDetail20 to 24	 predicts a 	-1.18E+03	 decrease in trafficking arrests
# AgeDetail25 to 29	 predicts a 	-1.19E+03	 decrease in trafficking arrests
# AgeDetail25 to 34	 predicts a 	-1.51E+03	 decrease in trafficking arrests
# AgeDetail30 to 34	 predicts a 	-1.18E+03	 decrease in trafficking arrests
# AgeDetail35 to 39	 predicts a 	-1.18E+03	 decrease in trafficking arrests
# AgeDetail35 to 44	 predicts a 	-1.49E+03	 decrease in trafficking arrests
# AgeDetail45 to 49	 predicts a 	-1.18E+03	 decrease in trafficking arrests
# AgeDetail45 to 54	 predicts a 	-1.50E+03	 decrease in trafficking arrests
# AgeDetail45 to 64	 predicts a 	-1.64E+03	 decrease in trafficking arrests
# AgeDetail50 to 54	 predicts a 	-1.18E+03	 decrease in trafficking arrests
# AgeDetail55 to 59	 predicts a 	-1.18E+03	 decrease in trafficking arrests
# AgeDetail55+	 predicts a 	-1.50E+03	 decrease in trafficking arrests
# AgeDetail60 to 64	 predicts a 	-1.18E+03	 decrease in trafficking arrests
# AgeDetail65 to 69	 predicts a 	-1.16E+03	 decrease in trafficking arrests
# AgeDetail70 to 74	 predicts a 	-1.15E+03	 decrease in trafficking arrests
# AgeDetail75 to 79	 predicts a 	-1.14E+03	 decrease in trafficking arrests
# AgeDetail80 to 84	 predicts a 	-1.13E+03	 decrease in trafficking arrests
# TotalHouseholds	 predicts a 	1.08E-03	 decrease in trafficking arrests
# ComputerDesktop or laptop	 predicts a 	-9.64E+02	 decrease in trafficking 
  # arrests
# ComputerDesktop or laptop with no other type of computing device	 predicts a 
  # 	8.22E+02	 decrease in trafficking arrests
# ComputerHas one or more types of computing devices	 predicts a 	-1.26E+03	 
  # decrease in trafficking arrests
# ComputerNo computer	 predicts a 	8.04E+02	 decrease in trafficking arrests
# ComputerOther computer	 predicts a 	8.99E+02	 decrease in trafficking 
  # arrests
# ComputerOther computer with no other type of computing device	 predicts a 	
  # 7.45E+02	 decrease in trafficking arrests
# ComputerSmartphone	 predicts a 	-9.72E+02	 increase in trafficking arrests
# ComputerSmartphone with no other type of computing device	 predicts a 	
  # 8.46E+02	 increase in trafficking arrests
# ComputerTablet or other portable wireless computer with no other type of 
  # device	 predicts a 	1.00E+03	 increase in trafficking arrests
# Education9th to 12th grade, no diploma	 predicts a 	6.26E+02	 increase in 
  # trafficking arrests
# EducationAssociate's degree	 predicts a 	6.13E+02	 increase in trafficking 
  # arrests
# EducationBachelor's degree	 predicts a 	5.09E+02	 increase in trafficking 
  # arrests
# EducationBachelor's degree or higher	 predicts a 	4.18E+02	 increase in 
  # trafficking arrests
# EducationGraduate or professional degree	 predicts a 	5.78E+02	 increase 
  # in trafficking arrests
# EducationHigh school graduate (includes equivalency)	 predicts a 	3.55E+02	
  #  increase in trafficking arrests
# EducationHigh school graduate or higher	 predicts a 	2.86E+02	 increase in 
  # trafficking arrests
# EducationLess than 9th grade	 predicts a 	6.43E+02	 increase in trafficking 
  # arrests
# EducationLess than high school graduate	 predicts a 	3.55E+02	 increase in 
  # trafficking arrests
# EducationSome college, no degree	 predicts a 	4.99E+02	 increase in 
  # trafficking arrests
# EmploymentUnemployed	 predicts a 	4.15E+02	 increase in trafficking arrests
# EmploymentWorked part-time or part-year in the past 12 months	 predicts a 	
  # 3.74E+02	 increase in trafficking arrests
# GenderFemale	 predicts a 	2.20E+02	 increase in trafficking arrests
# GenderMale	 predicts a 	1.43E+02	 increase in trafficking arrests
# IncomeInPast12Months$20,000 to $74,999	 predicts a 	3.60E+02	 increase in 
  # trafficking arrests
# IncomeInPast12Months$75,000 or more	 predicts a 	3.94E+02	 increase in 
  # trafficking arrests
# IncomeInPast12MonthsLess than $20,000	 predicts a 	7.22E+02	 increase in 
  # trafficking arrests
# InternetBroadband of any type	 predicts a 	-9.18E+02	 increase in trafficking 
  # arrests
# InternetCellular data plan	 predicts a 	-4.46E+02	 increase in trafficking  
  # arrests
# InternetCellular data plan with no other type of Internet subscription	 
  # predicts a 	6.61E+02	 increase in trafficking arrests
# InternetDial-up with no other type of Internet subscription	 predicts a 	
  # 9.69E+02	 increase in trafficking arrests
# InternetSatellite Internet service	 predicts a 	8.76E+02	 increase in 
  # trafficking arrests
# InternetWith an Internet subscription	 predicts a 	-1.07E+03	 increase in 
  # trafficking arrests
# InternetWithout an Internet subscription	 predicts a 	4.26E+02	 increase in 
  # trafficking arrests
# PovertyBelow poverty level	 predicts a 	3.52E+02	 increase in trafficking  
  # arrests
# PovertyPoverty status is determined	 predicts a 	-2.74E+02	 increase in 
  # trafficking arrests

    # With moderate significance, a one unit increase in:
# EducationSome college or associate's degree	 predicts a 	2.80E+02	 increase 
  # in trafficking arrests
# EmploymentWorked full-time, year-round in the past 12 months	 predicts a 	
  # 2.62E+02	 increase in trafficking arrests
# InternetBroadband such as cable, fiber optic or DSL	 predicts a 	-5.08E+02	 
  # increase in trafficking arrests

    # With low significance, a one unit increase in:
# EmploymentDid not work	 predicts a 	2.56E+02	 increase in trafficking 
  # arrests

    # These demographics do not predict trafficking crime arrests
# AgeDetail0 to 17
# AgeDetail0 to 4
# AgeDetail10 to 14
# AgeDetail15 to 19
# AgeDetail5 to 17
# AgeDetail5 to 9
# AgeDetailUnder 18
# AgeDetailUnder 5
# ComputerTablet or other portable wireless computer
# EmploymentEmployed



# Re-wrangling to better meet assumptions ----

  # Recode categorical variables

    # Create new variable
traffickCensus_2013to2021R = traffickCensus_2013to2021

View(traffickCensus_2013to2021R)
# 92,593 entries, 12 total columns


    # Age
traffickCensus_2013to2021R$AgeR = recode(
  traffickCensus_2013to2021R$Age,
  'Over 18' = 1,
  'Under 18' = 2,
  'Total all ages' = 3,
  .default = 0)

View(traffickCensus_2013to2021R)
# 92,593 entries, 13 total columns
  # Visually confirmed success


    # Age detail

      # Confirm unique values
unique(traffickCensus_2013to2021R$AgeDetail)

      # Recode
traffickCensus_2013to2021R$AgeDetailR = recode(
  traffickCensus_2013to2021R$AgeDetail,
  '0 to 17' = 1,
  '18 to 24' = 2,
  '25 to 34' = 3,
  '35 to 44' = 4,
  '45 to 54' = 5,
  '55+' = 6,
  'Under 5' = 7,
  '5 to 9' = 8,
  '10 to 14' = 9,
  '15 to 19' = 10,
  '20 to 24' = 11,
  '25 to 29' = 12,
  '30 to 34' = 13,
  '35 to 39' = 14,
  '0 to 4' = 15,
  '45 to 49' = 16,
  '50 to 54' = 17,
  '55 to 59' = 18,
  '60 to 64' = 19,
  '65 to 69' = 20,
  '70 to 74' = 21,
  '75 to 79' = 22,
  '80 to 84' = 23,
  '45 to 64' = 24,
  'Under 18' = 25,
  '5 to 17' = 26,
  '18 to 64' = 27,
  .default = 0)


View(traffickCensus_2013to2021R)
# 92,593 entries, 14 total columns
  # Visually confirmed success


    # Computer
  
      # Confirm unique values
unique(traffickCensus_2013to2021R$Computer)
  
      # Recode
traffickCensus_2013to2021R$ComputerR = recode(
  traffickCensus_2013to2021R$Computer,
  'Has one or more types of computing devices' = 1,
  'Desktop or laptop' = 2,
  'Desktop or laptop with no other type of computing device' = 3,
  'Smartphone' = 4,
  'Smartphone with no other type of computing device' = 5,
  'Tablet or other portable wireless computer' = 6,
  'Tablet or other portable wireless computer with no other type of computing device' = 7,
  'Other computer' = 8,
  'Other computer with no other type of computing device' = 9,
  'No computer' = 10,
  .default = 0)

View(traffickCensus_2013to2021R)
# 92,593 entries, 15 total columns
  # Visually confirmed success


    # Education

      # Confirm unique values
unique(traffickCensus_2013to2021R$Education)

      # Recode
traffickCensus_2013to2021R$EducationR = recode(
  traffickCensus_2013to2021R$Education,
  'Less than high school graduate' = 1,
  'High school graduate (includes equivalency)' = 2,
  'Some college or associate\'s degree' = 3,
  'Bachelor\'s degree or higher' = 4,
  'High school graduate or higher' = 5,
  'Less than 9th grade' = 6,
  '9th to 12th grade, no diploma' = 7,
  'Some college, no degree' = 8,
  'Associate\'s degree' = 9,
  'Bachelor\'s degree' = 10,
  'Graduate or professional degree' = 11,
  .default = 0)

View(traffickCensus_2013to2021R)
# 92,593 entries, 16 total columns
  # Visually confirmed success

    # Employment

      # Confirm unique values
unique(traffickCensus_2013to2021R$Employment)

      # Recode
traffickCensus_2013to2021R$EmploymentR = recode(
  traffickCensus_2013to2021R$Employment,
  'Employed' = 1,
  'Unemployed' = 2,
  'Worked full-time, year-round in the past 12 months' = 3,
  'Worked part-time or part-year in the past 12 months' = 4,
  'Did not work' = 5,
  .default = 0)

View(traffickCensus_2013to2021R)
# 92,593 entries, 17 total columns
  # Visually confirmed success

    # Gender
traffickCensus_2013to2021R$GenderR = recode(
  traffickCensus_2013to2021R$Gender,
  'Female' = 1,
  'Male' = 2,
  .default = 0)

View(traffickCensus_2013to2021R)
# 92,593 entries, 18 total columns
  # Visually confirmed success


    # IncomeInPast12Months
  
    # Confirm unique values
unique(traffickCensus_2013to2021R$IncomeInPast12Months)
  
      # Recode
traffickCensus_2013to2021R$IncomeInPast12MonthsR = recode(
  traffickCensus_2013to2021R$IncomeInPast12Months,
  'Less than $20,000' = 1,
  '$20,000 to $74,999' = 2,
  '$75,000 or more' = 3,
  .default = 0)

View(traffickCensus_2013to2021R)
# 92,593 entries, 19 total columns
  # Visually confirmed success


      # Internet

        # Confirm unique values
unique(traffickCensus_2013to2021R$Internet)

        # Recode
traffickCensus_2013to2021R$InternetR = recode(
  traffickCensus_2013to2021R$Internet,
  'With an Internet subscription' = 1,
  'Dial-up with no other type of Internet subscription' = 2,
  'Broadband of any type' = 3,
  'Cellular data plan' = 4,
  'Cellular data plan with no other type of Internet subscription' = 5,
  'Broadband such as cable, fiber optic or DSL' = 6,
  'Satellite Internet service' = 7,
  'Without an Internet subscription' = 8,
  .default = 0)

View(traffickCensus_2013to2021R)
# 92,593 entries, 20 total columns
  # Visually confirmed success


      # Poverty

      # Confirm unique values
unique(traffickCensus_2013to2021R$Poverty)

        # Recode
traffickCensus_2013to2021R$PovertyR = recode(
  traffickCensus_2013to2021R$Poverty,
  'Poverty status is determined' = 1,
  'Below poverty level' = 2,
  .default = 0)

View(traffickCensus_2013to2021R)
# 92,593 entries, 21 total columns
  # Visually confirmed success


  # Transform DV
traffickCensus_2013to2021R$TotalTraffickLog = log(
  traffickCensus_2013to2021R$TotalTraffick)

View(traffickCensus_2013to2021R)
# 92,593 entries, 22 total columns
  # Lots of infinite values

      # Drop NA's
traffickCensusTransformed = NaRV.omit(traffickCensus_2013to2021R)

View(traffickCensusTransformed)
# 33,313 entries, 22 total columns
  # Sample size still validated

      # Drop original columns
traffickCensusTransformed = subset(
  traffickCensusTransformed, select = -c(
    TotalTraffick, Age, AgeDetail, Computer, Education, Employment, Gender, 
    IncomeInPast12Months, Internet, Poverty))

View(traffickCensusTransformed)
# 33,313 entries, 12 total columns


  # Drop outliers

    # Create new model to use for outliers search
traffickCensusLmR = lm(
  formula = TotalTraffickLog ~ TotalPopulation + AgeR + AgeDetailR + 
    TotalHouseholds + ComputerR + EducationR + EmploymentR + GenderR + 
    IncomeInPast12MonthsR + InternetR + PovertyR, 
  data = traffickCensusTransformed)


    # Leverage
traffickCensusLev = hat(model.matrix(traffickCensusLmR))

plot(traffickCensusLev)

traffickCensus_2013to2021[traffickCensusLev > .2,]
# Leverage outliers: 1, 4, 7, 10

    # Distance
car::outlierTest(traffickCensusLm)
# Distance outliers: 41970, 41972, 41974, 41999, 42003, 42058, 42059, 42060, 
  # 42066, 42072

    # Influential
summary(influence.measures(traffickCensusLm))
# This determined several rows have low significance - none more influential
  # than that, and does include one identified above - the ones 
  # identified are rows:
  # 1, 73, 74, 75, 147, 148, 149, 154, 155, 156, 157, 158

    # Remove outliers
traffickCensusTransformedNoOutliers = traffickCensusTransformed[-c(
  1, 4, 7, 10, 41970, 41972, 41974, 41999, 42003, 42058, 42059, 42060, 
  42066, 42072, 73, 74, 75, 147, 148, 149, 154, 155, 156, 157, 158),]

View(traffickCensusTransformedNoOutliers)
# 33,298 entries, 12 total columns
  # Sample size still validated
  # Can't imagine moving so few will make a difference...



# Create multiple linear regression models with transformed DV & no outliers ----

  # With all IV's
traffickCensusNoOutliersLmAllIVs = lm(
  TotalTraffickLog ~ ., data = traffickCensusTransformedNoOutliers)
# Success

  # With no IV's
traffickCensusNoOutliersLmNoIVs = lm(
  TotalTraffickLog ~ 1, data = traffickCensusTransformedNoOutliers)
# Success



# Stepwise selection ----

  # Backward elimination
step(traffickCensusNoOutliersLmAllIVs, direction = 'backward')
# Removed age detail
  # Interesting that this is different from the model with outliers, when so
  # few were removed - clearly they really were significant!

  # Forward selection
step(traffickCensusNoOutliersLmNoIVs, direction = 'forward', scope = formula(
  traffickCensusNoOutliersLmAllIVs))
# Kept all IV's
  # Population was added first, implying it is significant

  # Hybrid selection
step(traffickCensusNoOutliersLmNoIVs, direction = 'both', scope = formula(
  traffickCensusNoOutliersLmAllIVs))
# Removed age detail
  # Glad it's aligned with BE
  # Added variables in the same order FS did




# Analyze models without outliers ----

  # Backward elimination
traffickCensusNoOutliersLmBE = lm(
  formula = TotalTraffickLog ~ TotalPopulation + TotalHouseholds + 
    AgeR + ComputerR + EducationR + EmploymentR + GenderR + IncomeInPast12MonthsR + 
    InternetR + PovertyR, data = traffickCensusTransformedNoOutliers)

summary(traffickCensusNoOutliersLmBE)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -6.5363 -1.2225  0.0756  1.1800  4.0338 
# Coefficients:
#                         Estimate Std. Error t value Pr(>|t|)    
# (Intercept)            6.839e+00  6.634e-02 103.086  < 2e-16 ***
# TotalPopulation        1.537e-07  4.179e-09  36.772  < 2e-16 ***
# TotalHouseholds        3.048e-07  1.122e-08  27.158  < 2e-16 ***
# AgeR                  -1.571e-01  2.434e-02  -6.454 1.10e-10 ***
# ComputerR              3.652e-02  5.634e-03   6.483 9.14e-11 ***
# EducationR             3.718e-02  3.363e-03  11.055  < 2e-16 ***
# EmploymentR            1.978e-02  9.778e-03   2.023   0.0431 *  
# GenderR                6.759e-02  1.219e-02   5.543 3.00e-08 ***
# IncomeInPast12MonthsR  9.427e-02  1.500e-02   6.284 3.34e-10 ***
# InternetR              2.581e-02  5.511e-03   4.683 2.84e-06 ***
# PovertyR               1.087e-01  1.500e-02   7.249 4.28e-13 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.557 on 33287 degrees of freedom
# Multiple R-squared:  0.05437,	Adjusted R-squared:  0.05409 
# F-statistic: 191.4 on 10 and 33287 DF,  p-value: < 2.2e-16
  # All variables are individually significant, and together all are 
    # significant and explain ~5% of the variance in trafficking crime arrests; 
    # reject the null and accept the alternative hypothesis

    # With high significance, a one unit increase in:
# TotalPopulation predicts a 1.537e-07 increase in trafficking arrests
# TotalHouseholds predicts a 3.048e-07 increase in trafficking arrests
# AgeR predicts a 1.571e-01 decrease in trafficking arrests
# ComputerR predicts a 3.652e-02 increase in trafficking arrests
# EducationR predicts a 3.718e-02 increase in trafficking arrests
# GenderR predicts a 6.759e-02 increase in trafficking arrests
# IncomeInPast12MonthsR predicts a 9.427e-02 increase in trafficking arrests
# InternetR predicts a 2.581e-02 increase in trafficking arrests
# PovertyR predicts a 1.087e-01 increase in trafficking arrests

    # With low significance, a one unit increase in:  
# EmploymentR predicts a 1.978e-02 increase in trafficking arrests

  
  
  # Forward selection
traffickCensusNoOutliersLmFS = lm(
  formula = TotalTraffickLog ~ TotalPopulation + TotalHouseholds + 
    EducationR + PovertyR + IncomeInPast12MonthsR + AgeDetailR + 
    ComputerR + GenderR + InternetR + EmploymentR + AgeR, 
  data = traffickCensusTransformedNoOutliers)

summary(traffickCensusNoOutliersLmFS)
# Residuals:
#     Min      1Q  Median      3Q     Max 
# -6.5360 -1.2229  0.0764  1.1812  4.0337 
# Coefficients:
#                         Estimate Std. Error t value Pr(>|t|)    
# (Intercept)            6.693e+00  1.706e-01  39.238  < 2e-16 ***
# TotalPopulation        1.537e-07  4.179e-09  36.770  < 2e-16 ***
# TotalHouseholds        3.048e-07  1.122e-08  27.156  < 2e-16 ***
# EducationR             3.716e-02  3.363e-03  11.050  < 2e-16 ***
# PovertyR               1.086e-01  1.500e-02   7.245 4.42e-13 ***
# IncomeInPast12MonthsR  9.422e-02  1.500e-02   6.281 3.41e-10 ***
# AgeDetailR             2.537e-02  2.733e-02   0.928   0.3533    
# ComputerR              3.650e-02  5.634e-03   6.479 9.37e-11 ***
# GenderR                6.755e-02  1.219e-02   5.540 3.05e-08 ***
# InternetR              2.579e-02  5.511e-03   4.680 2.88e-06 ***
# EmploymentR            1.977e-02  9.778e-03   2.022   0.0432 *  
# AgeR                  -1.084e-01  5.781e-02  -1.876   0.0607 .  
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# Residual standard error: 1.557 on 33286 degrees of freedom
# Multiple R-squared:  0.0544,	Adjusted R-squared:  0.05408 
# F-statistic: 174.1 on 11 and 33286 DF,  p-value: < 2.2e-16
  # All variables are individually significant, and together all are 
    # significant and explain ~5% of the variance in trafficking crime arrests; 
    # reject the null and accept the alternative hypothesis

    # With high significance, a one unit increase in:
# TotalPopulation predicts a 1.537e-07 increase in trafficking arrests
# TotalHouseholds predicts a 3.048e-07 increase in trafficking arrests
# EducationR predicts a 3.716e-02 increase in trafficking arrests
# PovertyR predicts a 1.086e-01 increase in trafficking arrests
# IncomeInPast12MonthsR predicts a 9.422e-02 increase in trafficking arrests
# ComputerR predicts a 3.650e-02 increase in trafficking arrests
# GenderR predicts a 6.755e-02 increase in trafficking arrests
# InternetR predicts a 2.579e-02 increase in trafficking arrests

    # With low significance, a one unit increase in:  
# EmploymentR predicts a 1.977e-02 increase in trafficking arrests

    # These demographics do not predict trafficking crime arrests
# AgeDetailR
# AgeR



# Test assumptions post hoc----

  # Linearity

    # With outliers
ggplot(traffickCensusTransformed, aes(
  x = TotalTraffickLog, y = TotalPopulation + AgeR + AgeDetailR +
    TotalHouseholds + ComputerR + EducationR + EmploymentR + GenderR +
    IncomeInPast12MonthsR + InternetR + PovertyR)) +
  geom_point() + 
  labs(x = "Trafficking Crimes", y = "Demographics") +
  theme_minimal() +
  stat_smooth(method = "lm", formula = y ~ x, se = FALSE, color = "red")
# Kind of like lines of dots...

    # Without outliers
ggplot(traffickCensusTransformedNoOutliers, aes(
  x = TotalTraffickLog, y = TotalPopulation + AgeR + AgeDetailR +
    TotalHouseholds + ComputerR + EducationR + EmploymentR + GenderR +
    IncomeInPast12MonthsR + InternetR + PovertyR)) +
  geom_point() + 
  labs(x = "Trafficking Crimes", y = "Demographics") +
  theme_minimal() +
  stat_smooth(method = "lm", formula = y ~ x, se = FALSE, color = "red")
# Pretty similar to version with outliers - though zoomed in, per se


  # Homoscedasticity

    # With outliers
lmtest::bptest(traffickCensusLm)
# data:  traffickCensusLmBE
# BP = 4038, df = 72, p-value < 2.2e-16
  # This p value below 0.05 violates the assumption of homoscedasticity

    # Without outliers
lmtest::bptest(traffickCensusNoOutliersLmBE)
# data:  traffickCensusNoOutliersLmBE
# BP = 209.39, df = 10, p-value < 2.2e-16
  # This p value below 0.05 violates the assumption of homoscedasticity



# Summary ----
# The relationship between trafficking arrests and census demographics is not 
# linear or homoscedastic, which means the results of a stepwise  multiple 
# linear regression model cannot be fully tested. That said, these are the 
# results:
  # With outliers: Demographics predictions of trafficking crime arrests account
  # for approximately 14% of variance; most significant predictors are:
    # Population
    # Age
    # Age detail
    # Households
    # Computer
  # Without outliers: Demographics predictions of trafficking crime arrests 
  # account for approximately 5% of variance
    # Population
    # Households
    # Education
# Further analysis will be completed to validate this model's results.