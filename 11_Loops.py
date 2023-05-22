#lets take a scenario where you wat to print "hello world" 10 times,
#so you will manually type print("hello world") 10 times.
# to make these tasks easier , we use loops in python
# there are two types of loops in python: for loop , while loop


##                                       FOR LOOP
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in
# other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# SYNTAX:
#         for 'value' in 'sequence':
#                {loop body}

##example:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#example:
for x in "banana":
  print(x)
#it jst listed out the words in the variable


#Question:
# Code to find the sum of squares of each element of the list using for loop
# creating the list of numbers
numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]

# initializing a variable that will store the sum
sum_ = 0

# using for loop to iterate over the list
for num in numbers:

    sum_ = sum_ + num ** 2

print("The sum of squares is: ", sum_)


###             ELSE in FOR loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

##          BREAK in FOR loop
# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.


##                                       WHILE LOOP
# With the while loop we can execute a set of statements as long as a condition is true.

#SYNtax:
#       while condition:
#           body of while loop
#example:
# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

#exaple:
# program to calculate the sum of numbers
# until the user enters zero

total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number  # total = total + number

    # take integer input again
    number = int(input('Enter a number: '))

print('total =', total)
