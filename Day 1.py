#
# print("Welcome to the Band Name Generator. ")
# street = input("What's the name of the city you grey yuo in?\n")
# pet = input("What's your pet name? \n ")
# print("Your brand name could be " + street + " " + pet)
#
#
# # Write a program that prints the number of characters in a user's name.

# name = input("Whats your Name ?")
# print(len(name))

#
# # 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 Don't change the code above 👆
#
# ####################################
# # Write your code below this line 👇
#
# c = a
# a = b
# b = c
#
# # Write your code above this line 👆
# ####################################
#
# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)


######################### Data types

# String

# print("Hello" [4]) #String Subscripting
#
# print('123' + '456') #Concansinating
#
# num_char = len(input("What is your Name?"))
# new_num_char = str(num_char)
#
# print("Your name has " + new_num_char + " characters.")
# print(type(num_char))

# a = float(123)
# print(type(a))
#
# print(70 +float(100.5))
# print(str(70) + str(100))

# Write a program that adds the digits in a 2 digit number. e.g.
# if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3.
# Your program should work for different inputs. e.g. any two-digit number.

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆
#
# ####################################
# # Write your code below this line 👇
#
# print(type(two_digit_number))
# a = int(two_digit_number[0])
# b = int(two_digit_number[1])
#
# output = int(a + b)
# print(output)

# print(int(6/2))
#
# print(3 * 3 + 3 / 3 - 3)
# print((3 * 3) / 3 + (3-3))

# Write a program that calculates the Body Mass Index (BMI) from a user's
# weight and height.
#
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a
# short person both weigh the same amount, the short person is usually more overweight.
#
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#
# Unsupported image
#
# Warning you should convert the result to a whole number.


# wight = int(input("What is your Weight in Kgs "))
# height = float(input("What is your Height "))
# BMI = wight / (height ** 2)
#
# print(int(BMI))


print(round(8/3, 2)) #round function used to round off intergers and float

print(type(8//3)) # // Double dicition can change a float to int

result = 4/2
result /=2
print(result)

#f-string used to mix string and other data type

score = 0
height = 1.8
isWinning = True

print(f'Your score is {score}, your height is {height}, your winning is {isWinning}')

