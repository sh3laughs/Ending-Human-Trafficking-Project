# %%
# DSO110 - Data Science Final Project
    # File 4
    # Wrangle and explore trafficking crime data for all years (2013- 2021)

# Import packages
import pandas as pd

# %%

# Import table

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import table
traffickingCrimes_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2013to2021.csv')

traffickingCrimes_2013to2021

# %%
# 209599 rows × 209 columns
    # Note: This trafficking data is organized more incrementally than just by 
        # state', hence substantially more rows of data – will aggregate by  
        # state in order to incorporate with the 'all crime' data

# Wrangling

    # Add new State column to align with all crime data table
def stateAsText (stateAsNumber):
		if stateAsNumber == 1:
			return 'ALABAMA'
		if stateAsNumber == 2:
			return 'ARIZONA'
		if stateAsNumber == 3:
			return 'ARKANSAS'
		if stateAsNumber == 4:
			return 'CALIFORNIA'
		if stateAsNumber == 5:
			return 'COLORADO'
		if stateAsNumber == 6:
			return 'CONNECTICUT'
		if stateAsNumber == 7:
			return 'DELAWARE'
		if stateAsNumber == 8:
			return 'WASHINGTON DC'
		if stateAsNumber == 9:
			return 'FLORIDA'
		if stateAsNumber == 10:
			return 'GEORGIA'
		if stateAsNumber == 11:
			return 'IDAHO'
		if stateAsNumber == 12:
			return 'ILLINOIS'
		if stateAsNumber == 13:
			return 'INDIANA'
		if stateAsNumber == 14:
			return 'IOWA'
		if stateAsNumber == 15:
			return 'KANSAS'
		if stateAsNumber == 16:
			return 'KENTUCKY'
		if stateAsNumber == 17:
			return 'LOUISIANA'
		if stateAsNumber == 18:
			return 'MAINE'
		if stateAsNumber == 19:
			return 'MARYLAND'
		if stateAsNumber == 20:
			return 'MASSACHUSETTS'
		if stateAsNumber == 21:
			return 'MICHIGAN'
		if stateAsNumber == 22:
			return 'MINNESOTA'
		if stateAsNumber == 23:
			return 'MISSISSIPPI'
		if stateAsNumber == 24:
			return 'MISSOURI'
		if stateAsNumber == 25:
			return 'MONTANA'
		if stateAsNumber == 26:
			return 'NEBRASKA'
		if stateAsNumber == 27:
			return 'NEVADA'
		if stateAsNumber == 28:
			return 'NEW HAMPSHIRE'
		if stateAsNumber == 29:
			return 'NEW JERSEY'
		if stateAsNumber == 30:
			return 'NEW MEXICO'
		if stateAsNumber == 31:
			return 'NEW YORK'
		if stateAsNumber == 32:
			return 'NORTH CAROLINA'
		if stateAsNumber == 33:
			return 'NORTH DAKOTA'
		if stateAsNumber == 34:
			return 'OHIO'
		if stateAsNumber == 35:
			return 'OKLAHOMA'
		if stateAsNumber == 36:
			return 'OREGON'
		if stateAsNumber == 37:
			return 'PENNSYLVANIA'
		if stateAsNumber == 38:
			return 'RHODE ISLAND'
		if stateAsNumber == 39:
			return 'SOUTH CAROLINA'
		if stateAsNumber == 40:
			return 'SOUTH DAKOTA'
		if stateAsNumber == 41:
			return 'TENNESSEE'
		if stateAsNumber == 42:
			return 'TEXAS'
		if stateAsNumber == 43:
			return 'UTAH'
		if stateAsNumber == 44:
			return 'VERMONT'
		if stateAsNumber == 45:
			return 'VIRGINIA'
		if stateAsNumber == 46:
			return 'WASHINGTON'
		if stateAsNumber == 47:
			return 'WEST VIRGINIA'
		if stateAsNumber == 48:
			return 'WISCONSIN'
		if stateAsNumber == 49:
			return 'WYOMING'
		if stateAsNumber == 50:
			return 'ALASKA'
		if stateAsNumber == 51:
			return 'HAWAII'
		else:
			return 'Other'
		
traffickingCrimes_2013to2021['StateR'] = traffickingCrimes_2013to2021[
	'NumericStateCode'].apply(stateAsText)

