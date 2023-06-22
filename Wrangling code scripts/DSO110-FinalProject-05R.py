# %%
# DSO110 - Data Science Final Project
    # File 5R
    # Wrangling: Suicide data for all years (2013- 2020) to prep for joining 
        # with crime data

# Import packages
import numpy as np
import pandas as pd

# %%

# Import table

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import tables for each year

        # 2013
suicide_2013 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/suicide/suicidesByAgeAndState_2013.csv')

suicide_2013

# %%
# 52 rows × 8 columns
    # Looks like 1 row per state, as well as DC and US
    # Other columns are counts per age bracket and totals
    # There appear to be plenty of missing values, some commas, and some whole 
        # numbers represented as decimals (ie: 1.0)


        # 2014
suicide_2014 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/suicide/suicidesByAgeAndState_2014.csv')

suicide_2014

# %%
# 52 rows × 8 columns

        # 2015
suicide_2015 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/suicide/suicidesByAgeAndState_2015.csv')

suicide_2015

# %%
# 52 rows × 8 columns

        # 2016
suicide_2016 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/suicide/suicidesByAgeAndState_2016.csv')

suicide_2016

# %%
# 52 rows × 8 columns

        # 2017
suicide_2017 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/suicide/suicidesByAgeAndState_2017.csv')

suicide_2017

# %%
# 52 rows × 8 columns

        # 2018
suicide_2018 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/suicide/suicidesByAgeAndState_2018.csv')

suicide_2018

# %%
# 52 rows × 8 columns

        # 2019
suicide_2019 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/suicide/suicidesByAgeAndState_2019.csv')

suicide_2019

# %%
# 52 rows × 8 columns

        # 2020
suicide_2020 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/suicide/suicidesByAgeAndState_2020.csv')

suicide_2020

# %%
# 52 rows × 8 columns


        # 2014- 2021 (less detail, but will pull 2021 data from this table)
suicide_2005to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Suicide/suicides_allYears.csv')

suicide_2005to2021

# %%
# 450 rows × 5 columns
    # This has usable columns for year, state, and tally


# Add year column to each single year table

    # 2013
suicide_2013['Year'] = 2013

suicide_2013

# %%
# 52 rows × 9 columns
    # Visually confirmed success

    # 2014
suicide_2014['Year'] = 2014

suicide_2014

# %%
# 52 rows × 9 columns
    # Visually confirmed success

    # 2015
suicide_2015['Year'] = 2015

suicide_2015

# %%
# 52 rows × 9 columns
    # Visually confirmed success

    # 2016
suicide_2016['Year'] = 2016

suicide_2016

# %%
# 52 rows × 9 columns
    # Visually confirmed success

    # 2017
suicide_2017['Year'] = 2017

suicide_2017

# %%
# 52 rows × 9 columns
    # Visually confirmed success

    # 2018
suicide_2018['Year'] = 2018

suicide_2018

# %%
# 52 rows × 9 columns
    # Visually confirmed success

    # 2019
suicide_2019['Year'] = 2019

suicide_2019

# %%
# 52 rows × 9 columns
    # Visually confirmed success

    # 2020
suicide_2020['Year'] = 2020

suicide_2020

# %%
# 52 rows × 9 columns
    # Visually confirmed success


# Prep all year data to be able to join only 2021 to the other individual years'
    # data

    # Subset 2014-2021 data to only include 2021
suicide_2021 = suicide_2005to2021[suicide_2005to2021['YEAR'] == 2021]

suicide_2021

# %%
# 50 rows × 5 columns
    # Visually confirmed success

    # Drop columns that won't be used
suicide_2021R = suicide_2021.drop(['RATE', 'URL'], axis = 1)

suicide_2021R

# %%
# 50 rows × 3 columns
    # Visually confirmed success

    # Rename columns
suicide_2021R.rename(columns = {'YEAR': 'Year', 'STATE': 'Location', 
                                'DEATHS': 'Total'}, inplace = True)

suicide_2021R

# %%
# 50 rows × 3 columns
    # Visually confirmed success


# Join tables for all years
suicides_2013to2021 = pd.concat([
    suicide_2013, suicide_2014, suicide_2015, suicide_2016, suicide_2017, 
    suicide_2018, suicide_2019, suicide_2020, suicide_2021R], axis = 0)
suicides_2013to2021

# %%
# 466 rows × 9 columns
    # Visually confirmed success


# Recode location variable to align with crime tables

    # Convert state names to upper case
suicides_2013to2021['Location'] = suicides_2013to2021['Location'].str.upper()

suicides_2013to2021

# %%
# Visually confirmed success

    # Recode location data to align with crime data
