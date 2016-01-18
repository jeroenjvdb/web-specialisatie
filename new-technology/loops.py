#!/usr/bin/python

whileLoopCount = 0
while whileLoopCount < 10:
	print(" " + str(whileLoopCount))
	whileLoopCount += 1

condition = True
while condition:
	print('this is true')
	condition = False

print()

condition = True
print(' zonder break')
while condition:
	print(' in while')
	condition = False
else:
	print(' in else')

print()

condition = True
print(' met break')
while condition:
	print(' in while')
	break
else:
	print(' in break')

print()


count = 0
while True:
	print(str(count))
	count += 1
	if count > 5:
		break

import random
print()
count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You win!")

print('\n')

for i in range(5):
	print(str(i))

print()
for i in range(5,10):
	print(i)
print()

for letter in word:
	print(letter)

print()

word = 'lol'
for index, letter in enumerate(word):
	print(index+1, letter)

print()
list_1 = [1,2,3,4,5]
list_2 = [6,5,4,3,2,1]
for a,b in zip(list_1, list_2):
	if a>b:
		print(" " + str(a))
	else:
		print(" " + str(b))

print()