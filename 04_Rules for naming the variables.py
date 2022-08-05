# 1. Variable name must be starting with a alphabet or an underscore(_).
abc = 100  # valid
_aaa = 10  # valid
# 11aa=20             #invalid
# 22=dasff             #invalid

# 2.The first character can be followed by alphabets,numbers and underscores
aa10 = 123  # valid
_a23a_ = 345  # valid
#  a656$$$=34567          #invalid
#  xyz-946= sfdteh        #invalid

# 3.Variable names are case sensitive i.e a and A are different in python
a=100
A=1234

# 4.There are many reserved words in python which cannot be used as variables.
#for example: break, class, try...etc