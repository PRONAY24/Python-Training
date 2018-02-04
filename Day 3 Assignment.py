#1.Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.

di = {'1':['a','b'], '2':['c','d']}         ## Expected Output: ac ad bc bd
x = list(di.values())
for i in x[0] :
    for j in x[1]:
        print(i+j)

print("==================")

#2.Write a Python program to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

print("=================")

#3.Write a Python program to sort (ascending and descending) a dictionary by value.
di = {'d':250,'a': 400, 'b': 200, 'c':300}
print(sorted(di))                           #Sorted dictionary by keys
print(sorted(di,reverse=True))              #Sorted dictionary by keys reversed

print(sorted(di.values()))                  #Sorted dictionary by values
print(sorted(di.values(),reverse=True))     #Sorted dictionary by values reversed

x = [value for (key,value) in sorted(di.items())]
print(x)                                    #Dictionary values sorted by keys
y = [key for (key,value) in sorted(di.items())]
print(y)                                    #Dictionary Keys sorted by values

print("======================")


#4. Write a Python program to get the maximum and minimum value in a dictionary
di = {'d':250,'a': 400, 'b': 200, 'c':300}
print("Maximum Value is :",max(di.values()))
print("Minimum Value is :",min(di.values()))

print("=======================")

#5. Write a Python program to remove duplicates from Dictionary.

di = {'d':250,'a': 400,'z':250, 'b': 200, 'c':300,'e':200}
di2 ={}
for (key,value) in di.items():
    if value not in di2.values():
        di2[key] = value
print(di2)

print("=======================")

#6. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
result = {}
for i in d1:
    if i in d2.keys():
        result[i] = d2[i] + d1[i]
    else:
        result[i] = d1[i]
for j in d2:
    if j not in result.keys():
        result[j]=d2[j]
print(result)

print("=======================")

#7. Write a Python program to get a list, sorted in increasing order by the last element in each
# tuple from a given list of non-empty tuples. Go to the editor

li = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
t = []
for i in range(len(li)):
    x = tuple(reversed(li[i]))
    t.append(x)
li = []
t.sort()
#print(t)
for i in range(len(t)):
    x = tuple(reversed(t[i]))
    li.append(x)
print(li)
print("=======================")

li = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(li,key=lambda x : x[1]))
print("Another option")
li.sort(key=lambda x : x[1])
print(li)
print("==========================")


#8. Write a Python program to select an item randomly from a list

import random
li = [12,23,30,44,35,46]
print(random.choice(li))
print("========================")

#9.Write a Python program to check whether a list contains a sublist
li = [1,2,3,4,[2,3,4],8,9]
x = 'Sublist is not present.'
for i in li:
    if type(i) is list:
        x = "Sublist is present."
print(x)

print("========================")

#10.Write a Python program to calculate number of days between two dates.
from datetime import date
d1, d2 =date(2014, 7, 2), date(2014, 7, 11)
x = d2 - d1
print(x.days,"days")

print("===========================")

#11.Write a Python program to display triangle of '*' pattern for a given number n
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + i*'* ')

print("=========================")