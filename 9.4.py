#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = raw_input("Enter file name: ")
fhand = open(fname)
count = 0
datastorage = ""
emails = {}

for line in fhand:
	line = line.rstrip("")

	if line.startswith('From ') and not line.startswith('From: '):
		words = ((line.rstrip()).lstrip()).split()	
		sugar = words[1]
		emails[sugar] = emails.get(sugar,0) + 1

for data in emails:
	if emails[data] > count:
		count = emails[data]
		datastorage = data
print datastorage, count
