# %%
# DSO110 - Data Science Final Project
    # File 10R
    # # Wrangling: Join census data with crime and suicide data

# Import packages
import pandas as pd

# %%

# Import tables

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import census data
census_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/census_2013to2021.csv')

census_2013to2021

# %%
# 90076 rows × 14 columns

        # Remove duplicate index column
census_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

census_2013to2021

# %%
# 90076 rows × 13 columns


    # Import crime and suicide data
crimeSuicide_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/crimeSuicide_2013to2021.csv')

crimeSuicide_2013to2021

# %%
# 2980 rows × 43 columns

        # Remove duplicate index column
crimeSuicide_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

crimeSuicide_2013to2021

# %%
# 2980 rows × 42 columns


    # Import crime data
traffickingAllCrimes_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/traffickingAllCrimes_2013to2021.csv')

traffickingAllCrimes_2013to2021

# %%
# 1377 rows × 41 columns

        # Remove duplicate index column
traffickingAllCrimes_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

traffickingAllCrimes_2013to2021

# %%
# 1377 rows × 40 columns



# Join data

    # Census, crime, and suicide
allData_2013to2021 = pd.merge(
    crimeSuicide_2013to2021, census_2013to2021, on = [
        'State', 'Year', 'Age', 'AgeDetail'], how = 'outer')

allData_2013to2021

# %%
# 92597 rows × 51 columns


    # Census and crime
crimeCensus_2013to2021 = pd.merge(
    traffickingAllCrimes_2013to2021, census_2013to2021, on = [
        'State', 'Year', 'Age'], how = 'outer')

crimeCensus_2013to2021

# %%
# 90535 rows × 50 columns



# Check for duplicates

        # All data - check
allData_2013to2021[allData_2013to2021.duplicated()]

# %%
# 4 rows are duplicates

        # All data - remove
allData_2013to2021 = allData_2013to2021.drop_duplicates()

allData_2013to2021

# %%
# 92593 rows × 51 columns


        # Census and crime - check
crimeCensus_2013to2021[crimeCensus_2013to2021.duplicated()]

# %%
# 4 rows are duplicates

        # Census and crime - remove
crimeCensus_2013to2021 = crimeCensus_2013to2021.drop_duplicates()

crimeCensus_2013to2021

# %%
# 90531 rows × 50 columns



# Clean up columns

    # Rename some columns

        # All data
allData_2013to2021 = allData_2013to2021.rename(columns = {
    'TotalAll': 'TotalCrime', 'Sex': 'SexCrime', 'AllOther': 'OtherCrime', 
    'FamilyChildren': 'FamilyChildrenCrime'})

allData_2013to2021

# %%
# Visually confirmed success

        # Census and crime
crimeCensus_2013to2021 = crimeCensus_2013to2021.rename(columns = {
    'TotalAll': 'TotalCrime', 'Sex': 'SexCrime', 'AllOther': 'OtherCrime', 
    'FamilyChildren': 'FamilyChildrenCrime'})

crimeCensus_2013to2021

# %%
# Visually confirmed success


    # Drop population from crime data

        # All data
allData_2013to2021.drop(
    columns = ['Population'], axis = 1, inplace = True)

allData_2013to2021

# %%
# 92593 rows × 50 columns

        # Census and crime
crimeCensus_2013to2021.drop(
    columns = ['Population'], axis = 1, inplace = True)

crimeCensus_2013to2021

# %%
# 90531 rows × 49 columns


    # Reorder columns

        # Confirm all column names
allData_2013to2021Columns = pd.DataFrame(allData_2013to2021.columns)

pd.options.display.max_rows = 50

allData_2013to2021Columns

# %%
# Printed 50 names

        # Reorder columns

            # All data
