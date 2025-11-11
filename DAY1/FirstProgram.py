print("Hello World")

x=100
y=200
print(x+y)

z=x+y
print(z)
print(type(z))
# this is how comments are written in Python
'''this is how comments are written in Python
 this is how comments are written in Python
 this is how comments are written in Python'''


print('Akash bhai zindabad\'')


import keyword

print(keyword.kwlist)

''' Output of print(keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
'while', 'with', 'yield']

'''

a=1
b=2
c=3

print(a,b,c)

d= "string"

print(a,b,c,d)

a,b,c= 1,2, 'akash'
print(a,b,c)

# swapping

x=1
y=2
print(x,y)

x,y=y,x
print(x,y)

x=5
y=6
x=y
y=x
print(x,y)