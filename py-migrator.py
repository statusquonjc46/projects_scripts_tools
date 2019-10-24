import os
import shutil

userName = input("Username:  ")
pstLoc = f"C:\\Users\{userName}\AppData\Local\Microsoft\Outlook"
newLoc = f"C:\\Users\{userName}\PST-Files"
pstList = []

for file in os.listdir(pstLoc):
	print(file)
	if file.endswith(".pst")
		pstList.append(file)

if len(pstList) > 0:
	print(pstList)
	for i in range(len(pstList)):
	print(f"Move PST file, {pstList[i]}, to {newLoc}.")
	pstFile = f"{pstList[i]}"
	shutil.move(f"{pstLoc}\{pstFile}", f"{newLoc}\{pstFile}")
else:
	print(f"No PST Files founfd in: {pstLoc}")
