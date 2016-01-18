#!/usr/bin/python

print('dictionaries')
personal_records = {
	'50fs': '24.00',
	'100fs': '52.11',
	'200fs': '1.54.42' 
}

print(personal_records['100fs'])
print(personal_records)
del personal_records['50fs']
print()
print(personal_records)

list_ception = {
	'key' : 'value',
	'list_key': ['this', 'is', 'a', 'list']
}
print(list_ception)