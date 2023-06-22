# DSO110 - Data Science Final Project
  # File 4-C
  # Analysis: Pearson Correlation

# Goal: Determine whether higher rates of reported arrests for human trafficking 
  # crimes are more likely to be found where there are higher rates of crime 
  # overall

# H0: Overall crime arrests do not predict arrests for trafficking crimes
# H1: Overall crime arrests do predict arrests for trafficking crimes

# IV: All crime arrests
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
traffickCrime_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, TotalAll, TotalTraffick)

View(traffickCrime_2013to2021)
# 1,386 entries, 2 total columns


  # Drop non-total rows
traffickCrime_2013to2021R = traffickCrime_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickCrime_2013to2021R)
# 459 entries, 3 total columns
  # Sample size still validated


  # Drop age column
traffickCrime_2013to2021R = subset(
  traffickCrime_2013to2021R, select = -(Age))

View(traffickCrime_2013to2021R)
# 459 entries, 2 total columns



# Correlations ----

  # Create a correlation test
cor.test(traffickCrime_2013to2021R$TotalTraffick, 
         traffickCrime_2013to2021R$TotalAll, 
         method = 'pearson', use = 'complete.obx')
# 	Pearson's product-moment correlation
# data:  traffickCrime_2013to2021$TotalTraffick and traffickCrime_2013to2021$TotalAll
# t = 11.313, df = 457, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.3930336 0.5363022
# sample estimates:
#       cor 
# 0.4677346
  # This p value indicates the test is significant - reject the null and accept 
    # the alternative hypothesis
    # The correlation coefficient - 0.47 - indicates a moderate correlation
    # This means that total crime arrests are moderately, significantly, and 
    # positively correlated with trafficking arrests - when there are more total 
    # crime arrests, there are more trafficking crime arrests


  # Create a correlation matrix
traffickCrimeMatrix = cor(traffickCrime_2013to2021R)

traffickCrimeMatrix
#               TotalAll TotalTraffick
# TotalAll     1.0000000     0.4677346


  # Plot the matrix (lol)
corrplot(traffickCrimeMatrix, type = 'upper', order = 'hclust',
         p.mat = traffickCrimeMatrix, sig.level = 0.05, bg = 'light blue')
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
# Among other correlations found, this finds a 51% correlation between
  # total crime and trafficking crime arrests, which validates the results above



# Summary ----
# Total crime arrests are moderately, significantly, and positively correlated 
# with trafficking arrests - when there are more total crime arrests, there are 
# more trafficking crime arrests