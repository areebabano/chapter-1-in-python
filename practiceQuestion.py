# # Q1: Write a Program to input 2 numbers & print thier sum. 

# num1 = input("Enter num1: ")
# num2 = input("Enter num2:")

# print("sum of num1 & num2 is ",num1 + num2) # output is ap jo bh input m number dogy wo usko concatenate kr k dega output beacuse input is string
# print(type(num1), type(num2)) # string

# num1 = int(input("enter num1: "))
# num2 = int(input("Enter num2: "))

# print("After type casting Sum of num1 & num2 is ", num1 + num2) # now perform addition operation between num1 and num2
# print(type(num1), type(num2)) # integer

# Q2: Write a program to input side of a square & print its area.

# with integer value 

# side = int(input("Enter a side of Square: "))
# print(type(side)) # integer
# area = side * side

# print("Area of square is ", area)

# with floating value 

# side = float(input("Enter a side of Square: "))
# print(type(side)) # float
# # area = side * side 
# area = side ** 2 # line 29 and 30 return same output 

# print("Area of square is ", area)

# Q3: Write a program to input 2 floting point numbers and print thier average.

# x = input("Enter a floating num1: ")
# y = input("Enter a floating num2: ")
# z = (x + y) / 2

# print("Average of points is ", z) # error

# corrected code 

# x = float(input("Enter a floating num1: "))
# y = float(input("Enter a floating num2: "))
# z = (x + y) / 2

# print("Average of points is ", z) # error

# Q4: Write a program to input a 2 integer numbers, a and b. Print True if a is greator than or equal to b. If not print false.

a = int(input("Enter a first number ")) 
b = int(input("Enter a second number "))
c = (a >= b) 

print("a is greator than or equal to b ", c) # print True / False

