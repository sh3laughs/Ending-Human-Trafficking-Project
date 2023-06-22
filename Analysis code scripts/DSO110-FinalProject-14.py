# %%
# DSO110 - Data Science Final Project
    # File 14
    # Analysis: Natural language processing

# Goal: Determine which definition keywords are common in individuals’ 
    # definitions of human trafficking

# Import packages
import matplotlib.pyplot as plt
import nltk
import pandas as pd
import seaborn as sns
from nltk.tokenize import RegexpTokenizer

# %%

# Import data

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import data

        # All responses
with open(
    '/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/Definitions from survey (all).txt',
      'r') as file:
    definition = file.read()

definition

# %%
# Success

        # Currently involved
with open(
    '/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/Definitions from survey (yes).txt',
      'r') as file:
    definitionInvolved = file.read()

definitionInvolved

# %%
# Success

       # Not currently involved
with open(
    '/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/Definitions from survey (no).txt',
      'r') as file:
    definitionNotInvolved = file.read()

definitionNotInvolved

# %%
# Success


# Convert to individual words

    # All responses
definitionSplitWords = RegexpTokenizer('\w+')
definitionWords = definitionSplitWords.tokenize(definition)

definitionWords[:5]

# %%
# ['Activities', 'that', 'involve', 'using', 'other']
    # Success!

    # Currently involved
defInvolvedSplitWords = RegexpTokenizer('\w+')
defInvolvedWords = definitionSplitWords.tokenize(definitionInvolved)

defInvolvedWords[:5]

# %%
# ['I', 'believe', 'human', 'trafficking', 'can']

    # Not crrently involved
defNotInvolvedSplitWords = RegexpTokenizer('\w+')
defNotInvolvedWords = definitionSplitWords.tokenize(definitionNotInvolved)

defNotInvolvedWords[:5]

# %%
# ['Activities', 'that', 'involve', 'using', 'other']


# Update all words to be lowercase

    # All responses
definitionWordsR = []

for word in definitionWords:
    definitionWordsR.append(word.lower())

definitionWordsR[:5]

# %%
# ['activities', 'that', 'involve', 'using', 'other']
    # Success

    # Currently involved
defInvolvedWordsR = []

for word in defInvolvedWords:
    defInvolvedWordsR.append(word.lower())

defInvolvedWordsR[:5]

# %%
# ['i', 'believe', 'human', 'trafficking', 'can']

    # Not currently involved
defNotInvolvedWordsR = []

for word in defNotInvolvedWords:
    defNotInvolvedWordsR.append(word.lower())

defNotInvolvedWordsR[:5]

# %%
# ['activities', 'that', 'involve', 'using', 'other']


# Remove stop words

    # Create list of stop words
nltk.download('stopwords')

definitionStopwords = nltk.corpus.stopwords.words('english')

definitionStopwords[:5]

# %%
# ['i', 'me', 'my', 'myself', 'we']

    # Create new definition variables without stopwords

        # All responses
definitionWordsNoStop = []

for word in definitionWordsR:
    if word not in definitionStopwords:
        definitionWordsNoStop.append(word)

definitionWordsNoStop[:5]

# %%
# ['activities', 'involve', 'using', 'humans', 'financial']
    # Love that this is getting interesting!

        # Currently involved
defInvolvedWordsNoStop = []

for word in defInvolvedWordsR:
    if word not in definitionStopwords:
        defInvolvedWordsNoStop.append(word)

defInvolvedWordsNoStop[:5]

# %%
# ['believe', 'human', 'trafficking', 'broadly', 'defined']

        # Not currently involved
defNotInvolvedWordsNoStop = []

for word in defNotInvolvedWordsR:
    if word not in definitionStopwords:
        defNotInvolvedWordsNoStop.append(word)

defNotInvolvedWordsNoStop[:5]

# %%
# ['activities', 'involve', 'using', 'humans', 'financial']


# Preview top 25 words

    # All responses - plotted
sns.set()
definitionWordsNoStopFreq = nltk.FreqDist(definitionWordsNoStop)
definitionWordsNoStopFreq.plot(25)

