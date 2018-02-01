print("Enter the series of numbers below separated by spaces -")
li = [int(x) for x in input().split()]
count_even = 0
for i in li:
    if i%2 == 0:
        count_even += 1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",len(li)-count_even)