traffickingCrimes_2013to2021

# %%
# 209599 rows × 210 columns
    # Visually confirmed success
    # Also see that some of the crime count variables have '\n' values I'll need
        # to remove


    # View data types for all variables
print(traffickingCrimes_2013to2021.dtypes.to_string)

# %%
# The crime count variables are string and need to be updated


    # Update crime count variables to numeric
        # Remove '\n' values from all variables
traffickingCrimes_2013to2021 = traffickingCrimes_2013to2021.replace(
	r'\n', '0', regex = True)

traffickingCrimes_2013to2021

# %%
# Visually confirmed success

        # Create variable with crime count columns
crimeCounts = [
	'JanuaryOffensesReportedorKnownCommercialSexActs',
    'JanuaryOffensesReportedorKnownInvoluntaryServitude',
    'JanuaryOffensesReportedorKnownGrandTotal',
    'JanuaryUnfoundedCommercialSexActs',
    'JanuaryUnfoundedInvoluntaryServitude',
    'JanuaryUnfoundedGrandTotal',
    'JanuaryNumberOfActualOffensesCommercialSexActs',
    'JanuaryNumberOfActualOffensesInvoluntaryServitude',
    'JanuaryNumberOfActualOffensesGrandTotal',
    'JanuaryTotalOffensesClearedCommercialSexActs',
    'JanuaryTotalOffensesClearedInvoluntaryServitude',
    'JanuaryTotalOffensesClearedGrandTotal',
    'JanuaryNumberOfClearancesUnder18CommercialSexActs',
    'JanuaryNumberOfClearancesUnder18InvoluntaryServitude',
    'JanuaryNumberOfClearancesUnder18GrandTotal',
    'FebruaryOffensesReportedorKnownCommercialSexActs',
    'FebruaryOffensesReportedorKnownInvoluntaryServitude',
    'FebruaryOffensesReportedorKnownGrandTotal',
    'FebruaryUnfoundedCommercialSexActs',
    'FebruaryUnfoundedInvoluntaryServitude',
    'FebruaryUnfoundedGrandTotal',
    'FebruaryNumberOfActualOffensesCommercialSexActs',
    'FebruaryNumberOfActualOffensesInvoluntaryServitude',
    'FebruaryNumberOfActualOffensesGrandTotal',
    'FebruaryTotalOffensesClearedCommercialSexActs',
    'FebruaryTotalOffensesClearedInvoluntaryServitude',
    'FebruaryTotalOffensesClearedGrandTotal',
    'FebruaryNumberOfClearancesUnder18CommercialSexActs',
    'FebruaryNumberOfClearancesUnder18InvoluntaryServitude',
    'FebruaryNumberOfClearancesUnder18GrandTotal',
    'MarchOffensesReportedorKnownCommercialSexActs',
    'MarchOffensesReportedorKnownInvoluntaryServitude',
    'MarchOffensesReportedorKnownGrandTotal',
    'MarchUnfoundedCommercialSexActs',
    'MarchUnfoundedInvoluntaryServitude',
    'MarchUnfoundedGrandTotal',
    'MarchNumberOfActualOffensesCommercialSexActs',
    'MarchNumberOfActualOffensesInvoluntaryServitude',
    'MarchNumberOfActualOffensesGrandTotal',
    'MarchTotalOffensesClearedCommercialSexActs',
    'MarchTotalOffensesClearedInvoluntaryServitude',
    'MarchTotalOffensesClearedGrandTotal',
    'MarchNumberOfClearancesUnder18CommercialSexActs',
    'MarchNumberOfClearancesUnder18InvoluntaryServitude',
    'MarchNumberOfClearancesUnder18GrandTotal',
    'AprilOffensesReportedorKnownCommercialSexActs',
    'AprilOffensesReportedorKnownInvoluntaryServitude',
    'AprilOffensesReportedorKnownGrandTotal',
    'AprilUnfoundedCommercialSexActs',
    'AprilUnfoundedInvoluntaryServitude',
    'AprilUnfoundedGrandTotal',
    'AprilNumberOfActualOffensesCommercialSexActs',
    'AprilNumberOfActualOffensesInvoluntaryServitude',
    'AprilNumberOfActualOffensesGrandTotal',
    'AprilTotalOffensesClearedCommercialSexActs',
    'AprilTotalOffensesClearedInvoluntaryServitude',
    'AprilTotalOffensesClearedGrandTotal',
    'AprilNumberOfClearancesUnder18CommercialSexActs',
    'AprilNumberOfClearancesUnder18InvoluntaryServitude',
    'AprilNumberOfClearancesUnder18GrandTotal',
    'MayOffensesReportedorKnownCommercialSexActs',
    'MayOffensesReportedorKnownInvoluntaryServitude',
    'MayOffensesReportedorKnownGrandTotal',
    'MayUnfoundedCommercialSexActs',
    'MayUnfoundedInvoluntaryServitude',
    'MayUnfoundedGrandTotal',
    'MayNumberOfActualOffensesCommercialSexActs',
    'MayNumberOfActualOffensesInvoluntaryServitude',
    'MayNumberOfActualOffensesGrandTotal',
    'MayTotalOffensesClearedCommercialSexActs',
    'MayTotalOffensesClearedInvoluntaryServitude',
    'MayTotalOffensesClearedGrandTotal',
    'MayNumberOfClearancesUnder18CommercialSexActs',
    'MayNumberOfClearancesUnder18InvoluntaryServitude',
    'MayNumberOfClearancesUnder18GrandTotal',
    'JuneOffensesReportedorKnownCommercialSexActs',
    'JuneOffensesReportedorKnownInvoluntaryServitude',
    'JuneOffensesReportedorKnownGrandTotal',
    'JuneUnfoundedCommercialSexActs',
    'JuneUnfoundedInvoluntaryServitude',
    'JuneUnfoundedGrandTotal',
    'JuneNumberOfActualOffensesCommercialSexActs',
    'JuneNumberOfActualOffensesInvoluntaryServitude',
    'JuneNumberOfActualOffensesGrandTotal',
    'JuneTotalOffensesClearedCommercialSexActs',
    'JuneTotalOffensesClearedInvoluntaryServitude',
    'JuneTotalOffensesClearedGrandTotal',
    'JuneNumberOfClearancesUnder18CommercialSexActs',
    'JuneNumberOfClearancesUnder18InvoluntaryServitude',
    'JuneNumberOfClearancesUnder18GrandTotal',
    'JulyOffensesReportedorKnownCommercialSexActs',
    'JulyOffensesReportedorKnownInvoluntaryServitude',
    'JulyOffensesReportedorKnownGrandTotal',
    'JulyUnfoundedCommercialSexActs',
    'JulyUnfoundedInvoluntaryServitude',
    'JulyUnfoundedGrandTotal',
    'JulyNumberOfActualOffensesCommercialSexActs',
    'JulyNumberOfActualOffensesInvoluntaryServitude',
    'JulyNumberOfActualOffensesGrandTotal',
    'JulyTotalOffensesClearedCommercialSexActs',
    'JulyTotalOffensesClearedInvoluntaryServitude',
    'JulyTotalOffensesClearedGrandTotal',
    'JulyNumberOfClearancesUnder18CommercialSexActs',
    'JulyNumberOfClearancesUnder18InvoluntaryServitude',
    'JulyNumberOfClearancesUnder18GrandTotal',
    'AugustOffensesReportedorKnownCommercialSexActs',
    'AugustOffensesReportedorKnownInvoluntaryServitude',
    'AugustOffensesReportedorKnownGrandTotal',
    'AugustUnfoundedCommercialSexActs',
    'AugustUnfoundedInvoluntaryServitude',
    'AugustUnfoundedGrandTotal',
    'AugustNumberOfActualOffensesCommercialSexActs',
    'AugustNumberOfActualOffensesInvoluntaryServitude',
    'AugustNumberOfActualOffensesGrandTotal',
    'AugustTotalOffensesClearedCommercialSexActs',
    'AugustTotalOffensesClearedInvoluntaryServitude',
    'AugustTotalOffensesClearedGrandTotal',
    'AugustNumberOfClearancesUnder18CommercialSexActs',
    'AugustNumberOfClearancesUnder18InvoluntaryServitude',
    'AugustNumberOfClearancesUnder18GrandTotal',
    'SeptemberOffensesReportedorKnownCommercialSexActs',
    'SeptemberOffensesReportedorKnownInvoluntaryServitude',
    'SeptemberOffensesReportedorKnownGrandTotal',
    'SeptemberUnfoundedCommercialSexActs',
    'SeptemberUnfoundedInvoluntaryServitude',
    'SeptemberUnfoundedGrandTotal',
    'SeptemberNumberOfActualOffensesCommercialSexActs',
    'SeptemberNumberOfActualOffensesInvoluntaryServitude',
    'SeptemberNumberOfActualOffensesGrandTotal',
    'SeptemberTotalOffensesClearedCommercialSexActs',
    'SeptemberTotalOffensesClearedInvoluntaryServitude',
    'SeptemberTotalOffensesClearedGrandTotal',
    'SeptemberNumberOfClearancesUnder18CommercialSexActs',
    'SeptemberNumberOfClearancesUnder18InvoluntaryServitude',
    'SeptemberNumberOfClearancesUnder18GrandTotal',
    'OctoberOffensesReportedorKnownCommercialSexActs',
    'OctoberOffensesReportedorKnownInvoluntaryServitude',
    'OctoberOffensesReportedorKnownGrandTotal',
    'OctoberUnfoundedCommercialSexActs',
    'OctoberUnfoundedInvoluntaryServitude',
    'OctoberUnfoundedGrandTotal',
    'OctoberNumberOfActualOffensesCommercialSexActs',
    'OctoberNumberOfActualOffensesInvoluntaryServitude',
    'OctoberNumberOfActualOffensesGrandTotal',
    'OctoberTotalOffensesClearedCommercialSexActs',
    'OctoberTotalOffensesClearedInvoluntaryServitude',
    'OctoberTotalOffensesClearedGrandTotal',
    'OctoberNumberOfClearancesUnder18CommercialSexActs',
    'OctoberNumberOfClearancesUnder18InvoluntaryServitude',
    'OctoberNumberOfClearancesUnder18GrandTotal',
    'NovemberOffensesReportedorKnownCommercialSexActs',
    'NovemberOffensesReportedorKnownInvoluntaryServitude',
    'NovemberOffensesReportedorKnownGrandTotal',
    'NovemberUnfoundedCommercialSexActs',
    'NovemberUnfoundedInvoluntaryServitude',
    'NovemberUnfoundedGrandTotal',
    'NovemberNumberOfActualOffensesCommercialSexActs',
    'NovemberNumberOfActualOffensesInvoluntaryServitude',
    'NovemberNumberOfActualOffensesGrandTotal',
    'NovemberTotalOffensesClearedCommercialSexActs',
    'NovemberTotalOffensesClearedInvoluntaryServitude',
    'NovemberTotalOffensesClearedGrandTotal',
    'NovemberNumberOfClearancesUnder18CommercialSexActs',
    'NovemberNumberOfClearancesUnder18InvoluntaryServitude',
    'NovemberNumberOfClearancesUnder18GrandTotal',
    'DecemberOffensesReportedorKnownCommercialSexActs',
    'DecemberOffensesReportedorKnownInvoluntaryServitude',
    'DecemberOffensesReportedorKnownGrandTotal',
    'DecemberUnfoundedCommercialSexActs',
    'DecemberUnfoundedInvoluntaryServitude',
    'DecemberUnfoundedGrandTotal',
    'DecemberNumberOfActualOffensesCommercialSexActs',
    'DecemberNumberOfActualOffensesInvoluntaryServitude',
    'DecemberNumberOfActualOffensesGrandTotal',
    'DecemberTotalOffensesClearedCommercialSexActs',
    'DecemberTotalOffensesClearedInvoluntaryServitude',
    'DecemberTotalOffensesClearedGrandTotal',
    'DecemberNumberOfClearancesUnder18CommercialSexActs',
    'DecemberNumberOfClearancesUnder18InvoluntaryServitude',
    'DecemberNumberOfClearancesUnder18GrandTotal']

