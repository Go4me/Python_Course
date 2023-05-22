#string is a data type that could include collection of characters
#eg: "Hey","Welcome to the course"
#Syntax: variable="string" or variable='string'
#example: name="kochi" or name='kochi'
name="kochi"
print(name)
print(type(name))

a='Tim said,"I am busy today"'
print(a)

b='''Hey there! 
   Welcome to my course'''   #for writing multiple lines or paragraphs we can use triple quote(''' or """) in begining as well as ending
print(b)


##     LEN FUNCTION
c= "My name is Jaison"
print(len(c))  #len will count space as one character
print(c[6])

#if i want to access/print every character in a string
for i in c:
    print(i)  #it will print the charcters in separate line

 # to make it print on same line
for i in c:
    print(i,end="")

print('\n') #to seprate out codes

##     SLICING IN STRING

stg="Jaison"  #here J starts at position 0
print(stg[0:5]) #can be written as print(stg[:5])
print(stg[5:]) #every character from 5th will be extracted
print(stg[2:5]) #every cahracter from 2nd poistion till 5th will be extracted,5th position will not be extracted


##  BUILT IN FUNCTIONS
stg="Welcome to my course"
print(stg.upper())  #syntax variable_name.upper() print the string in capital letters
print(stg.lower()) #syntax variable_name.lower() print the string in lower case
print(stg.find('s'))  #to find the index of the character in string
print(stg.index('o'))
print(stg.split(' '))  #we will get a list which will have elements as our words

print(stg.rpartition(" to ")) #will create a tupl out of strings

##   STRING CONCATINATION
a = "good";
b = "morning";
c = "all"
d = "{} {} {}!".format(a, b, c)      #curly braces are place holders they tell exactly where the respective string should be placed
print(d)





