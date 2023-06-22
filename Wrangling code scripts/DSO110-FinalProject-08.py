# %%
# DSO110 - Data Science Final Project
    # File 8
    # Wrangling: Census data for all years (2013- 2021)

# Import packages
import pandas as pd
import numpy as np
import re

# %%

# Import tables

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Age and sex data by year

        # 2013
ageSex_2013 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2013.csv')

ageSex_2013

# %%
# 54 rows × 435 columns
    # Looks like one row per state, plus a few territories
    # Columns are population counts for total, total per age, total per sex, and
        # total per sex by age; margins of error and percentages also included
    # The index is using codes (which I do have a "key" for), the human-
        # readable column names are actually in the first row of the data


        # 2014
ageSex_2014 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2014.csv')

ageSex_2014

# %%
# 54 rows × 435 columns

        # 2015
ageSex_2015 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2015.csv')

ageSex_2015

# %%
# 54 rows × 435 columns

        # 2016
ageSex_2016 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2016.csv')

ageSex_2016

# %%
# 54 rows × 435 columns

        # 2017
ageSex_2017 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2017.csv')

ageSex_2017

# %%
# 54 rows × 915 columns
    # Whew! Over double the columns – I can't quickly see what changed, 
    # ironically, but in the end will be dropping most either way

        # 2018
ageSex_2018 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2018.csv')

ageSex_2018

# %%
# 54 rows × 915 columns

        # 2019
ageSex_2019 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2019.csv')

ageSex_2019

# %%
# 54 rows × 915 columns

        # 2020
ageSex_2020 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2020.csv')

ageSex_2020

# %%
# 54 rows × 915 columns

        # 2021
ageSex_2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageAndSex_5YrEst_2021.csv')

ageSex_2021

# %%
# 54 rows × 915 columns


    # Computer and internet info - note:
        # Missing 2013-14
        # 2015-16 are 1 year estimates

        # 2015
compInternet_2015 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/computerInternet_1YrEst_2015.csv')

compInternet_2015

# %%
# 54 rows × 251 columns
    # These data are by number of household (not number of people)
    # Columns are by presence and type of computer, presence or type of 
        # internet, and household income


        # 2016
compInternet_2016 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/computerInternet_1YrEst_2016.csv')

compInternet_2016

# %%
# 54 rows × 251 columns

        # 2017
compInternet_2017 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/computerInternet_5YrEst_2017.csv')

compInternet_2017

# %%
# 54 rows × 251 columns

        # 2018
compInternet_2018 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/computerInternet_5YrEst_2018.csv')

compInternet_2018

# %%
# 54 rows × 251 columns

        # 2019
compInternet_2019 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/computerInternet_5YrEst_2019.csv')

compInternet_2019

# %%
# 54 rows × 251 columns

        # 2020
compInternet_2020 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/computerInternet_5YrEst_2020.csv')

compInternet_2020

# %%
# 54 rows × 251 columns

        # 2021
compInternet_2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/computerInternet_5YrEst_2021.csv')

compInternet_2021
# %%
# 54 rows × 251 columns


    # Education

        # 2013
education_2013 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2013.csv')

education_2013

# %%
# 54 rows × 459 columns
    # Columns are by age, sex, and level of education
        # Poverty levels also included


        # 2014
education_2014 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2014.csv')

education_2014

# %%
# 54 rows × 459 columns
    # Introduces info about earnings


        # 2015
education_2015 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2015.csv')

education_2015

# %%
# 54 rows × 1539 columns
    # I can't quickly see what changed, ironically, but in the end will be 
    # dropping most either way


        # 2016
education_2016 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2016.csv')

education_2016

# %%
# 54 rows × 1539 columns

        # 2017
education_2017 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2017.csv')

education_2017

# %%
# 54 rows × 1539 columns

        # 2018
education_2018 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2018.csv')

education_2018

# %%
# 54 rows × 1539 columns

        # 2019
education_2019 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2019.csv')

education_2019

# %%
# 54 rows × 1539 columns

        # 2020
education_2020 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2020.csv')

education_2020

# %%
# 54 rows × 1539 columns

        # 2021
education_2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_5YrEst_2021.csv')

education_2021

# %%
# 54 rows × 1539 columns


    # Poverty

        # 2013
poverty_2013 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2013.csv')

poverty_2013

# %%
# 54 rows × 555 columns
    # Columns are by sex, race, and work experience with varying poverty levels

        # 2014
poverty_2014 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2014.csv')

poverty_2014

# %%
# 54 rows × 555 columns

        # 2015
poverty_2015 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2015.csv')

poverty_2015

# %%
# 54 rows × 735 columns
    # It looks like maybe income levels are introduced with this data


        # 2016
poverty_2016 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2016.csv')

poverty_2016

# %%
# 54 rows × 735 columns

        # 2017
poverty_2017 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2017.csv')

poverty_2017

# %%
# 54 rows × 735 columns

        # 2018
