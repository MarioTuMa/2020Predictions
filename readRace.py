import csv
import json
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
with open('race.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    s = 0
    for row in spamreader:
        if(count == 0):
            s = row
            print(s)
            count+=1
        else:
            print(row)
            a_file = open("data/"+row[0]+"/stats.json", "w")
            a_file.write("{}")
            a_file.close()
            a_file = open("data/"+row[0]+"/stats.json", "r")
            json_object = json.load(a_file)
            json_object['race']=[]
            a_file.close()
            for i in range(len(s)):
                newobj = {}
                if(RepresentsInt(row[i])):
                    newobj[s[i]]=int(row[i])
                else:
                    newobj[s[i]]=row[i]
                json_object['race'].append(newobj)
            a_file = open("data/"+row[0]+"/stats.json", "w")
            json.dump(json_object, a_file)
            a_file.close()