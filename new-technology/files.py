#!/usr/bin/python

python_file = open('python.txt', 'r+')

print(python_file.read())
python_file.write('cuz you can acces files from within your code')

python_file.close()