crimeCounts

# %%
# Success

        # Convert crime counts to numeric data type
for column in crimeCounts:
    traffickingCrimes_2013to2021[column] = pd.to_numeric(traffickingCrimes_2013to2021[column], errors = 'coerce')

print(traffickingCrimes_2013to2021.dtypes.to_string)

# %%
# Success

    # Add a total column for all sex trafficking crimes for all years
traffickingCrimes_2013to2021[
	'TotalCommercialSexActs_2013to2021'] = traffickingCrimes_2013to2021[[
	'JanuaryOffensesReportedorKnownCommercialSexActs', 
    'FebruaryOffensesReportedorKnownCommercialSexActs', 
    'MarchOffensesReportedorKnownCommercialSexActs', 
    'AprilOffensesReportedorKnownCommercialSexActs', 
    'MayOffensesReportedorKnownCommercialSexActs', 
    'JuneOffensesReportedorKnownCommercialSexActs', 
    'JulyOffensesReportedorKnownCommercialSexActs', 
    'AugustOffensesReportedorKnownCommercialSexActs', 
    'SeptemberOffensesReportedorKnownCommercialSexActs', 
    'OctoberOffensesReportedorKnownCommercialSexActs', 
    'NovemberOffensesReportedorKnownCommercialSexActs', 
    'DecemberOffensesReportedorKnownCommercialSexActs',
    'JanuaryNumberOfActualOffensesCommercialSexActs',
    'FebruaryNumberOfActualOffensesCommercialSexActs',
    'MarchNumberOfActualOffensesCommercialSexActs',
    'AprilNumberOfActualOffensesCommercialSexActs',
    'MayNumberOfActualOffensesCommercialSexActs',
    'JuneNumberOfActualOffensesCommercialSexActs',
    'JulyNumberOfActualOffensesCommercialSexActs',
    'AugustNumberOfActualOffensesCommercialSexActs',
    'SeptemberNumberOfActualOffensesCommercialSexActs',
    'OctoberNumberOfActualOffensesCommercialSexActs',
    'NovemberNumberOfActualOffensesCommercialSexActs',
    'DecemberNumberOfActualOffensesCommercialSexActs',
    'JanuaryTotalOffensesClearedCommercialSexActs',
    'FebruaryTotalOffensesClearedCommercialSexActs',
    'MarchTotalOffensesClearedCommercialSexActs',
    'AprilTotalOffensesClearedCommercialSexActs',
    'MayTotalOffensesClearedCommercialSexActs',
    'JuneTotalOffensesClearedCommercialSexActs',
    'JulyTotalOffensesClearedCommercialSexActs',
    'AugustTotalOffensesClearedCommercialSexActs',
    'SeptemberTotalOffensesClearedCommercialSexActs',
    'OctoberTotalOffensesClearedCommercialSexActs',
    'NovemberTotalOffensesClearedCommercialSexActs',
    'DecemberTotalOffensesClearedCommercialSexActs',
    'JanuaryUnfoundedCommercialSexActs',
    'FebruaryUnfoundedCommercialSexActs',
    'MarchUnfoundedCommercialSexActs',
    'AprilUnfoundedCommercialSexActs',
    'MayUnfoundedCommercialSexActs',
    'JuneUnfoundedCommercialSexActs',
    'JulyUnfoundedCommercialSexActs',
    'AugustUnfoundedCommercialSexActs',
    'SeptemberUnfoundedCommercialSexActs',
    'OctoberUnfoundedCommercialSexActs',
    'NovemberUnfoundedCommercialSexActs',
    'DecemberUnfoundedCommercialSexActs']].sum(axis = 1)

