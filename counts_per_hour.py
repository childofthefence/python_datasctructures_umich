name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
list_of_dates = []
list_of_hours = {}
split_list = []
list_of_keys = []
for items in handle:
	if items.startswith("From:"): continue
	if items.startswith('From'):
		split_list = items.split(" ")
		list_of_dates.append(split_list[6])

for hours in list_of_dates:
	hours = hours.split(':')
	# print(hours)
	list_of_hours[hours[0]] = list_of_hours.get(hours[0], 0) + 1

for k, v in list_of_hours.items():
	list_of_keys.append(k)
list_of_keys.sort()

for keys in list_of_keys:
	print(keys + " " + str(list_of_hours[keys]))