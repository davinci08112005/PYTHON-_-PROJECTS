import string
import random

print(" --------- Welcome to  PASSWORD GENERATOR  -------------- ")
words = [random.choice(string.ascii_letters)for i in range (int(input('enter how many letters you want to input : ')))]
numbers = [random.choice(string.digits) for i in range (int(input("enter how many numbers you want to input :" )))] 
symbol = [random.choice(string.punctuation)for i in range (int(input("enter how many symbols you want to input : ")))]
key = words + numbers + symbol
random.shuffle(key)
input_length = int(input("enter the desired length of the password : "))
if input_length > len(key):
    print(f"the desired length exceeds the available character .Maximum length available : {len(key)} ") 
    input_length = len(key)

password = ''.join(key[:input_length])
print(f"generated password : {password }")    