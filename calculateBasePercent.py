import csv
import json
import pandas as pd
import sys

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

men = 44.08602151
women = 56.84210526

whitecollege = 53.81310419
whitenon = 33.58129649
black = 91.31334023
hispanic = 69.43556976
asian = 70.65217391
other = 60.86956522

turnoutwhitecollege = 57.30
turnoutwhitenon = 79.50
turnoutblack = 57.70
turnoutlatino = 46.10
turnoutother = 49.00





a18to29 = 60.43956044
a30to44 = 55.43478261
a45to64 = 45.83333333
a65plus = 46.39175258

totwc = 0
totwn = 0
totb = 0
toth = 0
toto = 0
with open('states.csv', newline='') as csvfile:
    states = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    s = 0

    count = 0
    print("Race")
    for state in states:
        state = state[0]
        a_file = open("data/"+state+"/stats.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        otherPop = json_object['race']['Total Population: Not Hispanic or Latino: Native Hawaiian and Other Pacific Islander Alone']
        otherPop += json_object['race']['Total Population: Not Hispanic or Latino: Some Other Race Alone']
        otherPop += json_object['race']['Total Population: Not Hispanic or Latino: American Indian and Alaska Native Alone']
        otherPop += json_object['race']['Total Population: Not Hispanic or Latino: Two or More Races']

        turnout = 0
        wcturnout = turnoutwhitecollege * json_object['race']['whitecollege']
        wnturnout = turnoutwhitenon * json_object['race']['whiteNonCollege']
        bturnout = turnoutblack * json_object['race']['Total Population: Not Hispanic or Latino: Black or African American Alone']
        lturnout = turnoutlatino * json_object['race']['Total Population: Hispanic or Latino']
        aturnout = turnoutother * json_object['race']['Total Population: Not Hispanic or Latino: Asian Alone']
        oturnout = turnoutother * (otherPop)

        totwc+= json_object['race']['whitecollege']
        totwn+= json_object['race']['whiteNonCollege']
        totb += json_object['race']['Total Population: Not Hispanic or Latino: Black or African American Alone']
        toth += json_object['race']['Total Population: Hispanic or Latino']
        toto +=  (otherPop) + json_object['race']['Total Population: Not Hispanic or Latino: Asian Alone']

        turnout += wcturnout + wnturnout + bturnout + lturnout + oturnout + aturnout


        sum = 0
        sum += whitecollege * wcturnout / turnout
        sum += whitenon * wnturnout / turnout
        sum += black * bturnout / turnout
        sum += hispanic * lturnout / turnout
        sum += asian * aturnout / turnout
        sum += other * oturnout  / turnout



        print(state,sum)
#
with open('states.csv', newline='') as csvfile:
    states = csv.reader(csvfile, delimiter=',', quotechar='|')
    age1 = 67.74193548
    age2 = 63.04347826
    age3 = 60.21505376
    age4 = 54.25531915
    age5 = 51.57894737
    age6 = 49.48453608

    turnoutage1829 = 46.1
    turnoutage3044 = 58.7
    turnoutage4564 = 66.6
    turnout65more = 70.9

    print("Age")
    for state in states:
        state = state[0]
        a_file = open("data/"+state+"/stats.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        sum = 0

        turnout = 0
        turnout += turnoutage1829 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; 18 to 64 years - 18 to 24 years']
        turnout += turnoutage1829 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 25 to 29 years']
        turnout += turnoutage3044 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 30 to 34 years']
        turnout += turnoutage3044 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 35 to 39 years']
        turnout += turnoutage3044 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 40 to 44 years']
        turnout += turnoutage4564 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 45 to 49 years']
        turnout += turnoutage4564 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 50 to 54 years']
        turnout += turnoutage4564 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 55 to 59 years']
        turnout += turnoutage4564 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 60 to 64 years']
        turnout += turnout65more * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 65 to 69 years']
        turnout += turnout65more * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 70 to 74 years']
        turnout += turnout65more * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 75 to 79 years']
        turnout += turnout65more * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 80 to 84 years']
        turnout += turnout65more * json_object['ageSex2018']["Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 85 years and over"]

        #print(state)
        #print(pop)
        sum += age1 * turnoutage1829 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; 18 to 64 years - 18 to 24 years'] / turnout
        sum += age2 * turnoutage1829 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 25 to 29 years'] / turnout
        sum += age3 * turnoutage3044 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 30 to 34 years'] / turnout
        sum += age3 * turnoutage3044 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 35 to 39 years'] / turnout
        sum += age4 * turnoutage3044 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 40 to 44 years'] / turnout
        sum += age4 * turnoutage4564 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 45 to 49 years'] / turnout
        sum += age5 * turnoutage4564 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 50 to 54 years'] / turnout
        sum += age5 * turnoutage4564 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 55 to 59 years'] / turnout
        sum += age5 * turnoutage4564 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 60 to 64 years'] / turnout
        sum += age6 * turnout65more * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 65 to 69 years'] / turnout
        sum += age6 * turnout65more * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 70 to 74 years'] / turnout
        sum += age6 * turnout65more * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 75 to 79 years'] / turnout
        sum += age6 * turnout65more * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 80 to 84 years'] / turnout
        sum += age6 * turnout65more * json_object['ageSex2018']["Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 85 years and over"] / turnout
        print(state,sum)
