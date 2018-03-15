#Assignment 9.4

name = input("Enter file:")
my_dict = {}
list_hold = []
max_index = None
max_value = None
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
#print(handle)
for lines in handle:
    if(lines.startswith("From") and not lines.startswith("From:")):
        sender = lines.split()
        list_hold.append(sender[1])
#print(list_hold)
for vals in list_hold:
    my_dict[vals] = my_dict.get(vals, 0) +1
    if(max_value == None):
        max_value = my_dict[vals]
        max_index = vals
    else:
        if(max_value<my_dict[vals]):
            max_value = my_dict[vals]
            max_index = vals
print("{} {}".format(vals, my_dict[vals]))