traffickingCrimes_2013to2021

# %%
# 209599 rows × 211 columns


# Pre-check data

    # View ranked list of total sex crimes by state for all years
traffickingCrimes_2013to2021.groupby('StateR')[
	'TotalCommercialSexActs_2013to2021'].sum().sort_values(
	ascending = False)

# %%
# Note: This confirmed that CA is missing from this trafficking crime data... I
        # I had actually gone through the extra steps to leverage this data 
        # because California was represented in it (and is not in the easier to 
        # work with data), but it looks like it is only partially represented - 
        # but not with the crime counts I will need for my analyses...
    # These values are also unrealistically low, implying these data are not
        # complete


    # Import alternate trafficking crime data
traffickingCrimesAlternate_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/traffickingCrimesAlternate_2013to2021.csv')

traffickingCrimesAlternate_2013to2021

# %%
# 3098 rows × 19 columns
    # At first glance, these data are similar to the other trafficking crime 
    # data, though with less additional data I won't use ;) - main difference
    # appears to be tracking only by year, not by month, which works for me if
    # the data are overall more usable


        # View ranked list of total sex crimes by state for all years with  
            # alternate dataset
traffickingCrimesAlternate_2013to2021.loc[
	traffickingCrimesAlternate_2013to2021[
	'OFFENSE_SUBCAT_NAME'] == 'Commercial Sex Acts'].groupby('STATE_NAME')[
	'ACTUAL_COUNT'].sum().sort_values(ascending = False)

