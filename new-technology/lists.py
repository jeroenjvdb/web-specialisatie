#!/usr/bin/python

first_list = ["hello", "world"]
print(first_list)
first_list[1] = "Antwerp"
first_list.append("!")
print("length: %d" % (len(first_list)))
print(first_list[0:2])

print("\na string is also a list (a list of characters)")
print(first_list[1][:3])

print()
hello_index = first_list.index('hello')
first_list.insert(hello_index, 'well')
print(first_list)

for word in first_list:
	print(word)
print('\nsort list:')
first_list.sort()
for word in first_list:
	print(word)