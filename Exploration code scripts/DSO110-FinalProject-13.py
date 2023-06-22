# %%
# DSO110 - Data Science Final Project
    # File 13
    # Exploration: Survey responses


# Import packages
import pandas as pd

# %%

# Import data

    # Enable viewing all columns in output
pd.options.display.max_columns = 425
pd.options.display.max_rows = 25

# %%

    # Import data

        # All responses
survey = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/SurveyResponses.csv')

survey

# %%
# 161 rows × 19 columns

            # Remove duplicate index column
survey.drop(['Unnamed: 0'], axis = 1, inplace = True)

survey

# %%
# 161 rows × 18 columns

        # Currently involved
surveyInvolved = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/SurveyInvolved.csv')

surveyInvolved

# %%
# 59 rows × 19 columns

            # Remove duplicate index column
surveyInvolved.drop(['Unnamed: 0'], axis = 1, inplace = True)

surveyInvolved

# %%
# 59 rows × 18 columns

        # Not currently involved
surveyNotInvolved = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Survey/SurveyNotInvolved.csv')

surveyNotInvolved

# %%
# 102 rows × 19 columns

            # Remove duplicate index column
surveyNotInvolved.drop(['Unnamed: 0'], axis = 1, inplace = True)

surveyNotInvolved

# %%
# 102 rows × 18 columns


# Confirm value counts

    # Age

        # All responses
survey.Age.value_counts()

# %%
# 21-29            52
# 40-49            34
# 30-39            30
# 50-59            24
# 60 or older      15
# 18-20             4
# 17 or younger     2

        # Currently involved
surveyInvolved.Age.value_counts()

# %%
# 40-49          17
# 50-59          11
# 21-29          11
# 30-39          11
# 60 or older     8
# 18-20           1

        # Not currently involved
surveyNotInvolved.Age.value_counts()

# %%
# 21-29            41
# 30-39            19
# 40-49            17
# 50-59            13
# 60 or older       7
# 18-20             3
# 17 or younger     2


    # Gender

        # All responses
survey.Gender.value_counts()

# %%
# Female   119
# Male      42

        # Currently involved
surveyInvolved.Gender.value_counts()

# %%
# Female    51
# Male       8

        # Not currently involved
surveyNotInvolved.Gender.value_counts()

# %%
# Female    68
# Male      34


    # Birthplace

        # All responses
survey.Birthplace.value_counts()

# %%
# USA              77
# Europe           42
# Canada           25
# Asia             11
# Africa            5
# South America     1

        # Currently involved
surveyInvolved.Birthplace.value_counts()

# %%
# USA       44
# Canada     9
# Europe     4
# Asia       2

        # Not currently involved
surveyNotInvolved.Birthplace.value_counts()

# %%    
# Europe           38
# USA              33
# Canada           16
# Asia              9
# Africa            5
# South America     1


    # Location

        # All responses
survey.Location.value_counts()

# %%
# USA       85
# Europe    47
# Canada    23
# Asia       4
# Africa     1
# Australia  1

        # Currently involved
surveyInvolved.Location.value_counts()

# %%
# USA       46
# Canada     9
# Europe     4

        # Not currently involved
surveyNotInvolved.Location.value_counts()

# %%
# Europe    43
# USA       39
# Canada    14
# Asia       4
# Africa     1
# Australia  1


    # Province

        # All responses
survey.Province.value_counts()

# %%
# Manitoba                 12
# Ontario                   4
# British Columbia          3
# Prince Edward Island      2
# Northwest Territories     1
# Alberta                   1

        # Currently involved
surveyInvolved.Province.value_counts()

# %%
# Manitoba                5
# Prince Edward Island    1
# Ontario                 1
# Alberta                 1
# British Columbia        1

        # Not currently involved
surveyNotInvolved.Province.value_counts()

# %%
# Manitoba                 7
# British Columbia         3
# Ontario                  2
# Prince Edward Island     1
# Northwest Territories    1


    # State

        # All responses
survey.State.value_counts()

# %%
# California	       16
# Washington	        7
# Texas	                6
# Florida	        5
# Oregon	        4
# Georgia	        4
# Tennessee	        4
# Oklahoma	        3
# Ohio	                3
# North Carolina	3
# New York	        3
# Colorado	        3
# Arizona	        3
# Washington DC	        2
# South Carolina	2
# Michigan	        2
# Iowa	                2
# Alaska	        2
# Pennsylvania	        1
# Missouri	        1
# Mississippi	        1
# Minnesota	        1
# Louisiana	        1
# Kentucky              1
# Kansas	        1
# Idaho	                1
# Connecticut	        1
# Alabama	        1
# Virginia              1

        # Currently involved
