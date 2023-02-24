print('Built In Types')
a = 2
b = 3
a or b # if x is False then y otherwise x
a and b
print(issubclass(bool, int)) 
print(True+False)

print('string')
a="hello"
print(type(a))

a = '123.456'
b = float(a)
#c = int(a) # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b) 
print(d)

print('Number type')
a = 2.0
b = 100 + 10j
print(a > b)
