# DSO110 - Data Science Final Project
  # File 3-C
  # Analysis: Pearson Correlation

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found where there are higher rates of reported 
  # non-trafficking sex crime arrests

# H0: Arrests for non-trafficking sex crimes are not correlated to trafficking
  # crime arrests
# H1: Arrests for non-trafficking sex crimes are correlated to trafficking
  # crime arrests 

# IV: Non-trafficking sex arrests
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

  # Subset data to only keep columns I'll use
traffickNonTraffickSex_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, TotalTraffick, TotalNonTraffickSex)

View(traffickNonTraffickSex_2013to2021)
# 1,386 entries, 3 total columns


  # Drop non-total rows
traffickNonTraffickSex_2013to2021 = traffickNonTraffickSex_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickNonTraffickSex_2013to2021)
# 459 entries, 3 total columns
  # Sample size still validated


  # Drop age column
traffickNonTraffickSex_2013to2021 = subset(
  traffickNonTraffickSex_2013to2021, select = -(Age))

View(traffickNonTraffickSex_2013to2021)
# 459 entries, 2 total columns


  # Remove rows with all 0's
traffickNonTraffickSex_2013to2021R = traffickNonTraffickSex_2013to2021[
  rowSums(traffickNonTraffickSex_2013to2021 != 0) > 0, ]

View(traffickNonTraffickSex_2013to2021R)
# 456 entries, 2 total columns



# Correlations ----

  # Create a correlation test
cor.test(traffickNonTraffickSex_2013to2021R$TotalTraffick, 
         traffickNonTraffickSex_2013to2021R$TotalNonTraffick, 
         method = 'pearson', use = 'complete.obx')
# 	Pearson's product-moment correlation
# data:  traffickNonTraffickSex_2013to2021R$TotalTraffick and traffickNonTraffickSex_2013to2021R$TotalNonTraffick
# t = 9.6827, df = 454, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.3346022 0.4870427
# sample estimates:
#       cor 
# 0.4137181
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # The correlation coefficient - 0.41 - indicates a moderate correlation
    # This means that non-trafficking sex crime arrests are moderately, 
    # significantly, and positively correlated with trafficking arrests - when
    # there are more non-trafficking sex crime arrests, there are more 
    # trafficking crime arrests


  # Create a correlation matrix
traffickNonTraffickSexMatrix = cor(traffickNonTraffickSex_2013to2021R)

traffickNonTraffickSexMatrix
#                     TotalTraffick TotalNonTraffickSex
# TotalTraffick           1.0000000           0.4137181


  # Plot the matrix (lol)
corrplot(traffickNonTraffickSexMatrix, type = 'upper', order = 'hclust',
         p.mat = traffickNonTraffickSexMatrix, sig.level = 0.05, 
         bg = 'light blue')
# Not super useful.. will try with full dataset...


    # Subset to only include numeric data
traffickingCrimeNumeric = subset(
  traffickingCrime_2013to2021, select = -c(State, Age))

View(traffickingCrimeNumeric)
# 1,386 entries, 39 total columns


    # Matrix for full dataset
traffickingCrimeMatrix = cor(traffickingCrimeNumeric)


    # Plot the matrix for full dataset - as a separate file for readability
colorPalette = colorRampPalette(c('#43eeab', 'white', 'hotpink'))(100)
png('traffickingCrimeMatrix.png', width = 25, height = 25, units = 'in', 
    res = 300)
corrplot(traffickingCrimeMatrix, col = colorPalette, method = 'number', 
         tl.col = 'blue', tl.srt = 45, type = 'upper')
dev.off()
browseURL('traffickingCrimeMatrix.png')
# Among other correlations found, this finds a 45% correlation between
  # non-trafficking and trafficking crime arrests, which validates the results 
  # above



# Summary ----
# Non-trafficking sex crime arrests are moderately, significantly, and 
# positively correlated with trafficking arrests - when there are more 
# non-trafficking sex crime arrests, there are more trafficking crime arrests