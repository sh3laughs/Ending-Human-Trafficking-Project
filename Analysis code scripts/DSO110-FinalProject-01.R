# DSO110 - Data Science Final Project
  # File 1
  # Analysis: Basic, one-way ANOVA

# Goal: Determine which states in the US have the highest prevalence of 
  # reported arrests for human trafficking crimes, based on FBI data from 
  # 2013-2021

# H0: States have equivalent prevalence of reported human trafficking arrests
# H1: States have differing prevalence of reported human trafficking arrests

# IV: State
# DV: Prevalence of trafficking arrests


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
traffickingByState_2013to2021 = traffickingCrime_2013to2021 %>% 
  select(Age, State, TotalTraffick)

View(traffickingByState_2013to2021)
# 1,386 entries, 3 total columns


  # Drop non-total rows
traffickingByState_2013to2021R = traffickingByState_2013to2021 %>%
  filter(Age == 'Total all ages')

View(traffickingByState_2013to2021R)
# 459 entries, 3 total columns
  # Sample size still validated


  # Drop age column
traffickingByState_2013to2021R = subset(
  traffickingByState_2013to2021R, select = -(Age))

View(traffickingByState_2013to2021R)
# 459 entries, 2 total columns


# Test assumptions ----

  # Check distribution
plotNormalHistogram(traffickingByState_2013to2021R$TotalTraffick)
# Very positively skewed


    # Transform
traffickingByState_2013to2021R$TotalTraffickSqrt = sqrt(
  traffickingByState_2013to2021R$TotalTraffick)

View(traffickingByState_2013to2021R)
# 459 entries, 3 total columns


    # Check distribution again
plotNormalHistogram(traffickingByState_2013to2021R$TotalTraffickSqrt)
# Better but not great


    # Transform again
traffickingByState_2013to2021R$TotalTraffickLog = log(
  traffickingByState_2013to2021R$TotalTraffick)

View(traffickingByState_2013to2021R)
# 459 entries, 4 total columns
  # Lots of infinite values

    # Drop NA's
traffickingByState_2013to2021R = NaRV.omit(traffickingByState_2013to2021R)

View(traffickingByState_2013to2021R)
# 293 entries, 4 total columns
  # Sample size still validated


    # Check distribution again
plotNormalHistogram(traffickingByState_2013to2021R$TotalTraffickLog)
# Great bell curve!



  # Check for homogeneity of variance
bartlett.test(TotalTraffickLog ~ State, data = traffickingByState_2013to2021R)
# 	Bartlett test of homogeneity of variances
# data:  TotalTraffickLog by State
# Bartlett's K-squared = 111.1, df = 50, p-value = 1.551e-06
  # The p value under 0.05 is test is significant, which violates the  
  # assumption of homogeneity of variance (this is heterogeneity of variance)


  # Sample size validated above



# Create model ----

  # Using Anova() function, per heterogeneity of variance
traffickingByStateAnova = lm(
  TotalTraffickLog ~ State, data = traffickingByState_2013to2021R)

Anova(traffickingByStateAnova, Type = 'II', white.adjust = TRUE)
# Coefficient covariances computed by hccm()
# Analysis of Deviance Table (Type II tests)
# Response: TotalTraffickLog
#            Df      F    Pr(>F)    
# State      50 43.996 < 2.2e-16 ***
# Residuals 242                      
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
  # The p value under 0.05 validates significance - validating that the number 
  # of reported arrests for trafficking crimes differs by state, though it 
  # doesn't tell us how it differs
  # Reject the null and accept the alternative hypothesis



# Post hoc analysis ----

  # Run pairwise t test and view only significant results
traffickingByStateTtest = pairwise.t.test(
  traffickingByState_2013to2021R$TotalTraffickLog, 
  traffickingByState_2013to2021R$State, p.adjust = 'bonferroni', 
  pool.sd = FALSE)

traffickingByStateTtestSig = tidy(
  traffickingByStateTtest, p.adjust.method = 'bonferroni')

traffickingByStateTtestSig = subset(
  traffickingByStateTtestSig, p.value <= 0.05)

View(traffickingByStateTtestSig)
# 118 entries, 3 total columns
  # So... 118 pairs of states have significantly different numbers of 
  # reported arrests for trafficking crimes - though this doesn't indicate 
  # which has higher vs. lower significance
  # A little math tells me that there are 1,275 possible combinations of two 
  # for 51 states (including DC)...


  # Look at means
