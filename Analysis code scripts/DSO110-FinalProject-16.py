# %%
# DSO110 - Data Science Final Project
    # File 16
    # Analysis: Machine learning - decision tree and random forest

# Goal: Determine what the leading, contributing factors to people being 
  # trafficked are, according to US census and FBI crime data for 2013- 2021

# H0: No census demographics predict arrests for trafficking crimes
# H1: One or more census demographics predict arrests for trafficking crimes

# IV's: Each demographic
# DV: Trafficking arrests

# Import packages
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# %%

# Import data

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import data
traffickingCensus = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/traffickingCensusNumeric.csv')

traffickingCensus

# %%
# 92462 rows × 13 columns

        # Remove duplicate index column
traffickingCensus.drop(['Unnamed: 0'], axis = 1, inplace = True)

traffickingCensus

# %%
# 92462 rows × 12 columns


# Wrangling

    # Define x variable for IV's
x = traffickingCensus.drop('TotalTraffick', axis = 1)

x

# %%
# 92462 rows × 11 columns

    # Define y variable for DV
y = traffickingCensus['TotalTraffick']

y

# %%
# 92462 rows × 1 columns

    # Create train / test split
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.3, 
                                                random_state = 75)

# %%
# Success



# Create initial decision tree model
traffickingCensusDecTree = DecisionTreeClassifier(random_state = 75)

# %%
# Success

    # Train the model
traffickingCensusDecTree.fit(xTrain, yTrain)

# %%
# DecisionTreeClassifier(random_state=75)


    # Run the model
traffickingCensusDecTreePredictions = traffickingCensusDecTree.predict(xTest)

# %%
# Success