# %%
# These values are much more realistic, but I'll check other variables to 
    # further confirm


# View ranked list of total juvenile sex crimes by state for all years

    # Original data

        # Add a total column for all juvenile sex trafficking crimes for all 
            # years
traffickingCrimes_2013to2021[
	'TotalJuvenileCommercialSexActs_2013to2021'] = traffickingCrimes_2013to2021[
	['JanuaryNumberOfClearancesUnder18CommercialSexActs',
     'FebruaryNumberOfClearancesUnder18CommercialSexActs',
     'MarchNumberOfClearancesUnder18CommercialSexActs',
     'AprilNumberOfClearancesUnder18CommercialSexActs',
     'MayNumberOfClearancesUnder18CommercialSexActs',
     'JuneNumberOfClearancesUnder18CommercialSexActs',
     'JulyNumberOfClearancesUnder18CommercialSexActs',
     'AugustNumberOfClearancesUnder18CommercialSexActs',
     'SeptemberNumberOfClearancesUnder18CommercialSexActs',
     'OctoberNumberOfClearancesUnder18CommercialSexActs',
     'NovemberNumberOfClearancesUnder18CommercialSexActs']].sum(axis = 1)

traffickingCrimes_2013to2021

# %%
# 209599 rows × 212 columns

        # View ranked list of total juvenile sex crimes by state for all years