surveyInvolved.State.value_counts()

# %%
# California        9
# Texas             4
# Florida           3
# Washington        3
# Georgia           3
# Washington DC     2
# Iowa              2
# Oregon            2
# Arizona           2
# Ohio              2
# Oklahoma          2
# Michigan          2
# Alabama           1
# Kansas            1
# Colorado          1
# North Carolina    1
# Louisiana         1
# Pennsylvania      1
# Minnesota         1
# South Carolina    1
# Tennessee         1

        # Not currently involved
surveyNotInvolved.State.value_counts()

# %%
# California        7
# Washington        4
# New York          3
# Tennessee         3
# Colorado          2
# Alaska            2
# Oregon            2
# Texas             2
# Florida           2
# North Carolina    2
# Georgia           1
# Missouri          1
# Idaho             1
# Oklahoma          1
# Arizona           1
# South Carolina    1
# Connecticut       1
# Mississippi       1
# Ohio              1
# Kentucky          1
# Virginia          1


    # QuantityTrafficked

        # All responses
survey.QuantityTrafficked.value_counts()

# %%
# No one actually knows   103
# 50 million               33
# 5 million                21
# 500,000                   4

        # Currently involved
surveyInvolved.QuantityTrafficked.value_counts()

# %%
# No one actually knows    40
# 50 million               14
# 5 million                 4
# 500,000                   1

        # Not currently involved
surveyNotInvolved.QuantityTrafficked.value_counts()

# %%
# No one actually knows    63
# 50 million               19
# 5 million                17
# 500,000                   3


    # PercentChildren

        # All responses
survey.PercentChildren.value_counts()

# %%
# 64%    89
# 24%    68
# 4%      4

        # Currently involved
surveyInvolved.PercentChildren.value_counts()

# %%
# 24%    31
# 64%    26
# 4%      2

        # Not currently involved
surveyNotInvolved.PercentChildren.value_counts()

# %%
# 64%    63
# 24%    37
# 4%      2


    # PercentSexual

        # All responses
survey.PercentSexual.value_counts()

# %%
# 87%   101
# 57%    56
# 7%      4

        # Currently involved
surveyInvolved.PercentSexual.value_counts()

# %%
# 87%    36
# 57%    21
# 7%      2

        # Not currently involved
surveyNotInvolved.PercentSexual.value_counts()

# %%
# 87%    65
# 57%    35
# 7%      2


    # Region

        # All responses
survey.Region.value_counts()

# %%
# Asia and the Pacific       53
# Americas                   42
# Africa                     34
# Europe and Central Asia    21
# Arab States                11

        # Currently involved
surveyInvolved.Region.value_counts()

# %%
# Asia and the Pacific       23
# Americas                   20
# Europe and Central Asia     7
# Arab States                 5
# Africa                      4

        # Not currently involved
surveyNotInvolved.Region.value_counts()

# %%
# Asia and the Pacific       30
# Africa                     29
# Americas                   22
# Europe and Central Asia    14
# Arab States                 7


    # Type

        # All responses
survey.Type.value_counts()

# %%
# Commercial sexual exploitation   102
# Forced labor                      51
# Forced marriage                    8

        # Currently involved
surveyInvolved.Type.value_counts()

# %%
# Commercial sexual exploitation    33
# Forced labor                      24
# Forced marriage                    2

        # Not currently involved
surveyNotInvolved.Type.value_counts()

# %%
# Commercial sexual exploitation    69
# Forced labor                      27
# Forced marriage                    6


    # Perpetrators

        # All responses
survey.Perpetrators.value_counts()

# %%
# Family 71
# Kidnappers / strangers 37
# Family, Kidnappers / strangers 13
# Family, Foster system, Kidnappers / strangers 13
# Family, Foster system 5
# Foster system, Kidnappers / strangers 5
# Foster system 3
# Family, Foster system, Friends/Acquintances 1
# Family, Known to the victim 1
# family, trusted friend, or someone who gains their trust 1
# Family, Master manipulators/opportunists 1
# Intimate Partner 1
# Family, Foster system, Kidnappers / strangers, Governments 1
# Kidnappers / strangers, Due to the previous Q, it’s both forced labor and 
        # marriage 1
# All the above 1
# Family, Foster system, Kidnappers / strangers, 1
# Foster system, Kidnappers / strangers, Mafia 1
# known perpetrator but not necessarily family 1
# Foster system, Kidnappers / strangers, Global élites: very wealthy, very 
        # powerful, and "above the law". 1
