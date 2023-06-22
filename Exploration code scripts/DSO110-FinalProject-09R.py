# %%
# DSO110 - Data Science Final Project
    # File 9R
    # Exploration: Initial exploration of crime and suicide data

# Import packages
import pandas as pd

# %%

#  Import data

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import data
crimeSuicide_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/crimeSuicide_2013to2021.csv')

crimeSuicide_2013to2021

# %%
# 2929 rows × 43 columns


# View ranked lists - all ages

    # Total reported crimes by state
crimeSuicide_2013to2021.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalAll'].sum()
    ).sort_values(ascending = False)

# %%
# Highest 5
    # CALIFORNIA       8836025
    # TEXAS            6525534
    # FLORIDA          5883669
    # TENNESSEE        2900268
    # PENNSYLVANIA     2375349


    # Total reported involuntary servitude crimes by state
crimeSuicide_2013to2021.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['InvoluntaryServitude'].sum()
    ).sort_values(ascending = False)

# %%
# Highest 5 states (also note many states seem to not report this...)
    # TEXAS             66387
    # NORTH CAROLINA     5766
    # KENTUCKY           5055
    # GEORGIA            4301
    # ILLINOIS           3472


    # Total reported commercial sex crimes by state (source: allCrimes)
crimeSuicide_2013to2021.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['CommercialSex'].sum()
    ).sort_values(ascending = False)

# %%
# Highest 5
    # CALIFORNIA       59154
    # TEXAS            35841
    # NEVADA           26015
    # FLORIDA          19591
    # PENNSYLVANIA     10950


    # Total reported commercial sex crimes by state (source: trafficking crimes)
crimeSuicide_2013to2021.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['CommercialSexAct'].sum()
    ).sort_values(ascending = False)

# %%
# Highest 5 (interesting that these data vary from the allCrime data for the 
        # same crime...)
    # TEXAS            120161
    # NEVADA            66437
    # MINNESOTA         60216
    # CALIFORNIA        59154
    # FLORIDA           37563


    # Total reported suicides by state
crimeSuicide_2013to2021.groupby('State').apply(
    lambda x: x[x['Age'] == 'Total all ages']['TotalSuicide'].sum()
    ).sort_values(ascending = False)

# %%
# Highest 5
    # CALIFORNIA       66159
    # TEXAS            56622
    # FLORIDA          49956
    # PENNSYLVANIA     29053
    # OHIO             26138


# View ranked lists - minors

        # Subset data for minors only
juvenileData = crimeSuicide_2013to2021.loc[
    crimeSuicide_2013to2021['Age'] == 'Under 18']

juvenileData

# %%
# 459 rows × 43 columns


        # Total reported crimes by state
juvenileData.groupby('State')[
	'TotalAll'].sum().sort_values(ascending = False)

# %%
# Highest 5
    # TEXAS            519047
    # CALIFORNIA       466133
    # FLORIDA          438830
    # WISCONSIN        341371
    # PENNSYLVANIA     296811


    # Total reported involuntary servitude crimes by state
juvenileData.groupby('State')[
	'InvoluntaryServitude'].sum().sort_values(ascending = False)

# %%
# Only three have reported this crime
    # MARYLAND         6303
    # TEXAS            2951
    # OHIO               64

    # Total reported commercial sex crimes by state (source: allCrimes)
juvenileData.groupby('State')[
	'CommercialSex'].sum().sort_values(ascending = False)

# %%
# Highest 5
    # CALIFORNIA       697
    # NEVADA           609
    # TEXAS            410
    # WISCONSIN        123
    # UTAH             109


    # Total reported commercial sex crimes by state (source: trafficking crimes)
juvenileData.groupby('State')[
	'CommercialSexAct'].sum().sort_values(ascending = False)

# %%
# Highest 5 
    # NEVADA         2880
    # TEXAS          1985
    # CALIFORNIA      697
    # OKLAHOMA        512
    # GEORGIA         414


    # Total reported suicides by state
juvenileData.groupby('State')[
    'TotalSuicide'].sum().sort_values(ascending = False)

# %%
# Highest 5
    # TEXAS            1267
    # CALIFORNIA        901
    # FLORIDA           560
    # OHIO              483
    # MICHIGAN          479

# %%



# View ranked lists - adults

        # Subset data for minors only
adultData = crimeSuicide_2013to2021.loc[
    crimeSuicide_2013to2021['Age'] == 'Over 18']

adultData

# %%
# 2062 rows × 43 columns


        # Total reported crimes by state
adultData.groupby('State')[
	'TotalAll'].sum().sort_values(ascending = False)

# %%
# Highest 5
    # CALIFORNIA       41550088
    # TEXAS            28065383
    # FLORIDA          27220563
    # TENNESSEE        12590546
    # PENNSYLVANIA     10369938


    # Total reported involuntary servitude crimes by state
adultData.groupby('State')[
	'InvoluntaryServitude'].sum().sort_values(ascending = False)

# %%
# Only three have reported this crime
    # TEXAS             273176
    # KENTUCKY           21555
    # NORTH CAROLINA     20946
    # ILLINOIS           16592
    # COLORADO           14996


    # Total reported commercial sex crimes by state (source: allCrimes)
adultData.groupby('State')[
	'CommercialSex'].sum().sort_values(ascending = False)

# %%
# Highest 5
    # CALIFORNIA       290837
    # TEXAS            169503
    # NEVADA           119246
    # FLORIDA           97490
    # PENNSYLVANIA      54461


    # Total reported commercial sex crimes by state (source: trafficking crimes)
adultData.groupby('State')[
	'CommercialSexAct'].sum().sort_values(ascending = False)

# %%
# Highest 5 
    # TEXAS            500028
    # CALIFORNIA       290837
    # NEVADA           275461
    # MINNESOTA        274060
    # FLORIDA          186855


    # Total reported suicides by state
adultData.groupby('State')[
    'TotalSuicide'].sum().sort_values(ascending = False)

# %%
# Highest 5
    # CALIFORNIA       61110
    # TEXAS            51162
    # FLORIDA          46045
    # PENNSYLVANIA     26750
    # NEW YORK         23897
# %%
