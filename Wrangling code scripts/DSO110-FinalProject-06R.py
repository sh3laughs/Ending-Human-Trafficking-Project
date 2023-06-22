# %%
# DSO110 - Data Science Final Project
    # File 6R
    # Wrangling: Trafficking crime data for all years (2013- 2021) to prep for
        # joining with crime and suicide data

# Import packages
import numpy as np
import pandas as pd

# %%

# Import table

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import table (removing "Alternate" from variable name in this new script)
traffickingCrimes_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/traffickingCrimesAlternate_2013to2021.csv')

traffickingCrimes_2013to2021

# %%
# 3098 rows × 19 columns


# Recode state to be align with the allCrime data

    # Confirm all 50 states are present all unique values
pd.options.display.max_rows = 55

stateCheckAlternate = pd.DataFrame(
	traffickingCrimes_2013to2021.STATE_NAME.unique())

stateCheckAlternate = stateCheckAlternate.sort_values(by = 0)

stateCheckAlternate

# %%
# Unfortunately CA is missing from this data (it was missing from original data
    # in the file 4 script, as well)


    # Recode all values to CAPS, as in traffickingCrimes dataset
traffickingCrimes_2013to2021[
	'State'] = traffickingCrimes_2013to2021['STATE_NAME'].str.upper()

stateCheckAlternateR = pd.DataFrame(
	traffickingCrimes_2013to2021.State.unique())

stateCheckAlternateR

# %%
# Visually confirmed success


        # Recode Federal
pd.options.display.max_rows = 25

traffickingCrimes_2013to2021['State'] = traffickingCrimes_2013to2021[
    'State'].replace('FEDERAL', 'WASHINGTON DC')

stateCheckAlternateR2 = pd.DataFrame(
	traffickingCrimes_2013to2021.State.unique())

stateCheckAlternateR2

# %%
# 50 rows × 1 columns
    # Visually confirmed success


# Subset to only keep columns I'll use, renamed
traffickingCrimes_2013to2021R = traffickingCrimes_2013to2021.loc[
    :, ['DATA_YEAR', 'OFFENSE_SUBCAT_NAME', 'ACTUAL_COUNT', 
        'JUVENILE_CLEARED_COUNT', 'State']].rename(
    columns = {'DATA_YEAR': 'Year', 'OFFENSE_SUBCAT_NAME': 'Crime',
               'ACTUAL_COUNT': 'Total', 'JUVENILE_CLEARED_COUNT': 'Juvenile',
               'State': 'State'})

traffickingCrimes_2013to2021R

# %%
# 3098 rows × 5 columns
    # Visually confirmed success


# Ensure data are numeric, with whole numbers

    # Create variable for columns that should be numeric
numericColumns = ['Year', 'Total', 'Juvenile']

numericColumns

# %%
# Success

    # Remove commas
traffickingCrimes_2013to2021R[numericColumns] = traffickingCrimes_2013to2021R[
    numericColumns].replace(',', '', regex = True)

traffickingCrimes_2013to2021R

# %%
# Visually confirmed success

    # Replace NA's with 0's and update data type for all count columns to 
        # integers
traffickingCrimes_2013to2021R[numericColumns] = traffickingCrimes_2013to2021R[
    numericColumns].fillna(0).astype(float).astype(int)

traffickingCrimes_2013to2021R

# %%
# Visually confirmed success



# Add columns for per-crime totals
    
    # All ages

        # Commercial sex acts
traffickingCrimes_2013to2021R[
    'CommercialSexAct'] = traffickingCrimes_2013to2021R.loc[
    traffickingCrimes_2013to2021R['Crime'] == 'Commercial Sex Acts'].groupby(
    ['State', 'Year'])['Total'].transform('sum')

traffickingCrimes_2013to2021R

# %%
# 3098 rows × 6 columns
    # Visually confirmed success


        # Involuntary servitude
traffickingCrimes_2013to2021R[
    'InvoluntaryServitude'] = traffickingCrimes_2013to2021R.loc[
    traffickingCrimes_2013to2021R['Crime'] == 'Involuntary Servitude'].groupby(
    ['State', 'Year'])['Total'].transform('sum')

