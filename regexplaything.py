import re

fortnight = "hey there, You Stupid fork, just playing around with regex"
vowels = "AEioU"
tester = "WhY dO yOU think: thAt I :wiLL always"
x = re.findall('[AEIOU]+', vowels)
y = re.findall('W.+?:', tester)
print(x)
print(y)