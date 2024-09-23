print ("*****************SIMPLE PYTHON CALCULATOR ********************")

num1 = float (input("enter the first number :"))
num2 = float (input("enter the second number :"))

print("Choose the operation you want to perform :\n")

print("1.ADDITION ")
print("2.SUBSTRACTION ")
print("3. MULTIPLICATION ")
print("4. DIVISION ")
print("5. MODULUS ")

choice = input ("enter the choice you want to perform (1/2/3/4/5): \n ")

if choice == "1":
    print(f"the addition of {num1} and {num2} is : ", num1 + num2)
elif choice == "2":
      print(f"the substraction of {num1} and {num2} is : ", num1 - num2)
elif choice == "3" :
     print(f"the multiplication of {num1} and {num2} is : ", num1 * num2)       
elif choice == "4":
    print(f"the division of {num1} and {num2} is : ", num1 / num2)
elif choice == "5":
     print(f"the modulus of {num1} and {num2} is : ", num1 % num2)
else :
     print(" SORRY YOU HAVE CHOOSEN INVALID OPTION!: ")