# Kidnappers / strangers, 1 percent, people of any kind of power, government, 
        # wealthy, greedy mean people. Drug dealers! 1
# someone who builds trust/a relationship with the victim 1

        # Currently involved
surveyInvolved.Perpetrators.value_counts()

# %%
# Family 34
# Kidnappers / strangers 7
# Family, Foster system, Kidnappers / strangers 4
# Family, Kidnappers / strangers 2
# Kidnappers / strangers, 1 percent, people of any kind of power, government, 
    # wealthy, greedy mean people. Drug dealers! 1
# Family, Foster system, Kidnappers / strangers, 1
# Family, Foster system 1
# All the above 1
# Family, Foster system, Friends/Acquintances 1
# Family, Foster system, Kidnappers / strangers, Governments 1
# Intimate Partner 1
# Family, Master manipulators/opportunists 1
# family, trusted friend, or someone who gains their trust 1
# Family, Known to the victim 1
# someone who builds trust/a relationship with the victim 1
# Foster system, Kidnappers / strangers 1

        # Not currently involved
surveyNotInvolved.Perpetrators.value_counts()

# %%
# Family 37
# Kidnappers / strangers 30
# Family, Kidnappers / strangers 11
# Family, Foster system, Kidnappers / strangers 9
# Foster system, Kidnappers / strangers 4
# Family, Foster system 4
# Foster system 3
# Foster system, Kidnappers / strangers, Global élites: very wealthy, very 
    # powerful, and "above the law". 1
# known perpetrator but not necessarily family 1
# Kidnappers / strangers, Due to the previous Q, it’s both forced labor and 
    # marriage 1
# Foster system, Kidnappers / strangers, Mafia 1


    # KnowSurvivors

        # All responses
survey.KnowSurvivors.value_counts()

# %%
# No     98
# Yes    63

        # Currently involved
surveyInvolved.KnowSurvivors.value_counts()

# %%
# Yes    50
# No      9

        # Not currently involved
surveyNotInvolved.KnowSurvivors.value_counts()

# %%
# No     89
# Yes    13

    # LocalTrafficking

        # All responses
survey.LocalTrafficking.value_counts()

# %%
# 1    63
# 5    35
# 2    26
# 3    20
# 4    17

        # Currently involved
surveyInvolved.LocalTrafficking.value_counts()

# %%
# 1    40
# 5    13
# 2     3
# 3     2
# 4     1

        # Not currently involved
surveyNotInvolved.LocalTrafficking.value_counts()

# %%
# 1    23
# 2    23
# 5    22
# 3    18
# 4    16


    # Involvement

        # All responses
survey.Involvement.value_counts()

# %%
# No    102
# Yes    59


    # Interest

        # All responses
survey.Interest.value_counts()

# %%
# Yes 102
# No 42
# Maybe 2
# Not right now 1
# It is very important but cannot personally engage 1
# Already in it 1
# I believe it is only God that will be able to truly correct the issues that 
        # plague mankind today.  He will not put up with the current conditions 
        # indefinitely. 1
# Currently engaged on the front lines in the anti-trafficking movement in the U.
        # S. 1
# Already actively engaged in the fight 1
# I already work in an RTC for adolescent female survivors of trafficking 1
# We are in this together ! 1
# maybe 1
# . 1
# Have sympathy, but am too far removed from it to do anything directly. 1
# Not at this time 1
# I have already worked for 8 years fighting Human Trafficking and now retired 1
# I wouldnt know where to start  1

        # Currently involved
surveyInvolved.Interest.value_counts()

# %%
# Yes 36
# No 16
# Not at this time 1
# . 1
# I already work in an RTC for adolescent female survivors of trafficking 1
# We are in this together ! 1
# Already actively engaged in the fight 1
# Currently engaged on the front lines in the anti-trafficking movement in the 
    # U.S. 1
# Already in it 1

        # Not currently involved
surveyNotInvolved.Interest.value_counts()

# %%
# Yes 66
# No 26
# Maybe 2
# I have already worked for 8 years fighting Human Trafficking and now retired 1
# Have sympathy, but am too far removed from it to do anything directly. 1
# maybe 1
# Not right now 1
# I believe it is only God that will be able to truly correct the issues that 
    # plague mankind today.  He will not put up with the current conditions 
    # indefinitely. 1
# It is very important but cannot personally engage 1
# I wouldnt know where to start 1