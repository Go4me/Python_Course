#DECLARING A VARIABLE
a = "Jaison"
# extract each character in the string
print(a[0])
print(a[2])

# extract multiple characters in the string
print(a[0:3])  # extract the character from 0th position till the 2nd position
# and the character in the 3rd position will be excluded
print(a[:3])  #it will automatically understand that teh extraction should be begin from 0th position.

print(a[3:])  #it will automatically understand that the extraction should be begin from the 5th position till the last position
print(a[0:20]) #well, here we do not have 20 characters thus it will print all thge characters available in the string

print(len(a)) # len(a)  will print the length of the string