# %%
# Super interesting!
    # I'd like to consolidate people, human, humans, person
    # Ditto coercion and coercing, forced and force, etc.
    # Great to see some key words from the legal definition - ie: coercion, 
    # force, fraud, and exploitation

    # All responses - ranked and printed
definitionWordsNoStopFreqRanked = definitionWordsNoStopFreq.most_common(25)

for word, frequency in definitionWordsNoStopFreqRanked:
    print(word, frequency)

# %%
# people 44
# labor 41
# sex 41
# sexual 34
# exploitation 30
# forced 28
# slavery 28
# human 28
# coercion 27
# humans 26
# force 22
# selling 21
# person 20
# illegal 16
# gain 16
# trafficking 16
# fraud 16
# use 15
# kidnapping 13
# work 12
# someone 12
# money 11
# purposes 11
# commercial 11
# using 10


    # Currently involved - plotted
sns.set()
defInvolvedWordsNoStopFreq = nltk.FreqDist(defInvolvedWordsNoStop)
defInvolvedWordsNoStopFreq.plot(25)

# %%
# Also interesting - makes sense that the words from legal definition show up 
    # in this list

    # Currently involved - ranked and printed
defInvolvedWordsNoStopFreqRanked = defInvolvedWordsNoStopFreq.most_common(25)

for word, frequency in defInvolvedWordsNoStopFreqRanked:
    print(word, frequency)

# %%
# labor 26
# sex 24
# coercion 21
# force 19
# sexual 17
# exploitation 17
# forced 16
# fraud 16
# human 15
# trafficking 15
# person 15
# commercial 11
# gain 9
# purpose 9
# use 9
# people 8
# slavery 8
# selling 7
# act 7
# someone 6
# etc 5
# acts 5
# trading 5
# humans 5
# benefit 5


    # Not currently involved - plotted
sns.set()
defNotInvolvedWordsNoStopFreq = nltk.FreqDist(defNotInvolvedWordsNoStop)
defNotInvolvedWordsNoStopFreq.plot(25)

# %%
# Makes sense that "kidnapping" is only common with people not yet involved
    # in the fight

    # Not currently involved - ranked and printed
defNotInvolvedWordsNoStopFreqRanked = defNotInvolvedWordsNoStopFreq.most_common(
    25)

for word, frequency in defNotInvolvedWordsNoStopFreqRanked:
    print(word, frequency)

# %%
# people 36
# humans 21
# slavery 20
# sexual 17
# sex 17
# labor 15
# selling 14
# exploitation 13
# human 13
# forced 12
# illegal 12
# kidnapping 11
# work 9
# money 8
# purposes 8
# using 7
# gain 7
# taken 7
# another 7
# use 6
# coercion 6
# form 6
# profit 6
# someone 6
# abuse 6


# Create a dataframe with all words, not just top 25

    # All words from all responses
definitionWordsFrequency = nltk.FreqDist(definitionWordsR)
definitionWordsFreq = definitionWordsFrequency.most_common()

definitionWordsFreqDups = pd.DataFrame(
    definitionWordsFreq, columns = ['Word', 'Frequency'])

definitionWordsFreqDups['Words'] = 'Stopword'
definitionWordsFreqDups['Respondents'] = 'Everyone'
definitionWordsFreqDups['Shared'] = 'Unique'

defInvolvedWordSet = set(defInvolvedWordsR)
defNotInvolvedWordSet = set(defNotInvolvedWordsR)

defWordsShared = defInvolvedWordSet.intersection(defNotInvolvedWordSet)
defInvolvedWordsUnique = defInvolvedWordSet.difference(defNotInvolvedWordSet)

for i, row in definitionWordsFreqDups.iterrows():
    word = row['Word']
    if word in defWordsShared:
        definitionWordsFreqDups.at[i, 'Shared'] = 'Common'

definitionWordsFreqDups

# %%
# 538 rows × 5 columns


    # Identify the words that are not Stopwords
for i, row in definitionWordsFreqDups.iterrows():
    word = row['Word']
    if word in definitionWordsNoStop:
        definitionWordsFreqDups.at[i, 'Words'] = 'Significant'

definitionWordsFreqDups

# %%
# Visualy confirmed success


    # Identify words from people currently involved in the fight
