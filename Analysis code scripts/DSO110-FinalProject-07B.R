# DSO110 - Data Science Final Project
  # File 7B
  # Analysis: Pearson Correlation

# Goal: Determine what the leading, contributing demographic factors to people 
  # being trafficked are, according to US census and FBI crime data for 2013- 
  # 2021

# H0: No census demographics predict arrests for trafficking crimes
# H1: One or more census demographics predict arrests for trafficking crimes

# IV: 
  # Before testing: TBD
  # After testing:
# DV: Trafficking arrests


# Import packages ----
library(corrplot)
library(dplyr)


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


  # Recode categorical variables

    # Age
traffickCensus_2013to2021$AgeR = recode(
  traffickCensus_2013to2021$Age,
  'Under 18' = 1,
  'Total all ages' = 2,
  .default = 0)

View(traffickCensus_2013to2021)
# 92,593 entries, 13 total columns
  # Visually confirmed success


    # Age detail

      # Confirm unique values
unique(traffickCensus_2013to2021$AgeDetail)

      # Recode
traffickCensus_2013to2021$AgeDetailR = recode(
  traffickCensus_2013to2021$AgeDetail,
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


View(traffickCensus_2013to2021)
# 92,593 entries, 14 total columns
  # Visually confirmed success


    # Computer
  
      # Confirm unique values
unique(traffickCensus_2013to2021$Computer)
  
      # Recode
traffickCensus_2013to2021$ComputerR = recode(
  traffickCensus_2013to2021$Computer,
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

View(traffickCensus_2013to2021)
# 92,593 entries, 15 total columns
  # Visually confirmed success


    # Education

      # Confirm unique values
unique(traffickCensus_2013to2021$Education)

      # Recode
traffickCensus_2013to2021$EducationR = recode(
  traffickCensus_2013to2021$Education,
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

View(traffickCensus_2013to2021)
# 92,593 entries, 16 total columns
  # Visually confirmed success

    # Employment

      # Confirm unique values
unique(traffickCensus_2013to2021$Employment)

      # Recode
traffickCensus_2013to2021$EmploymentR = recode(
  traffickCensus_2013to2021$Employment,
  'Employed' = 1,
  'Unemployed' = 2,
  'Worked full-time, year-round in the past 12 months' = 3,
  'Worked part-time or part-year in the past 12 months' = 4,
  'Did not work' = 5,
  .default = 0)

View(traffickCensus_2013to2021)
# 92,593 entries, 17 total columns
  # Visually confirmed success

    # Gender
traffickCensus_2013to2021$GenderR = recode(
  traffickCensus_2013to2021$Gender,
  'Female' = 1,
  'Male' = 2,
  .default = 0)

View(traffickCensus_2013to2021)
# 92,593 entries, 18 total columns
  # Visually confirmed success


    # IncomeInPast12Months
  
    # Confirm unique values
  unique(traffickCensus_2013to2021$IncomeInPast12Months)
  
      # Recode
traffickCensus_2013to2021$IncomeInPast12MonthsR = recode(
  traffickCensus_2013to2021$IncomeInPast12Months,
  'Less than $20,000' = 1,
  '$20,000 to $74,999' = 2,
  '$75,000 or more' = 3,
  .default = 0)

View(traffickCensus_2013to2021)
# 92,593 entries, 19 total columns
  # Visually confirmed success


      # Internet

        # Confirm unique values
unique(traffickCensus_2013to2021$Internet)

        # Recode
traffickCensus_2013to2021$InternetR = recode(
  traffickCensus_2013to2021$Internet,
  'With an Internet subscription' = 1,
  'Dial-up with no other type of Internet subscription' = 2,
  'Broadband of any type' = 3,
  'Cellular data plan' = 4,
  'Cellular data plan with no other type of Internet subscription' = 5,
  'Broadband such as cable, fiber optic or DSL' = 6,
  'Satellite Internet service' = 7,
  'Without an Internet subscription' = 8,
  .default = 0)

View(traffickCensus_2013to2021)
# 92,593 entries, 20 total columns
  # Visually confirmed success


      # Poverty

      # Confirm unique values
unique(traffickCensus_2013to2021$Poverty)

        # Recode
traffickCensus_2013to2021$PovertyR = recode(
  traffickCensus_2013to2021$Poverty,
  'Poverty status is determined' = 1,
  'Below poverty level' = 2,
  .default = 0)

View(traffickCensus_2013to2021)
# 92,593 entries, 21 total columns
  # Visually confirmed success


  # Subset to only include numeric data
traffickCensus_2013to2021R = traffickCensus_2013to2021 %>% select(
  TotalTraffick, TotalPopulation, AgeR, AgeDetailR, TotalHouseholds, ComputerR, 
  EducationR, EmploymentR, GenderR, IncomeInPast12MonthsR, InternetR, PovertyR)

View(traffickCensus_2013to2021R)
# 92,593 entries, 12 total columns


  # Subset to only include IV's
census_2013to2021 = traffickCensus_2013to2021 %>% select(
  TotalPopulation, AgeR, AgeDetailR, TotalHouseholds, ComputerR, 
  EducationR, EmploymentR, GenderR, IncomeInPast12MonthsR, InternetR, PovertyR)

View(census_2013to2021)
# 92,593 entries, 11 total columns



# Correlations ----

  # Run correlation tests on each possible IV
traffickCensusCtResults = list()

for (demographic in names(census_2013to2021)) {
  traffickCensusCt = cor.test(
    traffickCensus_2013to2021R$TotalTraffick, 
    traffickCensus_2013to2021R[[demographic]], 
    method = "pearson", use = "complete.obs")
  traffickCensusCtResults[[demographic]] = traffickCensusCt}

for (demographic in names(census_2013to2021)) {
  cat("Correlation test for", demographic, ":\n")
  print(traffickCensusCtResults[[demographic]])
  cat("\n")}
# Correlation test for TotalPopulation :
# 	Pearson's product-moment correlation
# data:  traffickCensus_2013to2021R$TotalTraffick and traffickCensus_2013to2021R[[demographic]]
# t = 16.138, df = 92591, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.04653512 0.05938119
# sample estimates:
#        cor 
# 0.05296035
  # This p value indicates the test is significant, but the correlation 
    # coefficient - 0.05 - indicates a weak correlation - accept the null and 
    # reject the alternative hypothesis


  # Print just the correlation coefficients, in ranked order
traffickCensusCtCoefficients = vector()

for (demographic in names(census_2013to2021)) {
  traffickCensusCtResults = cor.test(
    traffickCensus_2013to2021R$TotalTraffick, 
    traffickCensus_2013to2021R[[demographic]],
    method = "pearson", use = "complete.obs")
  
  traffickCensusCtCoefficients[demographic] = traffickCensusCtResults$estimate}

traffickCensusCtCoefficientsRanked = traffickCensusCtCoefficients[order(
  abs(traffickCensusCtCoefficients), decreasing = TRUE)]

for (demographic in names(traffickCensusCtCoefficientsRanked)) {
  cat("Correlation coefficient for", demographic, ":", 
      traffickCensusCtCoefficientsRanked[demographic], "\n")}
# Correlation coefficient for AgeDetailR : -0.2100901 
# Correlation coefficient for TotalPopulation : 0.1800564 
# Correlation coefficient for TotalHouseholds : 0.1736707 
# Correlation coefficient for IncomeInPast12MonthsR : 0.06991647 
# Correlation coefficient for InternetR : 0.06557326 
# Correlation coefficient for EmploymentR : 0.06260199 
# Correlation coefficient for ComputerR : 0.06081176 
# Correlation coefficient for GenderR : -0.0559172 
# Correlation coefficient for AgeR : 0.05390183 
# Correlation coefficient for PovertyR : 0.05296035 
# Correlation coefficient for EducationR : 0.04654063 
  # As seen in the results above, there are no moderate or strong correlations,
  # though, aligned with the regression model, age detail, population, and 
  # households have the highest signficance


  # Create a correlation matrix
traffickCensusMatrix = cor(traffickCensus_2013to2021R)

traffickCensusMatrix
# Long output ;)


  # Plot the matrix (lol)
corrplot(traffickCensusMatrix, type = 'upper', order = 'hclust',
         p.mat = traffickCensusMatrix, sig.level = 0.05, bg = 'light blue')
# Validates results above - no moderate or strong correlations



# Summary ----
# While each census demographics' correlation with trafficking crime arrests is 
# found to be significant, there are no moderate or strong correlations. The 
# strongest of these weak correlations are, in ranked order:
  # Age detail
  # Total population
  # Total households