traffickingCrimes_2013to2021.groupby('StateR')[
	'TotalJuvenileCommercialSexActs_2013to2021'].sum().sort_values(
	ascending = False)

# %%
# These values are also unrealistically low, further validating that these data
    # are not complete


    # Alternate data
traffickingCrimesAlternate_2013to2021.loc[
	traffickingCrimesAlternate_2013to2021[
	'OFFENSE_SUBCAT_NAME'] == 'Commercial Sex Acts'].groupby('STATE_NAME')[
	'JUVENILE_CLEARED_COUNT'].sum().sort_values(ascending = False)

# %%
# These values are pretty low... which hopefully is legitimate! They are at 
    # least more realistic than the original dataset's values... I'll do one 
    # more check before setting the original data aside


# View ranked list of total involuntary servitude crimes by state for all years

    # Original data

        # Add a total column for all involuntary servitude crimes for all years
traffickingCrimes_2013to2021[
	'TotalInvoluntaryServitude_2013to2021'] = traffickingCrimes_2013to2021[
	['JanuaryOffensesReportedorKnownInvoluntaryServitude',
     'JanuaryUnfoundedInvoluntaryServitude',
     'JanuaryNumberOfActualOffensesInvoluntaryServitude',
     'JanuaryTotalOffensesClearedInvoluntaryServitude',
     'JanuaryNumberOfClearancesUnder18InvoluntaryServitude',
     'FebruaryOffensesReportedorKnownInvoluntaryServitude',
     'FebruaryUnfoundedInvoluntaryServitude',
     'FebruaryNumberOfActualOffensesInvoluntaryServitude',
     'FebruaryTotalOffensesClearedInvoluntaryServitude',
     'FebruaryNumberOfClearancesUnder18InvoluntaryServitude',
     'MarchOffensesReportedorKnownInvoluntaryServitude',
     'MarchUnfoundedInvoluntaryServitude',
     'MarchNumberOfActualOffensesInvoluntaryServitude',
     'MarchTotalOffensesClearedInvoluntaryServitude',
     'MarchNumberOfClearancesUnder18InvoluntaryServitude',
     'AprilOffensesReportedorKnownInvoluntaryServitude',
     'AprilUnfoundedInvoluntaryServitude',
     'AprilNumberOfActualOffensesInvoluntaryServitude',
     'AprilTotalOffensesClearedInvoluntaryServitude',
     'AprilNumberOfClearancesUnder18InvoluntaryServitude',
     'MayOffensesReportedorKnownInvoluntaryServitude',
     'MayUnfoundedInvoluntaryServitude',
     'MayNumberOfActualOffensesInvoluntaryServitude',
     'MayTotalOffensesClearedInvoluntaryServitude',
     'MayNumberOfClearancesUnder18InvoluntaryServitude',
     'JuneOffensesReportedorKnownInvoluntaryServitude',
     'JuneUnfoundedInvoluntaryServitude',
     'JuneNumberOfActualOffensesInvoluntaryServitude',
     'JuneTotalOffensesClearedInvoluntaryServitude',
     'JuneNumberOfClearancesUnder18InvoluntaryServitude',
     'JulyOffensesReportedorKnownInvoluntaryServitude',
     'JulyUnfoundedInvoluntaryServitude',
     'JulyNumberOfActualOffensesInvoluntaryServitude',
     'JulyTotalOffensesClearedInvoluntaryServitude',
     'JulyNumberOfClearancesUnder18InvoluntaryServitude',
     'AugustOffensesReportedorKnownInvoluntaryServitude',
     'AugustUnfoundedInvoluntaryServitude',
     'AugustNumberOfActualOffensesInvoluntaryServitude',
     'AugustTotalOffensesClearedInvoluntaryServitude',
     'AugustNumberOfClearancesUnder18InvoluntaryServitude',
     'SeptemberOffensesReportedorKnownInvoluntaryServitude',
     'SeptemberUnfoundedInvoluntaryServitude',
     'SeptemberNumberOfActualOffensesInvoluntaryServitude',
     'SeptemberTotalOffensesClearedInvoluntaryServitude',
     'SeptemberNumberOfClearancesUnder18InvoluntaryServitude',
     'OctoberOffensesReportedorKnownInvoluntaryServitude',
     'OctoberUnfoundedInvoluntaryServitude',
     'OctoberNumberOfActualOffensesInvoluntaryServitude',
     'OctoberTotalOffensesClearedInvoluntaryServitude',
     'OctoberNumberOfClearancesUnder18InvoluntaryServitude',
     'NovemberOffensesReportedorKnownInvoluntaryServitude',
     'NovemberUnfoundedInvoluntaryServitude',
     'NovemberNumberOfActualOffensesInvoluntaryServitude',
     'NovemberTotalOffensesClearedInvoluntaryServitude',
     'NovemberNumberOfClearancesUnder18InvoluntaryServitude',
     'DecemberOffensesReportedorKnownInvoluntaryServitude',
     'DecemberUnfoundedInvoluntaryServitude',
     'DecemberNumberOfActualOffensesInvoluntaryServitude',
     'DecemberTotalOffensesClearedInvoluntaryServitude',
     'DecemberNumberOfClearancesUnder18InvoluntaryServitude']].sum(axis = 1)