allData_2013to2021ColumnsOrder = [
    'Year', 'State', 'TotalPopulation', 'Age', 'AgeDetail', 'NumberAgencies', 
    'TotalHouseholds', 'TotalTraffick', 'TotalNonTraffickSex', 'TotalSuicide', 
    'TotalCrime', 'TotalViolent', 'TotalProperty', 'CommercialSex', 
    'CommercialSexAct', 'InvoluntaryServitude', 'Rape', 'SexCrime', 
    'AggravatedAssault', 'Arson', 'Assault', 'Burglary', 'CarTheft', 
    'CurfewLoitering', 'DisorderlyConduct', 'DrugAbuse', 'Drunkenness', 'DUI', 
    'Embezzlement', 'FamilyChildrenCrime', 'ForgeryCounterfeit', 'Fraud', 
    'Gambling', 'Larceny', 'LiquorLaws', 'MurderManslaughter', 'OtherCrime', 
    'Robbery', 'StolenProperty', 'Suspicion', 'Vagrancy', 'Vandalism', 
    'Weapons', 'Computer', 'Education', 'Employment', 'Gender', 
    'IncomeInPast12Months', 'Internet', 'Poverty']

allData_2013to2021 = allData_2013to2021.loc[
    :, allData_2013to2021ColumnsOrder]

pd.options.display.max_rows = 25

allData_2013to2021

# %%
# Visually confirmed success

        # Census and crime
crimeCensus_2013to2021ColumnsOrder = [
    'Year', 'State', 'TotalPopulation', 'Age', 'AgeDetail', 'NumberAgencies', 
    'TotalHouseholds', 'TotalTraffick', 'TotalNonTraffickSex', 'TotalCrime', 
    'TotalViolent', 'TotalProperty', 'CommercialSex', 'CommercialSexAct', 
    'InvoluntaryServitude', 'Rape', 'SexCrime', 'AggravatedAssault', 'Arson', 
    'Assault', 'Burglary', 'CarTheft', 'CurfewLoitering', 'DisorderlyConduct', 
    'DrugAbuse', 'Drunkenness', 'DUI', 'Embezzlement', 'FamilyChildrenCrime', 
    'ForgeryCounterfeit', 'Fraud', 'Gambling', 'Larceny', 'LiquorLaws', 
    'MurderManslaughter', 'OtherCrime', 'Robbery', 'StolenProperty', 
    'Suspicion', 'Vagrancy', 'Vandalism', 'Weapons', 'Computer', 'Education', 
    'Employment', 'Gender', 'IncomeInPast12Months', 'Internet', 'Poverty']

crimeCensus_2013to2021 = crimeCensus_2013to2021.loc[
    :, crimeCensus_2013to2021ColumnsOrder]

pd.options.display.max_rows = 25

crimeCensus_2013to2021

# %%
# Visually confirmed success



# Ensure data are numeric, with whole numbers

    # Create variable for columns that shouldn't be numeric
nonNumericColumns = [
    'State', 'Age', 'AgeDetail', 'Computer', 'Education', 'Employment',
    'Gender', 'IncomeInPast12Months', 'Internet', 'Poverty']

nonNumericColumns

# %%
# Success

    # Create variable for columns that should be numeric

        # All data
allDataNumericColumns = [
    column for column in allData_2013to2021.columns if 
    column not in nonNumericColumns]

allDataNumericColumns

# %%
# Success

        # Census and crime
crimeCensusNumericColumns = [
    column for column in crimeCensus_2013to2021.columns if 
    column not in nonNumericColumns]

crimeCensusNumericColumns

# %%
# Success


    # Remove commas

        # All data
allData_2013to2021[allDataNumericColumns] = allData_2013to2021[
    allDataNumericColumns].replace(',', '', regex = True)

allData_2013to2021

# %%
# Visually confirmed success

        # Census and crime
crimeCensus_2013to2021[crimeCensusNumericColumns] = crimeCensus_2013to2021[
    crimeCensusNumericColumns].replace(',', '', regex = True)

crimeCensus_2013to2021

# %%
# Visually confirmed success


    # Replace NA's with 0's and update data type for all count columns to 
        # integers

        # All data
allData_2013to2021[allDataNumericColumns] = allData_2013to2021[
    allDataNumericColumns].fillna(0).astype(float).astype(int)

allData_2013to2021

# %%
# Visually confirmed success

        # Census and crime
crimeCensus_2013to2021[crimeCensusNumericColumns] = allData_2013to2021[
    crimeCensusNumericColumns].fillna(0).astype(float).astype(int)

crimeCensus_2013to2021

# %%
# Visually confirmed success


# Export to csv

    # All data
allData_2013to2021.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/allData_2013to2021.csv')

# %%

    # Census and crime
crimeCensus_2013to2021.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/crimeCensus_2013to2021.csv')

# %%
