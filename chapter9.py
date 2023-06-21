#  1. use open function to read the file of content 
# f = open('sample.txt', 'r')     
f = open('sample.txt') # by defualt the module is 'r' read
text = f.read()
# text = f.read(5) # print first five letter
print(text)
f.close()
                
#  2. other methods to read the file 
# f = open('sample.txt', 'r')     
f = open('sample.txt') 
text = f.readline() #read first line
print(text) 
text = f.readline() #read second line
print(text) 
text = f.readline() #read third line
print(text)
text = f.readline() #read forth line and so on 
print(text)
f.close()

'''  modules
1. read === 'r'
2. write === 'w'
3. append == 'a'
4. update == '+'
 
in the form of binary then we use rb, wb, +b, ab 
but form of text we dont use  "b" after modules  '''

# 3.  use open function to write and append the content of file
f = open('another.txt', 'w') # automatically create a file and write it there
text = f.write("hello dude how are you ?")
f = open('another.txt', 'a')
text = f.write(" I am good , what about you..?")
print(text)
f.close()

# 4. automatically open and close the file  using "with statement"
with open('another.txt', 'r') as t:
    a = t.read()
with open('another.txt', 'w') as t:
    a = t.write('Hey , what are you doing ..?')    
    print(a)

# ques(1) read the file and find out the word of 'twinkle'
f = open('another.txt' , 'r')
data = f.read()
if ('twinkle') in data:
    print('twinkle is present in the file')
else:
    print('twinkle is not present in the file')    
f.close()

# ques(2) make a function and user return the Hi-score , read a file which is either blank and some data then you need to update the data
def game():
    return 5799
score = game()
with open('another.txt')as p:
    high_score = p.read()
if high_score == '':
    with open ('another.txt', 'w')as f:
        f.write(str(score))
elif high_score<score:
    with open ('another.txt', 'w')as f:
        f.write(str(score))

# ques(3) generate multiplication table 2 to 20 
for i in range(2, 21):
    with open(f"tables/Multiplication_of_{i}.txt", 'w')as q:
        for j in range(1, 11):
            q.write(f"{i} X {j} = {i*j}\n" )
        
#  ques(4)  replace a word into another word
with open('another.txt')as p:
    content = p.read()
content = content.replace("bad", "good")
with open('another.txt', 'w')as p:
    p.write(content)

# ques(5) find the word "python" in log file 
with open('log.txt')as f:
    content = f.read()
if 'python' in content:
    print('Yes, python is present')
else:
    print('No, python is not present')

# # ques(6) find the line number where "python" is written
# con = True
# i = 1
# with open('log.txt')as p:
#     while con:
#         con = p.readline()
#         if 'python' in con:
#             print(con)
#             print(f"python is written in {i} line")
#         i += 1

# ques(7) copy file content into another file
with open("sample.txt") as p:
    content = p.read()
with open("another.txt", 'w')as p:
    p.write(content)

# ques(8) find the identical and matches in two files
with open ('sample.txt')as p:
    cont_1 = p.read()
with open ('another.txt')as p:
    cont_2 = p.read()
    if cont_1 == cont_2:
        print('Both files have same content')
    else : 
        print('Both files have different content')

# ques(9) wipe out the content in file
with open ('another.txt', 'w')as p :
    p.write('')

# ques(10) rename a file 
 