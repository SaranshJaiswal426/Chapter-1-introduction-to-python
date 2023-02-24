print('Here we see some list ')
int_list = [1, 2, 3]
string_list = ['abc', 'defghi']
#A list can be empty:
empty_list = []
#mixed list
mixed_list = [1, 'abc', True, 2.34, None]
#A list can contain another list as its element:
nested_list = [['a', 'b', 'c'], [1, 2, 3]]
print(nested_list)
#add some list 
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
names.append("Sia")
print(names)
#remove
names.remove("Bob")
print(names) 
#get index
names.index("Alice")
#length of string
print(len(names))
#count in same multiple items in list
x = [1, 1, 1, 2, 3, 4]
print(x.count(1))


b = [4, 3, 2, 1, 1, 1]
print(b.reverse())

print("tuple>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
ip_address = ('10.20.30.40', 8080)
print(ip_address)

print("Dictionaries ......................................")
state_capitals = {
 'Arkansas': 'Little Rock',
 'Colorado': 'Denver',
 'California': 'Sacramento',
 'Georgia': 'Atlanta'
}
print(state_capitals)