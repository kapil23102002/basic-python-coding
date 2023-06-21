# loop

# 1. While loop
i = 0
while (i <= 10):
    print(i)
    i = i + 1
print("Done")

j = 0
while (j < 5):
    print("kapil " + str(j))
    j = j + 1
print("Thakur")

friends = ['akash', 'aman', 'kunal', 'bobby', 'pratyaksh']
k = 0
while (k < len(friends)):
    print(friends[k])
    k = k + 1

# 2. For Loop
l = [3, 4, 235, 23 , 545]
for number in l:
    print(number)

# 3. Range 
for m in range(8): # start with o to 7
    print(m)
for m in range(2, 8): #start with 2 t0 7
    print(m)    
for m in range(1, 8, 2): #start with 1 t0 7 but every 2nd number is step size
    print(m) 

# 4. For with else
for n in range(1,11):
    print(n)
else:
    print("This is it...") # its print when the loop will end the range

# 5. Break Statement
for o in range(10):
    print(o)
    if o == 6:
     break  

# 6. Continue Statement
for p in range(10):
    if p == 6:
     continue  
    print(p)

# 7. pass  Statement (Pass is null statement in python)
q = 50
if q > 70:
    pass # it is used to ...if , while , for 
    print("kap is a coder")

# question(1) print a multiplication of a given number using for loop 
num = int(input("Enter your number : "))
for a in range (1, 11):
    # print(str(num) + " X " + str(a) +  " = " + str(num*a))  # OR
    print(f"{num}X{a}={num*a}")
    
# question(2) Greet that person which name is start with "K"
l1 = ["harry", "kapil", "akshay", "vishal", "kap"]
for name in l1:
    if name.startswith('k'):
        print("hello "  +  name)

# question(3) find the number is prime or not
num1 = int(input("Enter the Number : "))
prime = True
for b in range(2, num1):
    if(num1%b == 0):
        prime = False
        break
if prime:
        print(num1 ," is a prime number")    
else:
        print(num1 ," is not a prime number")

# # question(4) factorial of the given number
# num2 = int(input("Enter the Number : "))
# factorial = 1
# for c in range( 1 , num2+1):
#     factorial = factorial * c
# print (factorial)

# question(5) print a multiplication of a given number using for loop reverse order 
num = int(input("Enter your number : "))
for t in range (10, 0, -1):
    # print(str(num) + " X " + str(t) +  " = " + str(num*t))  # OR
    print(f"{num}X{t}={num*t}")
