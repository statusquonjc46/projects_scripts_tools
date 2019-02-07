import csv
import copy

newData = open("test.csv", "r")
dataBase = open("test1.csv", "r")

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
                userinput = input("Are these the same company: " + a +
                                  " and " + b + " [y for yes, n for no]\n")
                if userinput == "y":
                    print(a + " has been confirmed as the same company as " + b + "\n")
                    notInBoth.remove(a)
                if userinput == "n":
                    print("These companies do not match. Continuing matching process.\n")
print(preclin)


# REALLY BAD CODE FOLLOWS.
# for a in preclin:
#    for b in cmp:
#        print(a, b)
#        if a[:1] in b[:1]:
#            if a[:5] in b[:5]:
#                if a[:3] == "Bio" or a[:4] == "Gene" or a[:3] == "Cor" or a[:4] == "Phar":
#                    if a[:6] in b[:6]:
#                        userinput = input("Are these similar: " + a + " and " + b + " y for yes, n for no\n")
#                        if userinput == "y":
#                            print(a + " has been confirmed as the same company as " + b + "\n")
#                            if a in notInBoth:
#                                notInBoth.remove(a)
#                                break
#                        if userinput == "n":
#                            print("These companies do not match. Continuing matching process.\n")
#                            if a not in notInBoth:
#                                notInBoth.append(a)
#                                print("Added to list of companies not in our database.\n")
#                                break
#                            else:
#                                print(a, "\n")
#                                print("Already exists, not added\n")
#                else:
#                    userinput = input("Are these similar: " + a + " and " + b + " y for yes, n for no\n")
#                    if userinput == "y":
#                        print(a + " has been confirmed as the same company as " + b + "\n")
#                        if a in notInBoth:
#                            notInBoth.remove(a)
#                            break
#                    if userinput == "n":
#                        print("These companies do not match. Continuing matching process.\n")
#                        if a not in notInBoth:
#                            notInBoth.append(a)
#                            print("Added to list of companies not in our database.\n")
#                            break
#                        else:
#                            print(a, "\n")
#                            print("Already exists, not added\n")
#            else:
#                if a not in notInBoth:
#                    notInBoth.append(a)
#                    print("Added to list of companies not in our database.\n")
#                else:
#                    print("1")
#                    print(a, " ", b, "\n")
#                    print("Already exists, not added\n")
#        else:
#            if a not in notInBoth:
#                notInBoth.append(a)
#                print("Added to list of companies not in our database.\n")
#            break

# print(notInBoth)
#
csvFile = open('NotInDatabase.csv', 'w')
writer = csv.writer(csvFile)
for item in notInBoth:
    writer.writerow([item])
csvFile.close()