poverty_2018 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2018.csv')

poverty_2018

# %%
# 54 rows × 735 columns

        # 2019
poverty_2019 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2019.csv')

poverty_2019

# %%
# 54 rows × 735 columns

        # 2020
poverty_2020 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2020.csv')

poverty_2020

# %%
# 54 rows × 735 columns

        # 2021
poverty_2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_5YrEst_2021.csv')

poverty_2021

# %%
# 54 rows × 735 columns


# Add year columns to all tables to prep for joining tables
ageSex_2013['Year'] = 2013
ageSex_2014['Year'] = 2014
ageSex_2015['Year'] = 2015
ageSex_2016['Year'] = 2016
ageSex_2017['Year'] = 2017
ageSex_2018['Year'] = 2018
ageSex_2019['Year'] = 2019
ageSex_2020['Year'] = 2020
ageSex_2021['Year'] = 2021

compInternet_2015['Year'] = 2015
compInternet_2016['Year'] = 2016
compInternet_2017['Year'] = 2017
compInternet_2018['Year'] = 2018
compInternet_2019['Year'] = 2019
compInternet_2020['Year'] = 2020
compInternet_2021['Year'] = 2021

education_2013['Year'] = 2013
education_2014['Year'] = 2014
education_2015['Year'] = 2015
education_2016['Year'] = 2016
education_2017['Year'] = 2017
education_2018['Year'] = 2018
education_2019['Year'] = 2019
education_2020['Year'] = 2020
education_2021['Year'] = 2021

poverty_2013['Year'] = 2013
poverty_2014['Year'] = 2014
poverty_2015['Year'] = 2015
poverty_2016['Year'] = 2016
poverty_2017['Year'] = 2017
poverty_2018['Year'] = 2018
poverty_2019['Year'] = 2019
poverty_2020['Year'] = 2020
poverty_2021['Year'] = 2021

# %%
# Succes (no errors)


# Join tables

    # Age and sex
ageSex_2013to2021 = pd.concat([
    ageSex_2021, ageSex_2020, ageSex_2019, ageSex_2018, ageSex_2017, 
    ageSex_2016, ageSex_2015, ageSex_2014, ageSex_2013])

ageSex_2013to2021

# %%
# 485 rows × 917 columns


    # Computer and internet
compInternet_2015to2021 = pd.concat([
    compInternet_2021, compInternet_2020, compInternet_2019, compInternet_2018, 
    compInternet_2017, compInternet_2016, compInternet_2015])

compInternet_2015to2021

# %%
# 378 rows × 252 columns


    # Education
education_2013to2021 = pd.concat([
    education_2021, education_2020, education_2019, education_2018, 
    education_2017, education_2016, education_2015, education_2014, 
    education_2013])

education_2013to2021

# %%
# 485 rows × 1541 columns


    # Poverty
poverty_2013to2021 = pd.concat([
    poverty_2021, poverty_2020, poverty_2019, poverty_2018, poverty_2017, 
    poverty_2016, poverty_2015, poverty_2014, poverty_2013])

poverty_2013to2021

# %%
# 486 rows × 750 columns


# Drop columns I won't use

    # Age and sex

        # Confirm existing columns
ageSexColumns = ageSex_2013to2021.iloc[0]

ageSexColumnsDf = pd.melt(
    ageSexColumns.to_frame().reset_index(), id_vars = ['index'], 
    value_vars = [0], var_name = 'Column', value_name = 'Value')

ageSexColumnsDf

# %%
# 917 rows × 3 columns

        # Drop un-needed geography column, as well as margin of error, 
            # percent, selected, summary, and annotation for each year
ageSexDrop = ageSex_2013to2021.iloc[0].str.contains(
        'Annotation|Geography|Margin|Percent|SELECTED|SUMMARY', 
        case = False, na = False)

ageSex_2013to2021R = ageSex_2013to2021.loc[:, ~ageSexDrop]

ageSex_2013to2021R = ageSex_2013to2021R.loc[
    :, ~ageSex_2013to2021R.columns.str.contains('Unnamed')]

ageSex_2013to2021R

# %%
# 485 rows × 59 columns


    # Computer and internet

        # Confirm existing columns
compInternetColumns = compInternet_2015to2021.iloc[0]

compInternetColumnsDf = pd.melt(
    compInternetColumns.to_frame().reset_index(), id_vars = ['index'], 
    value_vars = [0], var_name = 'Column', value_name = 'Value')

compInternetColumnsDf

# %%
# 252 rows × 3 columns

        # Drop un-needed geography column, as well as margin of error, 
            # percent, selected, summary, and annotation for each year
compInternetDrop = compInternet_2015to2021.iloc[0].str.contains(
        'Annotation|Geography|Margin|Percent|SELECTED|SUMMARY', 
        case = False, na = False)

compInternet_2013to2021R = compInternet_2015to2021.loc[:, ~compInternetDrop]

