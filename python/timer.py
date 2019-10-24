import time

timerLen = input("Please enter how long you want to run the timer for: ")
i = 1
for i in range(int(timerLen)):
	print(i)
	time.sleep(1)
print("Time's up!") 
