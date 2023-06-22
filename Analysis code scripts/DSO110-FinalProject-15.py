# %%
# DSO110 - Data Science Final Project
    # File 15
    # Analysis: k-Means (Cluster Analysis)

# Goal: Determine what the leading, contributing factors to people being 
  # trafficked are, according to US census and FBI crime data for 2013- 2021

# H0: No census demographics predict arrests for trafficking crimes
# H1: One or more census demographics predict arrests for trafficking crimes

# IV's: Each demographic
# DV: Trafficking arrests

# Import packages
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# %%

# Import data

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import data
allData_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/allData_2013to2021.csv')

allData_2013to2021

# %%
# 92593 rows × 51 columns

        # Remove duplicate index column
allData_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

allData_2013to2021

# %%
# 92593 rows × 50 columns


# Wrangling

    # Subset to only include trafficking and demographic data
traffickingCensus = allData_2013to2021[[
    'Age', 'AgeDetail', 'Computer', 'Education', 'Employment', 'Gender', 'IncomeInPast12Months', 'Internet', 'Poverty', 'TotalHouseholds', 
    'TotalPopulation', 'TotalTraffick']]

traffickingCensus

# %%
# 92593 rows × 12 columns


    # Recode categorical variables

        # Age
traffickingCensus['AgeR'] = traffickingCensus['Age']

traffickingCensus['AgeR'].replace(['Total all ages', 'Under 18', 'Over 18'], [
    1, 2, 3], inplace = True)

traffickingCensus

# %%
# 92593 rows × 13 columns
    # Visually confirmed success

        # Age detail

            # Confirm unique values
traffickingCensus.AgeDetail.unique()

# %%

            # Recode
traffickingCensus['AgeDetailR'] = traffickingCensus['AgeDetail']

traffickingCensus['AgeDetailR'].replace([
    'nan', '0 to 17', '18 to 24', '25 to 34', '35 to 44', '45 to 54', '55+', 
    'Under 5', '5 to 9', '10 to 14', '15 to 19', '20 to 24', '25 to 29', 
    '30 to 34', '35 to 39', '0 to 4', '45 to 49', '50 to 54', '55 to 59', 
    '60 to 64', '65 to 69', '70 to 74', '75 to 79', '80 to 84', '45 to 64', 
    'Under 18', '5 to 17', '18 to 64'], [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
        20, 21, 22, 23, 24, 25, 26, 27], inplace = True)

traffickingCensus

# %%
# 92593 rows × 14 columns
    # Visually confirmed success


        # Computer

            # Confirm unique values
traffickingCensus.Computer.unique()

# %%

            # Recode
traffickingCensus['ComputerR'] = traffickingCensus['Computer']

traffickingCensus['ComputerR'].replace([
    'nan', 'Has one or more types of computing devices', 'Desktop or laptop',
    'Desktop or laptop with no other type of computing device', 'Smartphone', 
    'Smartphone with no other type of computing device',
    'Tablet or other portable wireless computer',
    'Tablet or other portable wireless computer with no other type of computing device', 'Other computer',
    'Other computer with no other type of computing device', 'No computer'], [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], inplace = True)

traffickingCensus

# %%
# 92593 rows × 15 columns
    # Visually confirmed success


        # Education

            # Confirm unique values
traffickingCensus.Education.unique()

# %%

            # Recode
traffickingCensus['EducationR'] = traffickingCensus['Education']

traffickingCensus['EducationR'].replace([
    'nan', 'Less than high school graduate', 
    'High school graduate (includes equivalency)',
    'Some college or associate\'s degree', "Bachelor's degree or higher", 
    'High school graduate or higher', 'Less than 9th grade', 
    '9th to 12th grade, no diploma', 'Some college, no degree', 
    "Associate's degree", "Bachelor's degree", 
    'Graduate or professional degree'], [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], inplace = True)

traffickingCensus

# %%
# 92593 rows × 16 columns
    # Visually confirmed success


        # Employment

            # Confirm unique values