compInternet_2013to2021R = compInternet_2013to2021R.loc[
    :, ~compInternet_2013to2021R.columns.str.contains('Unnamed')]

compInternet_2013to2021R

# %%
# 378 rows × 33 columns


    # Education

        # Confirm existing columns
educationColumns = education_2013to2021.iloc[0]

educationColumnsDf = pd.melt(
    educationColumns.to_frame().reset_index(), id_vars = ['index'], 
    value_vars = [0], var_name = 'Column', value_name = 'Value')

educationColumnsDf

# %%
# 1541 rows × 3 columns

        # Drop un-needed geography column, as well as margin of error, 
            # percent, selected, summary, and annotation for each year
educationDrop = education_2013to2021.iloc[0].str.contains(
        'Annotation|Geography|Margin|Percent|SELECTED|SUMMARY', 
        case = False, na = False)

education_2013to2021R = education_2013to2021.loc[:, ~educationDrop]

education_2013to2021R = education_2013to2021R.loc[
    :, ~education_2013to2021R.columns.str.contains('Unnamed')]

education_2013to2021R

# %%
# 485 rows × 194 columns


    # Poverty

        # Confirm existing columns
povertyColumns = poverty_2013to2021.iloc[0]

povertyColumnsDf = pd.melt(
    povertyColumns.to_frame().reset_index(), id_vars = ['index'], 
    value_vars = [0], var_name = 'Column', value_name = 'Value')

povertyColumnsDf

# %%
# 750 rows × 3 columns

        # Drop un-needed geography column, as well as margin of error, 
            # percent, selected, summary, and annotation for each year
povertyDrop = poverty_2013to2021.iloc[0].str.contains(
        'Annotation|Geography|Margin|Percent|SELECTED|SUMMARY', 
        case = False, na = False)

poverty_2013to2021R = poverty_2013to2021.loc[:, ~povertyDrop]

poverty_2013to2021R = poverty_2013to2021R.loc[
    :, ~poverty_2013to2021R.columns.str.contains('Unnamed')]

poverty_2013to2021R

# %%
# 486 rows × 110 columns


# Update column names to be human readable (instead of codes to translate)

    # Age and sex
ageSex_2013to2021R.columns = ageSex_2013to2021R.iloc[0]

ageSex_2013to2021R = ageSex_2013to2021R.rename(columns = {2021: 'Year'})

ageSex_2013to2021R = ageSex_2013to2021R.drop(ageSex_2013to2021R.index[0])

ageSex_2013to2021R

# %%
# 476 rows × 59 columns

    # Computer and internet
compInternet_2013to2021R.columns = compInternet_2013to2021R.iloc[0]

compInternet_2013to2021R = compInternet_2013to2021R.rename(
    columns = {2021: 'Year'})

compInternet_2013to2021R = compInternet_2013to2021R.drop(compInternet_2013to2021R.index[0])

compInternet_2013to2021R

# %%
# 371 rows × 33 columns

    # Education
education_2013to2021R.columns = education_2013to2021R.iloc[0]

education_2013to2021R = education_2013to2021R.rename(columns = {2021: 'Year'})

education_2013to2021R = education_2013to2021R.drop(education_2013to2021R.index[0])

education_2013to2021R

# %%
# 476 rows × 194 columns

    # Poverty
poverty_2013to2021R.columns = poverty_2013to2021R.iloc[0]

poverty_2013to2021R = poverty_2013to2021R.rename(columns = {2021: 'Year'})

poverty_2013to2021R = poverty_2013to2021R.drop(poverty_2013to2021R.index[0])

poverty_2013to2021R

# %%
# 477 rows × 110 columns


# Update location column to align with crime and suicide data

    # Age and sex

        # Recode to all caps
ageSex_2013to2021R['State'] = ageSex_2013to2021R[
    'Geographic Area Name'].str.upper()

ageSex_2013to2021R

# %%
# 476 rows × 60 columns
    # Visually confirmed success

        # Confirm unique location values
ageSex_2013to2021R.State.unique()

# %%
# array(['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA',
#        'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA',
#        'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND',
#        'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI',
#        'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE',
#        'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA',
#        'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA',
#        'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE',
#        'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'PUERTO RICO',
#        'UNITED STATES'], dtype=object)


        # Drop locations not in crime and suicide data
ageSex_2013to2021R = ageSex_2013to2021R.drop(
    ageSex_2013to2021R[
        (ageSex_2013to2021R['State'] == 'PUERTO RICO') | 
        (ageSex_2013to2021R['State'] == 'UNITED STATES')].index)

ageSex_2013to2021R

# %%
# 450 rows × 60 columns

        # Update name for Washington DC to align with crime and suicide data
ageSex_2013to2021R['State'] = ageSex_2013to2021R[
    'State'].replace('DISTRICT OF COLUMBIA', 'WASHINGTON DC')

ageSex_2013to2021R