for i, row in definitionWordsFreqDups.iterrows():
    word = row['Word']
    shared_value = row['Shared']
    
    if shared_value == 'Unique' and word in defInvolvedWordsR:
        definitionWordsFreqDups.at[i, 'Respondents'] = 'Currently Involved'

definitionWordsFreqDups

# %%
# Visualy confirmed success


    # Identify words from people not currently involved in the fight
for i, row in definitionWordsFreqDups.iterrows():
    word = row['Word']
    shared_value = row['Shared']
    
    if shared_value == 'Unique' and word in defNotInvolvedWordsR:
        definitionWordsFreqDups.at[
            i, 'Respondents'] = 'Not Currently Involved'

definitionWordsFreqDups

# %%
# Visualy confirmed success


# Export to csv
definitionWordsFreqDups.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/Definition Words With Duplicates.csv')

# %%

# Deduplicate

    # Create deduplication dictionary
deduplicate = {
    'abducting': 'abduction',
    'abusive': 'abuse',
    'abused': 'abuse',
    'abusing': 'abuse',
    'acts': 'act',
    'actions': 'act',
    'action': 'act',
    'activity': 'activities',
    'adult': 'adults',
    'assaulted': 'assault',
    'believing': 'believe',
    'benefits': 'benefit',
    'buying': 'bought',
    'child': 'children',
    'coercing': 'coercion',
    'coerced': 'coercion',
    'coerces': 'coercion',
    'compelling': 'compelled',
    'define': 'definition',
    'defined': 'definition',
    'drug': 'drugs',
    'drugged': 'drugs',
    'drugging': 'drugs',
    'examples': 'example',
    'exploiting': 'exploitation',
    'exploited': 'exploitation',
    'financially': 'financial',
    'force': 'forced',
    'forcing': 'forced',
    'forcefully': 'forced',
    'forces': 'forced',
    'forcible': 'forced',
    'forcibly': 'forced',
    'forms': 'form',
    'freely': 'free',
    'gaining': 'gain',
    'given': 'give',
    'illegally': 'illegal',
    'immigration': 'immigrant',
    'include': 'including',
    'individuals': 'individual',
    'inhuman': 'inhumane',
    'involved': 'involves',
    'involve': 'involves',
    'involvement': 'involves',
    'kidnap': 'kidnapping',
    'kidnapped': 'kidnapping',
    'knowingly': 'knowing',
    'later': 'late',
    'legally': 'legal',
    'lives': 'live',
    'lots': 'lot',
    'make': 'making',
    'makes': 'making',
    'manipulation': 'manipulated',
    'moved': 'moving',
    'move': 'moving',
    'moves': 'moving',
    'movements': 'movement',
    'obtaining': 'obtain',
    'organs': 'organ',
    'organized': 'organizations',
    'pays': 'pay',
    'human': 'people',
    'humans': 'people',
    'person': 'people',
    'beings': 'people',
    'persons': 'people',
    'places': 'place',
    'prisoners': 'prisoner',
    'products': 'product',
    'profiting': 'profit',
    'prostituted': 'prostitution',
    'providing': 'provide',
    'purposes': 'purpose',
    'recruiting': 'recruitment',
    'said': 'say',
    'sold': 'selling',
    'sell': 'selling',
    'service': 'services',
    'sexual': 'sex',
    'sexually': 'sex',
    'slave': 'slavery',
    'enslavement': 'slavery',
    'slaves': 'slavery',
    'enslave': 'slavery',
    'enslaved': 'slavery',
    'enslaver': 'slavery',
    'survive': 'survival',
    'survivor': 'survival',
    'survivors': 'survival',
    'taking': 'taken',
    'take': 'taken',
    'threats': 'threatened',
    'trade': 'trading',
    'traded': 'trading',
    'traffickers': 'trafficking',
    'traffic': 'trafficking',
    'trafficker': 'trafficking',
    'transporting': 'transportation',
    'transport': 'transportation',
    'transported': 'transportation',
    'sent': 'transportation',
    'trapped': 'trap',
    'treating': 'treated',
    'treatment': 'treated',
    'tricking': 'tricked',
    'using': 'use',
    'used': 'use',
    'uses': 'use',
    'victim': 'victims',
    'victimization': 'victims',
    'victimize': 'victims',
    'vulnerabilities': 'vulnerable',
    'working': 'work',
    'year': 'years'}

