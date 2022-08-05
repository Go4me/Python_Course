#1st Datatype
# Lists
# list is basically the collection of values.With list we can assign multiple values to a variables.
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # how to use list
print(b)  # printing list
print(type(b))  # to find out the type of the datatype the variable is containing i.e list

#####     N O T E      #######
# all the values inside the list have specific position called the index.
# Index starts from 0 to (n-1)where n is the position of the last member of the list.
# in list b , the value in the 0th position is 1,value in 1st position is 2....values in 8th position is 9.
#0th position= b[0], 1st position= b[1], 8th position= b[8]
################################

print(b[0]) #to print the specific value the the position.
print(b[8])

#to change the value in teh specific index in the list
b[1]=3
print(b)

#Tuple
#tuples are immutable and thats their main feature.
q= (1, 2, 3, 4)  #syntax for tuple datatype.Note here we used curve brackets instead of square brackets.
print(q)
print(type(q))   # to determine the datatype of the variable q,    i.e "tuple"
print(q[1])
#lets try to change the value
#q[1]=66
#rint(q)
#when you try to execute this code then it will surely throw an error and tells to change tuple with lists.


#if you want to store values to multiple variables
# #for example
l=1
k=2
j=3
print(l)
print(k)
print(j)
###############instead do:
(t,u,i)=1,2,3
print(u)
print(t)
print(i)
#or
print(t,u,i)

#lets do another
#let suppose z=1,c=1,v=1, so instead (z,c,v)= 1,1,1 -----we have:
z=c=v=1
print(c,z,v)