# %%
# Visually confirmed success

        # Drop original location column
ageSex_2013to2021R.drop(columns = ['Geographic Area Name'], inplace = True)

ageSex_2013to2021R

# %%
# 450 rows × 59 columns


    # Computer and internet

        # Recode to all caps
compInternet_2013to2021R['State'] = compInternet_2013to2021R[
    'Geographic Area Name'].str.upper()

compInternet_2013to2021R

# %%
# 371 rows × 34 columns
    # Visually confirmed success

        # Confirm unique location values
compInternet_2013to2021R.State.unique()

# %%
# array(['UNITED STATES', 'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS',
#        'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE',
#        'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO',
#        'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
#        'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'PUERTO RICO'],
#       dtype=object)


        # Drop locations not in crime and suicide data
compInternet_2013to2021R = compInternet_2013to2021R.drop(
    compInternet_2013to2021R[
        (compInternet_2013to2021R['State'] == 'PUERTO RICO') | 
        (compInternet_2013to2021R['State'] == 'UNITED STATES')].index)

compInternet_2013to2021R

# %%
# 357 rows × 34 columns

        # Update name for Washington DC to align with crime and suicide data
compInternet_2013to2021R['State'] = compInternet_2013to2021R[
    'State'].replace('DISTRICT OF COLUMBIA', 'WASHINGTON DC')

compInternet_2013to2021R

# %%
# Visually confirmed success

        # Drop original location column
compInternet_2013to2021R.drop(columns = ['Geographic Area Name'], inplace = True)

compInternet_2013to2021R

# %%
# 357 rows x 33 columns


    # Education

        # Recode to all caps
education_2013to2021R['State'] = education_2013to2021R[
    'Geographic Area Name'].str.upper()

education_2013to2021R

# %%
# 476 rows × 195 columns
    # Visually confirmed success

        # Confirm unique location values
education_2013to2021R.State.unique()

# %%
# array(['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA',
#        'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA',
#        'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND',
#        'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI',
#        'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 'NEW HAMPSHIRE',
#        'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 'NORTH CAROLINA',
#        'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 'PENNSYLVANIA',
#        'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 'TENNESSEE',
#        'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'PUERTO RICO',
#        'UNITED STATES'], dtype=object)


        # Drop locations not in crime and suicide data
education_2013to2021R = education_2013to2021R.drop(
    education_2013to2021R[
        (education_2013to2021R['State'] == 'PUERTO RICO') | 
        (education_2013to2021R['State'] == 'UNITED STATES')].index)

education_2013to2021R

# %%
# 450 rows × 195 columns

        # Update name for Washington DC to align with crime and suicide data
education_2013to2021R['State'] = education_2013to2021R[
    'State'].replace('DISTRICT OF COLUMBIA', 'WASHINGTON DC')

education_2013to2021R

# %%
# Visually confirmed success

        # Drop original location column
education_2013to2021R.drop(columns = ['Geographic Area Name'], inplace = True)

education_2013to2021R

# %%
# 450 rows x 194 columns


    # Poverty

        # Recode to all caps
poverty_2013to2021R['State'] = poverty_2013to2021R[
    'Geographic Area Name'].str.upper()

poverty_2013to2021R

# %%
# 477 rows × 111 columns
    # Visually confirmed success

        # Confirm unique location values
poverty_2013to2021R.State.unique()

# %%
# array(['UNITED STATES', 'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS',
#        'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE',
#        'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO',
#        'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
#        'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'PUERTO RICO'],
#       dtype=object)


        # Drop locations not in crime and suicide data
poverty_2013to2021R = poverty_2013to2021R.drop(
    poverty_2013to2021R[
        (poverty_2013to2021R['State'] == 'PUERTO RICO') | 
        (poverty_2013to2021R['State'] == 'UNITED STATES')].index)

poverty_2013to2021R

# %%
# 459 rows × 111 columns

        # Update name for Washington DC to align with crime and suicide data
poverty_2013to2021R['State'] = poverty_2013to2021R[
    'State'].replace('DISTRICT OF COLUMBIA', 'WASHINGTON DC')

poverty_2013to2021R

# %%
# Visually confirmed success

        # Drop original location column
poverty_2013to2021R.drop(columns = ['Geographic Area Name'], inplace = True)

poverty_2013to2021R

# %%
# 459 rows × 110 columns


# Export to csv

    # Age and sex
ageSex_2013to2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/ageSex_2013to2021.csv')

# %%

    # Computer and internet
compInternet_2013to2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/compInternet_2013to2021.csv')


# %%

    # Education
education_2013to2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/education_2013to2021.csv')

# %%

    # Poverty
poverty_2013to2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Census/poverty_2013to2021.csv')

# %%


# Join tables together into a single census table

    # Age and sex and computer and internet
census_2013to2021 = pd.merge(
    ageSex_2013to2021R, compInternet_2013to2021R, on = ['State', 'Year'], 
    how = 'outer')

