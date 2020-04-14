import pandas as pd
import csv
import json
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

f=pd.read_csv("R12502239_SL040_2018.csv")
l = f.columns.tolist()
keep_col = []
keep_col.append("Name of Area")
for col in l:
    #print(col)
    if("Total Population" in col and not "Years" in col):
        keep_col.append(col)
new_f = f[keep_col]
new_f.to_csv("race.csv", index=False)

with open('race.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    s = 0
    for row in spamreader:
        if(count < 1 or "uerto" in row[0]):
            s = row
            print(s)
            count+=1
        else:
            print(row)
            row[0] = row[0].replace(" ","")

            a_file = open("data/"+row[0]+"/stats.json", "w")
            a_file.write("{}")
            a_file.close()
            a_file = open("data/"+row[0]+"/stats.json", "r")
            json_object = json.load(a_file)
            temp = {}
            a_file.close()
            for i in range(len(s)):
                newobj = {}
                if(RepresentsInt(row[i])):
                    temp[s[i]]=int(row[i])
                else:
                    temp[s[i]]=row[i]

            json_object['race']=temp
            a_file = open("data/"+row[0]+"/stats.json", "w")
            json.dump(json_object, a_file)
            a_file.close()