# %%
# DSO110 - Data Science Final Project
    # File 3
    # Parse and combine trafficking crime text files for all years (2013- 2021)

# Import packages
import csv
import pandas as pd

# %%

# Create parser and run it on text file for 2013 trafficking crime data, to 
    # convert to a csv and export it

    # Create a variable of column names (to be used for all years' data)
columnNames = ['IdentifierCode', 'NumericStateCode', 'ORICode', 'Group', 
               'Division', 'Year', 'SequenceNumber', 'CoreCity', 'CoveredBy', 
               'CoveredByGroup', 'FieldOffice', 'NumberOfMonthsReported', 
               'AgencyCount', 'Population', 'AgencyName', 'AgencyStateName', 
               'January', 'February', 'March', 'April', 'May', 'June', 'July', 
               'August', 'September', 'October', 'November', 'December','JanuaryOffensesReportedorKnownCommercialSexActs',
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

columnNames

# %%
# Success

    # Prep csv read/ writer to work with the 2013 text file and create a new 
        # 2013 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2013.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2013.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2013 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2013 csv file
    traffickingCrimes_2013.writerow(columnNames)

    # Parse each line in the 2013 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2013 data to the new 2013 csv file
        traffickingCrimes_2013.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2013

# %%
# Success

# Import the new 2013 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2013R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2013.csv')

traffickingCrimes_2013R

# %%
# 22202 rows × 208 columns
    # These data are much longer than the allCrime data, per the locations 
        # being tracked much more incrementally, but I can group by the states
    # There are a lot of columns I won't need, but trafficking crimes (
        # commercial sex acts, involuntary servitude, and totals) are each 
        # included for minors, and totals, all by month


# Create parser and run it on text file for 2014 trafficking crime data, to 
    # convert to a csv and export it

    # Prep csv read/ writer to work with the 2014 text file and create a new 
        # 2014 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2014.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2014.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2014 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2014 csv file
    traffickingCrimes_2014.writerow(columnNames)

    # Parse each line in the 2014 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2014 data to the new 2014 csv file
        traffickingCrimes_2014.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2014

# %%
# Success

# Import the new 2014 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2014R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2014.csv')

traffickingCrimes_2014R

# %%
# 22332 rows × 208 columns

# Create parser and run it on text file for 2015 trafficking crime data, to 
    # convert to a csv and export it

    # Prep csv read/ writer to work with the 2015 text file and create a new 
        # 2015 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2015.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2015.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2015 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2015 csv file
    traffickingCrimes_2015.writerow(columnNames)

    # Parse each line in the 2015 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2015 data to the new 2015 csv file
        traffickingCrimes_2015.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2015

# %%
# Success

# Import the new 2015 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2015R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2015.csv')

traffickingCrimes_2015R

# %%
# 22524 rows × 208 columns

# Create parser and run it on text file for 2016 trafficking crime data, to 
    # convert to a csv and export it

    # Prep csv read/ writer to work with the 2016 text file and create a new 
        # 2016 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2016.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2016.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2016 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2016 csv file
    traffickingCrimes_2016.writerow(columnNames)

    # Parse each line in the 2016 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2016 data to the new 2016 csv file
        traffickingCrimes_2016.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2016

# %%
# Success

# Import the new 2016 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2016R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2016.csv')

traffickingCrimes_2016R

# %%
# 22519 rows × 208 columns

# Create parser and run it on text file for 2017 trafficking crime data, to 
    # convert to a csv and export it

    # Prep csv read/ writer to work with the 2017 text file and create a new 
        # 2017 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2017.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2017.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2017 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2017 csv file
    traffickingCrimes_2017.writerow(columnNames)

    # Parse each line in the 2017 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2017 data to the new 2017 csv file
        traffickingCrimes_2017.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2017

# %%
# Success

# Import the new 2017 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2017R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2017.csv')

traffickingCrimes_2017R

# %%
# 24362 rows × 208 columns

# Create parser and run it on text file for 2018 trafficking crime data, to 
    # convert to a csv and export it

    # Prep csv read/ writer to work with the 2018 text file and create a new 
        # 2018 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2018.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2018.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2018 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2018 csv file
    traffickingCrimes_2018.writerow(columnNames)

    # Parse each line in the 2018 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2018 data to the new 2018 csv file
        traffickingCrimes_2018.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2018

# %%
# Success

# Import the new 2018 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2018R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2018.csv')

traffickingCrimes_2018R

# %%
# 24372 rows × 208 columns

# Create parser and run it on text file for 2019 trafficking crime data, to 
    # convert to a csv and export it

    # Prep csv read/ writer to work with the 2019 text file and create a new 
        # 2019 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2019.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2019.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2019 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2019 csv file
    traffickingCrimes_2019.writerow(columnNames)

    # Parse each line in the 2019 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2019 data to the new 2019 csv file
        traffickingCrimes_2019.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2019

# %%
# Success

# Import the new 2019 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2019R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2019.csv')

traffickingCrimes_2019R

# %%
# 24428 rows × 208 columns

# Create parser and run it on text file for 2020 trafficking crime data, to 
    # convert to a csv and export it

    # Prep csv read/ writer to work with the 2020 text file and create a new 
        # 2020 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2020.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2020.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2020 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2020 csv file
    traffickingCrimes_2020.writerow(columnNames)

    # Parse each line in the 2020 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2020 data to the new 2020 csv file
        traffickingCrimes_2020.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2020

# %%
# Success

# Import the new 2020 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2020R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2020.csv')

traffickingCrimes_2020R

# %%
# 24620 rows × 208 columns

# Create parser and run it on text file for 2021 trafficking crime data, to 
    # convert to a csv and export it

    # Prep csv read/ writer to work with the 2021 text file and create a new 
        # 2021 csv file
with open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2021.txt',
           'r') as fileInput, open('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2021.csv',
                                    'w', newline = '') as fileOutput:
    traffickingCrimes_2021 = csv.writer(fileOutput)

    # Write the column names as the first row of the new 2021 csv file
    traffickingCrimes_2021.writerow(columnNames)

    # Parse each line in the 2021 text file
    for line in fileInput:
        IdentifierCode = line[0:1]
        NumericStateCode = line[1:3]
        ORICode = line[3:10]
        Group = line[10:12]
        Division = line[12:13]
        Year = line[13:15]
        SequenceNumber = line[15:20]
        CoreCity = line[20:21]
        CoveredBy = line[21:28]
        CoveredByGroup = line[28:29]
        FieldOffice = line[29:33]
        NumberOfMonthsReported = line[33:35]
        AgencyCount = line[35:36]
        Population = line[36:45]
        AgencyName = line[45:69]
        AgencyStateName = line[69:75]
        January = line[75:76]
        February = line[76:77]
        March = line[77:78]
        April = line[78:79]
        May = line[79:80]
        June = line[80:81]
        July = line[81:82]
        August = line[82:83]
        September = line[83:84]
        October = line[84:85]
        November = line[85:86]
        December = line[86:87]
        JanuaryOffensesReportedorKnownCommercialSexActs = line[87:92]
        JanuaryOffensesReportedorKnownInvoluntaryServitude = line[92:97]
        JanuaryOffensesReportedorKnownGrandTotal = line[97:102]
        JanuaryUnfoundedCommercialSexActs = line[102:107]
        JanuaryUnfoundedInvoluntaryServitude = line[107:112]
        JanuaryUnfoundedGrandTotal = line[112:117]
        JanuaryNumberOfActualOffensesCommercialSexActs = line[117:122]
        JanuaryNumberOfActualOffensesInvoluntaryServitude = line[122:127]
        JanuaryNumberOfActualOffensesGrandTotal = line[127:132]
        JanuaryTotalOffensesClearedCommercialSexActs = line[132:137]
        JanuaryTotalOffensesClearedInvoluntaryServitude = line[137:142]
        JanuaryTotalOffensesClearedGrandTotal = line[142:147]
        JanuaryNumberOfClearancesUnder18CommercialSexActs = line[147:152]
        JanuaryNumberOfClearancesUnder18InvoluntaryServitude = line[152:157]
        JanuaryNumberOfClearancesUnder18GrandTotal = line[157:162]
        FebruaryOffensesReportedorKnownCommercialSexActs = line[162:167]
        FebruaryOffensesReportedorKnownInvoluntaryServitude = line[167:172]
        FebruaryOffensesReportedorKnownGrandTotal = line[172:177]
        FebruaryUnfoundedCommercialSexActs = line[177:182]
        FebruaryUnfoundedInvoluntaryServitude = line[182:187]
        FebruaryUnfoundedGrandTotal = line[187:192]
        FebruaryNumberOfActualOffensesCommercialSexActs = line[192:197]
        FebruaryNumberOfActualOffensesInvoluntaryServitude = line[197:202]
        FebruaryNumberOfActualOffensesGrandTotal = line[202:208]
        FebruaryTotalOffensesClearedCommercialSexActs = line[208:212]
        FebruaryTotalOffensesClearedInvoluntaryServitude = line[212:217]
        FebruaryTotalOffensesClearedGrandTotal = line[217:222]
        FebruaryNumberOfClearancesUnder18CommercialSexActs = line[222:227]
        FebruaryNumberOfClearancesUnder18InvoluntaryServitude = line[227:232]
        FebruaryNumberOfClearancesUnder18GrandTotal = line[232:237]
        MarchOffensesReportedorKnownCommercialSexActs = line[237:242]
        MarchOffensesReportedorKnownInvoluntaryServitude = line[242:247]
        MarchOffensesReportedorKnownGrandTotal = line[247:252]
        MarchUnfoundedCommercialSexActs = line[252:257]
        MarchUnfoundedInvoluntaryServitude = line[257:262]
        MarchUnfoundedGrandTotal = line[262:267]
        MarchNumberOfActualOffensesCommercialSexActs = line[267:272]
        MarchNumberOfActualOffensesInvoluntaryServitude = line[272:277]
        MarchNumberOfActualOffensesGrandTotal = line[277:282]
        MarchTotalOffensesClearedCommercialSexActs = line[282:287]
        MarchTotalOffensesClearedInvoluntaryServitude = line[287:292]
        MarchTotalOffensesClearedGrandTotal = line[292:297]
        MarchNumberOfClearancesUnder18CommercialSexActs = line[297:302]
        MarchNumberOfClearancesUnder18InvoluntaryServitude = line[302:307]
        MarchNumberOfClearancesUnder18GrandTotal = line[307:312]
        AprilOffensesReportedorKnownCommercialSexActs = line[312:317]
        AprilOffensesReportedorKnownInvoluntaryServitude = line[317:322]
        AprilOffensesReportedorKnownGrandTotal = line[322:327]
        AprilUnfoundedCommercialSexActs = line[327:332]
        AprilUnfoundedInvoluntaryServitude = line[332:337]
        AprilUnfoundedGrandTotal = line[337:342]
        AprilNumberOfActualOffensesCommercialSexActs = line[342:347]
        AprilNumberOfActualOffensesInvoluntaryServitude = line[347:352]
        AprilNumberOfActualOffensesGrandTotal = line[352:357]
        AprilTotalOffensesClearedCommercialSexActs = line[357:362]
        AprilTotalOffensesClearedInvoluntaryServitude = line[362:367]
        AprilTotalOffensesClearedGrandTotal = line[367:372]
        AprilNumberOfClearancesUnder18CommercialSexActs = line[372:377]
        AprilNumberOfClearancesUnder18InvoluntaryServitude = line[377:382]
        AprilNumberOfClearancesUnder18GrandTotal = line[382:387]
        MayOffensesReportedorKnownCommercialSexActs = line[387:392]
        MayOffensesReportedorKnownInvoluntaryServitude = line[392:397]
        MayOffensesReportedorKnownGrandTotal = line[397:402]
        MayUnfoundedCommercialSexActs = line[402:407]
        MayUnfoundedInvoluntaryServitude = line[407:412]
        MayUnfoundedGrandTotal = line[412:417]
        MayNumberOfActualOffensesCommercialSexActs = line[417:422]
        MayNumberOfActualOffensesInvoluntaryServitude = line[422:427]
        MayNumberOfActualOffensesGrandTotal = line[427:432]
        MayTotalOffensesClearedCommercialSexActs = line[432:437]
        MayTotalOffensesClearedInvoluntaryServitude = line[437:442]
        MayTotalOffensesClearedGrandTotal = line[442:447]
        MayNumberOfClearancesUnder18CommercialSexActs = line[447:452]
        MayNumberOfClearancesUnder18InvoluntaryServitude = line[452:457]
        MayNumberOfClearancesUnder18GrandTotal = line[457:462]
        JuneOffensesReportedorKnownCommercialSexActs = line[462:467]
        JuneOffensesReportedorKnownInvoluntaryServitude = line[467:472]
        JuneOffensesReportedorKnownGrandTotal = line[472:477]
        JuneUnfoundedCommercialSexActs = line[477:482]
        JuneUnfoundedInvoluntaryServitude = line[482:487]
        JuneUnfoundedGrandTotal = line[487:492]
        JuneNumberOfActualOffensesCommercialSexActs = line[492:497]
        JuneNumberOfActualOffensesInvoluntaryServitude = line[497:502]
        JuneNumberOfActualOffensesGrandTotal = line[502:507]
        JuneTotalOffensesClearedCommercialSexActs = line[507:512]
        JuneTotalOffensesClearedInvoluntaryServitude = line[512:517]
        JuneTotalOffensesClearedGrandTotal = line[517:522]
        JuneNumberOfClearancesUnder18CommercialSexActs = line[522:527]
        JuneNumberOfClearancesUnder18InvoluntaryServitude = line[527:532]
        JuneNumberOfClearancesUnder18GrandTotal = line[532:537]
        JulyOffensesReportedorKnownCommercialSexActs = line[537:542]
        JulyOffensesReportedorKnownInvoluntaryServitude = line[542:547]
        JulyOffensesReportedorKnownGrandTotal = line[547:552]
        JulyUnfoundedCommercialSexActs = line[552:557]
        JulyUnfoundedInvoluntaryServitude = line[557:562]
        JulyUnfoundedGrandTotal = line[562:567]
        JulyNumberOfActualOffensesCommercialSexActs = line[567:572]
        JulyNumberOfActualOffensesInvoluntaryServitude = line[572:577]
        JulyNumberOfActualOffensesGrandTotal = line[577:582]
        JulyTotalOffensesClearedCommercialSexActs = line[582:587]
        JulyTotalOffensesClearedInvoluntaryServitude = line[587:592]
        JulyTotalOffensesClearedGrandTotal = line[592:597]
        JulyNumberOfClearancesUnder18CommercialSexActs = line[597:602]
        JulyNumberOfClearancesUnder18InvoluntaryServitude = line[602:607]
        JulyNumberOfClearancesUnder18GrandTotal = line[607:612]
        AugustOffensesReportedorKnownCommercialSexActs = line[612:617]
        AugustOffensesReportedorKnownInvoluntaryServitude = line[617:622]
        AugustOffensesReportedorKnownGrandTotal = line[622:627]
        AugustUnfoundedCommercialSexActs = line[627:632]
        AugustUnfoundedInvoluntaryServitude = line[632:637]
        AugustUnfoundedGrandTotal = line[637:642]
        AugustNumberOfActualOffensesCommercialSexActs = line[642:647]
        AugustNumberOfActualOffensesInvoluntaryServitude = line[647:652]
        AugustNumberOfActualOffensesGrandTotal = line[652:657]
        AugustTotalOffensesClearedCommercialSexActs = line[657:662]
        AugustTotalOffensesClearedInvoluntaryServitude = line[662:667]
        AugustTotalOffensesClearedGrandTotal = line[667:672]
        AugustNumberOfClearancesUnder18CommercialSexActs = line[672:677]
        AugustNumberOfClearancesUnder18InvoluntaryServitude = line[677:682]
        AugustNumberOfClearancesUnder18GrandTotal = line[682:687]
        SeptemberOffensesReportedorKnownCommercialSexActs = line[687:692]
        SeptemberOffensesReportedorKnownInvoluntaryServitude = line[692:697]
        SeptemberOffensesReportedorKnownGrandTotal = line[697:702]
        SeptemberUnfoundedCommercialSexActs = line[702:707]
        SeptemberUnfoundedInvoluntaryServitude = line[707:712]
        SeptemberUnfoundedGrandTotal = line[712:717]
        SeptemberNumberOfActualOffensesCommercialSexActs = line[717:722]
        SeptemberNumberOfActualOffensesInvoluntaryServitude = line[722:727]
        SeptemberNumberOfActualOffensesGrandTotal = line[727:732]
        SeptemberTotalOffensesClearedCommercialSexActs = line[732:737]
        SeptemberTotalOffensesClearedInvoluntaryServitude = line[737:742]
        SeptemberTotalOffensesClearedGrandTotal = line[742:747]
        SeptemberNumberOfClearancesUnder18CommercialSexActs = line[747:752]
        SeptemberNumberOfClearancesUnder18InvoluntaryServitude = line[752:757]
        SeptemberNumberOfClearancesUnder18GrandTotal = line[757:762]
        OctoberOffensesReportedorKnownCommercialSexActs = line[762:767]
        OctoberOffensesReportedorKnownInvoluntaryServitude = line[767:772]
        OctoberOffensesReportedorKnownGrandTotal = line[772:777]
        OctoberUnfoundedCommercialSexActs = line[777:782]
        OctoberUnfoundedInvoluntaryServitude = line[782:787]
        OctoberUnfoundedGrandTotal = line[787:792]
        OctoberNumberOfActualOffensesCommercialSexActs = line[792:797]
        OctoberNumberOfActualOffensesInvoluntaryServitude = line[797:802]
        OctoberNumberOfActualOffensesGrandTotal = line[802:807]
        OctoberTotalOffensesClearedCommercialSexActs = line[807:812]
        OctoberTotalOffensesClearedInvoluntaryServitude = line[812:817]
        OctoberTotalOffensesClearedGrandTotal = line[817:822]
        OctoberNumberOfClearancesUnder18CommercialSexActs = line[822:827]
        OctoberNumberOfClearancesUnder18InvoluntaryServitude = line[827:832]
        OctoberNumberOfClearancesUnder18GrandTotal = line[832:837]
        NovemberOffensesReportedorKnownCommercialSexActs = line[837:842]
        NovemberOffensesReportedorKnownInvoluntaryServitude = line[842:847]
        NovemberOffensesReportedorKnownGrandTotal = line[847:852]
        NovemberUnfoundedCommercialSexActs = line[852:857]
        NovemberUnfoundedInvoluntaryServitude = line[857:862]
        NovemberUnfoundedGrandTotal = line[862:867]
        NovemberNumberOfActualOffensesCommercialSexActs = line[867:872]
        NovemberNumberOfActualOffensesInvoluntaryServitude = line[872:877]
        NovemberNumberOfActualOffensesGrandTotal = line[877:882]
        NovemberTotalOffensesClearedCommercialSexActs = line[882:887]
        NovemberTotalOffensesClearedInvoluntaryServitude = line[887:892]
        NovemberTotalOffensesClearedGrandTotal = line[892:897]
        NovemberNumberOfClearancesUnder18CommercialSexActs = line[897:902]
        NovemberNumberOfClearancesUnder18InvoluntaryServitude = line[902:907]
        NovemberNumberOfClearancesUnder18GrandTotal = line[907:912]
        DecemberOffensesReportedorKnownCommercialSexActs = line[912:917]
        DecemberOffensesReportedorKnownInvoluntaryServitude = line[917:922]
        DecemberOffensesReportedorKnownGrandTotal = line[922:927]
        DecemberUnfoundedCommercialSexActs = line[927:932]
        DecemberUnfoundedInvoluntaryServitude = line[932:937]
        DecemberUnfoundedGrandTotal = line[937:942]
        DecemberNumberOfActualOffensesCommercialSexActs = line[942:947]
        DecemberNumberOfActualOffensesInvoluntaryServitude = line[947:952]
        DecemberNumberOfActualOffensesGrandTotal = line[952:957]
        DecemberTotalOffensesClearedCommercialSexActs = line[957:962]
        DecemberTotalOffensesClearedInvoluntaryServitude = line[962:967]
        DecemberTotalOffensesClearedGrandTotal = line[967:972]
        DecemberNumberOfClearancesUnder18CommercialSexActs = line[972:977]
        DecemberNumberOfClearancesUnder18InvoluntaryServitude = line[977:982]
        DecemberNumberOfClearancesUnder18GrandTotal = line[982:987]

        # Write the parsed 2021 data to the new 2021 csv file
        traffickingCrimes_2021.writerow(
            [IdentifierCode, NumericStateCode, ORICode, Group, Division, Year,
             SequenceNumber, CoreCity, CoveredBy, CoveredByGroup, FieldOffice, 
             NumberOfMonthsReported, AgencyCount, Population, AgencyName, 
             AgencyStateName, January, February, March, April, May, June, July, 
             August, September, October, November, December, 
             JanuaryOffensesReportedorKnownCommercialSexActs,
             JanuaryOffensesReportedorKnownInvoluntaryServitude,
             JanuaryOffensesReportedorKnownGrandTotal,
             JanuaryUnfoundedCommercialSexActs,
             JanuaryUnfoundedInvoluntaryServitude,
             JanuaryUnfoundedGrandTotal,
             JanuaryNumberOfActualOffensesCommercialSexActs,
             JanuaryNumberOfActualOffensesInvoluntaryServitude,
             JanuaryNumberOfActualOffensesGrandTotal,
             JanuaryTotalOffensesClearedCommercialSexActs,
             JanuaryTotalOffensesClearedInvoluntaryServitude,
             JanuaryTotalOffensesClearedGrandTotal,
             JanuaryNumberOfClearancesUnder18CommercialSexActs,
             JanuaryNumberOfClearancesUnder18InvoluntaryServitude,
             JanuaryNumberOfClearancesUnder18GrandTotal,
             FebruaryOffensesReportedorKnownCommercialSexActs,
             FebruaryOffensesReportedorKnownInvoluntaryServitude,
             FebruaryOffensesReportedorKnownGrandTotal,
             FebruaryUnfoundedCommercialSexActs,
             FebruaryUnfoundedInvoluntaryServitude,
             FebruaryUnfoundedGrandTotal,
             FebruaryNumberOfActualOffensesCommercialSexActs,
             FebruaryNumberOfActualOffensesInvoluntaryServitude,
             FebruaryNumberOfActualOffensesGrandTotal,
             FebruaryTotalOffensesClearedCommercialSexActs,
             FebruaryTotalOffensesClearedInvoluntaryServitude,
             FebruaryTotalOffensesClearedGrandTotal,
             FebruaryNumberOfClearancesUnder18CommercialSexActs,
             FebruaryNumberOfClearancesUnder18InvoluntaryServitude,
             FebruaryNumberOfClearancesUnder18GrandTotal,
             MarchOffensesReportedorKnownCommercialSexActs,
             MarchOffensesReportedorKnownInvoluntaryServitude,
             MarchOffensesReportedorKnownGrandTotal,
             MarchUnfoundedCommercialSexActs,
             MarchUnfoundedInvoluntaryServitude,
             MarchUnfoundedGrandTotal,
             MarchNumberOfActualOffensesCommercialSexActs,
             MarchNumberOfActualOffensesInvoluntaryServitude,
             MarchNumberOfActualOffensesGrandTotal,
             MarchTotalOffensesClearedCommercialSexActs,
             MarchTotalOffensesClearedInvoluntaryServitude,
             MarchTotalOffensesClearedGrandTotal,
             MarchNumberOfClearancesUnder18CommercialSexActs,
             MarchNumberOfClearancesUnder18InvoluntaryServitude,
             MarchNumberOfClearancesUnder18GrandTotal,
             AprilOffensesReportedorKnownCommercialSexActs,
             AprilOffensesReportedorKnownInvoluntaryServitude,
             AprilOffensesReportedorKnownGrandTotal,
             AprilUnfoundedCommercialSexActs,
             AprilUnfoundedInvoluntaryServitude,
             AprilUnfoundedGrandTotal,
             AprilNumberOfActualOffensesCommercialSexActs,
             AprilNumberOfActualOffensesInvoluntaryServitude,
             AprilNumberOfActualOffensesGrandTotal,
             AprilTotalOffensesClearedCommercialSexActs,
             AprilTotalOffensesClearedInvoluntaryServitude,
             AprilTotalOffensesClearedGrandTotal,
             AprilNumberOfClearancesUnder18CommercialSexActs,
             AprilNumberOfClearancesUnder18InvoluntaryServitude,
             AprilNumberOfClearancesUnder18GrandTotal,
             MayOffensesReportedorKnownCommercialSexActs,
             MayOffensesReportedorKnownInvoluntaryServitude,
             MayOffensesReportedorKnownGrandTotal,
             MayUnfoundedCommercialSexActs,
             MayUnfoundedInvoluntaryServitude,
             MayUnfoundedGrandTotal,
             MayNumberOfActualOffensesCommercialSexActs,
             MayNumberOfActualOffensesInvoluntaryServitude,
             MayNumberOfActualOffensesGrandTotal,
             MayTotalOffensesClearedCommercialSexActs,
             MayTotalOffensesClearedInvoluntaryServitude,
             MayTotalOffensesClearedGrandTotal,
             MayNumberOfClearancesUnder18CommercialSexActs,
             MayNumberOfClearancesUnder18InvoluntaryServitude,
             MayNumberOfClearancesUnder18GrandTotal,
             JuneOffensesReportedorKnownCommercialSexActs,
             JuneOffensesReportedorKnownInvoluntaryServitude,
             JuneOffensesReportedorKnownGrandTotal,
             JuneUnfoundedCommercialSexActs,
             JuneUnfoundedInvoluntaryServitude,
             JuneUnfoundedGrandTotal,
             JuneNumberOfActualOffensesCommercialSexActs,
             JuneNumberOfActualOffensesInvoluntaryServitude,
             JuneNumberOfActualOffensesGrandTotal,
             JuneTotalOffensesClearedCommercialSexActs,
             JuneTotalOffensesClearedInvoluntaryServitude,
             JuneTotalOffensesClearedGrandTotal,
             JuneNumberOfClearancesUnder18CommercialSexActs,
             JuneNumberOfClearancesUnder18InvoluntaryServitude,
             JuneNumberOfClearancesUnder18GrandTotal,
             JulyOffensesReportedorKnownCommercialSexActs,
             JulyOffensesReportedorKnownInvoluntaryServitude,
             JulyOffensesReportedorKnownGrandTotal,
             JulyUnfoundedCommercialSexActs,
             JulyUnfoundedInvoluntaryServitude,
             JulyUnfoundedGrandTotal,
             JulyNumberOfActualOffensesCommercialSexActs,
             JulyNumberOfActualOffensesInvoluntaryServitude,
             JulyNumberOfActualOffensesGrandTotal,
             JulyTotalOffensesClearedCommercialSexActs,
             JulyTotalOffensesClearedInvoluntaryServitude,
             JulyTotalOffensesClearedGrandTotal,
             JulyNumberOfClearancesUnder18CommercialSexActs,
             JulyNumberOfClearancesUnder18InvoluntaryServitude,
             JulyNumberOfClearancesUnder18GrandTotal,
             AugustOffensesReportedorKnownCommercialSexActs,
             AugustOffensesReportedorKnownInvoluntaryServitude,
             AugustOffensesReportedorKnownGrandTotal,
             AugustUnfoundedCommercialSexActs,
             AugustUnfoundedInvoluntaryServitude,
             AugustUnfoundedGrandTotal,
             AugustNumberOfActualOffensesCommercialSexActs,
             AugustNumberOfActualOffensesInvoluntaryServitude,
             AugustNumberOfActualOffensesGrandTotal,
             AugustTotalOffensesClearedCommercialSexActs,
             AugustTotalOffensesClearedInvoluntaryServitude,
             AugustTotalOffensesClearedGrandTotal,
             AugustNumberOfClearancesUnder18CommercialSexActs,
             AugustNumberOfClearancesUnder18InvoluntaryServitude,
             AugustNumberOfClearancesUnder18GrandTotal,
             SeptemberOffensesReportedorKnownCommercialSexActs,
             SeptemberOffensesReportedorKnownInvoluntaryServitude,
             SeptemberOffensesReportedorKnownGrandTotal,
             SeptemberUnfoundedCommercialSexActs,
             SeptemberUnfoundedInvoluntaryServitude,
             SeptemberUnfoundedGrandTotal,
             SeptemberNumberOfActualOffensesCommercialSexActs,
             SeptemberNumberOfActualOffensesInvoluntaryServitude,
             SeptemberNumberOfActualOffensesGrandTotal,
             SeptemberTotalOffensesClearedCommercialSexActs,
             SeptemberTotalOffensesClearedInvoluntaryServitude,
             SeptemberTotalOffensesClearedGrandTotal,
             SeptemberNumberOfClearancesUnder18CommercialSexActs,
             SeptemberNumberOfClearancesUnder18InvoluntaryServitude,
             SeptemberNumberOfClearancesUnder18GrandTotal,
             OctoberOffensesReportedorKnownCommercialSexActs,
             OctoberOffensesReportedorKnownInvoluntaryServitude,
             OctoberOffensesReportedorKnownGrandTotal,
             OctoberUnfoundedCommercialSexActs,
             OctoberUnfoundedInvoluntaryServitude,
             OctoberUnfoundedGrandTotal,
             OctoberNumberOfActualOffensesCommercialSexActs,
             OctoberNumberOfActualOffensesInvoluntaryServitude,
             OctoberNumberOfActualOffensesGrandTotal,
             OctoberTotalOffensesClearedCommercialSexActs,
             OctoberTotalOffensesClearedInvoluntaryServitude,
             OctoberTotalOffensesClearedGrandTotal,
             OctoberNumberOfClearancesUnder18CommercialSexActs,
             OctoberNumberOfClearancesUnder18InvoluntaryServitude,
             OctoberNumberOfClearancesUnder18GrandTotal,
             NovemberOffensesReportedorKnownCommercialSexActs,
             NovemberOffensesReportedorKnownInvoluntaryServitude,
             NovemberOffensesReportedorKnownGrandTotal,
             NovemberUnfoundedCommercialSexActs,
             NovemberUnfoundedInvoluntaryServitude,
             NovemberUnfoundedGrandTotal,
             NovemberNumberOfActualOffensesCommercialSexActs,
             NovemberNumberOfActualOffensesInvoluntaryServitude,
             NovemberNumberOfActualOffensesGrandTotal,
             NovemberTotalOffensesClearedCommercialSexActs,
             NovemberTotalOffensesClearedInvoluntaryServitude,
             NovemberTotalOffensesClearedGrandTotal,
             NovemberNumberOfClearancesUnder18CommercialSexActs,
             NovemberNumberOfClearancesUnder18InvoluntaryServitude,
             NovemberNumberOfClearancesUnder18GrandTotal,
             DecemberOffensesReportedorKnownCommercialSexActs,
             DecemberOffensesReportedorKnownInvoluntaryServitude,
             DecemberOffensesReportedorKnownGrandTotal,
             DecemberUnfoundedCommercialSexActs,
             DecemberUnfoundedInvoluntaryServitude,
             DecemberUnfoundedGrandTotal,
             DecemberNumberOfActualOffensesCommercialSexActs,
             DecemberNumberOfActualOffensesInvoluntaryServitude,
             DecemberNumberOfActualOffensesGrandTotal,
             DecemberTotalOffensesClearedCommercialSexActs,
             DecemberTotalOffensesClearedInvoluntaryServitude,
             DecemberTotalOffensesClearedGrandTotal,
             DecemberNumberOfClearancesUnder18CommercialSexActs,
             DecemberNumberOfClearancesUnder18InvoluntaryServitude,
             DecemberNumberOfClearancesUnder18GrandTotal])

traffickingCrimes_2021

# %%
# Success

# Import the new 2021 csv and preview it

    # Enable viewing all columns in output
pd.options.display.max_columns = 425

    # Import and call new table
traffickingCrimes_2021R = pd.read_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2021.csv')

traffickingCrimes_2021R

# %%
# 22240 rows × 208 columns

# Join all years' tables
traffickingCrimes_2013to2021 = pd.concat(
    [traffickingCrimes_2013R, traffickingCrimes_2014R, 
     traffickingCrimes_2015R, traffickingCrimes_2016R, 
     traffickingCrimes_2017R, traffickingCrimes_2018R, 
     traffickingCrimes_2019R, traffickingCrimes_2020R, 
     traffickingCrimes_2021R], axis = 0, ignore_index = True)

traffickingCrimes_2013to2021

# %%
# 209599 rows × 208 columns

    # Export file to csv
traffickingCrimes_2013to2021.to_csv('/Users/hannah/Library/CloudStorage/GoogleDrive-gracesnouveaux@gmail.com/My Drive/Bethel Tech/Data Science/DSO110 Final {Group} Project/HB_DSO110_Data/Crime/Unused trafficking crime data/traffickingCrimes_2013to2021.csv')

# %%
# Success