census_2013to2021

# %%
# 457 rows × 90 columns

    # Add education
census_2013to2021 = pd.merge(
    census_2013to2021, education_2013to2021R, on = ['State', 'Year'], 
    how = 'outer')

census_2013to2021

# %%
# 457 rows × 282 columns

    # Add poverty
census_2013to2021 = pd.merge(
    census_2013to2021, poverty_2013to2021R, on = ['State', 'Year'], 
    how = 'outer')

census_2013to2021

# %%
# 459 rows × 390 columns

    # Confirm whether there are duplicate column names
duplicated_columns = census_2013to2021.columns[
    census_2013to2021.columns.duplicated()].to_list()

duplicated_columns

# %%
# [] - nope!


    # Add a new total population column with values for all rows, based on the
        # values in the age and sex data (by adding for all matching state/year
        # rows)

        # Replace missing values in original population column with 0's
census_2013to2021['Estimate!!Total!!Total population'] = census_2013to2021[
    'Estimate!!Total!!Total population'].fillna(0)

census_2013to2021

# %%
# Visually confirmed success

        # Create a new variable with state and year to serve as an index, and 
            # original population
totalPopulation = census_2013to2021.set_index([
    'State', 'Year'])[['Estimate!!Total!!Total population']]

totalPopulation

# %%
# 459 rows × 1 columns

        # Forward fill the missing values for each state-year pairing - ie: 
            # Alaska 2021 should be here four times (once each for age and sex, 
            # computer and internet, education, and poverty) but only has 
            # values for the first instance, so this will take that value from 
            # the age and sex data and add it to the remaining three instances
            # from the other three topics
totalPopulation = totalPopulation.fillna(method = 'ffill')

totalPopulation

# %%
# 459 rows × 1 columns
    # Visually confirmed success


        # Add a new column to the census variable to hold these new, filled
            # population values
census_2013to2021['TotalPopulation'] = totalPopulation[
    'Estimate!!Total!!Total population'].values

census_2013to2021

# %%
# 459 rows × 391 columns


        # Check to confirm there are no mismatches between the orignal 
            # population values and the new ones
populationMismatches = False

for stateYear, group in census_2013to2021.groupby(['State', 'Year']):
    population = group['Estimate!!Total!!Total population'].unique()
    if len(population) == 1:
        if group['TotalPopulation'].iloc[0] != population[0]:
            print(f'Warning: Found different values for original and new population columns for state/year {stateYear}')
            print(f"Original population: {group['Estimate!!Total!!Total population'].iloc[0]}")
            print(f"New population: {group['TotalPopulation'].iloc[0]}")
            populationMismatches = True
    else:
        print(f'Warning: Found multiple values for original population for state/year {stateYear}: {population}')
        populationMismatches = True

if not populationMismatches:
    print('There are no mismatches between original and new populations')

# %%
# There are no mismatches between original and new populations
    # Hurray!


        # Drop original population column
census_2013to2021.drop(columns = [
    'Estimate!!Total!!Total population'], inplace = True)

census_2013to2021

# %%
# 459 rows × 390 columns
    # I may come back later and do this same fill in approach for other columns


# Remove 'Estimate!!' from relevant column titles
census_2013to2021.columns = census_2013to2021.columns.str.replace(
    'Estimate!!', '')

census_2013to2021

# %%
# Visually confirmed success


# Drop some more columns

    # MEDIAN EARNINGS, RACE, POVERTY RATE FOR THE POPULATION 25 YEARS AND OVER 
        # FOR WHOM POVERTY STATUS IS DETERMINED BY EDUCATIONAL ATTAINMENT LEVEL, 
        # UNRELATED INDIVIDUALS
census_2013to2021 = census_2013to2021.loc[
    :, ~census_2013to2021.columns.str.contains(re.compile(
    r'MEDIAN EARNINGS|RACE|UNRELATED INDIVIDUALS|POVERTY STATUS IS DETERMINED BY EDUCATIONAL ATTAINMENT LEVEL'))]

census_2013to2021

# %%
# 459 rows × 227 columns

    # Confirm remaing column names
census_2013to2021ColumnsDf = pd.DataFrame({
    'Column': census_2013to2021.columns})

pd.options.display.max_rows = 500

census_2013to2021ColumnsDf

# %%

    # Drop a few more that are redundant, by name
census_2013to2021.drop([
    'Total!!Population for whom poverty status is determined!!EMPLOYMENT STATUS!!Civilian labor force 16 years and over', 
    'Total!!Population for whom poverty status is determined!!WORK EXPERIENCE!!Population 16 years and over', 
    'Below poverty level!!Population for whom poverty status is determined!!AGE!!Under 18 years!!Related children of householder under 18 years', 
    'Below poverty level!!Population for whom poverty status is determined!!EMPLOYMENT STATUS!!Civilian labor force 16 years and over',
    'Below poverty level!!Population for whom poverty status is determined!!WORK EXPERIENCE!!Population 16 years and over'], axis = 1, inplace = True)

