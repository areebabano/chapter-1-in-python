# input() in python
# input() statement is used to accept values (using keyboard) from user.

name = input("enter your full name: ")
print("Hello! ", name)

# input() result always a string 

print (type(name)) # string

age = input("Enter your age: ")
print("your age is ", age)
print(type(age)) # string


# or if we want appropriate result so we use type casting int(input())

age = int(input("Enter your age: "))
print("your age is ", age)
print("After type casting age is ",type(age)) # integer

# but be careful when we use input() for integer values because if user enter something which is not integer it will throw error.
