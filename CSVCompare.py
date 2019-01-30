import csv
import copy

compareCSV = input("Enter the file you want to compare against CMP's Database: \n")
newData = open(compareCSV, "r")
dataBase = open("CMPList.csv", "r")

testList = list(newData)
test1List = list(dataBase)
preclin = []
cmp = []
newData.close()
dataBase.close()

notInBoth = []

for i in testList:
    new = i.strip()
    newer = new.replace('"', '')
    preclin.append(newer)
for j in test1List:
    new = j.strip()
    newer = new.replace('"', '')
    cmp.append(newer)

notInBoth = copy.deepcopy(preclin)

for a in preclin:
    for b in cmp:
        print(a, b)
        if a[0] == b[0]:
            if a[:6] in b[:6]:
                if a[:5] == "Pharm":
                    if a[:8] in b[:8]:
                        userinput = input("Are these the same company: [" + a + "] and [" + b + "] [y for yes, n for no]\n")
                        if userinput == "y":
                            print("--------------------------------------------------------------\n")
                            print("[" + a + "] has been confirmed as the same company as [" + b + "]\n")
                            print("--------------------------------------------------------------\n")
                            notInBoth.remove(a)
                            break
                        if userinput == "n":
                            print("----------------------------------------------------------\n")
                            print("These companies do not match. Continuing matching process.\n")
                            print("----------------------------------------------------------\n")
                userinput = input("Are these the same company: [" + a + "] and [" + b + "] [y for yes, n for no]\n")
                if userinput == "y":
                    print("--------------------------------------------------------------\n")
                    print("[" + a + "] has been confirmed as the same company as [" + b + "]\n")
                    print("--------------------------------------------------------------\n")
                    notInBoth.remove(a)
                    break
                if userinput == "n":
                    print("----------------------------------------------------------\n")
                    print("These companies do not match. Continuing matching process.\n")
                    print("----------------------------------------------------------\n")

print("All comparisons complete, creating new CSV of companies not in our database.\n")

csvFile = open("NotInDataBase.csv", 'w')
writer = csv.writer(csvFile)
for item in notInBoth:
    writer.writerow([item])
csvFile.close()

print("CSV creation complete. Exiting...")