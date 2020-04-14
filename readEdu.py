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
import pandas as pd

name = "White alone!!Bachelor's degree or higher"
f=pd.read_csv("edu.csv")
l = f.columns.tolist()
keep_col = []
keep_col.append("Geographic Area Name")
for col in l:
    #print(col)
    if(name in col) and not ("ale" in col) and not ("Error" in col) and not ("ercent") in col:
        keep_col.append(col)
new_f = f[keep_col]
new_f.to_csv("whiteedu.csv", index=False)

with open('whiteedu.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    s = 0

    count = 0
    print(new_f)
    for row in spamreader:

        if(count == 0):
            s = row
            #print(s)
            #print(len(s))
            count+=1
        else:
            # print(len(row))
            row[0] = row[0].replace(" ","")
            print(row)
            # #print(row)
            #
            a_file = open("data/"+row[0]+"/stats.json", "r")
            json_object = json.load(a_file)
            #
            # tempdata = {}
            a_file.close()
            json_object['race']['whitecollege'] = int(row[1])
            json_object['race']['whiteNonCollege'] = json_object['race']['Total Population: Not Hispanic or Latino: White Alone'] - int(row[1])
            # for i in range(len(s)):
            #     if(RepresentsInt(row[i])):
            #         row[i]=int(row[i])
            #         #print(s[i])
            #         tempdata[s[i]]=row[i]
            # json_object['ageSex'+n]=tempdata
            a_file = open("data/"+row[0]+"/stats.json", "w")
            json.dump(json_object, a_file)
            a_file.close()