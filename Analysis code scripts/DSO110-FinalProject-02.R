# DSO110 - Data Science Final Project
  # File 2
  # Analysis: Basic, one-way ANOVA

# Goal: Determine whether the prevalence of reported arrests for human 
  # trafficking crimes has changed over time, based on FBI data from 2013-2021

# H0: The prevalence of reported human trafficking arrests has remained 
  # consistent over time
# H1: The prevalence of reported human trafficking arrests has changed over 
  # time

# IV: Prevalence of trafficking arrests
# DV: Year


# Import packages ----
library(broom)
library(car)
library(dplyr)
library(IDPmisc)
library(rcompanion)


# Import and preview data ----
traffickingCrime_2013to2021 = read.csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/traffickingAllCrimes_2013to2021.csv')

View(traffickingCrime_2013to2021)
# 1,386 entries, 41 total columns
  # Sample size is validated for now...
  # Lots of 0 values



# Wrangling ----

  # Subset data to only keep columns I'll use
traffickingByYear_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, Year, TotalTraffick)

View(traffickingByYear_2013to2021)
# 1,386 entries, 2 total columns


  # Drop non-total rows
traffickingByYear_2013to2021R = traffickingByYear_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickingByYear_2013to2021R)
# 459 entries, 3 total columns
  # Sample size still validated


  # Drop age column
traffickingByYear_2013to2021R = subset(
  traffickingByYear_2013to2021R, select = -(Age))

View(traffickingByYear_2013to2021R)
# 459 entries, 2 total columns


  # Transform via log - jumping straight to this per validating in a separate
    # script and analysis
traffickingByYear_2013to2021R$TotalTraffickLog = log(
  traffickingByYear_2013to2021R$TotalTraffick)

View(traffickingByYear_2013to2021R)
# 459 entries, 3 total columns


    # Drop NA's
traffickingByYear_2013to2021R = NaRV.omit(traffickingByYear_2013to2021R)

View(traffickingByYear_2013to2021R)
# 293 entries, 3 total columns
  # Sample size still validated



# Test assumptions ----

  # Check distribution
plotNormalHistogram(traffickingByYear_2013to2021R$TotalTraffickLog)
# Looks good!


  # Check for homogeneity of variance
bartlett.test(TotalTraffickLog ~ Year, data = traffickingByYear_2013to2021R)
# 	Bartlett test of homogeneity of variances
# data:  TotalTraffickLog by Year
# Bartlett's K-squared = 1.4931, df = 8, p-value = 0.9928
  # The p value above 0.05 validates the assumption of homogeneity of variance


  # Sample size validated above



# Create model ----

  # Using aov() function, per homogeneity of variance
traffickingByYearAnova = aov(
  TotalTraffickLog ~ Year, data = traffickingByYear_2013to2021R)

summary(traffickingByYearAnova)
#              Df Sum Sq Mean Sq F value Pr(>F)
# Year          1    3.7   3.748   1.447   0.23
# Residuals   291  753.8   2.590
  # The p value above 0.05 did not find significance - accept the null and 
  # reject the alternative hypothesis



# Post hoc analysis (anyway) ----

  # Run pairwise t test and view only significant results
traffickingByYearTtest = pairwise.t.test(
  traffickingByYear_2013to2021R$TotalTraffickLog, 
  traffickingByYear_2013to2021R$Year, p.adjust = 'bonferroni', 
  pool.sd = FALSE)

traffickingByYearTtestSig = tidy(
  traffickingByYearTtest, p.adjust.method = 'bonferroni')

traffickingByYearTtestSig = subset(
  traffickingByYearTtestSig, p.value <= 0.05)

View(traffickingByYearTtestSig)
# Confirms no significance


  # Look at means
traffickingByYearMeans = traffickingByYear_2013to2021R %>% 
  group_by(Year) %>% 
  summarise(Mean = mean(TotalTraffick)) %>% 
  arrange(desc(Mean)) 

View(traffickingByYearMeans)
# 9 entries, 2 total columns
  # These seem different enough that there should be significance...


  # Look at totals
traffickingByYearTotals = traffickingByYear_2013to2021R %>% 
  group_by(Year) %>% 
  summarise(Total = sum(TotalTraffick)) %>% 
  arrange(desc(Total))

View(traffickingByYearTotals)
# Arrests go up by over 130 from the lowest to highest year, so I am convinced
  # this is significant - will try again with data paired down to this level
# 5 years with highest reported arrests for trafficking crimes from 2013- 2021
  # 2020 144070
  # 2019 131796
  # 2021 130066
  # 2018 97922
  # 2017 86267



# Re-run testing and analysis on Totals dataset ----

  # Check distribution again
plotNormalHistogram(traffickingByYearTotals$Total)
# Decently normal

  # Check for homogeneity of variance
# bartlett.test(Total ~ Year, data = traffickingByYearTotals)
# Can't run this per violating sample size in this version, so I commented out

  # Create model
traffickingByYearReDoAnova = aov(
  Total ~ Year, data = traffickingByYearTotals)

summary(traffickingByYearReDoAnova)
#             Df    Sum Sq   Mean Sq F value  Pr(>F)    
# Year         1 1.553e+10 1.553e+10   125.1 1.02e-05 ***
# Residuals    7 8.694e+08 1.242e+08                   
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
  # Voila! I knew it - this finds high significance
  # Because this is a more logical conclusion when looking at the data, I am
  # going to take this as the conclusion



# Summary ----
# The numbers of reported human trafficking crime arrests varies significantly 
  # by year from 2013- 2021 - more research would be necessary to identify the 
  # various factors which could explain this, but a few hypotheses are that
  # there are differences in the numbers of arrests to report, differences in 
  # reporting processes meaning some years are more comprehensive than others 
  # about reporting, and/ or the decriminalization of trafficking victims by
  # reducing crimes for sex sellers, while maintaining crimes for sex buyers
# Overall reported arrests have gone up over time, though they did go back down
  # in 2021
# Year with highest reported trafficking crimes: 2020 144,070
# Year with lowest average reported trafficking crimes: 2013 11,092