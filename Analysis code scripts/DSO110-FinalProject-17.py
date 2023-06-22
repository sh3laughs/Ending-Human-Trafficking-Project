# %%
# DSO110 - Data Science Final Project
    # File 16
    # Analysis: Machine learning - decision tree and random forest

# Goal: Determine whether there are any correlations between reported 
  # non-trafficking arrests and trafficking crime arrests in the FBI data

# H0: No correlation with any independent variables and trafficking crime
    # arrests
# H1: One or more independent variables are correlated to trafficking crime 
    # arrests   

# IV's: Each non-trafficking crime's arrests
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


    # Define x variable for IV's
x = traffickingCrime.drop('TotalTraffick', axis = 1)

x

# %%
# 1377 rows × 27 columns

    # Define y variable for DV
y = traffickingCrime['TotalTraffick']

y

# %%
# 1377 rows × 1 column

    # Create train / test split
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.3, 
                                                random_state = 75)

# %%
# Success



# Create decision tree model
traffickingCrimeDecTree = DecisionTreeClassifier(random_state = 75)

# %%
# Success

    # Train the model
traffickingCrimeDecTree.fit(xTrain, yTrain)

# %%
# DecisionTreeClassifier(random_state=75)


    # Run the model
traffickingCrimeDecTreePredictions = traffickingCrimeDecTree.predict(xTest)

# %%
# Success