traffickingCrimes_2013to2021R

# %%
# 3098 rows × 7 columns
    # Visually confirmed success


    # Under 18 - temporarily

        # Commercial sex acts
traffickingCrimes_2013to2021R[
    'CommercialSexActMinors'] = traffickingCrimes_2013to2021R.loc[
    traffickingCrimes_2013to2021R['Crime'] == 'Commercial Sex Acts'
    ].groupby(['State', 'Year'])['Juvenile'].transform('sum')

pd.options.display.max_rows = 3500

traffickingCrimes_2013to2021R

# %%
# 3098 rows × 8 columns
    # Visually confirmed success


        # Involuntary servitude
traffickingCrimes_2013to2021R[
    'InvoluntaryServitudeMinors'] = traffickingCrimes_2013to2021R.loc[
    traffickingCrimes_2013to2021R['Crime'] == 'Involuntary Servitude'
    ].groupby(['State', 'Year'])['Juvenile'].transform('sum')

traffickingCrimes_2013to2021R

# %%
# 3098 rows × 9 columns


# Add age column
traffickingCrimes_2013to2021R['Age'] = np.where(
    traffickingCrimes_2013to2021R['Juvenile'] != 0, 'Under 18', 
    'Total all ages')

traffickingCrimes_2013to2021R

# %%
# 3098 rows × 10 columns
    # Visually confirmed success


        # Drop separated age columns
traffickingCrimes_2013to2021R.drop(['Total', 'Juvenile'], axis = 1, 
                                   inplace = True)

pd.options.display.max_rows = 25

traffickingCrimes_2013to2021R

# %%
# 3098 rows × 8 columns

    # Drop duplicates (per the new CommercialSexAct and IS columns being sums from columns
        # now deleted, and thus causing duplicates)
traffickingCrimes_2013to2021R2 = traffickingCrimes_2013to2021R.drop_duplicates(
    ).reset_index()

traffickingCrimes_2013to2021R2

# %%
# 518 rows × 9 columns

    # Drop index column
traffickingCrimes_2013to2021R2.drop(['index'], axis = 1, inplace = True)

traffickingCrimes_2013to2021R2

# %%
# 518 rows × 8 columns


    # Drop crime text column
traffickingCrimes_2013to2021R2.drop(['Crime'], axis = 1, inplace = True)

traffickingCrimes_2013to2021R2

# %%
# 518 rows × 7 columns


# Remove rows where both crimes have zero values

    # Redefine numeric variables
numericColumnsR = [
    'Year', 'CommercialSexAct', 'InvoluntaryServitude', 
    'CommercialSexActMinors', 'InvoluntaryServitudeMinors']

numericColumnsR

# %%
# Success

    # Replace NA's with 0's and update data type for all count columns to 
        # integers (again)
traffickingCrimes_2013to2021R2[
    numericColumnsR] = traffickingCrimes_2013to2021R2[
        numericColumnsR].fillna(0).astype(float).astype(int)

traffickingCrimes_2013to2021R2

# %%
# Visually confirmed success

    # Remove 0 value rows
traffickingCrimes_2013to2021R3 = traffickingCrimes_2013to2021R2[
    (traffickingCrimes_2013to2021R2['CommercialSexAct'] != 0) | 
    (traffickingCrimes_2013to2021R2['InvoluntaryServitude'] != 0)| 
    (traffickingCrimes_2013to2021R2['CommercialSexActMinors'] != 0)| 
    (traffickingCrimes_2013to2021R2['InvoluntaryServitudeMinors'] != 0)
    ].reset_index()

traffickingCrimes_2013to2021R3

# %%
# 515 rows × 8 columns


    # Drop index column
traffickingCrimes_2013to2021R3.drop(['index'], axis = 1, inplace = True)

traffickingCrimes_2013to2021R3

# %%
# 518 rows × 7 columns



# Update to have only one row per year / state / age combo (right now some have 
    # multiple, per separate rows for CommercialSexAct and IS crime totals)

    # Update original crime columns based on age

        # CSA
