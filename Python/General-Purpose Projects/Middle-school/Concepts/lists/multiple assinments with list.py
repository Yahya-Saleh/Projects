#the two codes are the same
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

cat = ['fat', 'orange', 'loud']
cat = size, color, disposition
print(cat)
print(size)
print(color)
print(disposition)
#The number of variables and the length of the list must be exactly equal, or Python will give you a ValueError:
#>>> cat = ['fat', 'orange', 'loud']
#>>> size, color, disposition, name = cat
#Traceback (most recent call last):
#  File "<pyshell#84>", line 1, in <module>
#    size, color, disposition, name = cat
#ValueError: need more than 3 values to unpack
