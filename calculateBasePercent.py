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

a18to29 = 60.43956044
a30to44 = 55.43478261
a45to64 = 45.83333333
a65plus = 46.39175258
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
        sum = 0
        sum += whitecollege * json_object['race']['whitecollege'] / json_object['race']['Population']
        sum += whitenon * json_object['race']['whiteNonCollege'] / json_object['race']['Population']
        sum += black * json_object['race']['Non-HispanicBlack'] / json_object['race']['Population']
        sum += hispanic * json_object['race']['Hispanic'] / json_object['race']['Population']
        sum += asian * json_object['race']['Non-HispanicAsian'] / json_object['race']['Population']
        sum += other * json_object['race']['Non-HispanicIndian'] / json_object['race']['Population']
        print(state,sum)

    #print(states)

with open('states.csv', newline='') as csvfile:
    states = csv.reader(csvfile, delimiter=',', quotechar='|')
    age1 = 67.74193548
    age2 = 63.04347826
    age3 = 60.21505376
    age4 = 54.25531915
    age5 = 51.57894737
    age6 = 49.48453608
    print("Age")
    for state in states:
        state = state[0]
        a_file = open("data/"+state+"/stats.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        sum = 0


        #print(state)
        pop = json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total'] - json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Under 18 years']
        #print(pop)
        sum += age1 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; 18 to 64 years - 18 to 24 years'] / pop
        sum += age2 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 25 to 29 years'] / pop
        sum += age3 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 30 to 34 years'] / pop
        sum += age3 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 35 to 39 years'] / pop
        sum += age4 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 40 to 44 years'] / pop
        sum += age4 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 45 to 49 years'] / pop
        sum += age5 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 50 to 54 years'] / pop
        sum += age5 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 55 to 59 years'] / pop
        sum += age5 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 60 to 64 years'] / pop
        sum += age6 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 65 to 69 years'] / pop
        sum += age6 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 70 to 74 years'] / pop
        sum += age6 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 75 to 79 years'] / pop
        sum += age6 * json_object['ageSex2018']['Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 80 to 84 years'] / pop
        sum += age6 * json_object['ageSex2018']["Population Estimate (as of July 1) - 2018 - Both Sexes; Total - 85 years and over"] / pop
        print(state,sum)