traffickingCrimes_2013to2021R3.loc[
    traffickingCrimes_2013to2021R3['Age'] == 'Under 18', 'CommercialSexAct'
    ] = traffickingCrimes_2013to2021R3.loc[
        traffickingCrimes_2013to2021R3['Age'] == 'Under 18', 'CommercialSexActMinors']

pd.options.display.max_rows = 600

traffickingCrimes_2013to2021R3

# %%
# Visually confirmed success

        # IS
traffickingCrimes_2013to2021R3.loc[
    traffickingCrimes_2013to2021R3['Age'] == 'Under 18', 
    'InvoluntaryServitude'] = traffickingCrimes_2013to2021R3.loc[
        traffickingCrimes_2013to2021R3['Age'] == 'Under 18', 
        'InvoluntaryServitudeMinors']

traffickingCrimes_2013to2021R3

# %%
# Visually confirmed success

    # Drop CommercialSexActMinors and InvoluntaryServitudeMinors columns
traffickingCrimes_2013to2021R3 = traffickingCrimes_2013to2021R3.drop([
    'CommercialSexActMinors', 'InvoluntaryServitudeMinors'], axis = 1)

pd.options.display.max_rows = 25

traffickingCrimes_2013to2021R3

# %%
# 515 rows × 5 columns


# Add Over 18 values

    # Aggregate values by year, state, and age
traffickingCrimes_2013to2021R4 = traffickingCrimes_2013to2021R3.groupby([
    'Year', 'State', 'Age']).sum().reset_index()

pd.options.display.max_rows = 600

traffickingCrimes_2013to2021R4

# %%
# 336 rows × 5 columns
    # Visually confirmed success

    # Create a temporary variable for 'Over 18'
traffickingCrimesOver18 = traffickingCrimes_2013to2021R4[
    traffickingCrimes_2013to2021R4['Age'] == 'Total all ages'].copy()

traffickingCrimesOver18['Age'] = 'Over 18'

traffickingCrimesOver18

# %%

    # Update Over 18 values
for index, row in traffickingCrimesOver18.iterrows():
    year = row['Year']
    state = row['State']
    csaCrimes = row['CommercialSexAct']
    isCrimes = row['InvoluntaryServitude']
    
    under18 = traffickingCrimes_2013to2021R4[
        (traffickingCrimes_2013to2021R4['Year'] == year) & 
        (traffickingCrimes_2013to2021R4['State'] == state) & 
        (traffickingCrimes_2013to2021R4['Age'] == 'Under 18')]
    
    if not under18.empty:
        csaCrimes -= under18['CommercialSexAct'].values[0]
        isCrimes -= under18['InvoluntaryServitude'].values[0]
    
    traffickingCrimesOver18.at[index, 'CommercialSexAct'] = csaCrimes
    traffickingCrimesOver18.at[index, 'InvoluntaryServitude'] = isCrimes

traffickingCrimesOver18

# %%
# Visually confirmed success

    # Merge with original data
traffickingCrimes_2013to2021R5 = pd.concat([
    traffickingCrimes_2013to2021R4, traffickingCrimesOver18], 
    ignore_index = True)

pd.options.display.max_rows = 700

traffickingCrimes_2013to2021R5

# %%
# 620 rows × 5 columns
    # Visually confirmed success
    # I also manually calculated values based on original 2021 Texas data and
    # confirmed these values are accurate for all three Age values

pd.options.display.max_rows = 25



# Explore a bit to validate data

    # View CSA totals by state
traffickingCrimes_2013to2021R5.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['CommercialSexAct'].sum()
    ).sort_values(ascending = False)

# %%
# Values seem legitamate from a quick sanity check - top 5 states
    # TEXAS            120161
    # NEVADA            66437
    # MINNESOTA         60216
    # FLORIDA           37563
    # WISCONSIN         28078


# Add commercial sex counts from allCrime data for CA, which is missing from
    # this dataset, so that the trafficking totals reflect that

    # Import allCrime data
allCrimes_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimesWithTotals_2013to2021.csv')

allCrimes_2013to2021

# %%
# 918 rows × 38 columns

    # Subset the data to only include commercial sex data for CA

        # Keep only necessary columns