deduplicate

# %%
# Success

    # Use the dictionary to replace values in the dataframe
definitionWordsFreqExport = definitionWordsFreqDups.copy()

definitionWordsFreqExport['Word'].replace(deduplicate, inplace = True)

definitionWordsFreqExport

# %%
# 538 rows × 5 columns

for word in definitionWordsFreqExport['Word'].unique():
    indices = definitionWordsFreqExport[definitionWordsFreqExport['Word'] == word].index
    if len(indices) > 1:
        definitionWordsFreqExport.loc[indices, 'Shared'] = 'Common'
        definitionWordsFreqExport.loc[indices, 'Respondents'] = 'Everyone'

definitionWordsFreqExport = definitionWordsFreqExport.groupby(
    'Word', as_index = False).agg({
    'Frequency': 'sum',
    'Words': 'first',
    'Respondents': 'first',
    'Shared': 'first'}).reset_index(drop = True)

definitionWordsFreqExport

# %%
# 422 rows × 5 columns


# Export to csv
definitionWordsFreqExport.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/Definition Words.csv')

# %%


# Preview top 25 words

    # All responses
defWordsAllTop25Plot = definitionWordsFreqExport[
    (definitionWordsFreqExport['Words'] == 'Significant')].nlargest(
        25, 'Frequency')

plt.figure(figsize = (10, 6))
plt.bar(defWordsAllTop25Plot['Word'], defWordsAllTop25Plot['Frequency'])
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Top 25 Words by Frequency')
plt.xticks(rotation = 90)
plt.show()

# %%
# This is helpful - the top seven words now are people, sex, forced, slavery, 
    # labor, exploitation, and coercion


    # Common words
defWordsCommonTop25Plot = definitionWordsFreqExport[
    (definitionWordsFreqExport['Words'] == 'Significant') &
    (definitionWordsFreqExport['Shared'] == 'Common')].nlargest(25, 'Frequency')

plt.figure(figsize = (10, 6))
plt.bar(defWordsCommonTop25Plot['Word'], defWordsCommonTop25Plot['Frequency'])
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Top 25 Words by Frequency')
plt.xticks(rotation = 90)
plt.show()

# %%
# Only slightly different to list above - services shows up, which is interesting


    # Currently involved - unique
defWordsCommonTop25Plot = definitionWordsFreqExport[
    (definitionWordsFreqExport['Words'] == 'Significant') &
    (definitionWordsFreqExport['Respondents'] == 'Currently Involved')
    ].nlargest(25, 'Frequency')

plt.figure(figsize = (10, 6))
plt.bar(defWordsCommonTop25Plot['Word'], defWordsCommonTop25Plot['Frequency'])
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Top 25 Words by Frequency')
plt.xticks(rotation = 90)
plt.show()

# %%
# Top words are fraud, commercial, 18, engage, and harboring


    # Not currently involved - unique
defWordsCommonTop25Plot = definitionWordsFreqExport[
    (definitionWordsFreqExport['Words'] == 'Significant') &
    (definitionWordsFreqExport['Respondents'] == 'Not Currently Involved')
    ].nlargest(25, 'Frequency')

plt.figure(figsize = (10, 6))
plt.bar(defWordsCommonTop25Plot['Word'], defWordsCommonTop25Plot['Frequency'])
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Top 25 Words by Frequency')
plt.xticks(rotation = 90)
plt.show()

# %%
# Top words are country, across, borders - which is interesting per people not
    # currently involved in the fight thinking more about people being 
    # transported as part of the trafficking


# How many unique words for...

    # All responses
definitionWordsFreqExport['Word'].value_counts()

# %%
# 422 words

    # In common
definitionWordsFreqExport['Shared'].value_counts()['Common']

# %%
# 164 words

    # Unique to those currently involved in the fight
definitionWordsFreqExport['Respondents'].value_counts()['Currently Involved']

# %%
# 126 words

    # Unique to those currently involved in the fight
definitionWordsFreqExport['Respondents'].value_counts()[
    'Not Currently Involved']

# %%
# 132 words