def state (location):
		if location == 'AL':
			return 'ALABAMA'
		if location == 'AK':
			return 'ALASKA'
		if location == 'AZ':
			return 'ARIZONA'
		if location == 'AR':
			return 'ARKANSAS'
		if location == 'CA':
			return 'CALIFORNIA'
		if location == 'CO':
			return 'COLORADO'
		if location == 'CT':
			return 'CONNECTICUT'
		if location == 'DE':
			return 'DELAWARE'
		if location == 'DISTRICT OF COLUMBIA':
			return 'WASHINGTON DC'
		if location == 'FL':
			return 'FLORIDA'
		if location == 'GA':
			return 'GEORGIA'
		if location == 'HI':
			return 'HAWAII'
		if location == 'ID':
			return 'IDAHO'
		if location == 'IL':
			return 'ILLINOIS'
		if location == 'IN':
			return 'INDIANA'
		if location == 'IA':
			return 'IOWA'
		if location == 'KS':
			return 'KANSAS'
		if location == 'KY':
			return 'KENTUCKY'
		if location == 'LA':
			return 'LOUISIANA'
		if location == 'ME':
			return 'MAINE'
		if location == 'MD':
			return 'MARYLAND'
		if location == 'MA':
			return 'MASSACHUSETTS'
		if location == 'MI':
			return 'MICHIGAN'
		if location == 'MN':
			return 'MINNESOTA'
		if location == 'MS':
			return 'MISSISSIPPI'
		if location == 'MO':
			return 'MISSOURI'
		if location == 'MT':
			return 'MONTANA'
		if location == 'NE':
			return 'NEBRASKA'
		if location == 'NV':
			return 'NEVADA'
		if location == 'NH':
			return 'NEW HAMPSHIRE'
		if location == 'NJ':
			return 'NEW JERSEY'
		if location == 'NM':
			return 'NEW MEXICO'
		if location == 'NY':
			return 'NEW YORK'
		if location == 'NC':
			return 'NORTH CAROLINA'
		if location == 'ND':
			return 'NORTH DAKOTA'
		if location == 'OH':
			return 'OHIO'
		if location == 'OK':
			return 'OKLAHOMA'
		if location == 'OR':
			return 'OREGON'
		if location == 'PA':
			return 'PENNSYLVANIA'
		if location == 'RI':
			return 'RHODE ISLAND'
		if location == 'SC':
			return 'SOUTH CAROLINA'
		if location == 'SD':
			return 'SOUTH DAKOTA'
		if location == 'TN':
			return 'TENNESSEE'
		if location == 'TX':
			return 'TEXAS'
		if location == 'UT':
			return 'UTAH'
		if location == 'VT':
			return 'VERMONT'
		if location == 'VA':
			return 'VIRGINIA'
		if location == 'WA':
			return 'WASHINGTON'
		if location == 'WV':
			return 'WEST VIRGINIA'
		if location == 'WI':
			return 'WISCONSIN'
		if location == 'WY':
			return 'WYOMING'
		else:
			return location
		
suicides_2013to2021['State'] = suicides_2013to2021['Location'].apply(state)

suicides_2013to2021

# %%
# 466 rows × 10 columns
    # Visually confirmed success

    # Drop US rows
suicides_2013to2021 = suicides_2013to2021.drop(
    suicides_2013to2021[suicides_2013to2021['State'] == 'UNITED STATES'].index)

suicides_2013to2021

# %%
# 457 rows × 10 columns
    # Visually confirmed success

    # Drop Location column
suicides_2013to2021.drop(['Location'], axis = 1, inplace = True)

suicides_2013to2021

# %%
# 457 rows × 9 columns
    # Visually confirmed success



# Ensure data are numeric, with whole numbers

    # Create variable for columns that should be numeric
numericColumns = [col for col in suicides_2013to2021.columns if col != 'State']

numericColumns

# %%
# Success

    # Remove commas
suicides_2013to2021[numericColumns] = suicides_2013to2021[
    numericColumns].replace(',', '', regex = True)

suicides_2013to2021

# %%
# Visually confirmed success

    # Replace NA's with 0's and update data type for all count columns to 
        # integers
suicides_2013to2021[numericColumns] = suicides_2013to2021[
    numericColumns].fillna(0).astype(float).astype(int)

suicides_2013to2021

# %%
# Visually confirmed success



# Add new age columns, for alignment with crime data and to have a single age 
    # detail column, instead of separate columns, also updating the total column
    # for the counts because the current one is inaccurate (only 45-54 values)

    # Transform the data to a long format - adding an age detail column for the
        # existing column names and total column for the values / counts
columnsUnchanged = ['Year', 'State']

