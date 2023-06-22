# DSO110 - Data Science Final Project
  # File 6-C
  # Analysis: Pearson Correlation

# Goal: Determine whether higher rates of reported suicides are more likely to 
  # be found where there are higher rates of arrests for human trafficking 
  # crimes

# H0: Trafficking crimes arrests do not predict suicide rates
# H1: Trafficking crimes arrests do predict suicide rates

# IV: Trafficking arrests
# DV: Suicides


# Import packages ----
library(corrplot)
library(dplyr)


# Import and preview data ----
crimeSuicide_2013to2021 = read.csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/crimeSuicide_2013to2021.csv')

View(crimeSuicide_2013to2021)
# 3,021 entries, 43 total columns
  # Sample size is validated for now...
  # Lots of 0 values



# Wrangling ----

  # Subset data to only keep columns I'll use
suicideTraffick_2013to2021 = crimeSuicide_2013to2021 %>% 
  select(Age, TotalSuicide, TotalTraffick)

View(suicideTraffick_2013to2021)
# 3,021 entries, 3 total columns


  # Drop non-total rows
suicideTraffick_2013to2021R = suicideTraffick_2013to2021 %>%
  filter(Age == 'Total all ages')

View(suicideTraffick_2013to2021R)
# 459 entries, 3 total columns
  # Sample size still validated


  # Drop age column
suicideTraffick_2013to2021R = subset(
  suicideTraffick_2013to2021R, select = -(Age))

View(suicideTraffick_2013to2021R)
# 459 entries, 2 total columns



# Correlations ----

  # Create a correlation test
cor.test(suicideTraffick_2013to2021R$TotalSuicide, 
         suicideTraffick_2013to2021R$TotalTraffick, 
         method = 'pearson', use = 'complete.obx')
# 	Pearson's product-moment correlation
# data:  suicideTraffick_2013to2021$TotalSuicide and suicideTraffick_2013to2021$TotalTraffick
# t = 13.332, df = 457, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.4599247 0.5920283
# sample estimates:
#       cor 
# 0.5291756
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # The correlation coefficient - 0.53 - indicates a moderate correlation
    # This means that trafficking crime arrests are moderately, significantly, 
    # and positively correlated with suicides - when there are more trafficking 
    # crime arrests, there are more suicides


  # Create a correlation matrix
traffickCrimeMatrix = cor(suicideTraffick_2013to2021R)

traffickCrimeMatrix
#               TotalSuicide TotalTraffick
# TotalSuicide     1.0000000     0.5291756


  # Plot the matrix (lol)
corrplot(traffickCrimeMatrix, type = 'upper', order = 'hclust',
         p.mat = traffickCrimeMatrix, sig.level = 0.05, bg = 'light blue')
# Not super useful.. will try with full dataset...


    # Subset to only include numeric data
crimeSuicideNumeric = subset(crimeSuicide_2013to2021, select = -c(
  State, Age, AgeDetail))

View(crimeSuicideNumeric)
# 3,021 entries, 40 total columns


    # Matrix for full dataset
crimeSuicideMatrix = cor(crimeSuicideNumeric)


    # Plot the matrix for full dataset - as a separate file for readability
colorPalette = colorRampPalette(c('#43eeab', 'white', 'hotpink'))(100)
png('crimeSuicideMatrix.png', width = 25, height = 25, units = 'in', res = 300)
corrplot(crimeSuicideMatrix, col = colorPalette, method = 'number', tl.col = 'blue', 
         tl.srt = 45, type = 'upper')
dev.off()
browseURL('crimeSuicideMatrix.png')
# Among other correlations found, this finds a 34% correlation between
  # suicides and trafficking crime arrests, which validates the results above



# Summary ----
# Trafficking crime arrests are moderately, significantly, and positively 
# correlated with suicides - when there are more trafficking crime arrests, 
# there are more suicides.