traffickingByStateMeans = traffickingByState_2013to2021R %>% 
  group_by(State) %>% 
  summarise(Mean = mean(TotalTraffick)) %>% 
  arrange(desc(Mean)) 

View(traffickingByStateMeans)
# 51 entries, 2 total columns
  # This is helpful - though will be more helpful to merge the means and 
  # p-values into a single dataframe
  # 5 states with highest average reported arrests for trafficking crimes
    # TEXAS 23318.5000
    # NEVADA 11170.5000
    # FLORIDA 8112.2000
    # MINNESOTA 7757.2500
    # GEORGIA 6589.0000
  # 5 states with lowest average reported arrests for trafficking crimes
    # NEW YORK 149.3333
    # MONTANA 139.7143
    # VERMONT 130.5000
    # MISSISSIPPI 92.5000
    # WASHINGTON DC 24.0000


    # Update names of columns in significance variable to be more clear
colnames(traffickingByStateTtestSig) = c('State1', 'State2', 'p.value')

View(traffickingByStateTtestSig)
# Visually confirmed success


    # Ensure significance variable only includes unique pairs of states, in a
      # new variable means will be added to
traffickingByStateTtestSigAndMeans = traffickingByStateTtestSig %>% 
  group_by(group = paste(pmin(State1, State2), pmax(State1, State2))) %>% 
  slice_head(n = 1) %>% 
  ungroup() %>% 
  select(State1, State2)

View(traffickingByStateTtestSigAndMeans)
# 118 entries, 2 total columns


    # Add mean values for each state to the new variable
traffickingByStateTtestSigAndMeans = traffickingByStateTtestSigAndMeans %>% 
  left_join(traffickingByStateMeans, by = c('State1' = 'State')) %>% 
  rename(Mean1 = Mean) %>% 
  left_join(traffickingByStateMeans, by = c('State2' = 'State')) %>% 
  rename(Mean2 = Mean)

View(traffickingByStateTtestSigAndMeans)
# 118 entries, 4 total columns


    # Add p-values to the new variable
traffickingByStateTtestSigAndMeans$p.value = traffickingByStateTtestSig$p.value[
  match(paste(traffickingByStateTtestSigAndMeans$State1, 
              traffickingByStateTtestSigAndMeans$State2), 
        paste(traffickingByStateTtestSig$State1, 
              traffickingByStateTtestSig$State2))]

View(traffickingByStateTtestSigAndMeans)
# 118 entries, 5 total columns


    # Reorder columns in new variable
traffickingByStateTtestSigAndMeans = traffickingByStateTtestSigAndMeans[
  , c('State1', 'Mean1', 'State2', 'Mean2', 'p.value')]

View(traffickingByStateTtestSigAndMeans)
# Visually confirmed success
  # Five most significantly different pairs of states
    # CALIFORNIA | ALASKA | 3.732344e-02
    # FLORIDA | ALASKA | 2.983113e-02
    # MINNESOTA | ALASKA | 3.287761e-02
    # TEXAS | ALASKA | 9.885541e-03
    # CALIFORNIA | ARKANSAS | 4.802091e-03

  # Look at totals
traffickingByStateTotals = traffickingByState_2013to2021R %>% 
  group_by(State) %>% 
  summarise(Total = sum(TotalTraffick)) %>% 
  arrange(desc(Total)) 

View(traffickingByStateTotals)
# 5 states with highest reported arrests for trafficking crimes from 2013- 2021
  # TEXAS 186548
  # NEVADA 67023
  # MINNESOTA 62058
  # CALIFORNIA 59154
  # FLORIDA 40561
# 5 states with lowest reported arrests for trafficking crimes from 2013- 2021
  # VERMONT 783
  # KANSAS 448
  # NEW YORK 448
  # MISSISSIPPI 370
  # WASHINGTON DC 48



# Summary ----
# The numbers of reported arrests for human trafficking crimes varies 
  # significantly by state from 2013- 2021 - more research would be necessary 
  # to identify the various factors which could explain this, but a couple of 
  # hypotheses are that there are differences in the numbers of arrests and/ or 
  # differences in reporting processes meaning some states are more 
  # comprehensive than others about reporting
# 5 states with highest reported arrests for trafficking crimes from 2013- 2021
  # TEXAS 186,548
  # NEVADA 67,023
  # MINNESOTA 62,058
  # CALIFORNIA 59,154
  # FLORIDA 40,561
# 5 states with lowest reported arrests for trafficking crimes from 2013- 2021
  # VERMONT 783
  # KANSAS 448
  # NEW YORK 448
  # MISSISSIPPI 370
  # WASHINGTON DC 48