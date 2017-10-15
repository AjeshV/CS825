import os
import re
import csv

File1 = open("C:\Users\Ajesh\Desktop\UNH\Courses\CS825\Assignment 1\cs725-f17-a1-ping-n.txt", 'r')
File2 = open("C:\Users\Ajesh\Desktop\UNH\Courses\CS825\Assignment 1\cs725-f17-a1-ping-p.txt")


try:
    # reader = csv.DictReader(File1)
    # for row in reader:
        # print row
    for line in File1:
        fields = line.strip().split()
		#print fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7]
		#for i in range(0,7):
		#j=0
        #Var[i] = fields[j].strip().split()
		#j++
        #print fields[0]
        Var0 = fields[0].strip()
        #print Var0
        Var1 = fields[1].strip()
        Var2 = fields[2].strip()
        Var3 = fields[3].strip()
        Var4 = fields[4].strip()
        Var5 = fields[5].strip()
        Var6 = fields[6].strip()
        Var7 = fields[7].strip()
   
    result = ''.join([i for i in Var4 if i.isdigit()])
    print result
    
	p = re.compile(r'\d+\.\d+')  # Compile a pattern to capture float values
    floats = [float(i) for i in p.findall(Var6)]  # Convert strings to float
    print floats[0]
	
finally:
    File1.close()




