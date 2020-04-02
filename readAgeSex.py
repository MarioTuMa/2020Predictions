import csv
import json
import pandas as pd
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
import pandas as pd

f=pd.read_csv("ageSex.csv")
l = f.columns.tolist()
keep_col = []
keep_col.append("Geography")
for col in l:
    if("2018" in col):
        keep_col.append(col)

new_f = f[keep_col]
new_f.to_csv("ageSex.csv", index=False)

with open('ageSex.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    s = 0


    for row in spamreader:
        if(count == 0):
            s = row
            print(s)
            print(len(s))
            count+=1
        else:
            print(len(row))
            print(row)
            print(row[0])
            row[0] = row[0].replace(" ","")
            print(row[0])
            a_file = open("data/"+row[0]+"/stats.json", "r")
            json_object = json.load(a_file)
            json_object['ageSex']=[]
            a_file.close()
            for i in range(len(s)):
                newobj = {}
                if(RepresentsInt(row[i])):
                    newobj[s[i]]=int(row[i])
                else:
                    newobj[s[i]]=row[i]
                json_object['ageSex'].append(newobj)

            a_file = open("data/"+row[0]+"/stats.json", "w")
            json.dump(json_object, a_file)
            a_file.close()