# Types of operators

# 1. Arithmetic operators

a = 7
b = 4

print(a + b) #sum of arithmetic

print(a - b) #diff of arithmetic

print(a * b) #multiplication of arithmetic

print(a / b) #division of arithmetic

print(a % b) #modulus of arithmetic

print(a ** b) #exponentiation of arithmetic


# 2. Relational/Comparison operators

a = 10
b = 40

print(a == b) # check equality

print(a != b) # check inequality

print(a >= b) # check greater than and equal

print(a > b) # check greater than 

print(a <= b) # check less than and equal

print(a < b) # check less than


# 3. Assignment operators

num = 20
# num = num + 10
# print("num is : ", num) # print 30

num += 10  # result is same as line 43
print("num += ", num) # 20 + 10 print 30

num -= 10
print("num -= ", num) # 30 - 10 print 20

num *= 2
print("num *= ", num) # 20 * 2 print 40

num /= 5

print("num /= ", num) # 40 / 5 print 8

num %= 6
print("num %= ", num) # 8 / 6 print 2 beacause remainder is 2

num **= 4
print("num **= ", num) # 2 ** 4 print 16


# 4. Logical operators (y operators boolean values p work krty hen)

# not operator (y hamesha opposite print krta h)
# For Example 

print(not True) # print False
print(not False ) # print True

# with expressions

a = 20
b = 10

print("Not operator a > b ", not (a > b)) # print False

# and operator (both value true return true otherwise return false)

value1 = True
value2 = True

print("And operator value1 and value2 ", value1 and value2) # print True

value1 = True
value1 = False

print("And operator value1 and value2 ", value1 and value2) # print False

# or operator (either one of the value true return true otherwise return false)

value1 = True
value2 = False

print("Or operator value1 or value2", value1 or value2) # print True

value1 = False
value2 = False

print("Or operator value1 or value2 ", value1 or value2) # print False
print("Or operator", (a > b) or (a == b)) # print True
