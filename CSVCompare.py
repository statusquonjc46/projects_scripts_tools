import csv
import copy

compareCSV = input("Enter the file you want to compare against CMP's Database")
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
    preclin.append(new)
for j in test1List:
    new = j.strip()
    cmp.append(new)

notInBoth = copy.deepcopy(preclin)

for a in preclin:
    for b in cmp:
        print(a, b)
        if a[0] == b[0]:
            if a[:4] in b[:4]:
                userinput = input("Are these the same company: [" + a + "] and [" + b + "] [y for yes, n for no]\n")
                if userinput == "y":
                    print("--------------------------------------------------------------\n")
                    print("["a + "] has been confirmed as the same company as [" + b + "]\n")
                    print("--------------------------------------------------------------\n")
                    notInBoth.remove(a)
                if userinput == "n":
                    print("----------------------------------------------------------\n")
                    print("These companies do not match. Continuing matching process.\n")
                    print("----------------------------------------------------------\n")

print("All comparisons complete, creating new CSV of companies not in our database.\n")

csvFile = open('NotInDatabase.csv', 'w')
writer = csv.writer(csvFile)
for item in notInBoth:
    writer.writerow([item])
csvFile.close()

print("CSV creation complete. Exiting...")