# DSO110 - Data Science Final Project
  # File 5-B
  # Analysis: Pearson Correlation

# Goal: Determine whether there are any other correlations between reported 
  # non-trafficking arrests and trafficking crime arrests in the FBI data

# H0: No independent variables predict arrests for trafficking crimes
# H1: One or more independent variables predict arrests for trafficking crimes

# IV: TBD
# DV: Trafficking arrests


# Import packages ----
library(corrplot)
library(dplyr)


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
# 1,386 entries, 28 total columns


  # Drop non-total rows
traffickCrime_2013to2021R = traffickCrime_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickCrime_2013to2021R)
# 459 entries, 29 total columns
  # Sample size still validated


  # Drop age column
traffickCrime_2013to2021R = subset(traffickCrime_2013to2021R, select = -(Age))

View(traffickCrime_2013to2021R)
# 459 entries, 28 total columns


  # Subset to only include IV's
crime_2013to2021 = traffickCrime_2013to2021R %>% select(
  Rape, Sex, AggravatedAssault, Arson, Assault, Burglary,
  CarTheft, CurfewLoitering, DisorderlyConduct, DrugAbuse, Drunkenness, DUI, 
  Embezzlement, FamilyChildren, ForgeryCounterfeit, Fraud, Gambling, 
  Larceny, LiquorLaws, MurderManslaughter, AllOther, Robbery, StolenProperty, 
  Suspicion, Vagrancy, Vandalism, Weapons)

View(crime_2013to2021)
# 459 entries, 27 total columns



# Correlations ----

  # Run correlation tests on each possible IV
traffickCrimeCtResults = list()

for (crime in names(crime_2013to2021)) {
  traffickCrimeCt = cor.test(
    traffickCrime_2013to2021R$TotalTraffick, traffickCrime_2013to2021R[[crime]], 
    method = 'pearson', use = 'complete.obs')
  traffickCrimeCtResults[[crime]] = traffickCrimeCt}

for (crime in names(crime_2013to2021)) {
  cat('Correlation test for', crime, ':\n')
  print(traffickCrimeCtResults[[crime]])
  cat('\n')}
# Correlation test for Rape :
# 	Pearson's product-moment correlation
# data:  traffickCrime_2013to2021$TotalTraffick and traffickCrime_2013to2021[[crime]]
# t = 12.42, df = 457, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.4306393 0.5677855
# sample estimates:
#       cor 
# 0.5023654 
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # The correlation coefficient - 0.50 - indicates a moderate correlation
    # This means that arrests are moderately, significantly, and positively 
    # correlated with trafficking arrests - when there are more rape arrests, 
    # there are more trafficking crime arrests

  # Print just the correlation coefficients, in ranked order, for each crime
traffickCrimeCtCoefficients = vector()

for (crime in names(crime_2013to2021)) {
  traffickCrimeCtResults = cor.test(
    traffickCrime_2013to2021R$TotalTraffick, traffickCrime_2013to2021R[[crime]],
    method = 'pearson', use = 'complete.obs')
  
  traffickCrimeCtCoefficients[crime] = traffickCrimeCtResults$estimate}

traffickCrimeCtCoefficientsRanked = traffickCrimeCtCoefficients[order(
  abs(traffickCrimeCtCoefficients), decreasing = TRUE)]

for (crime in names(traffickCrimeCtCoefficientsRanked)) {
  cat('Correlation coefficient for', crime, ':', 
      traffickCrimeCtCoefficientsRanked[crime], '\n')}
# Correlation coefficient for Rape : 0.5883471 
# Correlation coefficient for Assault : 0.554472 
# Correlation coefficient for MurderManslaughter : 0.5223676 
# Correlation coefficient for Weapons : 0.5023654 
# Correlation coefficient for DUI : 0.4584126 
# Correlation coefficient for DrugAbuse : 0.4552506 
# Correlation coefficient for ForgeryCounterfeit : 0.448195 
# Correlation coefficient for CarTheft : 0.4377995 
# Correlation coefficient for AllOther : 0.426628 
# Correlation coefficient for Drunkenness : 0.4172113 
# Correlation coefficient for Robbery : 0.4022078 
# Correlation coefficient for AggravatedAssault : 0.3919692 
# Correlation coefficient for Larceny : 0.3914978 
# Correlation coefficient for Arson : 0.3442603 
# Correlation coefficient for Burglary : 0.3374415 
# Correlation coefficient for Vandalism : 0.332994 
# Correlation coefficient for Sex : 0.3324707 
# Correlation coefficient for Fraud : 0.3156746 
# Correlation coefficient for Vagrancy : 0.3090647 
# Correlation coefficient for Gambling : 0.2355253 
# Correlation coefficient for StolenProperty : 0.2219129 
# Correlation coefficient for LiquorLaws : 0.2164563 
# Correlation coefficient for Embezzlement : 0.2055427 
# Correlation coefficient for FamilyChildren : 0.1289662 
# Correlation coefficient for CurfewLoitering : 0.1024079 
# Correlation coefficient for DisorderlyConduct : 0.06847737 
# Correlation coefficient for Suspicion : -0.05469867 


  # Create a correlation matrix
traffickCrimeMatrix = cor(traffickCrime_2013to2021R)

traffickCrimeMatrix
# Long output ;)


  # Plot the matrix (lol)
corrplot(traffickCrimeMatrix, type = 'upper', order = 'hclust',
         p.mat = traffickCrimeMatrix, sig.level = 0.05, bg = 'light blue')
# Looks like assault and rape have the strongest (though still only moderate) 
  # correlations with trafficking arrests, which aligns with the results above; 
  # also aligned with the results above are moderate correlations with murder/
  # manslaughter and weapons - the rest are minor enough to not show strongly
  # on this matrix


# Summary ----
# The most significant non-trafficking crime arrests are that are each 
# moderately and positively correlated with trafficking arrests - when there 
# are more of each of these crime arrests, there are more trafficking crime 
# arrests - are, in ranked order:
  # Rape
  # Assault
  # Murder / manslaughter
  # Weapons