traffickingCrimes_2013to2021

# %%
# 209599 rows × 213 columns

        # View ranked list of total involuntary servitude crimes by state for  
            # all years
traffickingCrimes_2013to2021.groupby('StateR')[
	'TotalInvoluntaryServitude_2013to2021'].sum().sort_values(ascending = False)

# %%
# Yet again, these values seem illegitimately low...

    # Alternate data
traffickingCrimesAlternate_2013to2021.loc[
	traffickingCrimesAlternate_2013to2021[
	'OFFENSE_SUBCAT_NAME'] == 'Involuntary Servitude'].groupby('STATE_NAME')[
	'ACTUAL_COUNT'].sum().sort_values(ascending = False)

# %%
# And these data seem more accurate... I think that's enough to validate using
    # the alternative data


# Explore alternate data a bit more...

    # View list of total crimes by state and crime for all years
traffickingCrimesAlternate_2013to2021.groupby([
	'STATE_NAME', 'OFFENSE_SUBCAT_NAME'])['ACTUAL_COUNT'].sum()

# %%
# Aligned with data above, it looks like some states are more comprehensive in
    # their reporting than others...


    # View list of total juvenile crimes by state and crime for all years
traffickingCrimesAlternate_2013to2021.groupby([
	'STATE_NAME', 'OFFENSE_SUBCAT_NAME'])['JUVENILE_CLEARED_COUNT'].sum()

# %%
# Aligned with data above, it looks like some states are more comprehensive in
    # their reporting than others...
# %%
