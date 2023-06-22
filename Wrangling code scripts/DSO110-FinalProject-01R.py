# %%
# DSO110 - Data Science Final Project
    # File 1R
    # Wrangling: Joining allCrime tables for each year (2013- 2021)

# Import packages
import pandas as pd

# %%

# Import tables

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # 2013 All Crimes
allCrimes_2013 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2013.csv')

allCrimes_2013

# %%
# 102 rows × 35 columns
    # Looks like 2 rows per state - one for minors, and one for all ages
    # Other columns are counts per crime, as well as a total for all crimes, 
        # the number of reporting agencies, and the total population


    # 2014 All Crimes
allCrimes_2014 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2014.csv')

allCrimes_2014

# %%
# 102 rows × 35 columns

    # 2015 All Crimes
allCrimes_2015 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2015.csv')

allCrimes_2015

# %%
# 102 rows × 35 columns

    # 2016 All Crimes
allCrimes_2016 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2016.csv')

allCrimes_2016

# %%
# 102 rows × 35 columns

    # 2017 All Crimes
allCrimes_2017 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2017.csv')

allCrimes_2017

# %%
# 102 rows × 35 columns

    # 2018 All Crimes
allCrimes_2018 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2018.csv')

allCrimes_2018

# %%
# 102 rows × 35 columns

    # 2019 All Crimes
allCrimes_2019 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2019.csv')

allCrimes_2019

# %%
# 102 rows × 35 columns

    # 2020 All Crimes
allCrimes_2020 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2020.csv')

allCrimes_2020

# %%
# 102 rows × 35 columns

    # 2021 All Crimes
allCrimes_2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2021.csv')

allCrimes_2021

# %%
# 102 rows × 35 columns

# Rename columns

    # 2013
        # Return all column names
allCrimes_2013.columns

# %%

        # Rename
