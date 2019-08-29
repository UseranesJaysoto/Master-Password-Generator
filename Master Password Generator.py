#!/bin/python3

import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJK123456789<>?/'




number = input('number of password')
number = int(number)


length = input('password length?')
length= int(length)

for p in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)



  #Jaysoto