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
    #print(col)
    if("2012" in col):
        keep_col.append(col)
new_f = f[keep_col]
new_f.to_csv("ageSex2012.csv", index=False)

with open('ageSex2012.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    s = 0

    count = 0
    print(new_f)
    for row in spamreader:
        print(row)
        if(count == 0):
            s = row
            #print(s)
            #print(len(s))
            count+=1
        else:
            print(len(row))
            row[0] = row[0].replace(" ","")
            print(row)
            #print(row)

            a_file = open("data/"+row[0]+"/stats.json", "r")
            json_object = json.load(a_file)

            tempdata = {}
            a_file.close()
            for i in range(len(s)):
                if(RepresentsInt(row[i])):
                    row[i]=int(row[i])
                    #print(s[i])
                    tempdata[s[i]]=row[i]
            json_object['ageSex2012']=tempdata
            a_file = open("data/"+row[0]+"/stats.json", "w")
            json.dump(json_object, a_file)
            a_file.close()