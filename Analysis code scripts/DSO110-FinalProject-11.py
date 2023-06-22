# %%
# DSO110 - Data Science Final Project
    # File 11
    # Analysis: k-Means (Cluster Analysis)

# Goal: Determine whether there are any correlations between reported 
  # non-trafficking arrests and trafficking crime arrests in the FBI data

# H0: No correlation with any independent variables and trafficking crime
    # arrests
# H1: One or more independent variables are correlated to trafficking crime 
    # arrests   

# IV's: Each non-trafficking crime's arrests
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
traffickingCrime_2013to2021 = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/traffickingAllCrimes_2013to2021.csv')

traffickingCrime_2013to2021

# %%
# 1377 rows × 41 columns

        # Remove duplicate index column
traffickingCrime_2013to2021.drop(['Unnamed: 0'], axis = 1, inplace = True)

traffickingCrime_2013to2021

# %%
# 1377 rows × 40 columns


# Wrangling

    # Drop variables that aren't relevant
traffickingCrime = traffickingCrime_2013to2021.copy()

traffickingCrime.drop([
    'Year', 'State', 'Age', 'Population', 'NumberAgencies', 'TotalAll', 
    'TotalNonTraffickSex', 'TotalProperty', 'TotalViolent', 'CommercialSex', 
    'CommercialSexAct', 'InvoluntaryServitude'], axis = 1, inplace = True)

traffickingCrime

# %%
# 1377 rows × 28 columns


# k-Means Analysis

    # Create k-Means model
traffickingCrimeKm = KMeans(n_clusters = 2)

# %%

    # Fit the data to the model
traffickingCrimeKm.fit(traffickingCrime)

# %%
# KMeans(n_clusters=2)


# Interpretation

    # Plot each possible IV

        # Plot trafficking and rape
