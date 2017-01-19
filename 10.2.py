#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = raw_input("Enter file name: ")
fhand = open(fname)
count = 0
datastorage = ""
emails = {}

for line in fhand:
	line = line.rstrip("")

	if line.startswith('From ') and not line.startswith('From: '):
		words = ((line.rstrip()).lstrip()).split()	
		sugar = words[5]	
		broken = sugar.split(":")
		time = broken[0]
		emails[time] = emails.get(time,0) + 1
lst = emails.items()
lst.sort()
for key, val in lst :
    print key, val
