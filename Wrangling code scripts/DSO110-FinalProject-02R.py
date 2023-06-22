# %%
# DSO110 - Data Science Final Project
    # File 2R 
    # Wrangling: allCrime data for all years (2013- 2021)

# Import packages
import numpy as np
import pandas as pd

# %%

# Import table

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import table
allCrimes_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2013to2021.csv')

allCrimes_2013to2021

# %%
# 918 rows × 37 columns
    # There appear to be plenty of missing values, some commas, and some whole 
    # numbers represented as decimals (ie: 1.0)


# Remove duplicate index column
allCrimes_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

allCrimes_2013to2021

# %%
# 918 rows × 36 columns


# Ensure data are numeric, with whole numbers

    # Create variable for columns that shouldn't be numeric
nonNumericColumns = ['Age', 'State']

nonNumericColumns

# %%
# Success

    # Create variable for columns that should be numeric
numericColumns = [
    column for column in allCrimes_2013to2021.columns if 
    column not in nonNumericColumns]

numericColumns


# %%
# Success

    # Remove commas
allCrimes_2013to2021[numericColumns] = allCrimes_2013to2021[
    numericColumns].replace(',', '', regex = True)

allCrimes_2013to2021

# %%
# Visually confirmed success

    # Replace NA's with 0's and update data type for all count columns to 
        # integers
allCrimes_2013to2021[numericColumns] = allCrimes_2013to2021[
    numericColumns].fillna(0).astype(float).astype(int)

allCrimes_2013to2021

# %%
# Visually confirmed success



# Update Age column to include a third value for 'Over 18'

    # Group data by state and year
allCrimesStateYear = allCrimes_2013to2021.groupby(['State', 'Year'])

allCrimesStateYear

# %%
# Success


    # Create a list of crime columns
allCrimesValues = allCrimes_2013to2021.columns[
    ~allCrimes_2013to2021.columns.isin([
        'Age', 'NumberAgencies', 'Population', 'State', 'Year'])]

allCrimesValues

# %%
# Success


    # Iterate over each group and save updates to a new dataframe
allCrimes_2013to2021R = pd.DataFrame()

for name, group in allCrimesStateYear:
    state, year = name
    if 'Under 18' in group['Age'].values and 'Total all ages' in group[
        'Age'].values:
        under_18_row = group[group['Age'] == 'Under 18'].copy()
        total_all_ages_row = group[group['Age'] == 'Total all ages'].copy()
        over_18_row = total_all_ages_row.copy()
        over_18_row['Age'] = 'Over 18'
        over_18_row[allCrimesValues] = total_all_ages_row[
            allCrimesValues].values - under_18_row[allCrimesValues].values
        allCrimes_2013to2021R = pd.concat([allCrimes_2013to2021R, under_18_row, total_all_ages_row, over_18_row], ignore_index = True)

allCrimes_2013to2021R

# %%
# 1377 rows × 36 columns
    # Visually confirmed success


		# Validate this worked

			# Create filtered table with all rows for one state / year combo for
				# Under and Over 18
Alabama2013 = allCrimes_2013to2021R[(
	allCrimes_2013to2021R['State'] == 'ALABAMA') & 
	(allCrimes_2013to2021R['Year'] == 2013) & 
	(allCrimes_2013to2021R['Age'] != 'Total all ages')]

Alabama2013

# %%
# Visually confirmed success

			# Calculate sum of those values
Alabama2013TotalCalculated = Alabama2013['TotalAll'].sum()

Alabama2013TotalCalculated

# %%
# 2119

			# Confirm total from updated table
Alabama2013Total = allCrimes_2013to2021R.loc[
    (allCrimes_2013to2021R['State'] == 'ALABAMA') &
    (allCrimes_2013to2021R['Year'] == 2013) &
    (allCrimes_2013to2021R['Age'] == 'Total all ages'), 
	'TotalAll'].values[0] if not allCrimes_2013to2021R.empty else 0

Alabama2013Total

# %%
# 2119 - success!



# Explore a bit to validate data, and add total columns for some data

    # View ranked list of total crimes by state
allCrimes_2013to2021R.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalAll'].sum()
    ).sort_values(ascending = False)

# %%
# Values seem legitimate from a quick sanity check - top 5 states
    # CALIFORNIA       8836025
    # TEXAS            6525534
    # FLORIDA          5883669
    # TENNESSEE        2900268
    # PENNSYLVANIA     2375349


    # Add a total column for all non-trafficking sex crimes for all years
allCrimes_2013to2021R['TotalNonTraffickSex'] = allCrimes_2013to2021R[[
    'Rape', 'Sex']].sum(axis = 1)

allCrimes_2013to2021

# %%
# 918 rows × 37 columns

        # View ranked list of total non-trafficking sex crimes by state
allCrimes_2013to2021R.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalNonTraffickSex'].sum()
    ).sort_values(ascending = False)

# %%
# Values seem legitimate from a quick sanity check - top 5 states
    # CALIFORNIA       91168
    # TEXAS            39863
    # FLORIDA          36832
    # WISCONSIN        22375
    # NEW YORK         20933


    # View ranked list of total non-trafficking sex crimes by age
allCrimes_2013to2021R.groupby('Age')['TotalNonTraffickSex'].sum(
    ).sort_values(ascending = False)

# %%
# Values seem legitimate from a quick sanity check
    # Total all ages    489616
    # Over 18           411155
    # Under 18           78461



# Export file to csv
allCrimes_2013to2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimesWithTotals_2013to2021.csv')

# %%
