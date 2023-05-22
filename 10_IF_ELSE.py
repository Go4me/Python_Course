##  if-else is a decision making statement
# it has many formats ,thus the first one we are going to look is
#####                         If Statement
# SYNTAX:  if condition:
#            statement to execute if condition if true
# example:

a=60
if a>50:
    print("this is in if body")
print("this is outside if block ")

#####                         If-else Statement

# SYNTAX:  if condition:
#            statement to execute if condition if true
#          else :
#            statement to execute if condition if the condition inside the true block is false

# example:
i=20
if i%2==0:
    print("i is an even number")
else:
    print("i is odd number")


#####                         Nested If Statement
# SYNTAX:  if condition1 :
#             executes if the condition1 is true
#                 if condition2:
#                   executes if the condition2 is true
#example
c=21
if c>25:
    if c%2==0:
        print("c is even number less than 25")
    else:
        print("c is an odd number less than 25")
else:
    print("c is greater than 25")

#####                      If-Elif-Else Statement
#       If-elif-else statement is used in Python for decision-making i.e the program will
#        evaluate test expression and will execute the remaining statements only if the given
#           test expression turns out to be true. This allows validation for multiple expressions.

#SYNTAX:
#               if test expression:
#                   Body of if
#
#               elif test expression:
#                   Body of elif

#               elif test expression:
#                   Body of elif

#               elif test expression:
#                   Body of elif
#                there can be n number of elif statements
#                   else:
#                   Body of else
#example:
price=100
if price > 100:
    print("price is greater than 100")
elif price == 100:
    print("price is 100")
elif price < 100:
    print("price is less than 100")

#In the above example, the elif conditions are applied after the if condition.
# Python will evalute the if condition and if it evaluates to False then it will
# evalute the elif blocks and execute the elif block whose expression evaluates to True.
# If multiple elif conditions become True, then the first elif block will be executed.










