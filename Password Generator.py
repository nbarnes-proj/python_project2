#!/bin/python3
import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!&*?'

length = input('password length?')
length = int(length)

password = ''

for c in range(12):
  
  password += random.choice(chars)
print(password)