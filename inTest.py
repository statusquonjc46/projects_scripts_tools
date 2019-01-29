import csv

test = open("test.csv", "r")
test1 = open("test1.csv", "r")

testList = list(test)
test1List = list(test1)
preclin = []
biosafety = []
test.close()
test1.close()

notInBoth = []

for i in testList:
    new = i.strip()
    preclin.append(new)
for j in test1List:
    new = j.strip()
    biosafety.append(new)
    
for a in preclin:
    for b in biosafety:
        if a[:3] in b:
            if a[:3] == "Bio" or a[:3] == "Gen" or a[:3] == "Cor" or a[:3] == "Phar":
                if a[:5] in b:
                    userinput = input("Are these similar: " + a + " and " + b + " y for yes, n for no\n")
                    if userinput == "y":
                        print(a + " has been confirmed as the same company as " + b + "\n")
                        if a in notInBoth:
                            notInBoth.remove(a)
                            break
                    if userinput == "n":
                        print("These companies do not match. Continuing matching process.\n")
                        if a not in notInBoth:
                            notInBoth.append(a)
                            print("Added to list of companies not in our database.\n")
                        else:
                            print("Already exists, not added\n")
            else:
                userinput = input("Are these similar: " + a + " and " + b + " y for yes, n for no\n")
                if userinput == "y":
                    print(a + " has been confirmed as the same company as " + b + "\n")
                    if a in notInBoth:
                        notInBoth.remove(a)
                        break
                if userinput == "n":
                    print("These companies do not match. Continuing matching process.\n")
                    if a not in notInBoth:
                            notInBoth.append(a)
                            print("Added to list of companies not in our database.\n")
                    else:
                        print("Already exists, not added\n")
        else:
            if a not in notInBoth:
                notInBoth.append(a)
                print("Added to list of companies not in our database.\n")
            else:
                print("Already exists, not added\n")

print(notInBoth)

csvFile = open('NotInDatabase.csv', 'w')
writer = csv.writer(csvFile)
for item in notInBoth:
    writer.writerow([item])
csvFile.close()

