#Chapter 8

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split(' ')
    for word in words:
        word = word.replace('\n', '')
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)