traffickingCensus.Employment.unique()

# %%

            # Recode
traffickingCensus['EmploymentR'] = traffickingCensus['Employment']

traffickingCensus['EmploymentR'].replace([
    'nan', 'Employed', 'Unemployed', 
    'Worked full-time, year-round in the past 12 months',
    'Worked part-time or part-year in the past 12 months','Did not work'], [
        0, 1, 2, 3, 4, 5], inplace = True)

traffickingCensus

# %%
# 92593 rows × 17 columns
    # Visually confirmed success


        # Gender
traffickingCensus['GenderR'] = traffickingCensus['Gender']

traffickingCensus['GenderR'].replace([
    'nan', 'Female', 'Male'], [0, 1, 2], inplace = True)

traffickingCensus

# %%
# 91371 rows × 18 columns
    # Visually confirmed success


        # Income

            # Confirm unique values
traffickingCensus.IncomeInPast12Months.unique()

# %%

            # Recode
traffickingCensus['IncomeInPast12MonthsR'] = traffickingCensus[
    'IncomeInPast12Months']

traffickingCensus['IncomeInPast12MonthsR'].replace([
    'nan', 'Less than $20,000', '$20,000 to $74,999', '$75,000 or more'], [
        0, 1, 2, 3], inplace = True)

traffickingCensus

# %%
# 92593 rows × 19 columns
    # Visually confirmed success


        # Internet

            # Confirm unique values
traffickingCensus.Internet.unique()

# %%

            # Recode
traffickingCensus['InternetR'] = traffickingCensus['Internet']

traffickingCensus['InternetR'].replace([
    'nan', 'With an Internet subscription',
    'Dial-up with no other type of Internet subscription',
    'Broadband of any type', 'Cellular data plan',
    'Cellular data plan with no other type of Internet subscription',
    'Broadband such as cable, fiber optic or DSL',
    'Satellite Internet service', 'Without an Internet subscription'], [
        0, 1, 2, 3, 4, 5, 6, 7, 8], inplace = True)

traffickingCensus

# %%
# 92593 rows × 20 columns
    # Visually confirmed success


        # Poverty

            # Confirm unique values
traffickingCensus.Poverty.unique()

# %%

            # Recode
traffickingCensus['PovertyR'] = traffickingCensus['Poverty']

traffickingCensus['PovertyR'].replace([
    'nan', 'Poverty status is determined', 'Below poverty level'], [0, 1, 2], 
    inplace = True)

traffickingCensus

# %%
# 92593 rows × 21 columns
    # Visually confirmed success


        # Ensure data are numeric, with whole numbers

            # Subset to only include numeric data
traffickingCensusR = traffickingCensus[[
    'AgeR', 'AgeDetailR', 'ComputerR', 'EducationR', 'EmploymentR', 'GenderR', 'IncomeInPast12MonthsR', 'InternetR', 'PovertyR','TotalHouseholds', 'TotalPopulation', 'TotalTraffick']]

traffickingCensusR

# %%
# 92593 rows × 12 columns
    # Visually confirmed success

            # Remove commas
traffickingCensusR = traffickingCensusR.replace(',', '', regex = True)

traffickingCensusR

# %%
# Visually confirmed success

            # Replace NA's with 0's and update data type for all count 
                # columns to integers
traffickingCensusR = traffickingCensusR.fillna(0).astype(float).astype(int)

traffickingCensusR

# %%
# Visually confirmed success


    # Drop rows with no known demographics (other than Age, which is never 
        # empty)
traffickingCensusR = traffickingCensusR[~(traffickingCensusR[[
    'AgeDetailR', 'ComputerR', 'EducationR', 'EmploymentR', 'GenderR', 'IncomeInPast12MonthsR', 'InternetR', 'PovertyR','TotalHouseholds', 'TotalPopulation', 'TotalTraffick']] == 0).all(axis = 1)]

traffickingCensusR
# %%
# 92462 rows × 12 columns
    # Visually confirmed success - not a ton removed


    # Export to csv