pd.options.display.max_rows = 25

census_2013to2021

# %%
# 459 rows × 222 columns


# Transform the data to a long format and add new columns to align with format
    # of crime and suicide data

    # Define new variable for columns that don't need to be updated
columnsUnchanged = ['Year', 'State']

columnsUnchanged

# %%
# Success

    # Define new variables for columns to be updated
columnsToChange = [
    column for column in census_2013to2021.columns if 
    column not in columnsUnchanged]

columnsToChange

# %%
# Success

    # Transform using id and value variables
census_2013to2021R = census_2013to2021.melt(
    id_vars = columnsUnchanged, value_vars = columnsToChange, 
    var_name = 'Statistic', value_name = 'TotalPopulation')

census_2013to2021R

# %%
# 100980 rows × 4 columns

    # Drop rows with missing values or 0's in population column
census_2013to2021R.dropna(inplace = True)

census_2013to2021R = census_2013to2021R[census_2013to2021R[
    'TotalPopulation'] != 0]

census_2013to2021R

# %%
# 90076 rows × 4 columns
    # Visually confirmed success


    # Add gender column
census_2013to2021R['Gender'] = 'NA'

def gender(row):
    if 'Male' in row['Statistic']:
        return 'Male'
    elif 'Female' in row['Statistic']:
        return 'Female'
    else:
        return 'NA'