suicides_2013to2021Long = pd.melt(
    suicides_2013to2021, id_vars = columnsUnchanged, value_vars = [
	    '0 to 17', '18 to 24', '25 to 34', '35 to 44', '45 to 54', '55+', 
	    'Total'], var_name = 'AgeDetail', value_name = 'TotalSuicide')

suicides_2013to2021Long

# %%
# 3199 rows × 4 columns
    # Visually confirmed success

    	# Remove rows with missing values and 0's
suicides_2013to2021Long = suicides_2013to2021Long[(
    suicides_2013to2021Long['TotalSuicide'] != 0) & (
    suicides_2013to2021Long['TotalSuicide'].notnull())].reset_index(drop = True)

suicides_2013to2021Long

# %%
# 2792 rows × 4 columns
    # Visually confirmed success

    	# Remove Total rows other than 2021
suicides_2013to2021R = suicides_2013to2021Long[
    (suicides_2013to2021Long['AgeDetail'] != 'Total') | (
	    suicides_2013to2021Long['Year'] == 2021)].reset_index(drop=True)

suicides_2013to2021R

# %%
# 2384 rows × 4 columns


	# Create age column to align with crime data
suicides_2013to2021R['Age'] = suicides_2013to2021R.apply(
    lambda row: 'Under 18' if row[
	    'AgeDetail'] == '0 to 17' else 'Over 18', axis = 1)

suicides_2013to2021R

# %%
# 2384 rows × 5 columns


    	# Add new per state/year pairing rows for the total across all ages

       		# Group by state and year, with totals summmed
totalSuicides = suicides_2013to2021R.groupby([
    'State', 'Year'], as_index = False)['TotalSuicide'].sum()

totalSuicides

# %%
# 457 rows × 3 columns

        	# Add age columns
totalSuicides['AgeDetail'] = 'NA'
totalSuicides['Age'] = 'Total all ages'

totalSuicides

# %%
# 457 rows × 5 columns
    # Visually confirmed success

        	# Merge back with age detail data
suicides_2013to2021R = pd.concat([suicides_2013to2021R, totalSuicides])

suicides_2013to2021R

# %%
# 2841 rows × 5 columns
    # Visually confirmed success

	# Drop rows where the age detail column has "total" as a value
suicides_2013to2021R = suicides_2013to2021R[
	suicides_2013to2021R['AgeDetail'] != 'Total'].reset_index(drop = True)

suicides_2013to2021R

# %%
# 2792 rows × 5 columns

		# Validate this worked

			# Create filtered table with all rows for one state / year combo for
				# Under and Over 18
Alabama2013 = suicides_2013to2021R[(
	suicides_2013to2021R['State'] == 'ALABAMA') & 
	(suicides_2013to2021R['Year'] == 2013) & 
	(suicides_2013to2021R['Age'] != 'Total all ages')]

Alabama2013

# %%
# Visually confirmed success

			# Calculate sum of those values
Alabama2013TotalCalculated = Alabama2013['TotalSuicide'].sum()

Alabama2013TotalCalculated

# %%
# 1296

			# Confirm total from updated table
Alabama2013Total = suicides_2013to2021R.loc[
    (suicides_2013to2021R['State'] == 'ALABAMA') &
    (suicides_2013to2021R['Year'] == 2013) &
    (suicides_2013to2021R['Age'] == 'Total all ages'), 
	'TotalSuicide'].values[0] if not suicides_2013to2021R.empty else 0

Alabama2013Total

# %%
# 1296 - success!



# Explore a bit to validate data

    # View ranked list of total crimes by state
suicides_2013to2021R.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalSuicide'].sum()
    ).sort_values(ascending = False)

# %%
# Values seem legitimate from a quick sanity check - highest 5 states
	# CALIFORNIA       66159
	# TEXAS            56622
	# FLORIDA          49956
	# PENNSYLVANIA     29053
	# OHIO             26138


    # View ranked list of total crimes by year
suicides_2013to2021R.groupby('Year').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalSuicide'].sum()
    ).sort_values(ascending = False)

# %%
# Values seem legitimate from a quick sanity check – 2021 is lower per coming
		# from an alternate US government source than 2013-20
	# 2018    88286
	# 2019    86938
	# 2017    85716
	# 2020    84633
	# 2016    81411
	# 2015    79564
	# 2014    76780
	# 2013    73583
	# 2021    47310

    # View ranked list of total crimes by age
suicides_2013to2021R.groupby('Age')['TotalSuicide'].sum(
    ).sort_values(ascending = False)

# %%
# Values seem legitamate from a quick sanity check
	# Total all ages    704221
		# Note that this is not the sum of the values below, per 2021 only 
		# having total values, not under / over 18
	# Over 18           644858
	# Under 18           12053


# Export to csv
suicides_2013to2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Suicide/suicides_2013to2021.csv')

# %%
