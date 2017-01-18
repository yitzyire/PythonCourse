#3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. 
hrs = raw_input("Enter Hours:")
hours = float(hrs)

rte = raw_input("Enter rate amount:")
rate = float(rte)

if hours <= 40: 
	total = hours * rate
	print total
else: 
	#get the left over value of the 40 - variable
	overtime = hours - 40
    #get total before the 40 (can ref that later in the total)
	tempbufferfourty = 40 * rate  
	tempbufferremainder = overtime * (1.5 * rate) 
	total = tempbufferfourty + tempbufferremainder
	print total