plt.title('k Means - Trafficking (x) & Rape (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Rape, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# A clear clustering difference for rape arrests above and below ~1,200


        # Plot trafficking and non-trafficking, non-rape sex crimes
plt.title('k Means - Trafficking (x) & Sex (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Sex, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though fairly clear divisions for less than ~2,100 
    # sex crime arrests


        # Plot trafficking and aggravated assault
plt.title('k Means - Trafficking (x) & AggravatedAssault (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.AggravatedAssault, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# A clear clustering difference for aggravated assault arrests above and below 
    # ~19k


        # Plot trafficking and arson
plt.title('k Means - Trafficking (x) & Arson (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Arson, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though a fairly clear division for less than ~250 
    # arson arrests


        # Plot trafficking and assault
plt.title('k Means - Trafficking (x) & Assault (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Assault, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# A clear clustering difference for assault arrests above and below ~50k


        # Plot trafficking and burglary
plt.title('k Means - Trafficking (x) & Burglary (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Burglary, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though a fairly clear division for less than ~10k 
    # burglary arrests


        # Plot trafficking and car theft
plt.title('k Means - Trafficking (x) & CarTheft (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.CarTheft, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though a fairly clear division for less than ~4k 
    # burglary arrests


        # Plot trafficking and curfew / loitering
plt.title('k Means - Trafficking (x) & CurfewLoitering (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.CurfewLoitering, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though fairly clear divisions for less than ~3,700 
    # curfew / loitering arrests and ~5k trafficking arrests


        # Plot trafficking and disorderly conduct
plt.title('k Means - Trafficking (x) & DisorderlyConduct (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.DisorderlyConduct, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though a fairly clear division for less than ~14k 
    # disorderly conduct arrests and ~4k trafficking arrests


        # Plot trafficking and drug abuse
plt.title('k Means - Trafficking (x) & DrugAbuse (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.DrugAbuse, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a tiny bit of overlap, though a fairly clear division for less than 
    # ~70k drug abuse arrests


        # Plot trafficking and drunkenness
plt.title('k Means - Trafficking (x) & Drunkenness (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Drunkenness, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though fairly clear divisions for less than ~30k 
    # drunkenness arrests


        # Plot trafficking and DUI
plt.title('k Means - Trafficking (x) & DUI (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.DUI, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a tiny bit of overlap, though a fairly clear division for less than 
    # ~30k DUI arrests


        # Plot trafficking and embezzlement
plt.title('k Means - Trafficking (x) & Embezzlement (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Embezzlement, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though a fairly clear division for less than ~500 
    # embezzlement arrests and 15k trafficking arrests


        # Plot trafficking and family / children crimes
plt.title('k Means - Trafficking (x) & FamilyChildren (y)')
plt.scatter(traffickingCrime.TotalTraffick, 
            traffickingCrime.FamilyChildren, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though fairly clear divisions for less than ~5k 
    # family / children crime arrests and ~4k trafficking arrests


        # Plot trafficking and forgery / counterfeit
plt.title('k Means - Trafficking (x) & ForgeryCounterfeit (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.ForgeryCounterfeit, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though a fairly clear division for less than ~1k 
    # forgery / counterfeit arrests


        # Plot trafficking and fraud
plt.title('k Means - Trafficking (x) & Fraud (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Fraud, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though a fairly clear division for less than ~5k 
    # fraud arrests


        # Plot trafficking and gambling
plt.title('k Means - Trafficking (x) & Gambling (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Gambling, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though a fairly clear division for less than ~100 
    # gambling arrests


        # Plot trafficking and larceny
plt.title('k Means - Trafficking (x) & Larceny (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Larceny, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though a fairly clear division for less than ~25k 
    # larceny arrests


        # Plot trafficking and liquor laws
plt.title('k Means - Trafficking (x) & LiquorLaws (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.LiquorLaws, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though a fairly clear division for less than ~14k 
    # liquor law arrests and ~4k trafficking arrests


        # Plot trafficking and murder / manslaughter
plt.title('k Means - Trafficking (x) & MurderManslaughter (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.MurderManslaughter, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# A clear clustering difference for murder / manslaughter arrests above and 
    # below ~600


        # Plot trafficking and other crime
plt.title('k Means - Trafficking (x) & AllOther (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.AllOther, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though a fairly clear division for less than ~160k 
    # other crime arrests


        # Plot trafficking and robbery
plt.title('k Means - Trafficking (x) & Robbery (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Robbery, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though a fairly clear division for less than ~5k 
    # robbery arrests


        # Plot trafficking and stolen property
plt.title('k Means - Trafficking (x) & StolenProperty (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.StolenProperty, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though fairly clear divisions for less than ~5k 
    # stolen property arrests and ~5k trafficking arrests


        # Plot trafficking and suspicion
plt.title('k Means - Trafficking (x) & Suspicion (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Suspicion, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though a fairly clear division for less than ~5k 
    # trafficking arrests


        # Plot trafficking and vagrancy
plt.title('k Means - Trafficking (x) & Vagrancy (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Vagrancy, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though fairly clear divisions for less than ~2k 
    # vagrancy arrests and ~5k trafficking arrests


        # Plot trafficking and vandalism
plt.title('k Means - Trafficking (x) & Vandalism (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Vandalism, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a lot of overlap, though a fairly clear division for less than ~5k 
    # vandalism arrests


        # Plot trafficking and weapons
plt.title('k Means - Trafficking (x) & Weapons (y)')
plt.scatter(traffickingCrime.TotalTraffick, traffickingCrime.Weapons, 
            c = traffickingCrimeKm.labels_, cmap = 'viridis')

# %%
# There is a bit of overlap, though a fairly clear division for less than ~5k 
    # weapons arrests



    # Add cluster labels to data
traffickingCrime['Cluster'] = traffickingCrimeKm.labels_

traffickingCrime

# %%
# 466539 rows × 29 columns

        # Investigate summary statistics by cluster

            # Trafficking
trafficking = traffickingCrime.groupby('Cluster')['TotalTraffick']

print('Trafficking Min:')
if len(trafficking) > 0:
    print(trafficking.min().apply('{:,.0f}'.format))
print('\n')

print('Trafficking Max:')
if len(trafficking) > 0:
    print(trafficking.max().apply('{:,.0f}'.format))
print('\n')

print('Trafficking Avg:')
if len(trafficking) > 0:
    print(trafficking.mean().apply('{:,.0f}'.format))
print('\n')

print('Trafficking Total:')
if len(trafficking) > 0:
    print(trafficking.sum().apply('{:,.0f}'.format))

# %%
# Trafficking Min:
# Cluster
# 0    0
# 1    0
# Name: TotalTraffick, dtype: object

# Trafficking Max:
# Cluster
# 0    34,788
# 1    32,703
# Name: TotalTraffick, dtype: object

# Trafficking Avg:
# Cluster
# 0    10,447
# 1       791
# Name: TotalTraffick, dtype: object

# Trafficking Total:
# Cluster
# 0      501,466
# 1    1,050,958
# Name: TotalTraffick, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Rape
rape = traffickingCrime.groupby('Cluster')['Rape']

print('Rape Min:')
if len(rape) > 0:
    print(rape.min().apply('{:,.0f}'.format))
print('\n')

print('Rape Max:')
if len(rape) > 0:
    print(rape.max().apply('{:,.0f}'.format))
print('\n')

print('Rape Avg:')
if len(rape) > 0:
    print(rape.mean().apply('{:,.0f}'.format))
print('\n')

print('Rape Total:')
if len(rape) > 0:
    print(rape.sum().apply('{:,.0f}'.format))

# %%
# Rape Min:
# Cluster
# 0    1,378
# 1        0
# Name: Rape, dtype: object

# Rape Max:
# Cluster
# 0    2,561
# 1    1,656
# Name: Rape, dtype: object

# Rape Avg:
# Cluster
# 0    1,907
# 1      174
# Name: Rape, dtype: object

# Rape Total:
# Cluster
# 0     91,528
# 1    231,744
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Sex
Sex = traffickingCrime.groupby('Cluster')['Sex']

print('Sex Crime Min:')
if len(Sex) > 0:
    print(Sex.min().apply('{:,.0f}'.format))
print('\n')

print('Sex Crime Max:')
if len(Sex) > 0:
    print(Sex.max().apply('{:,.0f}'.format))
print('\n')

print('Sex Crime Avg:')
if len(Sex) > 0:
    print(Sex.mean().apply('{:,.0f}'.format))
print('\n')

print('Sex Crime Total:')
if len(Sex) > 0:
    print(Sex.sum().apply('{:,.0f}'.format))

# %%
# Sex Crime Min:
# Cluster
# 0    707
# 1      0
# Name: Sex, dtype: object

# Sex Crime Max:
# Cluster
# 0    10,286
# 1     3,564
# Name: Sex, dtype: object

# Sex Crime Avg:
# Cluster
# 0    4,555
# 1      329
# Name: Sex, dtype: object

# Sex Crime Total:
# Cluster
# 0    218,642
# 1    437,318
# Name: Sex, dtype: object
    # The 1 cluster has more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though
    # Since these results appear to be consistent, it seems like the data are
    # clustered based on quantity of arrests – when a single row (ie: state / 
    # year combo) had higher arrests for crimes, that row was attributed to 
    # cluster 0, the rest were attributed to cluster 1 - so cluster 0 has far
    # fewer state / year combo's, but far more arrests... I wonder if cluster 0
    # is mainly from high-reporting states - will try to validate that


            # AggravatedAssault
aggravatedAssault = traffickingCrime.groupby('Cluster')['AggravatedAssault']

print('Aggravated Assault Min:')
if len(aggravatedAssault) > 0:
    print(aggravatedAssault.min().apply('{:,.0f}'.format))
print('\n')

print('Aggravated Assault Max:')
if len(aggravatedAssault) > 0:
    print(aggravatedAssault.max().apply('{:,.0f}'.format))
print('\n')

print('Aggravated Assault Avg:')
if len(aggravatedAssault) > 0:
    print(aggravatedAssault.mean().apply('{:,.0f}'.format))
print('\n')

print('Arson Total:')
if len(aggravatedAssault) > 0:
    print(aggravatedAssault.sum().apply('{:,.0f}'.format))

# %%
# Aggravated Assault Min:
# Cluster
# 0    18,575
# 1         0
# Name: AggravatedAssault, dtype: object

# Aggravated Assault Max:
# Cluster
# 0    89,618
# 1    23,012
# Name: AggravatedAssault, dtype: object

# Aggravated Assault Avg:
# Cluster
# 0    44,046
# 1     2,509
# Name: AggravatedAssault, dtype: object

# Arson Total:
# Cluster
# 0    2,114,222
# 1    3,334,384
# Name: AggravatedAssault, dtype: object
    # The 1 cluster has more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Arson
arson = traffickingCrime.groupby('Cluster')['Arson']

print('Arson Min:')
if len(arson) > 0:
    print(arson.min().apply('{:,.0f}'.format))
print('\n')

print('Arson Max:')
if len(arson) > 0:
    print(arson.max().apply('{:,.0f}'.format))
print('\n')

print('Arson Avg:')
if len(arson) > 0:
    print(arson.mean().apply('{:,.0f}'.format))
print('\n')

print('Arson Total:')
if len(arson) > 0:
    print(arson.sum().apply('{:,.0f}'.format))

# %%
# Arson Min:
# Cluster
# 0    190
# 1      0
# Name: Arson, dtype: object

# Arson Max:
# Cluster
# 0    2,051
# 1      643
# Name: Arson, dtype: object

# Arson Avg:
# Cluster
# 0    649
# 1     74
# Name: Arson, dtype: object

# Arson Total:
# Cluster
# 0    31,173
# 1    98,523
# Name: Arson, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Assault
assault = traffickingCrime.groupby('Cluster')['Assault']

print('Assault Min:')
if len(assault) > 0:
    print(assault.min().apply('{:,.0f}'.format))
print('\n')

print('Assault Max:')
if len(assault) > 0:
    print(assault.max().apply('{:,.0f}'.format))
print('\n')

print('Assault Avg:')
if len(assault) > 0:
    print(assault.mean().apply('{:,.0f}'.format))
print('\n')

print('Assault Total:')
if len(assault) > 0:
    print(assault.sum().apply('{:,.0f}'.format))

# %%
# Assault Min:
# Cluster
# 0    62,995
# 1         0
# Name: Assault, dtype: object

# Assault Max:
# Cluster
# 0    99,345
# 1    73,456
# Name: Assault, dtype: object

# Assault Avg:
# Cluster
# 0    77,835
# 1     8,673
# Name: Assault, dtype: object

# Assault Total:
# Cluster
# 0     3,736,074
# 1    11,526,494
# Name: Assault, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Burglary
burglary = traffickingCrime.groupby('Cluster')['Burglary']

print('Burglary Min:')
if len(burglary) > 0:
    print(burglary.min().apply('{:,.0f}'.format))
print('\n')

print('Burglary Max:')
if len(burglary) > 0:
    print(burglary.max().apply('{:,.0f}'.format))
print('\n')

print('Burglary Avg:')
if len(burglary) > 0:
    print(burglary.mean().apply('{:,.0f}'.format))
print('\n')

print('Burglary Total:')
if len(burglary) > 0:
    print(burglary.sum().apply('{:,.0f}'.format))

# %%
# Burglary Min:
# Cluster
# 0    6,537
# 1        0
# Name: Burglary, dtype: object

# Burglary Max:
# Cluster
# 0    50,390
# 1    14,163
# Name: Burglary, dtype: object

# Burglary Avg:
# Cluster
# 0    20,884
# 1     1,419
# Name: Burglary, dtype: object

# Burglary Total:
# Cluster
# 0    1,002,442
# 1    1,885,712
# Name: Burglary, dtype: object
    # The 1 cluster has more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # CarTheft
carTheft = traffickingCrime.groupby('Cluster')['CarTheft']

print('Car Theft Min:')
if len(carTheft) > 0:
    print(carTheft.min().apply('{:,.0f}'.format))
print('\n')

print('Car Theft Max:')
if len(carTheft) > 0:
    print(carTheft.max().apply('{:,.0f}'.format))
print('\n')

print('Car Theft Avg:')
if len(carTheft) > 0:
    print(carTheft.mean().apply('{:,.0f}'.format))
print('\n')

print('Car Theft Total:')
if len(carTheft) > 0:
    print(carTheft.sum().apply('{:,.0f}'.format))

# %%
# Car Theft Min:
# Cluster
# 0    3,440
# 1        0
# Name: CarTheft, dtype: object

# Car Theft Max:
# Cluster
# 0    19,501
# 1     5,637
# Name: CarTheft, dtype: object

# Car Theft Avg:
# Cluster
# 0    8,953
# 1      569
# Name: CarTheft, dtype: object

# Car Theft Total:
# Cluster
# 0    429,746
# 1    756,210
# Name: CarTheft, dtype: object
    # The 1 cluster has more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # CurfewLoitering
curfewLoitering = traffickingCrime.groupby('Cluster')['CurfewLoitering']

print('Curfew / Loitering Min:')
if len(curfewLoitering) > 0:
    print(curfewLoitering.min().apply('{:,.0f}'.format))
print('\n')

print('Curfew / Loitering Max:')
if len(curfewLoitering) > 0:
    print(curfewLoitering.max().apply('{:,.0f}'.format))
print('\n')

print('Curfew / Loitering Avg:')
if len(curfewLoitering) > 0:
    print(curfewLoitering.mean().apply('{:,.0f}'.format))
print('\n')

print('Curfew / Loitering Total:')
if len(curfewLoitering) > 0:
    print(curfewLoitering.sum().apply('{:,.0f}'.format))

# %%
# Curfew / Loitering Min:
# Cluster
# 0    0
# 1    0
# Name: CurfewLoitering, dtype: object

# Curfew / Loitering Max:
# Cluster
# 0     4,087
# 1    17,143
# Name: CurfewLoitering, dtype: object

# Curfew / Loitering Avg:
# Cluster
# 0    648
# 1    302
# Name: CurfewLoitering, dtype: object

# Curfew / Loitering Total:
# Cluster
# 0     31,087
# 1    400,811
# Name: CurfewLoitering, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is higher in cluster 0, though


            # DisorderlyConduct
disorderlyConduct = traffickingCrime.groupby('Cluster')['DisorderlyConduct']

print('Disorderly Conduct Min:')
if len(disorderlyConduct) > 0:
    print(disorderlyConduct.min().apply('{:,.0f}'.format))
print('\n')

print('Disorderly Conduct Max:')
if len(disorderlyConduct) > 0:
    print(disorderlyConduct.max().apply('{:,.0f}'.format))
print('\n')

print('Disorderly Conduct Avg:')
if len(disorderlyConduct) > 0:
    print(disorderlyConduct.mean().apply('{:,.0f}'.format))
print('\n')

print('Disorderly Conduct Total:')
if len(disorderlyConduct) > 0:
    print(disorderlyConduct.sum().apply('{:,.0f}'.format))

# %%
# Disorderly Conduct Min:
# Cluster
# 0    0
# 1    0
# Name: DisorderlyConduct, dtype: object

# Disorderly Conduct Max:
# Cluster
# 0    20,602
# 1    44,251
# Name: DisorderlyConduct, dtype: object

# Disorderly Conduct Avg:
# Cluster
# 0    4,195
# 1    3,385
# Name: DisorderlyConduct, dtype: object

# Disorderly Conduct Total:
# Cluster
# 0      201,354
# 1    4,499,290
# Name: DisorderlyConduct, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is higher in cluster 0, though


            # DrugAbuse
drugAbuse = traffickingCrime.groupby('Cluster')['DrugAbuse']

print('Drug Abuse Min:')
if len(drugAbuse) > 0:
    print(drugAbuse.min().apply('{:,.0f}'.format))
print('\n')

print('Drug Abuse Max:')
if len(drugAbuse) > 0:
    print(drugAbuse.max().apply('{:,.0f}'.format))
print('\n')

print('Drug Abuse Avg:')
if len(drugAbuse) > 0:
    print(drugAbuse.mean().apply('{:,.0f}'.format))
print('\n')

print('Drug Abuse Total:')
if len(drugAbuse) > 0:
    print(drugAbuse.sum().apply('{:,.0f}'.format))

# %%
# Drug Abuse Min:
# Cluster
# 0    66,934
# 1         0
# Name: DrugAbuse, dtype: object

# Drug Abuse Max:
# Cluster
# 0    229,083
# 1     82,337
# Name: DrugAbuse, dtype: object

# Drug Abuse Avg:
# Cluster
# 0    148,014
# 1     10,758
# Name: DrugAbuse, dtype: object

# Drug Abuse Total:
# Cluster
# 0     7,104,673
# 1    14,297,829
# Name: DrugAbuse, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Drunkenness
drunkenness = traffickingCrime.groupby('Cluster')['Drunkenness']

print('Drunkenness Min:')
if len(drunkenness) > 0:
    print(drunkenness.min().apply('{:,.0f}'.format))
print('\n')

print('Drunkenness Max:')
if len(drunkenness) > 0:
    print(drunkenness.max().apply('{:,.0f}'.format))
print('\n')

print('Drunkenness Avg:')
if len(drunkenness) > 0:
    print(drunkenness.mean().apply('{:,.0f}'.format))
print('\n')

print('Drunkenness Total:')
if len(drunkenness) > 0:
    print(drunkenness.sum().apply('{:,.0f}'.format))

# %%
# Drunkenness Min:
# Cluster
# 0    0
# 1    0
# Name: Drunkenness, dtype: object

# Drunkenness Max:
# Cluster
# 0    92,767
# 1    29,367
# Name: Drunkenness, dtype: object

# Drunkenness Avg:
# Cluster
# 0    41,786
# 1     1,801
# Name: Drunkenness, dtype: object

# Drunkenness Total:
# Cluster
# 0    2,005,708
# 1    2,393,504
# Name: Drunkenness, dtype: object
    # The 1 cluster has more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # DUI
dui = traffickingCrime.groupby('Cluster')['DUI']

print('DUI Min:')
if len(dui) > 0:
    print(dui.min().apply('{:,.0f}'.format))
print('\n')

print('DUI Max:')
if len(dui) > 0:
    print(dui.max().apply('{:,.0f}'.format))
print('\n')

print('DUI Avg:')
if len(dui) > 0:
    print(dui.mean().apply('{:,.0f}'.format))
print('\n')

print('DUI Total:')
if len(dui) > 0:
    print(dui.sum().apply('{:,.0f}'.format))

# %%
# DUI Min:
# Cluster
# 0    28,939
# 1         0
# Name: DUI, dtype: object

# DUI Max:
# Cluster
# 0    161,055
# 1     55,964
# Name: DUI, dtype: object

# DUI Avg:
# Cluster
# 0    77,989
# 1     7,496
# Name: DUI, dtype: object

# DUI Total:
# Cluster
# 0    3,743,470
# 1    9,962,034
# Name: DUI, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Embezzlement
embezzlement = traffickingCrime.groupby('Cluster')['Embezzlement']

print('Embezzlement Min:')
if len(embezzlement) > 0:
    print(embezzlement.min().apply('{:,.0f}'.format))
print('\n')

print('Embezzlement Max:')
if len(embezzlement) > 0:
    print(embezzlement.max().apply('{:,.0f}'.format))
print('\n')

print('Embezzlement Avg:')
if len(embezzlement) > 0:
    print(embezzlement.mean().apply('{:,.0f}'.format))
print('\n')

print('Embezzlement Total:')
if len(embezzlement) > 0:
    print(embezzlement.sum().apply('{:,.0f}'.format))

# %%
# Embezzlement Min:
# Cluster
# 0    193
# 1      0
# Name: Embezzlement, dtype: object

# Embezzlement Max:
# Cluster
# 0    1,086
# 1    1,609
# Name: Embezzlement, dtype: object

# Embezzlement Avg:
# Cluster
# 0    804
# 1    127
# Name: Embezzlement, dtype: object

# Embezzlement Total:
# Cluster
# 0     38,615
# 1    168,543
# Name: Embezzlement, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # FamilyChildren
FamilyChildren = traffickingCrime.groupby('Cluster')['FamilyChildren']

print('Family / Children Min:')
if len(FamilyChildren) > 0:
    print(FamilyChildren.min().apply('{:,.0f}'.format))
print('\n')

print('Family / Children Max:')
if len(FamilyChildren) > 0:
    print(FamilyChildren.max().apply('{:,.0f}'.format))
print('\n')

print('Family / Children Avg:')
if len(FamilyChildren) > 0:
    print(FamilyChildren.mean().apply('{:,.0f}'.format))
print('\n')

print('Family / Children Total:')
if len(FamilyChildren) > 0:
    print(FamilyChildren.sum().apply('{:,.0f}'.format))

# %%
# Family / Children Min:
# Cluster
# 0    0
# 1    0
# Name: FamilyChildren, dtype: object

# Family / Children Max:
# Cluster
# 0     5,207
# 1    11,168
# Name: FamilyChildren, dtype: object

# Family / Children Avg:
# Cluster
# 0    1,435
# 1      806
# Name: FamilyChildren, dtype: object

# Family / Children Total:
# Cluster
# 0       68,888
# 1    1,071,210
# Name: FamilyChildren, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # ForgeryCounterfeit
forgeryCounterfeit = traffickingCrime.groupby('Cluster')['ForgeryCounterfeit']

print('Forgery / Counterfeit Min:')
if len(forgeryCounterfeit) > 0:
    print(forgeryCounterfeit.min().apply('{:,.0f}'.format))
print('\n')

print('Forgery / Counterfeit Max:')
if len(forgeryCounterfeit) > 0:
    print(forgeryCounterfeit.max().apply('{:,.0f}'.format))
print('\n')

print('Forgery / Counterfeit Avg:')
if len(forgeryCounterfeit) > 0:
    print(forgeryCounterfeit.mean().apply('{:,.0f}'.format))
print('\n')

print('Forgery / Counterfeit Total:')
if len(forgeryCounterfeit) > 0:
    print(forgeryCounterfeit.sum().apply('{:,.0f}'.format))

# %%
# Forgery / Counterfeit Min:
# Cluster
# 0    1,183
# 1        0
# Name: ForgeryCounterfeit, dtype: object

# Forgery / Counterfeit Max:
# Cluster
# 0    5,598
# 1    3,790
# Name: ForgeryCounterfeit, dtype: object

# Forgery / Counterfeit Avg:
# Cluster
# 0    3,571
# 1      397
# Name: ForgeryCounterfeit, dtype: object

# Forgery / Counterfeit Total:
# Cluster
# 0    171,411
# 1    527,629
# Name: ForgeryCounterfeit, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Fraud
fraud = traffickingCrime.groupby('Cluster')['Fraud']

print('Fraud Min:')
if len(fraud) > 0:
    print(fraud.min().apply('{:,.0f}'.format))
print('\n')

print('Fraud Max:')
if len(fraud) > 0:
    print(fraud.max().apply('{:,.0f}'.format))
print('\n')

print('Fraud Avg:')
if len(fraud) > 0:
    print(fraud.mean().apply('{:,.0f}'.format))
print('\n')

print('Fraud Total:')
if len(fraud) > 0:
    print(fraud.sum().apply('{:,.0f}'.format))

# %%
# Fraud Min:
# Cluster
# 0    4,929
# 1        0
# Name: Fraud, dtype: object

# Fraud Max:
# Cluster
# 0    13,988
# 1    13,751
# Name: Fraud, dtype: object

# Fraud Avg:
# Cluster
# 0    8,099
# 1    1,045
# Name: Fraud, dtype: object

# Fraud Total:
# Cluster
# 0      388,748
# 1    1,389,200
# Name: Fraud, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Gambling
gambling = traffickingCrime.groupby('Cluster')['Gambling']

print('Gambling Min:')
if len(gambling) > 0:
    print(gambling.min().apply('{:,.0f}'.format))
print('\n')

print('Gambling Max:')
if len(gambling) > 0:
    print(gambling.max().apply('{:,.0f}'.format))
print('\n')

print('Gambling Avg:')
if len(gambling) > 0:
    print(gambling.mean().apply('{:,.0f}'.format))
print('\n')

print('Gambling Total:')
if len(gambling) > 0:
    print(gambling.sum().apply('{:,.0f}'.format))

# %%
# Gambling Min:
# Cluster
# 0    71
# 1     0
# Name: Gambling, dtype: object

# Gambling Max:
# Cluster
# 0      675
# 1    2,019
# Name: Gambling, dtype: object

# Gambling Avg:
# Cluster
# 0    321
# 1     28
# Name: Gambling, dtype: object

# Gambling Total:
# Cluster
# 0    15,401
# 1    36,841
# Name: Gambling, dtype: object
    # The 1 cluster has arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # Larceny
larceny = traffickingCrime.groupby('Cluster')['Larceny']

print('Larceny Min:')
if len(larceny) > 0:
    print(larceny.min().apply('{:,.0f}'.format))
print('\n')

print('Larceny Max:')
if len(larceny) > 0:
    print(larceny.max().apply('{:,.0f}'.format))
print('\n')

print('Larceny Avg:')
if len(larceny) > 0:
    print(larceny.mean().apply('{:,.0f}'.format))
print('\n')

print('Larceny Total:')
if len(larceny) > 0:
    print(larceny.sum().apply('{:,.0f}'.format))

# %%
# Larceny Min:
# Cluster
# 0    27,091
# 1         0
# Name: Larceny, dtype: object

# Larceny Max:
# Cluster
# 0    108,288
# 1     50,564
# Name: Larceny, dtype: object

# Larceny Avg:
# Cluster
# 0    63,086
# 1     8,428
# Name: Larceny, dtype: object

# Larceny Total:
# Cluster
# 0     3,028,141
# 1    11,201,003
# Name: Larceny, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # LiquorLaws
liquorLaws = traffickingCrime.groupby('Cluster')['LiquorLaws']

print('Liquor Laws Min:')
if len(liquorLaws) > 0:
    print(liquorLaws.min().apply('{:,.0f}'.format))
print('\n')

print('Liquor Laws Max:')
if len(liquorLaws) > 0:
    print(liquorLaws.max().apply('{:,.0f}'.format))
print('\n')

print('Liquor Laws Avg:')
if len(liquorLaws) > 0:
    print(liquorLaws.mean().apply('{:,.0f}'.format))
print('\n')

print('Liquor Laws Total:')
if len(liquorLaws) > 0:
    print(liquorLaws.sum().apply('{:,.0f}'.format))

# %%
# Liquor Laws Min:
# Cluster
# 0    2,285
# 1        0
# Name: LiquorLaws, dtype: object

# Liquor Laws Max:
# Cluster
# 0    25,229
# 1    20,590
# Name: LiquorLaws, dtype: object

# Liquor Laws Avg:
# Cluster
# 0    10,666
# 1     1,998
# Name: LiquorLaws, dtype: object

# Liquor Laws Total:
# Cluster
# 0      511,985
# 1    2,654,685
# Name: LiquorLaws, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # MurderManslaughter
murderManslaughter = traffickingCrime.groupby('Cluster')['MurderManslaughter']

print('Murder / Manslaughter Min:')
if len(murderManslaughter) > 0:
    print(murderManslaughter.min().apply('{:,.0f}'.format))
print('\n')

print('Murder / Manslaughter Max:')
if len(murderManslaughter) > 0:
    print(murderManslaughter.max().apply('{:,.0f}'.format))
print('\n')

print('Murder / Manslaughter Avg:')
if len(murderManslaughter) > 0:
    print(murderManslaughter.mean().apply('{:,.0f}'.format))
print('\n')

print('Murder / Manslaughter Total:')
if len(murderManslaughter) > 0:
    print(murderManslaughter.sum().apply('{:,.0f}'.format))

# %%
# Murder / Manslaughter Min:
# Cluster
# 0    592
# 1      0
# Name: MurderManslaughter, dtype: object

# Murder / Manslaughter Max:
# Cluster
# 0    1,594
# 1      923
# Name: MurderManslaughter, dtype: object

# Murder / Manslaughter Avg:
# Cluster
# 0    946
# 1     90
# Name: MurderManslaughter, dtype: object

# Murder / Manslaughter Total:
# Cluster
# 0     45,415
# 1    119,399
# Name: MurderManslaughter, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # AllOther
AllOther = traffickingCrime.groupby('Cluster')['AllOther']

print('Other Crimes Min:')
if len(AllOther) > 0:
    print(AllOther.min().apply('{:,.0f}'.format))
print('\n')

print('Other Crimes Max:')
if len(AllOther) > 0:
    print(AllOther.max().apply('{:,.0f}'.format))
print('\n')

print('Other Crimes Avg:')
if len(AllOther) > 0:
    print(AllOther.mean().apply('{:,.0f}'.format))
print('\n')

print('Other Crimes Total:')
if len(AllOther) > 0:
    print(AllOther.sum().apply('{:,.0f}'.format))

# %%
# Other Crimes Min:
# Cluster
# 0    158,834
# 1          0
# Name: AllOther, dtype: object

# Other Crimes Max:
# Cluster
# 0    425,913
# 1    148,599
# Name: AllOther, dtype: object

# Other Crimes Avg:
# Cluster
# 0    266,654
# 1     25,123
# Name: AllOther, dtype: object

# Other Crimes Total:
# Cluster
# 0    12,799,371
# 1    33,388,773
# Name: AllOther, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though
    

            # Robbery
robbery = traffickingCrime.groupby('Cluster')['Robbery']

print('Robbery Min:')
if len(robbery) > 0:
    print(robbery.min().apply('{:,.0f}'.format))
print('\n')

print('Robbery Max:')
if len(robbery) > 0:
    print(robbery.max().apply('{:,.0f}'.format))
print('\n')

print('Robbery Avg:')
if len(robbery) > 0:
    print(robbery.mean().apply('{:,.0f}'.format))
print('\n')

print('Robbery Total:')
if len(robbery) > 0:
    print(robbery.sum().apply('{:,.0f}'.format))

# %%
# Robbery Min:
# Cluster
# 0    3,695
# 1        0
# Name: Robbery, dtype: object

# Robbery Max:
# Cluster
# 0    16,942
# 1     5,873
# Name: Robbery, dtype: object

# Robbery Avg:
# Cluster
# 0    8,562
# 1      639
# Name: Robbery, dtype: object

# Robbery Total:
# Cluster
# 0    410,964
# 1    848,800
# Name: Robbery, dtype: object
    # The 1 cluster has more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


            # StolenProperty
stolenProperty = traffickingCrime.groupby('Cluster')['StolenProperty']

print('Stolen Property Min:')
if len(stolenProperty) > 0:
    print(stolenProperty.min().apply('{:,.0f}'.format))
print('\n')

print('Stolen Property Max:')
if len(stolenProperty) > 0:
    print(stolenProperty.max().apply('{:,.0f}'.format))
print('\n')

print('Stolen Property Avg:')
if len(stolenProperty) > 0:
    print(stolenProperty.mean().apply('{:,.0f}'.format))
print('\n')

print('Stolen Property Total:')
if len(stolenProperty) > 0:
    print(stolenProperty.sum().apply('{:,.0f}'.format))

# %%
# Stolen Property Min:
# Cluster
# 0    619
# 1      0
# Name: StolenProperty, dtype: object

# Stolen Property Max:
# Cluster
# 0    19,613
# 1     4,661
# Name: StolenProperty, dtype: object

# Stolen Property Avg:
# Cluster
# 0    6,242
# 1      711
# Name: StolenProperty, dtype: object

# Stolen Property Total:
# Cluster
# 0    299,631
# 1    944,949
# Name: StolenProperty, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though
    

            # Suspicion
suspicion = traffickingCrime.groupby('Cluster')['Suspicion']

print('Suspicion Min:')
if len(suspicion) > 0:
    print(suspicion.min().apply('{:,.0f}'.format))
print('\n')

print('Suspicion Max:')
if len(suspicion) > 0:
    print(suspicion.max().apply('{:,.0f}'.format))
print('\n')

print('Suspicion Avg:')
if len(suspicion) > 0:
    print(suspicion.mean().apply('{:,.0f}'.format))
print('\n')

print('Suspicion Total:')
if len(suspicion) > 0:
    print(suspicion.sum().apply('{:,.0f}'.format))

# %%
# Suspicion Min:
# Cluster
# 0    0
# 1    0
# Name: Suspicion, dtype: object

# Suspicion Max:
# Cluster
# 0      8
# 1    288
# Name: Suspicion, dtype: object

# Suspicion Avg:
# Cluster
# 0    0
# 1    8
# Name: Suspicion, dtype: object

# Suspicion Total:
# Cluster
# 0        20
# 1    10,142
# Name: Suspicion, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    #### The average number of arrests is also far higher in cluster 1
    

            # Vagrancy
vagrancy = traffickingCrime.groupby('Cluster')['Vagrancy']

print('Vagrancy Min:')
if len(vagrancy) > 0:
    print(vagrancy.min().apply('{:,.0f}'.format))
print('\n')

print('Vagrancy Max:')
if len(vagrancy) > 0:
    print(vagrancy.max().apply('{:,.0f}'.format))
print('\n')

print('Vagrancy Avg:')
if len(vagrancy) > 0:
    print(vagrancy.mean().apply('{:,.0f}'.format))
print('\n')

print('Vagrancy Total:')
if len(vagrancy) > 0:
    print(vagrancy.sum().apply('{:,.0f}'.format))

# %%
# Vagrancy Min:
# Cluster
# 0    0
# 1    0
# Name: Vagrancy, dtype: object

# Vagrancy Max:
# Cluster
# 0    8,105
# 1    3,383
# Name: Vagrancy, dtype: object

# Vagrancy Avg:
# Cluster
# 0    2,427
# 1      144
# Name: Vagrancy, dtype: object

# Vagrancy Total:
# Cluster
# 0    116,482
# 1    191,596
# Name: Vagrancy, dtype: object
    # The 1 cluster has more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though
    

            # Vandalism
vandalism = traffickingCrime.groupby('Cluster')['Vandalism']

print('Vandalism Min:')
if len(vandalism) > 0:
    print(vandalism.min().apply('{:,.0f}'.format))
print('\n')

print('Vandalism Max:')
if len(vandalism) > 0:
    print(vandalism.max().apply('{:,.0f}'.format))
print('\n')

print('Vandalism Avg:')
if len(vandalism) > 0:
    print(vandalism.mean().apply('{:,.0f}'.format))
print('\n')

print('Vandalism Total:')
if len(vandalism) > 0:
    print(vandalism.sum().apply('{:,.0f}'.format))

# %%
# Vandalism Min:
# Cluster
# 0    5,026
# 1        0
# Name: Vandalism, dtype: object

# Vandalism Max:
# Cluster
# 0    17,493
# 1    15,131
# Name: Vandalism, dtype: object

# Vandalism Avg:
# Cluster
# 0    9,451
# 1    1,617
# Name: Vandalism, dtype: object

# Vandalism Total:
# Cluster
# 0      453,666
# 1    2,148,452
# Name: Vandalism, dtype: object
    # The 1 cluster has far more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though
    

            # Weapons
weapons = traffickingCrime.groupby('Cluster')['Weapons']

print('Weapons Min:')
if len(weapons) > 0:
    print(weapons.min().apply('{:,.0f}'.format))
print('\n')

print('Weapons Max:')
if len(weapons) > 0:
    print(weapons.max().apply('{:,.0f}'.format))
print('\n')

print('Weapons Avg:')
if len(weapons) > 0:
    print(weapons.mean().apply('{:,.0f}'.format))
print('\n')

print('Weapons Total:')
if len(weapons) > 0:
    print(weapons.sum().apply('{:,.0f}'.format))

# %%
# Weapons Min:
# Cluster
# 0    4,028
# 1        0
# Name: Weapons, dtype: object

# Weapons Max:
# Cluster
# 0    28,547
# 1    12,916
# Name: Weapons, dtype: object

# Weapons Avg:
# Cluster
# 0    14,173
# 1     1,118
# Name: Weapons, dtype: object

# Weapons Total:
# Cluster
# 0      680,309
# 1    1,485,213
# Name: Weapons, dtype: object
    # The 1 cluster has more arrests than the 0 cluster
    # The average number of arrests is far higher in cluster 0, though


    # View Cluster distribution
traffickingCrime.Cluster.value_counts()

# %%
# 1    1329
# 0      48
# Name: Cluster, dtype: int64
    # This makes sense - as noted above, the data are clustered based on 
    # quantity of arrests – when a single row (ie: state / year combo) had 
    # higher arrests for crimes, that row was attributed to cluster 0, the rest 
    # were attributed to cluster 1 - so cluster 1 has far fewer state / year 
    # combo's, but far more arrests


# Add state and year back into the data to determine if that's related to the 
    # clustering
traffickingCrime = pd.concat([traffickingCrime, traffickingCrime_2013to2021[[
    'State', 'Year']]], axis = 1)

traffickingCrime

# %%
# 1377 rows × 31 columns
    # Visually confirmed success

    # Confirm which states are in each cluster
clustersStates = traffickingCrime.groupby('Cluster')['State'].unique()

print('States in Cluster 0:', clustersStates[0])
print('States in Cluster 1:', clustersStates[1])

# %%
# States in Cluster 0: ['CALIFORNIA' 'FLORIDA' 'TEXAS']
# States in Cluster 1: ['ALABAMA' 'ALASKA' 'ARIZONA' 'ARKANSAS' 'CALIFORNIA' 'COLORADO'
#  'CONNECTICUT' 'DELAWARE' 'FLORIDA' 'GEORGIA' 'HAWAII' 'IDAHO' 'ILLINOIS'
#  'INDIANA' 'IOWA' 'KANSAS' 'KENTUCKY' 'LOUISIANA' 'MAINE' 'MARYLAND'
#  'MASSACHUSETTS' 'MICHIGAN' 'MINNESOTA' 'MISSISSIPPI' 'MISSOURI' 'MONTANA'
#  'NEBRASKA' 'NEVADA' 'NEW HAMPSHIRE' 'NEW JERSEY' 'NEW MEXICO' 'NEW YORK'
#  'NORTH CAROLINA' 'NORTH DAKOTA' 'OHIO' 'OKLAHOMA' 'OREGON' 'PENNSYLVANIA'
#  'RHODE ISLAND' 'SOUTH CAROLINA' 'SOUTH DAKOTA' 'TENNESSEE' 'TEXAS' 'UTAH'
#  'VERMONT' 'VIRGINIA' 'WASHINGTON' 'WASHINGTON DC' 'WEST VIRGINIA'
#  'WISCONSIN' 'WYOMING']
    # Validated! Cluster 0 only has arrest data for three states, and cluster 1
    # has data for all states - these three states are also three of the five
    # identified in an ANOVA test as having the highest reports of trafficking
    # crime arrests, which makes this even more interesting


    # Confirm which years are in each cluster
clustersYears = traffickingCrime.groupby('Cluster')['Year'].unique()

print('Years in Cluster 0:', clustersYears[0])
print('Years in Cluster 1:', clustersYears[1])

# %%
# Years in Cluster 0: [2013 2014 2015 2016 2017 2018 2019 2020 2021]
# Years in Cluster 1: [2013 2014 2015 2016 2017 2018 2019 2020 2021]
    # Ok, both clusters have data for all years, which means the clustering 
    # really is based on those three states reporting more arrests; that said
    # because all states are also in both clusters, there must have been some
    # years where those states reported higher crimes than others

# %%

# Summary: When clustering trafficking and non-trafficking crime arrest data
# there are clearly correlated clusters for trafficking arrests and most 
# individual crime arrests. One cluster is based on the reports of these arrests 
# in California, Florida, and Texas, per those states each having years with 
# much higher arrest reports. The other cluster includes all states, based on 
# the arrest reports being much fewer for those three states in those years and 
# for all other states for all years. The crimes that are not as clearly 
# correlated with trafficking crime arrests are
    # Curfew / loitering
    # Disorderly conduct
    # Family / children crimes
    # Stolen property
    # Suspicion
    # Vagrancy
# This means that the remaining crimes follow the same clustering pattern
# as trafficking crimes