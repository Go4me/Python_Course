## DICTIONARY is an unordered collection of data stored as a pair of key and value
## SYNTAX:  variable_name= {key1:value1,key2:value2,....}

##  CREATING DICTIONARY
d1={}
print(d1)
print(type)

d2={1:"welcome",2:"to",3:"this",4:"course"}
print(d2)

d3={"name":"Jaison","age":22,"profession":"student"}
print(d3)

d4=dict({1:"welcome",2:"to",3:"this",4:"course"})
print(d4)

d5=dict([(1,"welcome"),(2,"to"),(3,"this"),(4,"course")])  #tuples within a list
print(d5)

#   NESTED DICTIONARIES
#dictionary within dictionary
d6={"name":{"first":"Jaison","last":"crew"},"age":22,"profession":"student"}
print(d6)

## ADDING ELEMENTS
d={}
d[0]="welcome"  #here 0 becomes your key and welcome becomes its value
print(d)

d[1]=("how","are","you")  #adding tuple to the dictionary
print(d)

d["name"]="sam"
print(d)

#you can also add dictionary as an already existing dictionary
d["name"]={"first":"sam","last":"crew"}
print(d)

#  ACCESSING ELEMENTS
print(d["name"])
print(d["name"]["first"])

print(d.get(1))


## DELETING ELEMENTS
d.pop(0)
print(d)

d.popitem()  #it always delete the last elememt of dictionary
print(d)

