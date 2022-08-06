import os

directory = input('Please enter the directory: ')
if os.path.isdir(directory):
  os.chdir(directory)
else:
  print('Making directory!')
  os.mkdir(directory)
fileName = input('Please enter the file name you wish to save: ')
completePath = os.path.join(directory, fileName)
if os.path.isfile(fileName): 
  print('File already exists')
else:
  print('File doesnt exist')
name = input('Please enter your name: ')
address = input('Please enter your address: ')
phonenumber = input('Please enter your phone number: ')

with open(completePath, 'w') as file:
  file.write(f'{name}, {address}, {phonenumber}')
  
with open(completePath, 'r') as file:
  print(file.read())
