# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
value_array=[]
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        line=line.split(':')
        line[1] = line[1].replace('\n', '')
        total = total + float(line[1])
        count = count + 1
        #print(line[1])
        #value_array.append(float(line[1]))
        
print("Average spam confidence: {0:.12f}".format(total/count))