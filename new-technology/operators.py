#!/usr/bin/python
"""
Equal to (==)
Not equal to (!=)
Less than (<)
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=)
"""
print('boolean operators: \n')

print('True and True is ' + str(True and True))
print('True and False is ' + str(True and False))
print('False and False is ' + str(False and False))
print()
print('True or True is ' +str(True or True))
print('True or False is ' + str(True or False) )
print('False or True is ' + str(False or True))
print('False or False is ' + str(False or False))
print()
print('Not True is ' + str(not True))
print('Not False is ' + str(not False))
print('\n\n')
print('if else \n')


if True:
	print('you are in the if loop (if(true))')
else:
	print('you are not in the if loop (if(true))')

if False:
	print('you are in the if loop (if(false))')
else:
	print('you are not in the if loop (if(false))')

if False:
	print('this will not be printed (elif)')
elif True:
	print('this will be printed (elif)')