#1.Write a Python program to find the second smallest number in a list

print("Enter your numbers : ")
li = [int(x) for x in input().split()]      # taking inputs as integer separated by spaces
li.sort()                                   # Sorting the list
print("Second smallest number :",li[1])

print("----------------")

#2. Write a Python program to convert a list of multiple integers into a single integer

li = [1,2,3]
li_str = {str(x) for x in li}       #Converting each element to string
print(int("".join(li_str)))         #Joining the strings and typecasting to integer

print("-----------------")

#3.Write a Python program to check a list is empty or not.
li = [2,3]                      #Creating the list
if li == []:                    #Checking if the list is empty or not
    print("List is empty")
else:
    print("List is not empty")

print("----------------")

#4.Write a Python program to compute the differeces between two lists.

x = ["red", "orange", "green", "blue", "white"]
y = ["black", "yellow", "green", "blue"]
print(list(set(x)-set(y)))                  #Difference between two lists
print(list(set(y)-set(x)))

print("----------------")

#5.Write a Python program to count the number of characters (character frequency) in a string

sample = 'google.com'
di = {}
for i in sample:
    di[i] = sample.count(i)             # counting each letter and storing it in dictionary
print(di)

print("----------------")

#6.Write a Python program that takes a list of words and returns the length of the longest one

li = input("Enter some words :")
li_string = li.split()
longest_word = ""
for i in li_string:
    if len(i) > len(longest_word):      # checking the longest word and assigning to longest_word
        longest_word = i
print(longest_word)

print("----------------")

#7.Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
string = input("Enter a string :")
check = 0
for i in range(4):
    if string[i].isupper() :        #checking first 4 characters
        check+=1
if check>1:
    print("More than 2 uppercase character :",string.upper())
else:
    print("No change :",string)

print("----------------")