census_2013to2021R['Gender'] = census_2013to2021R.apply(gender, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 5 columns

        # Validate this worked
genderRows = census_2013to2021R[(census_2013to2021R['Gender'] == 'Male') |
                                (census_2013to2021R['Gender'] == 'Female')]

genderRows

# %%
# 40408 rows × 5 columns
    # Visually confirmed success


    # Add age detail column
census_2013to2021R['AgeDetail'] = 'NA'

def ageDetail(row):
    if '0 to 4' in row['Statistic']:
        return '0 to 4'
    elif '5 to 9' in row['Statistic']:
        return '5 to 9'
    elif '10 to 14' in row['Statistic']:
        return '10 to 14'
    elif '15 to 19' in row['Statistic']:
        return '15 to 19'
    elif '20 to 24' in row['Statistic']:
        return '20 to 24'
    elif '25 to 29' in row['Statistic']:
        return '25 to 29'
    elif '30 to 34' in row['Statistic']:
        return '30 to 34'
    elif '35 to 39' in row['Statistic']:
        return '35 to 39'
    elif '40 to 44' in row['Statistic']:
        return '40 to 44'
    elif '45 to 49' in row['Statistic']:
        return '45 to 49'
    elif '50 to 54' in row['Statistic']:
        return '50 to 54'
    elif '55 to 59' in row['Statistic']:
        return '55 to 59'
    elif '60 to 64' in row['Statistic']:
        return '60 to 64'
    elif '65 to 69' in row['Statistic']:
        return '65 to 69'
    elif '70 to 74' in row['Statistic']:
        return '70 to 74'
    elif '75 to 79' in row['Statistic']:
        return '75 to 79'
    elif '80 to 84' in row['Statistic']:
        return '80 to 84'
    elif '85+' in row['Statistic']:
        return '85+'
    elif '18 to 24' in row['Statistic']:
        return '18 to 24'
    elif '25+' in row['Statistic']:
        return '25+'
    elif '25 to 34' in row['Statistic']:
        return '25 to 34'
    elif '16+' in row['Statistic']:
        return '16+'
    elif '0 to 17' in row['Statistic']:
        return '0 to 17'
    elif '5 to 17' in row['Statistic']:
        return '5 to 17'
    elif '18 to 64' in row['Statistic']:
        return '18 to 64'
    elif '18 to 34' in row['Statistic']:
        return '18 to 34'
    elif '35 to 64' in row['Statistic']:
        return '35 to 64'
    elif '60+' in row['Statistic']:
        return '60+'
    elif '65+' in row['Statistic']:
        return '65+'
    elif '35 to 44' in row['Statistic']:
        return '35 to 44'
    elif '45 to 64' in row['Statistic']:
        return '45 to 64'
    elif 'Under 5' in row['Statistic']:
        return 'Under 5'
    elif 'Under 18' in row['Statistic']:
        return 'Under 18'
    else:
        return 'NA'

census_2013to2021R['AgeDetail'] = census_2013to2021R.apply(ageDetail, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 6 columns
    # Visually confirmed success


    # Add age column
census_2013to2021R['Age'] = 'NA'

def ageDetail(row):
    if '0 to 4' in row['Statistic']:
        return 'Under 18'
    elif '5 to 9' in row['Statistic']:
        return 'Under 18'
    elif '10 to 14' in row['Statistic']:
        return 'Under 18'
    elif '15 to 19' in row['Statistic']:
        return 'Under 18'
    elif '16+' in row['Statistic']:
        return 'Total all ages'
    elif '0 to 17' in row['Statistic']:
        return 'Under 18'
    elif '5 to 17' in row['Statistic']:
        return 'Under 18'
    elif 'Under 5' in row['Statistic']:
        return 'Under 18'
    elif 'Under 18' in row['Statistic']:
        return 'Under 18'
    else:
        return 'Total all ages'

census_2013to2021R['Age'] = census_2013to2021R.apply(ageDetail, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 7 columns
    # Visually confirmed success

    # Add households column
census_2013to2021R['TotalHouseholds'] = 'NA'

def totalHouseholds(row):
    if 'Total households' in row['Statistic']:
        row['TotalHouseholds'] = row['TotalPopulation']
        row['TotalPopulation'] = 0
    else:
        row['TotalHouseholds'] = 0
    return row

census_2013to2021R = census_2013to2021R.apply(totalHouseholds, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 8 columns

        # Validate this worked
householdRows = census_2013to2021R[(census_2013to2021R['TotalHouseholds'] != 0)]

householdRows

# %%
# 11067 rows × 8 columns
    # Visually confirmed success


    # Add computer column
census_2013to2021R['Computer'] = 'NA'

def computer(row):
    if 'Desktop or laptop with no other type of computing device' in row[
        'Statistic']:
        return 'Desktop or laptop with no other type of computing device'
    elif 'Desktop or laptop' in row['Statistic']:
        return 'Desktop or laptop'
    elif 'Smartphone with no other type of computing device' in row[
        'Statistic']:
        return 'Smartphone with no other type of computing device'
    elif 'Smartphone' in row['Statistic']:
        return 'Smartphone'
    elif 'Tablet or other portable wireless computer with no other type of computing device' in row['Statistic']:
        return 'Tablet or other portable wireless computer with no other type of computing device'
    elif 'Tablet or other portable wireless computer' in row['Statistic']:
        return 'Tablet or other portable wireless computer'
    elif 'Other computer with no other type of computing device' in row[
        'Statistic']:
        return 'Other computer with no other type of computing device'
    elif 'Other computer' in row['Statistic']:
        return 'Other computer'
    elif 'Has one or more types of computing devices' in row['Statistic']:
        return 'Has one or more types of computing devices'
    elif 'No computer' in row['Statistic']:
        return 'No computer'
    else:
        return 'NA'

census_2013to2021R['Computer'] = census_2013to2021R.apply(computer, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 9 columns

        # Validate this worked
computerRows = census_2013to2021R[(census_2013to2021R['Computer'] != 'NA')]

computerRows

# %%
# 3570 rows × 9 columns
    # Visually confirmed success


    # Add internet column
census_2013to2021R['Internet'] = 'NA'

def internet(row):
    if 'Dial-up with no other type of Internet subscription' in row[
        'Statistic']:
        return 'Dial-up with no other type of Internet subscription'
    elif 'Cellular data plan with no other type of Internet subscription' in row[
        'Statistic']:
        return 'Cellular data plan with no other type of Internet subscription'
    elif 'Broadband such as cable, fiber optic or DSL' in row['Statistic']:
        return 'Broadband such as cable, fiber optic or DSL'
    elif 'Satellite Internet service' in row['Statistic']:
        return 'Satellite Internet service'
    elif 'Cellular data plan' in row['Statistic']:
        return 'Cellular data plan'
    elif 'Broadband of any type' in row['Statistic']:
        return 'Broadband of any type'
    elif 'Without an Internet subscription' in row['Statistic']:
        return 'Without an Internet subscription'
    elif 'With an Internet subscription' in row['Statistic']:
        return 'With an Internet subscription'
    else:
        return 'NA'

census_2013to2021R['Internet'] = census_2013to2021R.apply(internet, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 10 columns

        # Validate this worked
internetRows = census_2013to2021R[(census_2013to2021R['Internet'] != 'NA')]

internetRows

# %%
# 3927 rows × 10 columns
    # Visually confirmed success


    # Add income column
census_2013to2021R['IncomeInPast12Months'] = 'NA'

def income(row):
    if 'Less than $20,000' in row['Statistic']:
        return 'Less than $20,000'
    elif '$20,000 to $74,999' in row['Statistic']:
        return '$20,000 to $74,999'
    elif '$75,000 or more' in row['Statistic']:
        return '$75,000 or more'
    else:
        return 'NA'

census_2013to2021R['IncomeInPast12Months'] = census_2013to2021R.apply(
    income, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 11 columns

        # Validate this worked
incomeRows = census_2013to2021R[(
    census_2013to2021R['IncomeInPast12Months'] != 'NA')]

incomeRows

# %%
# 4284 rows × 11 columns
    # Visually confirmed success


    # Add education column
census_2013to2021R['Education'] = 'NA'

def education(row):
    if 'Less than high school graduate' in row['Statistic']:
        return 'Less than high school graduate'
    elif 'High school graduate (includes equivalency)' in row['Statistic']:
        return 'High school graduate (includes equivalency)'
    elif 'Some college or associate\'s degree' in row['Statistic']:
        return 'Some college or associate\'s degree'
    elif 'Bachelor\'s degree or higher' in row['Statistic']:
        return 'Bachelor\'s degree or higher'
    elif 'Less than 9th grade' in row['Statistic']:
        return 'Less than 9th grade'
    elif '9th to 12th grade, no diploma' in row['Statistic']:
        return '9th to 12th grade, no diploma'
    elif 'Some college, no degree' in row['Statistic']:
        return 'Some college, no degree'
    elif 'Associate\'s degree' in row['Statistic']:
        return 'Associate\'s degree'
    elif 'Bachelor\'s degree' in row['Statistic']:
        return 'Bachelor\'s degree'
    elif 'Graduate or professional degree' in row['Statistic']:
        return 'Graduate or professional degree'
    elif 'High school graduate or higher' in row['Statistic']:
        return 'High school graduate or higher'
    else:
        return 'NA'

census_2013to2021R['Education'] = census_2013to2021R.apply(education, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 12 columns

        # Validate this worked
educationRows = census_2013to2021R[(census_2013to2021R['Education'] != 'NA')]

educationRows

# %%
# 29004 rows × 12 columns
    # Visually confirmed success


    # Add poverty column
census_2013to2021R['Poverty'] = 'NA'

def poverty(row):
    if 'Below poverty level' in row['Statistic']:
        return 'Below poverty level'
    elif 'poverty status is determined' in row['Statistic']:
        return 'Poverty status is determined'
    else:
        return 'NA'

census_2013to2021R['Poverty'] = census_2013to2021R.apply(poverty, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 13 columns

        # Validate this worked
povertyRows = census_2013to2021R[(
    census_2013to2021R['Poverty'] != 'NA')]

povertyRows

# %%
# 11475 rows × 13 columns
    # Visually confirmed success


    # Add education column
census_2013to2021R['Employment'] = 'NA'

def employment(row):
    if 'Employed' in row['Statistic']:
        return 'Employed'
    elif 'Unemployed' in row['Statistic']:
        return 'Unemployed'
    elif 'Worked full-time, year-round in the past 12 months' in row[
        'Statistic']:
        return 'Worked full-time, year-round in the past 12 months'
    elif 'Worked part-time or part-year in the past 12 months' in row[
        'Statistic']:
        return 'Worked part-time or part-year in the past 12 months'
    elif 'Did not work' in row['Statistic']:
        return 'Did not work'
    else:
        return 'NA'

census_2013to2021R['Employment'] = census_2013to2021R.apply(
    employment, axis = 1)

census_2013to2021R

# %%
# 90076 rows × 14 columns

        # Validate this worked
employmentRows = census_2013to2021R[(census_2013to2021R['Employment'] != 'NA')]

employmentRows

# %%
# 8262 rows × 14 columns
    # Visually confirmed success


    # Drop statistic column
census_2013to2021R.drop(['Statistic'], axis = 1, inplace = True)

census_2013to2021R

# %%
# 90076 rows × 13 columns


# Ensure data are numeric, with whole numbers

    # Create variable for columns that should be numeric
numericColumns = ['Year', 'TotalPopulation', 'TotalHouseholds']

numericColumns

# %%
# Success

    # Remove commas
census_2013to2021R[numericColumns] = census_2013to2021R[
    numericColumns].replace(',', '', regex = True)

census_2013to2021R

# %%
# Visually confirmed success

    # Replace NA's with 0's and update data type for all count columns to 
        # integers
census_2013to2021R[numericColumns] = census_2013to2021R[
    numericColumns].replace('(X)', np.nan)

census_2013to2021R[numericColumns] = census_2013to2021R[
    numericColumns].fillna(0).astype(float).astype(int)

census_2013to2021R

# %%
# Visually confirmed success


# Explore a bit to validate data

        # View ranked list of total populations by year
census_2013to2021R.groupby(
    'Year')['TotalPopulation'].sum().sort_values(ascending = False)

# %%
# Values seem legitamate from a quick sanity check - taking into account that 
    # it's summing the actual total per state with incremental totals for 
    # various configurations - top 5 states
    # 2021    6512977061
    # 2020    6491768932
    # 2019    6442880821
    # 2018    6139632214
    # 2017    5843053963


        # View ranked list of highest popuulation by state
census_2013to2021R.groupby('State')[
    'TotalPopulation'].max().sort_values(ascending = False)

# %%
# Values seem legitamate from a quick sanity check - top 5 states
    # CALIFORNIA       39455353
    # TEXAS            28862581
    # FLORIDA          21339762
    # NEW YORK         20114745
    # PENNSYLVANIA     12970650


# Export to csv
census_2013to2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/census_2013to2021.csv')

# %%
