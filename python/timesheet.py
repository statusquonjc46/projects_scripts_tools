#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Timesheet creator for my work time sheets.
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import sys
import os
import time

userName = input("Please enter your name: ")
userDay = input("What weekday are you entering times for: ")
noChange = input("Has your schedule changed from 7:30AM - 4PM? (Y/N)")

if noChange == "N" or noChange == "n":
	userStart = "7:30AM"
	userEnd = "4:00PM"
else:
	userStart = input("Please enter your start time: ")
	userEnd = input("Please enter your end time: ")

lunchLng = input("How long was lunch? ")
inputDate = time.asctime(time.localtime(time.time()))
newSheet = input("Do you need a new sheet? \n")
fileLoc = '/Users/nicholascoletta/salient-crgt/timesheets/'

if newSheet == "yes":
	weekEnd = input("Please enter the week end date: ")
	outFile = open(f'{fileLoc}timesheet-{weekEnd}','a+')
	outFile.write(f'----{weekEnd}----\n')
	outFile.write(f'{userName}\n')
else:
	weekEnd = input("Please enter current week end date for appending to open timesheet: \n")
	outFile = open(f'{fileLoc}timesheet-{weekEnd}', 'a+')

PWDfile = f'{fileLoc}timesheet-{weekEnd}'

print("\n*Current timesheet below*\n")
print(f'----{outFile.name}----')
os.system(f'cat {PWDfile}')
outFile.write("-----------------------------------------------------------------\n")
outFile.write(f'{userDay} - Start: {userStart} - End: {userEnd} - Lunch: {lunchLng}. | Created By: {userName} On: {inputDate}\n')
outFile.write("-----------------------------------------------------------------\n")
outFile.close()

print(f'[Submitted, {userName}, Thank you!]\n')
print(f'Printing updated timesheet for week end date: {weekEnd}\n')
os.system(f'cat {PWDfile}')