# Interpret decision tree model

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCrimeDecTreeCmValues = pd.crosstab(
    yTest, traffickingCrimeDecTreePredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCrimeDecTreeCmValues

# %%
# 129 rows × 101 columns

        # Generate new column labels
traffickingCrimeDecTreeCmColumnLabels = [
    f"TotalTraffick {column} (Actual)"
    for column in traffickingCrimeDecTreeCmValues.columns]

traffickingCrimeDecTreeCmColumnLabels

# %%
# Success

        # Generate new column labels
traffickingCrimeDecTreeCmRowLabels = [
    f"TotalTraffick {row} (Predicted)"
    for row in traffickingCrimeDecTreeCmValues.index]

traffickingCrimeDecTreeCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffickingCrimeDecTreeCmCleaned = pd.DataFrame(
    index = traffickingCrimeDecTreeCmRowLabels, 
    columns = traffickingCrimeDecTreeCmColumnLabels, 
    data = traffickingCrimeDecTreeCmValues.values)

traffickingCrimeDecTreeCmCleaned

# %%
# 129 rows × 101 columns

        # Format for readability
traffickingCrimeDecTreeCmReadable = traffickingCrimeDecTreeCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCrimeDecTreeCmReadable

# %%
# Voila!
    # Pretty, but so much to review, it's hard to gauge accuracy overall...
    # The color highlights indicate the relative frequencies or counts of 
    # predictions. Darker colors represent lower frequencies or counts, while 
    # brighter colors represent higher frequencies or counts. This color scheme 
    # helps visually identify patterns and discrepancies in the confusion 
    # matrix. For example, a dark blue cell indicates a low count or frequency 
    # of predictions for a particular combination of actual and predicted 
    # labels. On the other hand, a bright yellow cell indicates a high count or 
    # frequency of predictions for that combination. By using the viridis color 
    # map, you can easily identify areas of the confusion matrix where the model 
    # performs well (brighter colors) or struggles (darker colors) in terms of 
    # making accurate predictions.


    # Classification report
print(classification_report(yTest, traffickingCrimeDecTreePredictions))

# %%
#     accuracy                           0.51       414
#    macro avg       0.12      0.13      0.12       414
# weighted avg       0.48      0.51      0.49       414
    # Not terrible - though it's 78% accurate at guessing 0 arrests, which means
    # it's probably noticeably worse at accurately guessing when there are 
    # arrests - after a random forest model on full dataset, I'll also try on
    # data without 0 arrests



# Create initial random forest model
traffickingCrimeRF = RandomForestClassifier(random_state = 75)

# %%

    # Train model
traffickingCrimeRF.fit(xTrain, yTrain)

# %%
# RandomForestClassifier(random_state=75)

    # Run model
traffickingCrimeRFPredictions = traffickingCrimeRF.predict(xTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCrimeRFCmValues = pd.crosstab(
    yTest, traffickingCrimeRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCrimeRFCmValues

# %%
# 129 rows × 82 columns

        # Generate new column labels
traffickingCrimeRFCmColumnLabels = [
    f"TotalTraffick {column} (Actual)"
    for column in traffickingCrimeRFCmValues.columns]

traffickingCrimeRFCmColumnLabels

# %%
# Success

        # Generate new column labels
traffickingCrimeRFCmRowLabels = [
    f"TotalTraffick {row} (Predicted)"
    for row in traffickingCrimeRFCmValues.index]

traffickingCrimeRFCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffickingCrimeRFCmCleaned = pd.DataFrame(
    index = traffickingCrimeRFCmRowLabels, 
    columns = traffickingCrimeRFCmColumnLabels, 
    data = traffickingCrimeRFCmValues.values)

traffickingCrimeRFCmCleaned

# %%
# 129 rows × 82 columns

        # Format for readability
traffickingCrimeRFCmReadable = traffickingCrimeRFCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCrimeRFCmReadable

# %%
# Pretty but a lot to read


    # Classification report
print(classification_report(yTest, traffickingCrimeRFPredictions))

# %%
#     accuracy                           0.57       414
#    macro avg       0.17      0.16      0.16       414
# weighted avg       0.46      0.57      0.49       414
    # Moving in the right direction! It's still 66% accurate at guessing 0 
    # arrests, which means it's probably noticeably worse at accurately guessing 
    # when there are arrests



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
    traffickingCrimeRFnEst = RandomForestClassifier(
        n_estimators = num, random_state = 75)
    traffickingCrimeRFnEst.fit(xTrain, yTrain)
    accuracy = accuracy_score(
        yTest, traffickingCrimeRFnEst.predict(xTest))
    numTreesResults.append((num, accuracy))

numTreesResultsRanked = sorted(
    numTreesResults, key=lambda x: x[1], reverse = True)

for num, accuracy in numTreesResultsRanked:
    print(num, ":", accuracy)

# %%
# 500 : 0.5821256038647343
# 50 : 0.572463768115942
# 250 : 0.572463768115942
# 75 : 0.5700483091787439
# 100 : 0.5676328502415459
# 20 : 0.5628019323671497
# 10 : 0.5410628019323671
# 8 : 0.5241545893719807
# 5 : 0.5120772946859904
# 4 : 0.49033816425120774
# 1 : 0.41304347826086957
    # 500 it is...


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
traffickingCrimeRFtuning = RandomForestClassifier(
    n_estimators = 500, random_state = 75)

# %%
# Success

        # Run search with hyperparameter variables
traffickingCrimeRFSearch = RandomizedSearchCV(
    estimator = traffickingCrimeRFtuning, 
    param_distributions = random_grid, n_iter = 90, cv = 5, 
    random_state = 75)

# %%
# Success

        # Train search model
traffickingCrimeRFSearch.fit(xTrain, yTrain)

# %%
# RandomizedSearchCV(cv=5,
#                    estimator=RandomForestClassifier(n_estimators=500,
#                                                     random_state=75),
#                    n_iter=90,
#                    param_distributions={'max_depth': [10, 20, 30, 40, 50, 60,
#                                                       70, 80, 90, None],
#                                         'max_features': ['auto', None, 
    # 'log2'],
#                                         'min_samples_leaf': [1, 2, 4]},
#                    random_state=75)


         # Confirm best hyperparameter options
traffickingCrimeRFSearch.best_params_

# %%
# {'min_samples_leaf': 1, 'max_features': None, 'max_depth': 30}


    # Create and train new model with these options
traffickingCrimeRFtuned = RandomForestClassifier(
    n_estimators = 500, min_samples_leaf = 1, max_features = None, 
    max_depth = 30)

traffickingCrimeRFtuned.fit(xTrain, yTrain)

# %%
# RandomForestClassifier(max_depth=30, max_features=None, n_estimators=500)

    # Test model
traffickingCrimeRFtunedPredictions = traffickingCrimeRFtuned.predict(xTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCrimeRFTunedCmValues = pd.crosstab(
    yTest, traffickingCrimeRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCrimeRFTunedCmValues

# %%
# 129 rows × 82 columns

        # Convert to a dataframe with updated labels
traffickingCrimeRFTunedCmCleaned = pd.DataFrame(
    index = traffickingCrimeRFCmRowLabels, 
    columns = traffickingCrimeRFCmColumnLabels, 
    data = traffickingCrimeRFTunedCmValues.values)

traffickingCrimeRFTunedCmCleaned

# %%
# 129 rows × 82 columns

        # Format for readability
traffickingCrimeRFTunedCmReadable = traffickingCrimeRFTunedCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCrimeRFTunedCmReadable

# %%
# Still a lot to review..


    # Classification report
print(classification_report(yTest, traffickingCrimeRFtunedPredictions))

# %%
#     accuracy                           0.59       414
#    macro avg       0.22      0.21      0.21       414
# weighted avg       0.53      0.59      0.54       414
    # Not amazing, but not too shabby, either
    

    # Find feature importance for hypertuned model
traffickingCrimeFeatImp = pd.Series(
    traffickingCrimeRFtuned.feature_importances_, index = x.columns)
traffickingCrimeFeatImp = traffickingCrimeFeatImp.sort_values(
    ascending = False)

traffickingCrimeFeatImp.plot(kind = 'barh', figsize = (10, 5))

# %%
# This is interesting - DUI has highest impact by almost double the next, 
    # which is liquor laws, followed closely by car theft and rape, and 
    # the rest are down from there



# Subset to exclude 0 values for trafficking and try again
traffickingCrimeNoZeros = traffickingCrime[
    traffickingCrime.TotalTraffick > 0]

traffickingCrimeNoZeros

# %%
# 647 rows × 28 columns

    # Define x variable for IV's
xNoZeros = traffickingCrimeNoZeros.drop('TotalTraffick', axis = 1)

xNoZeros

# %%
# 647 rows × 27 columns

    # Define y variable for DV
yNoZeros = traffickingCrimeNoZeros['TotalTraffick']

yNoZeros

# %%
# 647 rows × 1 columns

    # Create train / test split
xNoZerosTrain, xNoZerosTest, yNoZerosTrain, yNoZerosTest = train_test_split(
    xNoZeros, yNoZeros, test_size = 0.3, random_state = 75)

# %%
# Success



# Create no zeros decision tree model
traffickingCrimeNoZerosDecTree = DecisionTreeClassifier(random_state = 75)

# %%
# Success

    # Train the model
traffickingCrimeNoZerosDecTree.fit(xNoZerosTrain, yNoZerosTrain)

# %%
# DecisionTreeClassifier(random_state=75)


    # Run the model
traffickingCrimeNoZerosDecTreePredictions = traffickingCrimeNoZerosDecTree.predict(xNoZerosTest)

# %%
# Success



# Interpret no zeros decision tree model

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCrimeNoZerosDecTreeCmValues = pd.crosstab(
    yNoZerosTest, traffickingCrimeNoZerosDecTreePredictions, 
    rownames = ['Actual'], colnames = ['Predicted'], dropna = True)

traffickingCrimeNoZerosDecTreeCmValues

# %%
# 120 rows × 100 columns

        # Generate new column labels
traffickingCrimeNoZerosDecTreeCmColumnLabels = [
    f"TotalTraffick {column} (Actual)"
    for column in traffickingCrimeNoZerosDecTreeCmValues.columns]

traffickingCrimeNoZerosDecTreeCmColumnLabels

# %%
# Success

        # Generate new column labels
traffickingCrimeNoZerosDecTreeCmRowLabels = [
    f"TotalTraffick {row} (Predicted)"
    for row in traffickingCrimeNoZerosDecTreeCmValues.index]

traffickingCrimeNoZerosDecTreeCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffickingCrimeNoZerosDecTreeCmCleaned = pd.DataFrame(
    index = traffickingCrimeNoZerosDecTreeCmRowLabels, 
    columns = traffickingCrimeNoZerosDecTreeCmColumnLabels, 
    data = traffickingCrimeNoZerosDecTreeCmValues.values)

traffickingCrimeNoZerosDecTreeCmCleaned

# %%
# 120 rows × 100 columns

        # Format for readability
traffickingCrimeNoZerosDecTreeCmReadable = traffickingCrimeNoZerosDecTreeCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCrimeNoZerosDecTreeCmReadable

# %%
# A lot to reveiew...


    # Classification report
print(classification_report(
    yNoZerosTest, traffickingCrimeNoZerosDecTreePredictions))

# %%
#     accuracy                           0.21       195
#    macro avg       0.12      0.13      0.12       195
# weighted avg       0.23      0.21      0.20       195
    # Better than I expected!



# Create no zeros random forest model
traffickingCrimeNoZerosRF = RandomForestClassifier(random_state = 75)

# %%

    # Train model
traffickingCrimeNoZerosRF.fit(xNoZerosTrain, yNoZerosTrain)

# %%
# RandomForestClassifier(random_state=75)

    # Run model
traffickingCrimeNoZerosRFPredictions = traffickingCrimeNoZerosRF.predict(xNoZerosTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCrimeNoZerosRFCmValues = pd.crosstab(
    yNoZerosTest, traffickingCrimeNoZerosRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCrimeNoZerosRFCmValues

# %%
# 120 rows × 93 columns

        # Generate new column labels
traffickingCrimeNoZerosRFCmColumnLabels = [
    f"TotalTraffick {column} (Actual)"
    for column in traffickingCrimeNoZerosRFCmValues.columns]

traffickingCrimeNoZerosRFCmColumnLabels

# %%
# Success

        # Generate new column labels
traffickingCrimeNoZerosRFCmRowLabels = [
    f"TotalTraffick {row} (Predicted)"
    for row in traffickingCrimeNoZerosRFCmValues.index]

traffickingCrimeNoZerosRFCmRowLabels

# %%
# Success

        # Convert to a dataframe with updated labels
traffickingCrimeNoZerosRFCmCleaned = pd.DataFrame(
    index = traffickingCrimeNoZerosRFCmRowLabels, 
    columns = traffickingCrimeNoZerosRFCmColumnLabels, 
    data = traffickingCrimeNoZerosRFCmValues.values)

traffickingCrimeNoZerosRFCmCleaned

# %%
# 120 rows × 93 columns

        # Format for readability
traffickingCrimeNoZerosRFCmReadable = traffickingCrimeNoZerosRFCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCrimeNoZerosRFCmReadable

# %%
# Aaand, a lot to review


    # Classification report
print(classification_report(yNoZerosTest, traffickingCrimeNoZerosRFPredictions))

# %%
#     accuracy                           0.38       195
#    macro avg       0.23      0.26      0.24       195
# weighted avg       0.36      0.38      0.36       195
    # Now we're getting somewhere!



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
    traffickingCrimeNoZerosRFnEst = RandomForestClassifier(
        n_estimators = num, random_state = 75)
    traffickingCrimeNoZerosRFnEst.fit(xNoZerosTrain, yNoZerosTrain)
    accuracy = accuracy_score(
        yNoZerosTest, traffickingCrimeNoZerosRFnEst.predict(xNoZerosTest))
    numTreesNoZerosResults.append((num, accuracy))

numTreesNoZerosResultsRanked = sorted(
    numTreesNoZerosResults, key=lambda x: x[1], reverse = True)

for num, accuracy in numTreesNoZerosResultsRanked:
    print(num, ":", accuracy)

# %%
# 250 : 0.4
# 500 : 0.4
# 100 : 0.37948717948717947
# 50 : 0.37435897435897436
# 75 : 0.36923076923076925
# 20 : 0.3384615384615385
# 8 : 0.3076923076923077
# 10 : 0.2923076923076923
# 5 : 0.26666666666666666
# 4 : 0.26153846153846155
# 1 : 0.1641025641025641
    # Odd for the first two to be so precise...


     # Determine best option for remaining three hyperparameters

        # Create RF model to test hyperparameters with
traffickingCrimeNoZerosRFtuning = RandomForestClassifier(
    n_estimators = 250, random_state = 75)

# %%
# Success

        # Run search with hyperparameter variables
traffickingCrimeNoZerosRFSearch = RandomizedSearchCV(
    estimator = traffickingCrimeNoZerosRFtuning, 
    param_distributions = random_grid, n_iter = 90, cv = 5, 
    random_state = 75)

# %%
# Success

        # Train search model
traffickingCrimeNoZerosRFSearch.fit(xNoZerosTrain, yNoZerosTrain)

# %%
# RandomizedSearchCV(cv=5,
#                    estimator=RandomForestClassifier(n_estimators=250,
#                                                     random_state=75),
#                    n_iter=90,
#                    param_distributions={'max_depth': [10, 20, 30, 40, 50, 60,
#                                                       70, 80, 90, None],
#                                         'max_features': ['auto', None, 
    # 'log2'],
#                                         'min_samples_leaf': [1, 2, 4]},
#                    random_state=75)


         # Confirm best hyperparameter options
traffickingCrimeNoZerosRFSearch.best_params_

# %%
# {'min_samples_leaf': 1, 'max_features': None, 'max_depth': 40}


    # Create and train new model with these options
traffickingCrimeNoZerosRFtuned = RandomForestClassifier(
    n_estimators = 250, min_samples_leaf = 1, max_features = None, 
    max_depth = 40)

traffickingCrimeNoZerosRFtuned.fit(xNoZerosTrain, yNoZerosTrain)

# %%
# RandomForestClassifier(max_depth=40, max_features=None, n_estimators=250)

    # Test model
traffickingCrimeNoZerosRFtunedPredictions = traffickingCrimeNoZerosRFtuned.predict(xNoZerosTest)

# %%
# Success


# Interpret

    # Confusion matrix as a formatted dataframe for legibility

        # Compute the confusion matrix values
traffickingCrimeNoZerosRFTunedCmValues = pd.crosstab(
    yNoZerosTest, traffickingCrimeNoZerosRFPredictions, rownames = ['Actual'], 
    colnames = ['Predicted'], dropna = True)

traffickingCrimeNoZerosRFTunedCmValues

# %%
# 120 rows × 93 columns

        # Convert to a dataframe with updated labels
traffickingCrimeNoZerosRFTunedCmCleaned = pd.DataFrame(
    index = traffickingCrimeNoZerosRFCmRowLabels, 
    columns = traffickingCrimeNoZerosRFCmColumnLabels, 
    data = traffickingCrimeNoZerosRFTunedCmValues.values)

traffickingCrimeNoZerosRFTunedCmCleaned

# %%
# 120 rows × 93 columns

        # Format for readability
traffickingCrimeNoZerosRFTunedCmReadable = traffickingCrimeNoZerosRFTunedCmCleaned.style\
    .background_gradient(cmap = 'viridis')\
    .set_properties(**{'font-size': '12pt'})

traffickingCrimeNoZerosRFTunedCmReadable

# %%
# A lot to read...


    # Classification report
print(classification_report(yNoZerosTest, traffickingCrimeNoZerosRFtunedPredictions))

# %%
#     accuracy                           0.42       195
#    macro avg       0.26      0.30      0.27       195
# weighted avg       0.40      0.42      0.40       195
    # Not too shabby!
    

    # Find feature importance for hypertuned model
traffickingCrimeNoZerosFeatImp = pd.Series(
    traffickingCrimeNoZerosRFtuned.feature_importances_, index = x.columns)
traffickingCrimeNoZerosFeatImp = traffickingCrimeNoZerosFeatImp.sort_values(
    ascending = False)

traffickingCrimeNoZerosFeatImp.plot(kind = 'barh', figsize = (10, 5))

# %%
# Predictors have changed - DUI is still strongly the highest, followed closely
    # by embesslement, then stolen property and down from there

# %%

# Summary: Non-trafficking crime arrests are able to predict when there will be 
# zero trafficking crime arrests with 59% accuracy, and are able to predict 
# when there will be trafficking crime arrests with 42% accuracy. In both cases
# DUI arrests is the strongest predictor.