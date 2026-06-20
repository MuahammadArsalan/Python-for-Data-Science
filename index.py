
#Variable

#print("Hello world");


'''
x = 5
y = "John"
print(x)
print(y)
'''

'''

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
'''

'''x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x);
print(y);
print(z);'''

'''x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
'''

'''fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

'''



#Simple Calculator

'''num1 = float(input("Enter first number"));
num2 = float(input("Enter second number"));
print("num1 = ",num1);
print("num2 = ",num2);

op = input("select operation + ,- ,* ,/")

if op == "+":
    print("Sum is " , num1+num2);
 
elif op ==" -":
    print("difference is " , num1-num2);
 
elif op == "*":
    print("Multiple is " , num1*num2);
 
elif op == "/":
    print("Division is " , num1/num2);
else:
    print("Invalid operation");


'''


'''num1 = float(input("1 number: "))
num2 = float(input("2 number: "))
num3 = float(input("3 number: "))

if num1 > num2 and num1 >num3 :
    print(num1)
elif num2 > num1 and num2 >num3:
    print(num2)
elif num3 > num1 and num3 >num2:
    print(num3)
else:
    print("trio are equal")    

'''
# print 1-100 numbers
'''
for x in range(1,101):
    print(x)

'''


# print 1-100 even numbers
'''
for x in range(1,101):
    if x % 2 == 0:
        print(x)
'''


#Pritning Table

'''
num = int(input("Number enter karo: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
'''

#fabonacci
'''n = int(input("Kitne terms chahiye? "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b'''



#Remove dulicate
'''
numbers = [10, 20, 20, 30, 40, 40, 50]

unique = list(set(numbers))

print(numbers)
print(unique)'''


'''
numbers = [10, 20, 20, 30, 40, 40, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)



'''

#Dictionaries

'''Arsalan = {
    "name" :"arsalan",
    "age" :20,
    "country" :"Pakistan",

}
print(Arsalan["name"])
Arsalan.pop("country")
print(Arsalan);'''

'''text = input("Enter sentence: ")

words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
'''

total = 0
count = 0
with open("myFile.txt","r") as file:
  for line in file:
     name, marks = line.strip().split(",")
     total += int(marks )
     count += 1



print(total)
print(count)
print("avg == ",total/count)
