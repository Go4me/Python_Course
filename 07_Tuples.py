#Tuples is collection of immutable heterogenous python objects
x=(1,89,'f','ff','o',99)
#the indices of  the variable are..
# at 0th position - 1
# at 1st position -89
# at 2nd position -'f'
# at 3rd position - 'ff'
# at 4rth position - 'o'
# at 5th position - 99

# 1. CREATING TUPLES
a=()  #empty tuple
print(type(a))  #tells the class of variable a

city= 'Kochi',   #its OK to not put the curved brackets ,but neccesary to put that single comma
print(type(city))

# STANDARD WAY OF WRITING A TUPLE
city=('Kochi','Bangalore','chennai','delhi')
print(city)

# DIFFERENCE IN TUPLES AND LISTS WHEN IT COMES TO EXECUTION
# 1. List is mutable whereas tuple is immutable
# 2. List uses quare brakets. Tuple may ormay not use parenthesis

#examples:
city=('kochi','mumbai','kolkata','bangalore')
print(city)    #prints the content in tuple
print(city[1])  #prints the 1st element in tuple
print(city[-1]) #prints the 1st element from the last in tuple

##                 CONCATENATION
#LETS TAKE TWO TUPLES AND CONCATENATE THEM
city=('Kochi','Bangalore','chennai','delhi')
num=(1,2,3,4,5,6,7)
print(city + num)   #this "+" will join these both tuples together
#   result= ('Kochi', 'Bangalore', 'chennai', 'delhi', 1, 2, 3, 4, 5, 6, 7)


##                   NESTING
#lest now put tuples inside a tuple
a=(city,num)  #this will put the tuples city and num inside a new tuple 'a'
print(a)

##                 REPETATION
# suppose you want to print "python" 5 times. then use:
rep=("python",)*5
print(rep)
#another way:
rep=('python',)
print(rep*10)


##                 SLICING
#suppose you want to cut or slice the tuple.i.e suppose you do not want first elemet in your tuple ,then:
num=(2,3,4,5)
print(num[1:])  #the synatx is num[1:] here the 1 represents 1st element
#lets do more examples:
a=(1,2,3,4,5,6,7,8,9)
print(a[1:])   #will result in (2, 3, 4, 5, 6, 7, 8, 9), as it will slice the first element from others
print(a[2:])  #will result in (3, 4, 5, 6, 7, 8, 9),it will slice the first two elements
print(a[3:])    #will result in (4, 5, 6, 7, 8, 9), it will slice the first three elements
print(a[4:7])   #will result in (5, 6, 7), it will slice the first four elements and elements after 7th position
print(a[5:8])   #will result in (6, 7, 8),it will slice the first five elements and also the elements after 8th position
print(a[:9])    #will result in (1, 2, 3, 4, 5, 6, 7, 8, 9)
#hope you got the concept of slicing

##            REVERSING A TUPLE
a=(1,2,3,4,5,6,7,8,9)
print(a[::-1]) #here :: is used to leave the first and last index empty,-1 will reverse the tuple

##               UNPACKING
#suppose i want to have the letters of the word "beautiful" to be in tuple, lets check it out:
a="beautiful"
print(tuple(a))  #tuple(variable) will separate out the thing and make everything as a tuple

##               DELETING TUPLE
#to delete tuples we use del()
f=(1,2,3,4,5)
print(f)
del f  #when u try print(f) after this operation,then it will throw an error

##       BUILT IN FUNCTIONS
num1=(1,2,2,2,2,2,3,4,5,6,7,8)
print(num1.count(2))  #syntax variable_name.count() will tell you the count of number or letter in that particular tuple
print(sum(num1))    #syntax sum(variable_name) it will give the sum of all elements in that tuple
print(len(num1))    #synatx len(variable_name) it will give you the length of tuple
print(max(num1))  #syntax max(variable_name) it will give the maximum or highest value in that tuple
print(min(num1))  #synatx min(variable_name) it will give you the minimum nor lowest value in the tuple


##      CONVERTING LIST TO TUPLE
lst=[1,2,3,4,5]  #declared a list
tpl=tuple(lst)   #syntax new_variable=tuple(variable used to store list)
print(tpl)


##      NESTING TUPLES IN A LIST
lst=[(1,2,3,4),(5,6,7,8)]
lst.append(("tuple","added")) #syntax variable_name.append(tuple elemts to be added) for adding tuple inside list
print(lst)

#to remove a list or tuple inside a list:
a=[(1,2,3,4),(5,6,7,8)]
a.remove((1,2,3,4))  #syntax variable_name.remove(tuple elemts to be removed) for removing tuple inside list
print(a)

##    NESTING LIST WITHIN TUPLES
g=(['a','b'],['c','d'])
print(g)

#to modify the tuple, we have to modify the list as the tuple cannot be modified.
g[0].append('z')   #syntax variable_name[position of list].append(elements to be added) for adding element in list inside tuple
print(g)

#to remove
e=(['a','b'],['c','d'])
e[0].remove('b')
print(e)

#NOTE : we cannot add a complete list to the tuple as tuple cannot be modified.