# Interpret initial decision tree model

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCensusDecTreeCmValues = pd.crosstab(
    yTest, traffickingCensusDecTreePredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCensusDecTreeCmValues

# %%
# 246 rows × 203 columns

        # Generate new column labels
traffickingCensusDecTreeCmColumnLabels = [
    f'TotalTraffick {column} (Actual)'
    for column in traffickingCensusDecTreeCmValues.columns]

traffickingCensusDecTreeCmColumnLabels

# %%
# Success

        # Generate new column labels
traffickingCensusDecTreeCmRowLabels = [
    f'TotalTraffick {row} (Predicted)'
    for row in traffickingCensusDecTreeCmValues.index]

traffickingCensusDecTreeCmRowLabels


# %%
# Success

        # Convert to a dataframe with updated labels
traffickingCensusDecTreeCmCleaned = pd.DataFrame(
    index = traffickingCensusDecTreeCmRowLabels, 
    columns = traffickingCensusDecTreeCmColumnLabels, 
    data = traffickingCensusDecTreeCmValues.values)

traffickingCensusDecTreeCmCleaned

# %%
# 246 rows × 203 columns

        # Format for readability
traffickingCensusDecTreeCmReadable = traffickingCensusDecTreeCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCensusDecTreeCmReadable

# %%
# Voila!
    # Overall theme seems to be that the model is best at predicting no 
    # trafficking arrests, poor at predicting high trafficking arrests, and
    # pretty much incapable of predicting low arrests
    # The color highlights indicate the relative frequencies or counts of 
    # predictions. Darker colors represent lower frequencies or counts, while 
    # brighter colors represent higher frequencies or counts. This color scheme 
    # helps visually identify patterns and discrepancies in the confusion 
    # matrix. For example, a dark blue cell indicates a low count or frequency 
    # of predictions for a particular combination of actual and predicted 
    # labels. On the other hand, a bright yellow cell indicates a high count or 
    # frequency of predictions for that combination.
    # By using the viridis color map, you can easily identify areas of the 
    # confusion matrix where the model performs well (brighter colors) or 
    # struggles (darker colors) in terms of making accurate predictions.


    # Classification report
print(classification_report(yTest, traffickingCensusDecTreePredictions))

# %%
#     accuracy                           0.56     27739
#    macro avg       0.01      0.01      0.01     27739
# weighted avg       0.54      0.56      0.55     27739
    # This validates the results above that the model is best at predicting no 
    # trafficking arrests, poor at predicting high trafficking arrests, and
    # pretty much incapable of predicting low arrests
    # This model's accuracy is 56% - better than I expected, but not great and
    # only this good based on predicting no arrests
    # I wonder how the accuracy would change if 0 values were removed



# Create initial random forest model
traffickingCensusRF = RandomForestClassifier(random_state = 75)

# %%

    # Train model
traffickingCensusRF.fit(xTrain, yTrain)

# %%
# RandomForestClassifier(random_state=75)

    # Run model
traffickingCensusRFPredictions = traffickingCensusRF.predict(xTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCensusRFCmValues = pd.crosstab(
    yTest, traffickingCensusRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCensusRFCmValues

# %%
# 246 rows × 203 columns

        # Generate new column labels
traffickingCensusRFCmColumnLabels = [
    f'TotalTraffick {column} (Actual)'
    for column in traffickingCensusRFCmValues.columns]

traffickingCensusRFCmColumnLabels

# %%
# Success

        # Generate new column labels
traffickingCensusRFCmRowLabels = [
    f'TotalTraffick {row} (Predicted)'
    for row in traffickingCensusRFCmValues.index]

traffickingCensusRFCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffickingCensusRFCmCleaned = pd.DataFrame(
    index = traffickingCensusRFCmRowLabels, 
    columns = traffickingCensusRFCmColumnLabels, 
    data = traffickingCensusRFCmValues.values)

traffickingCensusRFCmCleaned

# %%
# 246 rows × 203 columns

        # Format for readability
traffickingCensusRFCmReadable = traffickingCensusRFCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCensusRFCmReadable

# %%
# This aligns with decision tree model in seemingly being best at predicting no 
    # trafficking arrests, poor at predicting high trafficking arrests, and
    # incapable of predicting low arrests


    # Classification report
print(classification_report(yTest, traffickingCensusRFPredictions))

# %%
#     accuracy                           0.56     27739
#    macro avg       0.01      0.01      0.01     27739
# weighted avg       0.54      0.56      0.55     27739
    # These results imply the random forest model is best (83%) at predicting
    # no trafficking arrests, and can barely predict arrests at all, which makes
    # the overal model 56% accurate, but that's really all about 0 values
    # I wonder how the accuracy would change if 0 values were removed



# Hyperparameter Tuning

    # Determine how many trees is best for my forest ;)

        # Create an array with commonly used quantities
numTrees = [1, 4, 5, 8, 10, 20, 50, 75, 100, 250, 500]

numTrees

# %%
# [1, 4, 5, 8, 10, 20, 50, 75, 100, 250, 500]

        # Create an empty variable to store accuracy scores for each test model
numTreesResults = []

numTreesResults

# %%
# []

        # Create a for loop to create, train, test, and confirm accuracy for a 
            # separate random forest model for each value in the array above,
            # then print results for each value in ranked order
for num in numTrees:
    traffickingCensusRFnEst = RandomForestClassifier(
        n_estimators = num, random_state = 75)
    traffickingCensusRFnEst.fit(xTrain, yTrain)
    accuracy = accuracy_score(
        yTest, traffickingCensusRFnEst.predict(xTest))
    numTreesResults.append((num, accuracy))

numTreesResultsRanked = sorted(
    numTreesResults, key=lambda x: x[1], reverse = True)

for num, accuracy in numTreesResultsRanked:
    print(num, ':', accuracy)

# %%
# 4 : 0.5723710299578211
# 8 : 0.5687659973322758
# 10 : 0.5684054940697213
# 5 : 0.5682612927646995
# 20 : 0.565665669274307
# 50 : 0.5645841594866433
# 100 : 0.5642957568765997
# 250 : 0.5642597065503443
# 500 : 0.5642597065503443
# 75 : 0.5642236562240889
# 1 : 0.5616280327336962
    # So 4 trees is best, though none are amazing


     # Determine best option for remaining three hyperparameters

        # Create variables for each parameter, using common options
max_features = ['auto', None, 'log2']
max_depth = [10, 20, 30, 40, 50, 60, 70, 80, 90, None]
min_samples_leaf = [1, 2, 4]

print(max_features)
print(max_depth)
print(min_samples_leaf)

# %%
# Success

        # Create grid of options
random_grid = {'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_leaf': min_samples_leaf}

random_grid

# %%
# Success

        # Create RF model to test hyperparameters with
traffickingCensusRFtuning = RandomForestClassifier(
    n_estimators = 4, random_state = 75)

# %%
# Success

        # Run search with hyperparameter variables
traffickingCensusRFSearch = RandomizedSearchCV(
    estimator = traffickingCensusRFtuning, 
    param_distributions = random_grid, n_iter = 90, cv = 5, 
    random_state = 75)

# %%
# Success

        # Train search model
traffickingCensusRFSearch.fit(xTrain, yTrain)

# %%
# RandomizedSearchCV(cv=5,
#                    estimator=RandomForestClassifier(n_estimators=4,
#                                                     random_state=75),
#                    n_iter=90,
#                    param_distributions={'max_depth': [10, 20, 30, 40, 50, 60,
#                                                       70, 80, 90, None],
#                                         'max_features': ['auto', None, 'log2'],
#                                         'min_samples_leaf': [1, 2, 4]},
#                    random_state=75)

         # Confirm best hyperparameter options
traffickingCensusRFSearch.best_params_

# %%
# {'min_samples_leaf': 4, 'max_features': 'auto', 'max_depth': 10}


    # Create and train new model with these options
traffickingCensusRFtuned = RandomForestClassifier(
    n_estimators = 4, min_samples_leaf = 4, max_features = 'auto', 
    max_depth = 10)

traffickingCensusRFtuned.fit(xTrain, yTrain)

# %%
# RandomForestClassifier(max_depth=10, min_samples_leaf=4, n_estimators=4)

    # Test model
traffickingCensusRFtunedPredictions = traffickingCensusRFtuned.predict(xTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCensusRFTunedCmValues = pd.crosstab(
    yTest, traffickingCensusRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCensusRFTunedCmValues

# %%
# 246 rows × 203 columns

        # Convert to a dataframe with updated labels
traffickingCensusRFTunedCmCleaned = pd.DataFrame(
    index = traffickingCensusRFCmRowLabels, 
    columns = traffickingCensusRFCmColumnLabels, 
    data = traffickingCensusRFTunedCmValues.values)

traffickingCensusRFTunedCmCleaned

# %%
# 246 rows × 203 columns

        # Format for readability
traffickingCensusRFTunedCmReadable = traffickingCensusRFTunedCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCensusRFTunedCmReadable

# %%
# Results seem pretty much the same as pre-tuning - will remove 0 values to try
    # again


    # Classification report
print(classification_report(yTest, traffickingCensusRFtunedPredictions))

# %%
#     accuracy                           0.64     27739
#    macro avg       0.00      0.00      0.00     27739
# weighted avg       0.41      0.64      0.50     27739
    # Ok, so the overall accuracy did go up by 10% which is good, though it's
    # almost exclusively about predicting 0 arrests
    

    # Find feature importance for hypertuned model
traffickingCensusFeatImp = pd.Series(
    traffickingCensusRFtuned.feature_importances_, index = x.columns)

traffickingCensusFeatImp = traffickingCensusFeatImp.sort_values(
    ascending = False)

traffickingCensusFeatImp.plot(kind = 'barh', figsize = (10, 5))

# %%
# Ok, so age detail is the best predictor, followed by total population, age, 
    # and total households, the rest are less strong



# Subset to exclude 0 values for trafficking and try again
traffickingCensusNoZeros = traffickingCensus[
    traffickingCensus.TotalTraffick > 0]

traffickingCensusNoZeros

# %%
# 33313 rows × 12 columns

    # Define x variable for IV's
xNoZeros = traffickingCensusNoZeros.drop('TotalTraffick', axis = 1)

xNoZeros

# %%
# 33313 rows × 11 columns

    # Define y variable for DV
yNoZeros = traffickingCensusNoZeros['TotalTraffick']

yNoZeros

# %%
# 33313 rows × 1 columns

    # Create train / test split
xNoZerosTrain, xNoZerosTest, yNoZerosTrain, yNoZerosTest = train_test_split(
    xNoZeros, yNoZeros, test_size = 0.3, random_state = 75)

# %%
# Success



# Create no zeros decision tree model
traffickingCensusNoZerosDecTree = DecisionTreeClassifier(random_state = 75)

# %%
# Success

    # Train the model
traffickingCensusNoZerosDecTree.fit(xNoZerosTrain, yNoZerosTrain)

# %%
# DecisionTreeClassifier(random_state=75)


    # Run the model
traffickingCensusNoZerosDecTreePredictions = traffickingCensusNoZerosDecTree.predict(xNoZerosTest)

# %%
# Success



# Interpret no zeros decision tree model

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCensusNoZerosDecTreeCmValues = pd.crosstab(
    yNoZerosTest, traffickingCensusNoZerosDecTreePredictions, 
    rownames = ['Actual'], colnames = ['Predicted'], dropna = True)

traffickingCensusNoZerosDecTreeCmValues

# %%
# 247 rows × 203 columns

        # Generate new column labels
traffickingCensusNoZerosDecTreeCmColumnLabels = [
    f'TotalTraffick {column} (Actual)'
    for column in traffickingCensusNoZerosDecTreeCmValues.columns]

traffickingCensusNoZerosDecTreeCmColumnLabels

# %%
# Success

        # Generate new column labels
traffickingCensusNoZerosDecTreeCmRowLabels = [
    f'TotalTraffick {row} (Predicted)'
    for row in traffickingCensusNoZerosDecTreeCmValues.index]

traffickingCensusNoZerosDecTreeCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffickingCensusNoZerosDecTreeCmCleaned = pd.DataFrame(
    index = traffickingCensusNoZerosDecTreeCmRowLabels, 
    columns = traffickingCensusNoZerosDecTreeCmColumnLabels, 
    data = traffickingCensusNoZerosDecTreeCmValues.values)

traffickingCensusNoZerosDecTreeCmCleaned

# %%
# 247 rows × 203 columns

        # Format for readability
traffickingCensusNoZerosDecTreeCmReadable = traffickingCensusNoZerosDecTreeCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCensusNoZerosDecTreeCmReadable

# %%
# Well, it's just not looking good...


    # Classification report
print(classification_report(
    yNoZerosTest, traffickingCensusNoZerosDecTreePredictions))

# %%
#     accuracy                           0.03      9994
#    macro avg       0.01      0.01      0.01      9994
# weighted avg       0.03      0.03      0.03      9994
    # Pathetic ;)



# Create no zeros random forest model
traffickingCensusNoZerosRF = RandomForestClassifier(random_state = 75)

# %%

    # Train model
traffickingCensusNoZerosRF.fit(xNoZerosTrain, yNoZerosTrain)

# %%
# RandomForestClassifier(random_state=75)

    # Run model
traffickingCensusNoZerosRFPredictions = traffickingCensusNoZerosRF.predict(
    xNoZerosTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCensusNoZerosRFCmValues = pd.crosstab(
    yNoZerosTest, traffickingCensusNoZerosRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCensusNoZerosRFCmValues

# %%
# 247 rows × 203 columns

        # Generate new column labels
traffickingCensusNoZerosRFCmColumnLabels = [
    f'TotalTraffick {column} (Actual)'
    for column in traffickingCensusNoZerosRFCmValues.columns]

traffickingCensusNoZerosRFCmColumnLabels

# %%
# Success

        # Generate new column labels
traffickingCensusNoZerosRFCmRowLabels = [
    f'TotalTraffick {row} (Predicted)'
    for row in traffickingCensusNoZerosRFCmValues.index]

traffickingCensusNoZerosRFCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffickingCensusNoZerosRFCmCleaned = pd.DataFrame(
    index = traffickingCensusNoZerosRFCmRowLabels, 
    columns = traffickingCensusNoZerosRFCmColumnLabels, 
    data = traffickingCensusNoZerosRFCmValues.values)

traffickingCensusNoZerosRFCmCleaned

# %%
# 247 rows × 203 columns

        # Format for readability
traffickingCensusNoZerosRFCmReadable = traffickingCensusNoZerosRFCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCensusNoZerosRFCmReadable

# %%
# This seems only slightly better than the no zeros decision tree model


    # Classification report
print(classification_report(yNoZerosTest, traffickingCensusNoZerosRFPredictions))

# %%
#     accuracy                           0.03      9994
#    macro avg       0.00      0.00      0.00      9994
# weighted avg       0.02      0.03      0.02      9994
    # And, in fact, it is worse



# Hyperparameter Tuning

    # Determine how many trees is best for my forest ;)

        # Create an empty variable to store accuracy scores for each test model
numTreesNoZerosResults = []

numTreesNoZerosResults

# %%
# []

        # Create a for loop to create, train, test, and confirm accuracy for a 
            # separate random forest model for each value in the array above,
            # then print results for each value in ranked order
for num in numTrees:
    traffickingCensusNoZerosRFnEst = RandomForestClassifier(
        n_estimators = num, random_state = 75)
    traffickingCensusNoZerosRFnEst.fit(xNoZerosTrain, yNoZerosTrain)
    accuracy = accuracy_score(
        yNoZerosTest, traffickingCensusNoZerosRFnEst.predict(xNoZerosTest))
    numTreesNoZerosResults.append((num, accuracy))

numTreesNoZerosResultsRanked = sorted(
    numTreesNoZerosResults, key=lambda x: x[1], reverse = True)

for num, accuracy in numTreesNoZerosResultsRanked:
    print(num, ':', accuracy)

# %%
# 5 : 0.02871723033820292
# 8 : 0.02861717030218131
# 10 : 0.028517110266159697
# 4 : 0.028116870122073243
# 20 : 0.027416449869921953
# 250 : 0.027416449869921953
# 500 : 0.027216329797878726
# 100 : 0.027116269761857114
# 50 : 0.026916149689813887
# 75 : 0.026916149689813887
# 1 : 0.02601560936561937
    # So 5 trees is best, though none are even good


     # Determine best option for remaining three hyperparameters

        # Create RF model to test hyperparameters with
traffickingCensusNoZerosRFtuning = RandomForestClassifier(
    n_estimators = 4, random_state = 75)

# %%
# Success

        # Run search with hyperparameter variables
traffickingCensusNoZerosRFSearch = RandomizedSearchCV(
    estimator = traffickingCensusNoZerosRFtuning, 
    param_distributions = random_grid, n_iter = 90, cv = 5, 
    random_state = 75)

# %%
# Success

        # Train search model
traffickingCensusNoZerosRFSearch.fit(xNoZerosTrain, yNoZerosTrain)

# %%
# RandomizedSearchCV(cv=5,
#                    estimator=RandomForestClassifier(n_estimators=4,
#                                                     random_state=75),
#                    n_iter=90,
#                    param_distributions={'max_depth': [10, 20, 30, 40, 50, 60,
#                                                       70, 80, 90, None],
#                                         'max_features': ['auto', None, 'log2'],
#                                         'min_samples_leaf': [1, 2, 4]},
#                    random_state=75)

         # Confirm best hyperparameter options
traffickingCensusNoZerosRFSearch.best_params_

# %%
# {'min_samples_leaf': 1, 'max_features': 'auto', 'max_depth': 10}


    # Create and train new model with these options
traffickingCensusNoZerosRFtuned = RandomForestClassifier(
    n_estimators = 5, min_samples_leaf =1, max_features = 'auto', 
    max_depth = 10)

traffickingCensusNoZerosRFtuned.fit(xNoZerosTrain, yNoZerosTrain)

# %%
# RandomForestClassifier(max_depth=10, n_estimators=5)

    # Test model
traffickingCensusNoZerosRFtunedPredictions = traffickingCensusNoZerosRFtuned.predict(xNoZerosTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCensusNoZerosRFTunedCmValues = pd.crosstab(
    yNoZerosTest, traffickingCensusNoZerosRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCensusNoZerosRFTunedCmValues

# %%
# 247 rows × 203 columns

        # Convert to a dataframe with updated labels
traffickingCensusNoZerosRFTunedCmCleaned = pd.DataFrame(
    index = traffickingCensusNoZerosRFCmRowLabels, 
    columns = traffickingCensusNoZerosRFCmColumnLabels, 
    data = traffickingCensusNoZerosRFTunedCmValues.values)

traffickingCensusNoZerosRFTunedCmCleaned

# %%
# 247 rows × 203 columns

        # Format for readability
traffickingCensusNoZerosRFTunedCmReadable = traffickingCensusNoZerosRFTunedCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCensusNoZerosRFTunedCmReadable

# %%
# Results seem pretty much the same as pre-tuning


    # Classification report
print(classification_report(yNoZerosTest, traffickingCensusNoZerosRFtunedPredictions))

# %%
#     accuracy                           0.07      9994
#    macro avg       0.00      0.00      0.00      9994
# weighted avg       0.02      0.07      0.02      9994
    # Ok, so the overall accuracy did go up by 4% which is good, this is still
    # a pretty much useless model
    

    # Find feature importance for hypertuned model
traffickingCensusNoZerosFeatImp = pd.Series(
    traffickingCensusNoZerosRFtuned.feature_importances_, 
    index = xNoZeros.columns)

traffickingCensusNoZerosFeatImp = traffickingCensusNoZerosFeatImp.sort_values(
    ascending = False)

traffickingCensusNoZerosFeatImp.plot(kind = 'barh', figsize=(10, 5))

# %%
# Ok, so total population is the best predictor, followed by total households, 
    # and down from there
    # Interesting that these are different from the variables that are good at
    # predicting 0 arrests
    # I wonder how this would differ if population and households were removed,
    # will subset differently to find out



# Subset to exclude population and households and try again
traffCensusNoPopHouse = traffickingCensus.drop([
    'TotalPopulation', 'TotalHouseholds'], axis = 1)

traffCensusNoPopHouse

# %%
# 92462 rows × 11 columns


    # Define x variable for IV's
xNoPopHouse = traffCensusNoPopHouse.drop('TotalTraffick', axis = 1)

xNoPopHouse

# %%
# 92462 rows × 9 columns

    # Define y variable for DV
yNoPopHouse = traffCensusNoPopHouse['TotalTraffick']

yNoPopHouse

# %%
# 92462 rows × 1 columns

    # Create train / test split
xNoPopHouseTrain, xNoPopHouseTest, yNoPopHouseTrain, yNoPopHouseTest = train_test_split(
    xNoPopHouse, yNoPopHouse, test_size = 0.3, random_state = 75)

# %%
# Success



# Create no population / households decision tree model
traffCensusNoPopHouseDecTree = DecisionTreeClassifier(random_state = 75)

# %%
# Success

    # Train the model
traffCensusNoPopHouseDecTree.fit(xNoPopHouseTrain, yNoPopHouseTrain)

# %%
# DecisionTreeClassifier(random_state=75)


    # Run the model
traffCensusNoPopHouseDecTreePredictions = traffCensusNoPopHouseDecTree.predict(xNoPopHouseTest)

# %%
# Success



# Interpret no population / households decision tree model

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffCensusNoPopHouseDecTreeCmValues = pd.crosstab(
    yNoPopHouseTest, traffCensusNoPopHouseDecTreePredictions, 
    rownames = ['Actual'], colnames = ['Predicted'], dropna = True)

traffCensusNoPopHouseDecTreeCmValues

# %%
# 246 rows × 3 columns

        # Generate new column labels
traffCensusNoPopHouseDecTreeCmColumnLabels = [
    f'TotalTraffick {column} (Actual)'
    for column in traffCensusNoPopHouseDecTreeCmValues.columns]

traffCensusNoPopHouseDecTreeCmColumnLabels

# %%
# Success

        # Generate new column labels
traffCensusNoPopHouseDecTreeCmRowLabels = [
    f'TotalTraffick {row} (Predicted)'
    for row in traffCensusNoPopHouseDecTreeCmValues.index]

traffCensusNoPopHouseDecTreeCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffCensusNoPopHouseDecTreeCmCleaned = pd.DataFrame(
    index = traffCensusNoPopHouseDecTreeCmRowLabels, 
    columns = traffCensusNoPopHouseDecTreeCmColumnLabels, 
    data = traffCensusNoPopHouseDecTreeCmValues.values)

traffCensusNoPopHouseDecTreeCmCleaned

# %%
# 246 rows × 3 columns

        # Format for readability
traffCensusNoPopHouseDecTreeCmReadable = traffCensusNoPopHouseDecTreeCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffCensusNoPopHouseDecTreeCmReadable

# %%
# Doesn't look great


    # Classification report
print(classification_report(
    yNoPopHouseTest, traffCensusNoPopHouseDecTreePredictions))

# %%
#     accuracy                           0.64     27739
#    macro avg       0.00      0.00      0.00     27739
# weighted avg       0.40      0.64      0.49     27739
    # This wouldn't be too shabby, except that the entire 64% appears to come
    # from predicting zero arrests, so I'll subset again after these models



# Create no population / households random forest model
traffCensusNoPopHouseRF = RandomForestClassifier(random_state = 75)

# %%

    # Train model
traffCensusNoPopHouseRF.fit(xNoPopHouseTrain, yNoPopHouseTrain)

# %%
# RandomForestClassifier(random_state=75)

    # Run model
traffCensusNoPopHouseRFPredictions = traffCensusNoPopHouseRF.predict(xNoPopHouseTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffCensusNoPopHouseRFCmValues = pd.crosstab(
    yNoPopHouseTest, traffCensusNoPopHouseRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffCensusNoPopHouseRFCmValues

# %%
# 246 rows × 3 columns

        # Generate new column labels
traffCensusNoPopHouseRFCmColumnLabels = [
    f'TotalTraffick {column} (Actual)'
    for column in traffCensusNoPopHouseRFCmValues.columns]

traffCensusNoPopHouseRFCmColumnLabels

# %%
# Success

        # Generate new column labels
traffCensusNoPopHouseRFCmRowLabels = [
    f'TotalTraffick {row} (Predicted)'
    for row in traffCensusNoPopHouseRFCmValues.index]

traffCensusNoPopHouseRFCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffCensusNoPopHouseRFCmCleaned = pd.DataFrame(
    index = traffCensusNoPopHouseRFCmRowLabels, 
    columns = traffCensusNoPopHouseRFCmColumnLabels, 
    data = traffCensusNoPopHouseRFCmValues.values)

traffCensusNoPopHouseRFCmCleaned

# %%
# 246 rows × 3 columns

        # Format for readability
traffCensusNoPopHouseRFCmReadable = traffCensusNoPopHouseRFCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffCensusNoPopHouseRFCmReadable

# %%
# This seems only slightly better than the no population / households decision 
    # tree model


    # Classification report
print(classification_report(yNoPopHouseTest, traffCensusNoPopHouseRFPredictions))

# %%
#     accuracy                           0.64     27739
#    macro avg       0.00      0.00      0.00     27739
# weighted avg       0.40      0.64      0.49     27739
    # About the same...



# Hyperparameter Tuning

    # Determine how many trees is best for my forest ;)

        # Create an empty variable to store accuracy scores for each test model
numTreesNoPopHouseResults = []

numTreesNoPopHouseResults

# %%
# []

        # Create a for loop to create, train, test, and confirm accuracy for a 
            # separate random forest model for each value in the array above,
            # then print results for each value in ranked order
for num in numTrees:
    traffCensusNoPopHouseRFnEst = RandomForestClassifier(
        n_estimators = num, random_state = 75)
    traffCensusNoPopHouseRFnEst.fit(xNoPopHouseTrain, yNoPopHouseTrain)
    accuracy = accuracy_score(
        yNoPopHouseTest, traffCensusNoPopHouseRFnEst.predict(xNoPopHouseTest))
    numTreesNoPopHouseResults.append((num, accuracy))

numTreesNoPopHouseResultsRanked = sorted(
    numTreesNoPopHouseResults, key=lambda x: x[1], reverse = True)

for num, accuracy in numTreesNoPopHouseResultsRanked:
    print(num, ':', accuracy)

# %%
# 1 : 0.6359638054724396
# 4 : 0.6359638054724396
# 5 : 0.6359638054724396
# 8 : 0.6359638054724396
# 10 : 0.6359638054724396
# 20 : 0.6359638054724396
# 50 : 0.6359638054724396
# 75 : 0.6359638054724396
# 100 : 0.6359638054724396
# 250 : 0.6359638054724396
# 500 : 0.6359638054724396
    # Weird that they're all identical...


     # Determine best option for remaining three hyperparameters

        # Create RF model to test hyperparameters with
traffCensusNoPopHouseRFtuning = RandomForestClassifier(
    n_estimators = 1, random_state = 75)

# %%
# Success

        # Run search with hyperparameter variables
traffCensusNoPopHouseRFSearch = RandomizedSearchCV(
    estimator = traffCensusNoPopHouseRFtuning, 
    param_distributions = random_grid, n_iter = 90, cv = 5, 
    random_state = 75)

# %%
# Success

        # Train search model
traffCensusNoPopHouseRFSearch.fit(xNoPopHouseTrain, yNoPopHouseTrain)

# %%
# RandomizedSearchCV(cv=5,
#                    estimator=RandomForestClassifier(n_estimators=1,
#                                                     random_state=75),
#                    n_iter=90,
#                    param_distributions={'max_depth': [10, 20, 30, 40, 50, 60,
#                                                       70, 80, 90, None],
#                                         'max_features': ['auto', None, 
    # 'log2'],
#                                         'min_samples_leaf': [1, 2, 4]},
#                    random_state=75)

         # Confirm best hyperparameter options
traffCensusNoPopHouseRFSearch.best_params_

# %%
# {'min_samples_leaf': 1, 'max_features': 'auto', 'max_depth': 10}


    # Create and train new model with these options
traffCensusNoPopHouseRFtuned = RandomForestClassifier(
    n_estimators = 1, min_samples_leaf = 1, max_features = 'auto', 
    max_depth = 10)

traffCensusNoPopHouseRFtuned.fit(xNoPopHouseTrain, yNoPopHouseTrain)

# %%
# RandomForestClassifier(max_depth=10, n_estimators=1)

    # Test model
traffCensusNoPopHouseRFtunedPredictions = traffCensusNoPopHouseRFtuned.predict(xNoPopHouseTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffCensusNoPopHouseRFTunedCmValues = pd.crosstab(
    yNoPopHouseTest, traffCensusNoPopHouseRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffCensusNoPopHouseRFTunedCmValues

# %%
# 246 rows × 3 columns

        # Convert to a dataframe with updated labels
traffCensusNoPopHouseRFTunedCmCleaned = pd.DataFrame(
    index = traffCensusNoPopHouseRFCmRowLabels, 
    columns = traffCensusNoPopHouseRFCmColumnLabels, 
    data = traffCensusNoPopHouseRFTunedCmValues.values)

traffCensusNoPopHouseRFTunedCmCleaned

# %%
# 246 rows × 3 columns

        # Format for readability
traffCensusNoPopHouseRFTunedCmReadable = traffCensusNoPopHouseRFTunedCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffCensusNoPopHouseRFTunedCmReadable

# %%
# Results seem pretty much the same as pre-tuning


    # Classification report
print(classification_report(yNoPopHouseTest, traffCensusNoPopHouseRFtunedPredictions))

# %%
#     accuracy                           0.64     27739
#    macro avg       0.00      0.00      0.00     27739
# weighted avg       0.40      0.64      0.49     27739
    # Yep.. same..
    

    # Find feature importance for hypertuned model
traffCensusNoPopHouseFeatImp = pd.Series(
    traffCensusNoPopHouseRFtuned.feature_importances_, 
    index = xNoPopHouse.columns)

traffCensusNoPopHouseFeatImp = traffCensusNoPopHouseFeatImp.sort_values(
    ascending = False)

traffCensusNoPopHouseFeatImp.plot(kind = 'barh', figsize=(10, 5))

# %%
# Age detail is by far the best, then age and computer, the rest barely at all



# Subset to exclude population and households AND zeros and try again

    # Remove population and households
traffCensusNoPopHouseZeros = traffickingCensus.drop([
    'TotalPopulation', 'TotalHouseholds'], axis = 1)

traffCensusNoPopHouseZeros

# %%
# 92462 rows × 11 columns


        # Drop zeros
traffCensusNoPopHouseZeros = traffCensusNoPopHouseZeros[
    traffCensusNoPopHouseZeros.TotalTraffick > 0]

traffCensusNoPopHouseZeros

# %%
# 33313 rows × 10 columns


    # Define x variable for IV's
xNoPopHouseZeros = traffCensusNoPopHouseZeros.drop('TotalTraffick', axis = 1)

xNoPopHouseZeros

# %%
# 33313 rows × 9 columns

    # Define y variable for DV
yNoPopHouseZeros = traffCensusNoPopHouseZeros['TotalTraffick']

yNoPopHouseZeros

# %%
# 33313 rows × 1 columns

    # Create train / test split
xNoPopHouseZerosTrain, xNoPopHouseZerosTest, yNoPopHouseZerosTrain, yNoPopHouseZerosTest = train_test_split(
    xNoPopHouseZeros, yNoPopHouseZeros, test_size = 0.3, random_state = 75)

# %%
# Success



# Create no population / households decision tree model
traffCensusNoPopHouseZerosDecTree = DecisionTreeClassifier(random_state = 75)

# %%
# Success

    # Train the model
traffCensusNoPopHouseZerosDecTree.fit(xNoPopHouseZerosTrain, yNoPopHouseZerosTrain)

# %%
# DecisionTreeClassifier(random_state=75)


    # Run the model
traffCensusNoPopHouseZerosDecTreePredictions = traffCensusNoPopHouseZerosDecTree.predict(xNoPopHouseZerosTest)

# %%
# Success



# Interpret no population / households decision tree model

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffCensusNoPopHouseZerosDecTreeCmValues = pd.crosstab(
    yNoPopHouseZerosTest, traffCensusNoPopHouseZerosDecTreePredictions, 
    rownames = ['Actual'], colnames = ['Predicted'], dropna = True)

traffCensusNoPopHouseZerosDecTreeCmValues

# %%
# 247 rows × 4 columns

        # Generate new column labels
traffCensusNoPopHouseZerosDecTreeCmColumnLabels = [
    f'TotalTraffick {column} (Actual)'
    for column in traffCensusNoPopHouseZerosDecTreeCmValues.columns]

traffCensusNoPopHouseZerosDecTreeCmColumnLabels

# %%
# Success

        # Generate new column labels
traffCensusNoPopHouseZerosDecTreeCmRowLabels = [
    f'TotalTraffick {row} (Predicted)'
    for row in traffCensusNoPopHouseZerosDecTreeCmValues.index]

traffCensusNoPopHouseZerosDecTreeCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffCensusNoPopHouseZerosDecTreeCmCleaned = pd.DataFrame(
    index = traffCensusNoPopHouseZerosDecTreeCmRowLabels, 
    columns = traffCensusNoPopHouseZerosDecTreeCmColumnLabels, 
    data = traffCensusNoPopHouseZerosDecTreeCmValues.values)

traffCensusNoPopHouseZerosDecTreeCmCleaned

# %%
# 247 rows × 4 columns

        # Format for readability
traffCensusNoPopHouseZerosDecTreeCmReadable = traffCensusNoPopHouseZerosDecTreeCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffCensusNoPopHouseZerosDecTreeCmReadable

# %%
# Not amazing


    # Classification report
print(classification_report(
    yNoPopHouseZerosTest, traffCensusNoPopHouseZerosDecTreePredictions))

# %%
#     accuracy                           0.07      9994
#    macro avg       0.00      0.00      0.00      9994
# weighted avg       0.01      0.07      0.01      9994
    # Not great, but better than the no zeros model that includes population
    # and households



# Create no population / households random forest model
traffCensusNoPopHouseZerosRF = RandomForestClassifier(random_state = 75)

# %%

    # Train model
traffCensusNoPopHouseZerosRF.fit(xNoPopHouseZerosTrain, yNoPopHouseZerosTrain)

# %%
# RandomForestClassifier(random_state=75)

    # Run model
traffCensusNoPopHouseZerosRFPredictions = traffCensusNoPopHouseZerosRF.predict(xNoPopHouseZerosTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffCensusNoPopHouseZerosRFCmValues = pd.crosstab(
    yNoPopHouseZerosTest, traffCensusNoPopHouseZerosRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffCensusNoPopHouseZerosRFCmValues

# %%
# 247 rows × 4 columns

        # Generate new column labels
traffCensusNoPopHouseZerosRFCmColumnLabels = [
    f'TotalTraffick {column} (Actual)'
    for column in traffCensusNoPopHouseZerosRFCmValues.columns]

traffCensusNoPopHouseZerosRFCmColumnLabels

# %%
# Success

        # Generate new column labels
traffCensusNoPopHouseZerosRFCmRowLabels = [
    f'TotalTraffick {row} (Predicted)'
    for row in traffCensusNoPopHouseZerosRFCmValues.index]

traffCensusNoPopHouseZerosRFCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffCensusNoPopHouseZerosRFCmCleaned = pd.DataFrame(
    index = traffCensusNoPopHouseZerosRFCmRowLabels, 
    columns = traffCensusNoPopHouseZerosRFCmColumnLabels, 
    data = traffCensusNoPopHouseZerosRFCmValues.values)

traffCensusNoPopHouseZerosRFCmCleaned

# %%
# 247 rows × 4 columns

        # Format for readability
traffCensusNoPopHouseZerosRFCmReadable = traffCensusNoPopHouseZerosRFCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffCensusNoPopHouseZerosRFCmReadable

# %%
# This seems only slightly better than the decision tree model


    # Classification report
print(classification_report(yNoPopHouseZerosTest, traffCensusNoPopHouseZerosRFPredictions))

# %%
#     accuracy                           0.07      9994
#    macro avg       0.00      0.00      0.00      9994
# weighted avg       0.01      0.07      0.01      9994
    # About the same...



# Hyperparameter Tuning

    # Determine how many trees is best for my forest ;)

        # Create an empty variable to store accuracy scores for each test model
numTreesNoPopHouseZerosResults = []

numTreesNoPopHouseZerosResults

# %%
# []

        # Create a for loop to create, train, test, and confirm accuracy for a 
            # separate random forest model for each value in the array above,
            # then print results for each value in ranked order
for num in numTrees:
    traffCensusNoPopHouseZerosRFnEst = RandomForestClassifier(
        n_estimators = num, random_state = 75)
    traffCensusNoPopHouseZerosRFnEst.fit(xNoPopHouseZerosTrain, yNoPopHouseZerosTrain)
    accuracy = accuracy_score(
        yNoPopHouseZerosTest, traffCensusNoPopHouseZerosRFnEst.predict(xNoPopHouseZerosTest))
    numTreesNoPopHouseZerosResults.append((num, accuracy))

numTreesNoPopHouseZerosResultsRanked = sorted(
    numTreesNoPopHouseZerosResults, key=lambda x: x[1], reverse = True)

for num, accuracy in numTreesNoPopHouseZerosResultsRanked:
    print(num, ':', accuracy)

# %%
# 100 : 0.07444466680008005
# 20 : 0.07384430658395037
# 50 : 0.07384430658395037
# 75 : 0.07384430658395037
# 250 : 0.07384430658395037
# 500 : 0.07384430658395037
# 10 : 0.07264358615169102
# 8 : 0.07104262557534521
# 5 : 0.0694416649989994
# 4 : 0.06904142485491295
# 1 : 0.06643986391835101
    # At least there's some variance..


     # Determine best option for remaining three hyperparameters

        # Create RF model to test hyperparameters with
traffCensusNoPopHouseZerosRFtuning = RandomForestClassifier(
    n_estimators = 100, random_state = 75)

# %%
# Success

        # Run search with hyperparameter variables
traffCensusNoPopHouseZerosRFSearch = RandomizedSearchCV(
    estimator = traffCensusNoPopHouseZerosRFtuning, 
    param_distributions = random_grid, n_iter = 90, cv = 5, 
    random_state = 75)

# %%
# Success

        # Train search model
traffCensusNoPopHouseZerosRFSearch.fit(xNoPopHouseZerosTrain, yNoPopHouseZerosTrain)

# %%
# RandomizedSearchCV(cv=5, estimator=RandomForestClassifier(random_state=75),
#                    n_iter=90,
#                    param_distributions={'max_depth': [10, 20, 30, 40, 50, 60,
#                                                       70, 80, 90, None],
#                                         'max_features': ['auto', None, 
    # 'log2'],
#                                         'min_samples_leaf': [1, 2, 4]},
#                    random_state=75)

         # Confirm best hyperparameter options
traffCensusNoPopHouseZerosRFSearch.best_params_

# %%
# {'min_samples_leaf': 4, 'max_features': 'auto', 'max_depth': 10}


    # Create and train new model with these options
traffCensusNoPopHouseZerosRFtuned = RandomForestClassifier(
    n_estimators = 1, min_samples_leaf = 4, max_features = 'auto', 
    max_depth = 10)

traffCensusNoPopHouseZerosRFtuned.fit(xNoPopHouseZerosTrain, yNoPopHouseZerosTrain)

# %%
# RandomForestClassifier(max_depth=10, min_samples_leaf=4, n_estimators=1)

    # Test model
traffCensusNoPopHouseZerosRFtunedPredictions = traffCensusNoPopHouseZerosRFtuned.predict(xNoPopHouseZerosTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffCensusNoPopHouseZerosRFTunedCmValues = pd.crosstab(
    yNoPopHouseZerosTest, traffCensusNoPopHouseZerosRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffCensusNoPopHouseZerosRFTunedCmValues

# %%
# 247 rows × 4 columns

        # Convert to a dataframe with updated labels
traffCensusNoPopHouseZerosRFTunedCmCleaned = pd.DataFrame(
    index = traffCensusNoPopHouseZerosRFCmRowLabels, 
    columns = traffCensusNoPopHouseZerosRFCmColumnLabels, 
    data = traffCensusNoPopHouseZerosRFTunedCmValues.values)

traffCensusNoPopHouseZerosRFTunedCmCleaned

# %%
# 247 rows × 4 columns

        # Format for readability
traffCensusNoPopHouseZerosRFTunedCmReadable = traffCensusNoPopHouseZerosRFTunedCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffCensusNoPopHouseZerosRFTunedCmReadable

# %%
# Results seem pretty much the same as pre-tuning


    # Classification report
print(classification_report(yNoPopHouseZerosTest, traffCensusNoPopHouseZerosRFtunedPredictions))

# %%
#     accuracy                           0.07      9994
#    macro avg       0.00      0.00      0.00      9994
# weighted avg       0.01      0.07      0.01      9994
    # Yep.. same..
    

    # Find feature importance for hypertuned model
traffCensusNoPopHouseZerosFeatImp = pd.Series(
    traffCensusNoPopHouseZerosRFtuned.feature_importances_, 
    index = xNoPopHouseZeros.columns)

traffCensusNoPopHouseZerosFeatImp = traffCensusNoPopHouseZerosFeatImp.sort_values(
    ascending = False)

traffCensusNoPopHouseZerosFeatImp.plot(kind = 'barh', figsize=(10, 5))
# %%
# The remaining demographics all have more impact now, as expected - education
    # has highest impact, followed by gender, age detail, and computer - the 
    # rest go down after that



# Summary: Census demographics are able to predict when there will be zero 
# trafficking crime arrests with 64% accuracy, but are only able to predict when 
# there will be trafficking crime arrests with 7% accuracy. The demographics 
# that are able to predict trafficking crime arrests vary based on whether 
# arrests are being predicted or not.
    # Age detail is the best predictor of zero arrests, followed by total 
        # population, age, and total households - in that order; when population
        # and households are excluded, age and computer show up as having 
        # impact, though age detail much greater still
    # Total population is the best predictor of arrests, followed by total 
        # households; when those variables are removed, education has 
        # greatest impact, followed by gender, age detail, and computer