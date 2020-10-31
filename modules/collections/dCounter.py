#collections.Counter()
#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values

#A Counter dict is more friendly than an ordinary dict; it will return value 0 if a key doesn't exist. You can find out by running a couple of lines in iPython or Python shell.

from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

print(myList)

print(sorted(myList))

print(Counter(myList))

print(Counter(myList).items())

print(Counter(myList).keys())

print(Counter(myList).values())