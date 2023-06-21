# # 1. def function

# def percent(marks) :
#     m = (sum(marks)/600)*100
#     return m
# marks1 = [34, 56, 64, 23 , 56, 28]
# percentage1 = percent(marks1)

# marks2 = [33, 46, 94, 93 , 56, 38]
# percentage2 = percent(marks2)

# print(percentage1, percentage2)

# # 2. greet a user with good day using function
# def greet(NAME):
#     print('Good Day ,', NAME)
# greet('kapil')

# # there are two types of function in python 
# # (a) built in function (already present in python like - range , print, sum
# # (b) user defined function (defined by user like - greet , marks

# # 3. function with argument
# def my_sum(num1, num2):
#     return(num1 * num2)
# v = my_sum(25, 25)
# print(v)
 
# # 4. default parameter value 
# def greet(NAME = 'kap'):
#     print('Good Day ,', NAME)
# greet()

# # # 5. factorial in def
# # def factorial(n):
# #     product = 1
# #     for i in range (n):
# #        product = product * (i+1)
# #     return product
# # n = factorial(5)
# # print(n)

# # # 6. factorial in def_recursion
# # def fact_recursion(n):
# #     if n == 1 or 0:
# #      return 1
# #     return n * fact_recursion(n-1)     
# # v = fact_recursion(5)
# # print(v)

# # ques(1) find greatest of three numbers using def
# def numbers(num1 , num2, num3):
#     if (num1 > num2):
#       if (num1 > num3):
#          return num1
#       else:
#          return num3
#     else:  
#       if (num2 > num3):
#         return num2
#       else:
#         return num3
# v = numbers(5 , 66, 8)
# print(v)

# # ques(2) celcious to fahranhite
# def celcious(num):
#     a = (num * 9/5) + 32
#     return a
# v = celcious(0)
# print(v)

# # ques(3) some print() are written in one line, so use end= ""
# print('helllo', end=" ")
# print('kapil', end=" ")
# print('how ', end=" ")
# print('are', end=" ")
# print('you', end=" ")
# print('?', end=" ")

# # ques(4) sum  of first n number in def recursion
# def sum_recursion(n):
#     if n == 1 or 0:
#         return 1
#     return (n + sum_recursion(n-1))
# v = sum_recursion(5)
# print(v)

# # ques(5) print a star pattern
# n = 6
# for i in range(n):
#     print('*' * (n-i))

# # ques(6) convert into inch to cm
# def inch(n):
#     a = n * 2.54 
#     return a
# v = inch(6)
# print(v)

# # # ques(7) remove a given word and strip at a time 
# # def remove_and_strip(string , word):
# #     str = string.replace(word, 'GOOD')
# #     return str.strip()
# # this = 'kapil is bad boy'
# # v = remove_and_strip(this , "bad")
# # print(v)

# ques(8) multiplication of given number
def multiplication(num):
    for i in range (1, 11):
     print(f"{num * i}")

v = multiplication(10)
print(v)