californiaCommercialSexAct = allCrimes_2013to2021[[
    'Age', 'CommercialSex', 'State', 'Year']]

californiaCommercialSexAct

# %%
# 918 rows × 4 columns

        # Keep only the rows for CA
californiaCommercialSexAct = californiaCommercialSexAct[californiaCommercialSexAct['State'] == 'CALIFORNIA']

californiaCommercialSexAct

# %%
# Visually confirmed success


        # Create a temporary variable for 'Over 18'
californiaCommercialSexActOver18 = californiaCommercialSexAct[
    californiaCommercialSexAct['Age'] == 'Total all ages'].copy()

californiaCommercialSexActOver18['Age'] = 'Over 18'

californiaCommercialSexActOver18

# %%

    # Update Over 18 values
for index, row in californiaCommercialSexActOver18.iterrows():
    year = row['Year']
    state = row['State']
    csaCrimes = row['CommercialSex']
    
    under18 = californiaCommercialSexAct[
        (californiaCommercialSexAct['Year'] == year) & 
        (californiaCommercialSexAct['State'] == state) & 
        (californiaCommercialSexAct['Age'] == 'Under 18')]
    
    if not under18.empty:
        csaCrimes -= under18['CommercialSex'].values[0]
    
    californiaCommercialSexActOver18.at[index, 'CommercialSex'] = csaCrimes

californiaCommercialSexActOver18

# %%
# Visually confirmed success

    # Merge with original CA CSA ata
californiaCommercialSexActR = pd.concat([
    californiaCommercialSexAct, californiaCommercialSexActOver18], 
    ignore_index = True)

californiaCommercialSexActR

# %%
# 27 rows × 4 columns

    # Add labor crime column
californiaCommercialSexActR['InvoluntaryServitude'] = 0

californiaCommercialSexActR

# %%
# 27 rows × 5 columns

    # Rename CSA column and reorder all columns
californiaCommercialSexActR2 = californiaCommercialSexActR.rename(
    columns = {'CommercialSex': 'CommercialSexAct'}).reindex(
        columns = ['Year', 'State', 'Age', 'CommercialSexAct', 
                   'InvoluntaryServitude'])

californiaCommercialSexActR2

# %%
# Visually confirm success

    # Check to confirm is CA is missing completely, or present with 0's
traffickingCrimes_2013to2021R5.State.unique()

# %%
# Confirmed it is missing completely

    # Add CA rows to overall dataset
traffickingCrimes_2013to2021R6 = traffickingCrimes_2013to2021R5.append(
    californiaCommercialSexActR2, ignore_index = True)

pd.options.display.max_rows = 700

traffickingCrimes_2013to2021R6

# %%
# 647 rows × 5 columns
    # Visually confirmed success


# Add trafficking total column
traffickingCrimes_2013to2021R6[
    'TotalTraffick'] = traffickingCrimes_2013to2021R6[
        'CommercialSexAct'] + traffickingCrimes_2013to2021R6[
            'InvoluntaryServitude']

pd.options.display.max_rows = 25

traffickingCrimes_2013to2021R6

# %%
# 647 rows × 6 columns
    # Visually confirmed success



# Explore a bit to validate data

    # View total traffick arrests by state
traffickingCrimes_2013to2021R6.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalTraffick'].sum()
    ).sort_values(ascending = False)

# %%
# Values seem legitimate from a quick sanity check - top 5 states
    # TEXAS            186548
    # NEVADA            67023
    # MINNESOTA         62058
    # CALIFORNIA        59154
    # FLORIDA           40561


    # View total traffick arrests by state
traffickingCrimes_2013to2021R6.groupby('Age')['TotalTraffick'].sum(
    ).sort_values(ascending = False)

# %%
# Values seem legitimate from a quick sanity check
    # Total all ages    772189
		# Note that this is not the sum of the values below, per not all states
        # or years having Under 18 data
    # Over 18           762063
    # Under 18           18172

# Export to csv
traffickingCrimes_2013to2021R6.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/traffickingCrimes_2013to2021.csv')

# %%
