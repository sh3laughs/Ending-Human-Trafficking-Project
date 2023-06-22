# %%
# DSO110 - Data Science Final Project
    # File 7R
    # Wrangling: Joining allCrime, trafficking crime, and suicide data for all 
        # years (2013- 2021)

# Import packages
import pandas as pd

# %%

# Import tables

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # allCrime data
allCrimes_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimesWithTotals_2013to2021.csv')

allCrimes_2013to2021

# %%
# 1377 rows × 38 columns

        # Remove duplicate index column
allCrimes_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

allCrimes_2013to2021

# %%
# 1377 rows × 37 columns


    # Trafficking crime data
traffickingCrimes_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/traffickingCrimes_2013to2021.csv')

traffickingCrimes_2013to2021

# %%
# 647 rows × 7 columns

        # Remove duplicate index column
traffickingCrimes_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

traffickingCrimes_2013to2021

# %%
# 647 rows × 6 columns


    # Suicide data
suicides_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Suicide/suicides_2013to2021.csv')

suicides_2013to2021

# %%
# 2792 rows × 6 columns

        # Remove duplicate index column
suicides_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

suicides_2013to2021

# %%
# 2792 rows × 5 columns



# Join allCrime and trafficking crime data
traffickingAllCrimes_2013to2021 = pd.merge(
    allCrimes_2013to2021, traffickingCrimes_2013to2021, on = [
        'State', 'Age', 'Year'], how = 'outer')

traffickingAllCrimes_2013to2021

# %%
# 1211 rows × 40 columns
    # Visually confirmed success


# Reorder columns

    # Confirm all column names
traffickingAllCrimes_2013to2021Columns = pd.DataFrame(
    traffickingAllCrimes_2013to2021.columns)

pd.options.display.max_rows = 500

traffickingAllCrimes_2013to2021Columns

# %%
# Printed 430 names

    # Reorder columns
traffickingAllCrimes_2013to2021ColumnsOrder = [
    'Year', 'State', 'Age', 'Population', 'NumberAgencies', 'TotalAll', 
    'TotalTraffick', 'TotalNonTraffickSex', 'TotalProperty', 'TotalViolent', 
    'CommercialSex', 'CommercialSexAct', 'InvoluntaryServitude', 'Rape', 'Sex', 
    'AggravatedAssault', 'AllOther', 'Arson', 'Assault', 'Burglary', 'CarTheft', 
    'CurfewLoitering', 'DisorderlyConduct', 'DrugAbuse', 'Drunkenness', 'DUI', 
    'Embezzlement', 'FamilyChildren', 'ForgeryCounterfeit', 'Fraud', 'Gambling', 
    'Larceny', 'LiquorLaws', 'MurderManslaughter', 'Robbery', 'StolenProperty', 
    'Suspicion', 'Vagrancy', 'Vandalism', 'Weapons']

traffickingAllCrimes_2013to2021R = traffickingAllCrimes_2013to2021.loc[
    :, traffickingAllCrimes_2013to2021ColumnsOrder]

pd.options.display.max_rows = 25

traffickingAllCrimes_2013to2021R

# %%
# 1377 rows × 40 columns
    # Visually confirmed success


# Ensure data are numeric, with whole numbers

    # Create variable for columns that shouldn't be numeric
nonNumericColumns = ['Age', 'State']

nonNumericColumns

# %%
# Success

    # Create variable for columns that should be numeric
numericColumns = [
    column for column in traffickingAllCrimes_2013to2021R.columns if 
    column not in nonNumericColumns]

numericColumns

# %%
# Success

    # Remove commas
traffickingAllCrimes_2013to2021R[
    numericColumns] = traffickingAllCrimes_2013to2021R[numericColumns].replace(
        ',', '', regex = True)

traffickingAllCrimes_2013to2021R

# %%
# Visually confirmed success

    # Replace NA's with 0's and update data type for all count columns to 
        # integers
traffickingAllCrimes_2013to2021R[
    numericColumns] = traffickingAllCrimes_2013to2021R[
    numericColumns].fillna(0).astype(float).astype(int)

traffickingAllCrimes_2013to2021R

# %%
# Visually confirmed success



# Explore a bit to validate data

    # View total traffick arrests by state
traffickingAllCrimes_2013to2021R.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalTraffick'].sum()
    ).sort_values(ascending = False)

# %%
# Confirmed values are the same from trafficking dataframe before merging


    # View total non-trafficking sex crime arrests by age
traffickingAllCrimes_2013to2021R.groupby('Age')['TotalNonTraffickSex'].sum(
    ).sort_values(ascending = False)

# %%
# Confirmed values are the same from trafficking dataframe before merging



# Export to csv
traffickingAllCrimes_2013to2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/traffickingAllCrimes_2013to2021.csv')

# %%
# Success



# Join crime and suicide
crimeSuicide_2013to2021 = pd.merge(
    traffickingAllCrimes_2013to2021R, suicides_2013to2021, on = [
        'State', 'Age', 'Year'], how = 'outer')

pd.options.display.max_rows = 4000

crimeSuicide_2013to2021

# %%
# Visually confirmed success


# Ensure data are numeric, with whole numbers

    # Create variable for columns that shouldn't be numeric
nonNumericColumns = ['Age', 'AgeDetail', 'State']

nonNumericColumns

# %%
# Success

    # Create variable for columns that should be numeric
numericColumns = [
    column for column in crimeSuicide_2013to2021.columns if 
    column not in nonNumericColumns]

numericColumns

# %%
# Success

    # Remove commas
crimeSuicide_2013to2021[numericColumns] = crimeSuicide_2013to2021[
    numericColumns].replace(',', '', regex = True)

crimeSuicide_2013to2021

# %%
# Visually confirmed success

    # Replace NA's with 0's and update data type for all count columns to 
        # integers
crimeSuicide_2013to2021[numericColumns] = crimeSuicide_2013to2021[
    numericColumns].fillna(0).astype(float).astype(int)

crimeSuicide_2013to2021

# %%
# Visually confirmed success



# Explore a bit to validate data

pd.options.display.max_rows = 25

    # View total traffick arrests by state
crimeSuicide_2013to2021.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalTraffick'].sum()
    ).sort_values(ascending = False)

# %%
# These values are higher than before merging, which makes sense in this context
    # because the AgeDetail column duplicated some Over 18 values


    # View non-trafficking sex crime arrests by age
crimeSuicide_2013to2021.groupby('Age')['TotalNonTraffickSex'].sum(
    ).sort_values(ascending = False)

# %%
# Confirmed total and Over 18 values are are higher than before merging, which 
    # makes sense in this context because the AgeDetail column duplicated some 
    # Over 18 values


# Export to csv
crimeSuicide_2013to2021.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/crimeSuicide_2013to2021.csv')

# %%
