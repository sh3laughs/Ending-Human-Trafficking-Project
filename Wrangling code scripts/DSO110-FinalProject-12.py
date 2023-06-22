# %%
# DSO110 - Data Science Final Project
    # File 12
    # Wrangling: Survey responses


# Import packages
import pandas as pd

# %%

# Import data

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import data
survey = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/Human Trafficking Awareness (Responses) - Form Responses.csv')

survey

# %%
# 161 rows × 19 columns


# Update columns

    # Confirm column names
survey.columns

# %%
# 'Timestamp', 'What is your age?', 'What is your gender?',
# 'Where were you born?', 'Where do you currently live?',
# 'What province do you live in?', 'Which state do you live in?',
# 'How would you define human trafficking?',
# 'How many people are in slavery globally every year?',
# 'What percentage of reported victims of slavery are minors / children?',
# 'What percentage of reported victims are forced into sexual slavery / 
    # trafficking?',
# 'Which region has the highest prevalence of reported victims?',
# 'Which type of slavery has the most reported victims?',
# 'Who are most often the traffickers?',
# 'Do you personally know any survivors of human trafficking?',
# 'Please rate the likelihood that there are active trafficking operations in 
    #  the area you live in',
# 'Are you actively engaged in fighting human trafficking?',
# 'Are you interested in opportunities to fight human trafficking?',
# 'Any other thoughts you would like to share?'


    # Drop timestamp column
surveyR = survey.drop(columns = ['Timestamp'])

surveyR

# %%
# 161 rows × 18 columns


    # Rename columns
surveyR.rename(columns = {
    'What is your age?': 'Age', 
    'What is your gender?': 'Gender', 
    'Where were you born?': 'Birthplace', 
    'Where do you currently live?': 'Location', 
    'What province do you live in?': 'Province', 
    'Which state do you live in?': 'State', 
    'How would you define human trafficking?': 'Definition', 
    'How many people are in slavery globally every year?': 'QuantityTrafficked', 
    'What percentage of reported victims of slavery are minors / children?': 
    'PercentChildren', 
    'What percentage of reported victims are forced into sexual slavery / trafficking?':
    'PercentSexual', 
    'Which region has the highest prevalence of reported victims?': 'Region', 
    'Which type of slavery has the most reported victims?': 'Type', 
    'Who are most often the traffickers?': 'Perpetrators', 
    'Do you personally know any survivors of human trafficking?': 
    'KnowSurvivors', 
    'Please rate the likelihood that there are active trafficking operations in the area you live in':
    'LocalTrafficking', 
    'Are you actively engaged in fighting human trafficking?': 'Involvement', 
    'Are you interested in opportunities to fight human trafficking?': 
    'Interest', 
    'Any other thoughts you would like to share?': 'Thoughts'}, inplace = True)

surveyR

# %%
# Visually confirmed success


# Export to csv
surveyR.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/SurveyResponses.csv')

# %%


# Subset to have separate tables for those who are and are not currently
    # involved in fighting trafficking

    # Currently involved
surveyInvolved = surveyR[surveyR['Involvement'] == 'Yes']

surveyInvolved

# %%
# 59 rows × 18 columns

    # Not currently involved
surveyNotInvolved = surveyR[surveyR['Involvement'] == 'No']

surveyNotInvolved

# %%
# 102 rows × 18 columns

    # Export subsetted data to csv

        # Currently involved
surveyInvolved.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/SurveyInvolved.csv')

# %%

        # Not currently involved
surveyNotInvolved.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/SurveyNotInvolved.csv')

# %%