allCrimes_2013R = allCrimes_2013.rename(columns={
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape3': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness4': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2013\nestimated \npopulation': 'Population'})

allCrimes_2013R.columns

# %%
# Visually confirmed success

    # 2014
        # Return all column names
allCrimes_2014.columns

# %%

        # Rename
allCrimes_2014R = allCrimes_2014.rename(columns={
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape3': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness4': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2014\nestimated \npopulation': 'Population'})

allCrimes_2014R.columns

# %%
# Visually confirmed success

    # 2015
        # Return all column names
allCrimes_2015.columns

# %%

        # Rename
allCrimes_2015R = allCrimes_2015.rename(columns = {
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape3': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness4': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2015\nestimated \npopulation': 'Population'})

allCrimes_2015R.columns

# %%
# Visually confirmed success

    # 2016
        # Return all column names
allCrimes_2016.columns

# %%

        # Rename
allCrimes_2016R = allCrimes_2016.rename(columns={
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape3': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness4': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2016\nestimated \npopulation': 'Population'})

allCrimes_2016R.columns

# %%
# Visually confirmed success

    # 2017
        # Return all column names
allCrimes_2017.columns

# %%

        # Rename
allCrimes_2017R = allCrimes_2017.rename(columns={
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape3': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness4': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2017\nestimated \npopulation': 'Population'})

allCrimes_2017R.columns

# %%
# Visually confirmed success

    # 2018
        # Return all column names
allCrimes_2018.columns

# %%

        # Rename
allCrimes_2018R = allCrimes_2018.rename(columns={
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape3': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness4': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2018\nestimated \npopulation': 'Population'})

allCrimes_2018R.columns

# %%
# Visually confirmed success

    # 2019
        # Return all column names
allCrimes_2019.columns

# %%

        # Rename
allCrimes_2019R = allCrimes_2019.rename(columns={
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape3': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness4': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2019\nestimated \npopulation': 'Population'})

allCrimes_2019R.columns

# %%
# Succes# Visually confirmed success

    # 2020
        # Return all column names
allCrimes_2020.columns

# %%

        # Rename
allCrimes_2020R = allCrimes_2020.rename(columns={
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape3': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness4': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2020\nestimated \npopulation': 'Population'})

allCrimes_2020R.columns

# %%
# Visually confirmed success

    # 2021
        # Return all column names
allCrimes_2021.columns

# %%

        # Rename
allCrimes_2021R = allCrimes_2021.rename(columns={
    'State': 'State',
    'Age': 'Age',
    'Total\nall \nclasses1': 'TotalAll',
    'Violent\ncrime2': 'TotalViolent',
    'Property\ncrime2': 'TotalProperty',
    'Murder and\nnonnegligent\nmanslaughter': 'MurderManslaughter',
    'Rape': 'Rape',
    'Robbery': 'Robbery',
    'Aggravated\nassault': 'AggravatedAssault',
    'Burglary': 'Burglary',
    'Larceny-\ntheft': 'Larceny',
    'Motor\nvehicle\ntheft': 'CarTheft',
    'Arson': 'Arson',
    'Other\nassaults': 'Assault',
    'Forgery and\ncounterfeiting': 'ForgeryCounterfeit',
    'Fraud': 'Fraud',
    'Embezzlement': 'Embezzlement',
    'Stolen\nproperty;\nbuying,\nreceiving,\npossessing':          
        'StolenProperty',
    'Vandalism': 'Vandalism',
    'Weapons;\ncarrying,\npossessing,\netc.': 'Weapons',
    'Prostitution and\ncommercialized\nvice': 'CommercialSex',
    'Sex offenses\n(except\nrape and\nprostitution)': 'Sex',
    'Drug \nabuse\nviolations': 'DrugAbuse',
    'Gambling': 'Gambling',
    'Offenses\nagainst\nthe family\nand\nchildren': 'FamilyChildren',
    'Driving\nunder the\ninfluence': 'DUI',
    'Liquor\nlaws': 'LiquorLaws',
    'Drunkenness3': 'Drunkenness',
    'Disorderly\nconduct': 'DisorderlyConduct',
    'Vagrancy': 'Vagrancy',
    'All other\noffenses\n(except\ntraffic)': 'AllOther',
    'Suspicion4': 'Suspicion',
    'Curfew\nand\nloitering\nlaw\nviolations': 'CurfewLoitering',
    'Number\nof\nagencies': 'NumberAgencies',
    '2021\nestimated \npopulation': 'Population'})

allCrimes_2021R.columns

# %%
# Visually confirmed success


# Recode some values in State columns to clean them up

    # Confirm unique values and their counts for State columns

        # 2013
allCrimes_2013R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2013R['StateR'] = allCrimes_2013R['State']

allCrimes_2013R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2013R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2013R

# %%
# Visually confirmed success


        # 2014
allCrimes_2014R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2014R['StateR'] = allCrimes_2014R['State']

allCrimes_2014R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2014R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2014R

# %%
# Visually confirmed success


        # 2015
allCrimes_2015R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2015R['StateR'] = allCrimes_2015R['State']

allCrimes_2015R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2015R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2015R

# %%
# Visually confirmed success


        # 2016
allCrimes_2016R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2016R['StateR'] = allCrimes_2016R['State']

allCrimes_2016R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2016R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2016R

# %%
# Visually confirmed success


        # 2017
allCrimes_2017R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2017R['StateR'] = allCrimes_2017R['State']

allCrimes_2017R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2017R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2017R

# %%
# Visually confirmed success


        # 2018
allCrimes_2018R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2018R['StateR'] = allCrimes_2018R['State']

allCrimes_2018R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2018R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2018R

# %%
# Visually confirmed success


        # 2019
allCrimes_2019R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2019R['StateR'] = allCrimes_2019R['State']

allCrimes_2019R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2019R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2019R

# %%
# Visually confirmed success


        # 2020
allCrimes_2020R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2020R['StateR'] = allCrimes_2020R['State']

allCrimes_2020R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2020R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2020R

# %%
# Visually confirmed success


        # 2021
allCrimes_2021R.State.unique()

# %%
# array(['ALABAMA5', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
#        'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA6',
#        'FLORIDA5, 7', 'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS8',
#        'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA', 'MAINE',
#        'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
#        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
#        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK5',
#        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
#        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
#        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
#        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'], dtype=object)

            # Add new state column to recode some values
allCrimes_2021R['StateR'] = allCrimes_2021R['State']

allCrimes_2021R
                                               
# %%
# 102 rows × 36 columns

    # Update select values
allCrimes_2021R['StateR'].replace(
    ['ALABAMA5', 'DISTRICT OF COLUMBIA6', 'FLORIDA5, 7', 'ILLINOIS8', 
     'MINNESOTA7', 'NEW YORK5'], ['ALABAMA', 'WASHINGTON DC', 'FLORIDA', 'ILLINOIS', 'MINNESOTA', 'NEW YORK'], inplace = True)

allCrimes_2021R

# %%
# Visually confirmed success


# Add year column to each year's table

    # 2013
allCrimes_2013R['Year'] = 2013

allCrimes_2013R

# %%
# 102 rows × 37 columns
    # Visually confirmed success

    # 2014
allCrimes_2014R['Year'] = 2014

allCrimes_2014R

# %%
# 102 rows × 37 columns
    # Visually confirmed success

    # 2015
allCrimes_2015R['Year'] = 2015

allCrimes_2015R

# %%
# 102 rows × 37 columns
    # Visually confirmed success

    # 2016
allCrimes_2016R['Year'] = 2016

allCrimes_2016R

# %%
# 102 rows × 37 columns
    # Visually confirmed success

    # 2017
allCrimes_2017R['Year'] = 2017

allCrimes_2017R

# %%
# 102 rows × 37 columns
    # Visually confirmed success

    # 2018
allCrimes_2018R['Year'] = 2018

allCrimes_2018R

# %%
# 102 rows × 37 columns
    # Visually confirmed success

    # 2019
allCrimes_2019R['Year'] = 2019

allCrimes_2019R

# %%
# 102 rows × 37 columns
    # Visually confirmed success

    # 2020
allCrimes_2020R['Year'] = 2020

allCrimes_2020R

# %%
# 102 rows × 37 columns
    # Visually confirmed success

    # 2021
allCrimes_2021R['Year'] = 2021

allCrimes_2021R

# %%
# 102 rows × 37 columns
    # Visually confirmed success


# Join tables for all years
allCrimes_2013to2021 = pd.concat([
    allCrimes_2013R, allCrimes_2014R, allCrimes_2015R, allCrimes_2016R,
    allCrimes_2017R, allCrimes_2018R, allCrimes_2019R, allCrimes_2020R, 
    allCrimes_2021R], axis = 0)

allCrimes_2013to2021

# %%
# 918 rows × 37 columns
    # Visually confirmed success
    # 918 = 102 x 9


    # Drop original State column
allCrimes_2013to2021.drop(['State'], axis = 1, inplace = True)

allCrimes_2013to2021

# %%
# 918 rows × 36 columns


    # Rename recoded State column
allCrimes_2013to2021 = allCrimes_2013to2021.rename(
    columns = {'StateR': 'State'})

allCrimes_2013to2021

# %%
# Visually confirmed success


# Export files to csv

    # 2013
allCrimes_2013R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2013R.csv')

    # 2014
allCrimes_2014R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2014R.csv')

    # 2015
allCrimes_2015R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2015R.csv')

    # 2016
allCrimes_2016R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2016R.csv')

    # 2017
allCrimes_2017R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2017R.csv')

    # 2018
allCrimes_2018R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2018R.csv')

    # 2019
allCrimes_2019R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2019R.csv')

    # 2020
allCrimes_2020R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2020R.csv')

    # 2021
allCrimes_2021R.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2021R.csv')

    # 2013-2021
allCrimes_2013to2021.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/allCrimes_2013to2021.csv')

# %%