traffickingCensusR.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/traffickingCensusNumeric.csv')
# %%
# Success



# k-Means Analysis

    # Create k-Means model
traffickingCensusKm = KMeans(n_clusters = 2)

# %%

    # Fit the data to the model
traffickingCensusKm.fit(traffickingCensusR)

# %%
# KMeans(n_clusters=2)


# Interpretation

    # Plot each possible IV

        # Plot trafficking and age
plt.title('k Means - Trafficking (x) & Age (y)')
plt.scatter(traffickingCensusR.TotalTraffick, traffickingCensusR.AgeR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only "total all ages", but
    # the other cluster has data for all age groups

        # Plot trafficking and age detail
plt.title('k Means - Trafficking (x) & Age Detail (y)')
plt.scatter(traffickingCensusR.TotalTraffick, traffickingCensusR.AgeDetailR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no age
    # detail assigned, the other cluster has data for all age detail groups 
    # and when no age detail group is assigned

        # Plot trafficking and computer
plt.title('k Means - Trafficking (x) & Computer (y)')
plt.scatter(traffickingCensusR.TotalTraffick, traffickingCensusR.ComputerR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no
    # computer info assigned, the other cluster has data for all computer 
    # info and when no computer info is assigned

        # Plot trafficking and education
plt.title('k Means - Trafficking (x) & Education (y)')
plt.scatter(traffickingCensusR.TotalTraffick, traffickingCensusR.EducationR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no
    # education info assigned, the other cluster has data for all education 
    # info and when no education info is assigned

        # Plot trafficking and employment
plt.title('k Means - Trafficking (x) & Employment (y)')
plt.scatter(traffickingCensusR.TotalTraffick, traffickingCensusR.EmploymentR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no
    # employment info assigned, the other cluster has data for all employment 
    # info and when no employment info is assigned

        # Plot trafficking and gender
plt.title('k Means - Trafficking (x) & Gender (y)')
plt.scatter(traffickingCensusR.TotalTraffick, traffickingCensusR.GenderR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no
    # gender, the other cluster has data for both genders and no gender

        # Plot trafficking and income
plt.title('k Means - Trafficking (x) & Income (y)')
plt.scatter(traffickingCensusR.TotalTraffick, 
            traffickingCensusR.IncomeInPast12MonthsR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no
    # income assigned, the other cluster has data for all incomes and when no 
    # income is assigned

        # Plot trafficking and internet
plt.title('k Means - Trafficking (x) & Internet (y)')
plt.scatter(traffickingCensusR.TotalTraffick, traffickingCensusR.InternetR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no
    # internet info assigned, the other cluster has data for all internet 
    # info and when no internet info is assigned

        # Plot trafficking and poverty
plt.title('k Means - Trafficking (x) & Poverty (y)')
plt.scatter(traffickingCensusR.TotalTraffick, traffickingCensusR.PovertyR, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no
    # poverty level assigned and for "Poverty status is determined" level, 
    # the other cluster has data for both poverty levels and when no poverty 
    # level is assigned

        # Plot trafficking and total households
plt.title('k Means - Trafficking (x) & Total Households (y)')
plt.scatter(traffickingCensusR.TotalTraffick, 
            traffickingCensusR.TotalHouseholds, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# Clustering has a lot of overlap - one cluster is only for data with no
    # households assigned, the other cluster has data for whether or not 
    # households are assigned

        # Plot trafficking and total population
plt.title('k Means - Trafficking (x) & Total Population (y)')
plt.scatter(traffickingCensusR.TotalTraffick, 
            traffickingCensusR.TotalPopulation, 
            c = traffickingCensusKm.labels_, 
            cmap = 'viridis')

# %%
# A clear clustering difference for populations above and below whatever 0.5 
    # stands represents



# Summary: When clustering trafficking and demographic data there are only 
# clearly correlated clusters for trafficking arrests and total population. One 
# cluster is for higher populations than the other.