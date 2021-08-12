# a = int(input())
# print(a*2)
# b = input()
# print(b)



# h = (input())
# h = h.strip("'").split(" ")
# h[0],h[1] = int(h[1]),int(h[0])
# h[0] = int(h[0])*(int(h[2]))
# h[1] = int(h[2])+(int(h[1]))
# print(h[0],h[1])

# n = int(input())

# if (n % 2 == 0) and (2 <= n <= 5):
#     print("Not Weird")
# elif(n % 2 == 0) and (6 <= n <= 20):
#     print("Weird")
# elif(n % 2 == 0) and (n >= 20):
#     print("Not Weird")
# else:
#     print("Weird")

# n = int(input())
# for i in range(1,n+1):
#     print(i,end="")

# a = input("No. of students:")
# b = input("No. of subjects:")
# print(a,b,end=" ")

# c = input("\nMarks of first student: ")
# d = input("\nMarks of second student)

# n, x = map(int, input().split()) 

# sheet = []
# for _ in range(x):
#     sheet.append( map(float, input().split()) ) 

# for i in zip(*sheet): 
#     print( sum(i)/len(i) )
# n = int(input())
# i = 0
# while i < n:
#     print(i**2)
#     i += 1

# n = int(input("Enter a number: "))
# if n > 1:
#     for i in range(2,n):
#         if (n % i) == 0:
#             print(f"{n} is not a prime number")
#             break
#     else:
#         print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")




    # def is_leap(year):
    #     leap = False
        
    #     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
        
    #     return leap

    # year = int(input())

# print(eval(input()))


# def mutate_string(string, position, character):
#     return string[:position] + character + string[position+1:]
# s = input()
# i, c = input().split()
# s_new = mutate_string(s, int(i), c)
# print(s_new)

# l,r,k = map(int,input().split())
# count = 0
# for i in range(l,r+1):
#     if i % k == 0:
#         count += 1
# print(count)

# a,b = map(int,input().split())
# if a <= 23 and 500 <= b <= 1000:
#     print("Take Medicine")
# else:
#     print("Don't take medicine")

# a = (input())
# if len(a) % 3 == 0:
#     print("Yes")
# else:
#     print("No")

# a,b,c = map(int,input().split())
# d = max(a,b,c)
# print(d)

# N = int(input())
# for i in range(1,11):
#     print(N*i)

# a = int(input())
# if a % 3 == 0:
#     print("Yes")
# else:
#     print("No")

# n = int(input())

# if n % 5 != 0:
#     print((n//5) + 1)
# else:
#     print(n//5)

# a = int(input())
# N = (input())
# for i in range(1):
#     print(N)

# t = int(input())
# while t:
#     n = int(input())
#     if n>=2:
#         print('YES')
#     else:
#         print('NO')
#     t -= 1

# N = int(input())
# X = int(input())
# for i  in range(N):
#     Y = int(input())
#     if Y >= X:
#         print("YES")
#     else:
#         print("NO")

# print("Let's see some examples.\n\nDid you notice the empty lines?")
# print("Do you notice\t the tab space?\nDid you see that I have moved to next line?")
# print("Do you want a \" in your text?")
# print("Are you going to store more info about escape sequence in Z:\\\\user\\escape_sequence.txt??")
# #Every print starts with a new line, end can change that behavior by specifying your own character
# print("Did you see I start here", end=" ")
# print("and I end in the same line although from a different print?")
# print("As observed escape sequences help you to format your output.")

# a = int(input("Number_of_days: "))
# Seconds = a *60 *60
# Seconds = a *60 *60 *60
# Seconds = a *24 *60
# Seconds = a *24 *60 *60
# print("Total number of seconds",Seconds)

# def multiplyStrings(self,s1,s2):
#    s1,s2 = map(int,input().split())
#    return s1 * s2
# print(multiplyStrings("self","s1","s2"))

# n = int(input())
# arr = list(map(int,input().split()))
# a = max(arr)
# while max(arr) == a:
#    arr.remove(max(arr))

# print(max(arr))

# n = int(input())
# integer_list = list(map(int, input().split()))
# for i in range(len(integer_list)):
#        integer_list[i] = int(integer_list[i])
# t = tuple(integer_list)
# print(hash(t))

# n = int(input())
# a = set()
# for i in range(n):
#     a.add(input())
# print(a)
# print(len(a))

# n = int(input())
# a = set()
# for i in range(n):
#     a.add(int(input()))
# s = sum(a)
# d = len(a)
# avg = s/d
# print(avg)

# def average(array):
#     return sum(set(arr))/len(set(arr))
# n = int(input())
# arr = list(map(int, input().split()))
# result = average(arr)
# print(result)

# a = float(input("Enter a number:"))
# if a > 0:
#     print(f"{a} is positive number")
# elif a == 0:
#     print(f"{a} is zero")
# else:
#     print(f"{a} is negative number")

# num = int(input("Enter a number:"))
# if num > 1:
#     for i in range(2,num):
#         if num % i == 0 :
#             print(f"{num} is not a prime number")
#             print(i,"times", num//i,"is", num)
#             break
#     else:
#           print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# lower = int(input("Enter a lower number:"))
# upper = int(input("Enter a higher number:"))
# for num in range(lower,upper+1):
#     if num > 1:
#         for i in range(2,num):
#             if(num % i) ==0:
#                 break
#         else:
#             print(num)

# num = int(input("Enter a number:"))
# factorial = 1
# if num < 0 :
#     print("Sorry,factorial does not exist for negative number")
# elif num == 0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial * i
#     print("The factorial of",num,"is",factorial)

#num = int(input("Show the multiplication table of?:"))
#for i in range(1,11):
#    print(num,"x",i,"=",num*i)

'''heros=['spider man','thor','hulk','iron man','captain america']'''
# Length of the list
'''a = len(heros)'''

# Add 'black panther' at the end of this list
'''b = heros.append('black panther')'''

# You realize that you need to add 'black panther' after 'hulk', 
# so remove it from the list first and then add it after 'hulk'
'''c = heros.pop(5)
d = heros.insert(3,'black panther')'''


# Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange
# (because he is cool).Do that with one line of code.
'''heros[1:3] = ['doctor strange']
print(heros)'''

# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions
# available in list)
'''heros.sort()
print(heros)'''

#Create 3 variables to store street, city and country, now create address variable to store entire address.
#Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the 
#address in such a way that the street, city and country prints in a separate line
'''street = "H No 5, Bhawani Dham"
city = "Bhopal"
country = "India"
address = (f'{street}\n{city}\n{country}')
print(address)'''

#Create a variable to store the string "Earth revolves around the sun"
#Print "revolves" using slice operator
#Print "sun" using negative index
'''a = 'Earth revolves around the sun'
b = a[6:14]
print(b)'''

#Create two variables to store how many fruits and vegetables you eat in a day. 
#Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits 
#that you eat everyday. Use python f string for this.
'''x = 10
y = 9
print(f'"I eat {x} veggies and {y} fruits daily"')'''

#I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, 
# the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with 
# new ones and print the new string. Also try to do this in one line.
'''s = 'maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print(s)'''

#Write a program that asks user to enter a city name and it should tell which country the city belongs to

'''india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

a=input("Enter city name: ")

if a in india:
    print(f'{a} belongs to india')
elif a in pakistan:
    print(f'{a} belongs to pakistan')
elif a in bangladesh:
    print(f'{a} belongs to bangladesh')
else:
    print("I don't have knowledge about",a)'''

#Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
#For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai
#and dhaka it should print "They don't belong to same country"
'''india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter first city name: ")
city2 = input("Enter second city name: ")
if city1 in india and city2 in india:
    print(f'{city1} and {city2} belongs to india')
elif city1 in pakistan and city2 in pakistan:
    print(f'{city1} and {city2} belongs to pakistan')
elif city1 in bangladesh and city2 in bangladesh:
    print(f'{city1} and {city2} belongs to bangladesh')
else:
    print("They don't belong to the same country")'''

#Write a python program that can tell you if your sugar is normal or not. Normal fasting level 
#sugar range is 80 to 100.
#1. Ask user to enter his fasting sugar level

'''a=float(input("Enter your fasting sugar level: "))'''

#2. If it is below 80 to 100 range then print that sugar is low

'''if a<80:
    print(f'{a}, it is low')'''

#3. If it is above 100 then print that it is high otherwise print that it is normal

'''elif a>100:
    print(f'{a}, it is high')
else:
    print(f'{a}, it is normal')'''

# exp = [100,200,300,400,500]
# mon = ['Jan','Feb','Mar','Apr','May']
# total = 0
# for i in range(len(exp)):
#     print('Month ',mon[i],'Expend ',exp[i])
#     total = total + exp[i]
# print(total)

# After flipping a coin 10 times you got this result,
'''result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]'''
# Using for loop figure out how many times you got heads
'''count = 0
for i in result:
    if i == 'heads':
        count += 1
print("Heads count is",count) '''

# Print square of all numbers between 1 to 10 except even numbers
'''for i in range(1,11):
    if i%2 == 0:
        continue
    print(i*i)'''

# Lets say you are running a 5 km race. Write a program that,
# Upon completing each 1 km asks you "are you tired?"        
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
'''for i in range(5):
    print(f"you ran {i+1} miles"
    a = input("are you tired?")
    if a == "yes":
        print(f"you didn't finish the race but ran {i+1} miles")
        break
if a == "no":
    print("Congratulations you have finish the race")'''

'''for i in range(4):
    for j in range(7):
        print("$ ",end="")
    print()'''

# for i in range(4):
#     for j in range(i+1):
#         print("# ",end="")
#     print()

# for i in range(10):
#     for j in range(10-i):
#         print("# ",end="")
#     print()

# for i in range(4):
#     for j in range(4-i):
#         print(i+j+1,end="")
#     print()

'''M Pattern'''
# for row in range(0,7):
#     for col in range(0,7):
#         if(col == 0 or col == 6):
#             print("*",end="")
#         elif(row == 1 and (col == 1 or col == 5)):
#             print("*",end="") 
#         elif(row == 2 and (col == 2 or col == 4)):
#             print("*",end="")
#         elif(row == col == 3):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()    

'''H Pattern'''
# for row in range(0,7):
#     for col in range(0,7):
#         if(col == 0 or col == 6):
#             print("*",end="")
#         elif(row == 3 and (col == 2 or col == 4)):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
 
# nums = [11,21,78,98,88]

# for num in nums:
#     if num % 5 == 0:
#         print(num)
#         break
# else:
#     print("not found")

# num = 53
# for i in range(2,num):
#     if num % i == 0:
#         print("Not Prime Number")
#         break
# else:
#     print("Prime Number")

# from array import *

# vals = array('i',[1,3,5,7])
# # vals.reverse()
# newArr = array(vals.typecode,(a*a for a in vals))
# for i in newArr:
#     print(i)

# from array import *
# arr = array('i',[])

# n = int(input("Enter the length of the array "))

# for i in range(n):
#     x = int(input("Enter the value "))
#     arr.append(x)
# print(arr)

'''Searching in array Manual Method'''
# val = int(input("Enter the value you want to search "))

# k = 0
# for e in arr:
#     if e == val:
#         print(k)
#         break
    
#     k +=1

'''Searching in array by function isme loop lagane ki jarurat nhi padeghi
'''
# print(arr.index(val))

''' numpy Library '''

# from numpy import *
# arr = array([1,2,3,4,5,6.5],int)
# print(arr.dtype)
# print(arr)

'''Ways of creating numpy in array 
1. array()
2. linspace()'''

# from numpy import *
# arr = linspace(0,12,2)
# print(arr)

''' 3. arange() '''

# from  numpy import *
# arr = arange(0,20,6)
# print(arr)

''' 4. logspace() '''

# from numpy import*
# arr = logspace(1,10,3)
# print("%.2f"%arr[1])
# print(arr)

''' 5. zeros() '''

# from numpy import *
# arr = zeros(6,int)
# print(arr)

''' 6. ones() '''

# from numpy import *
# arr = ones(5,int)
# print(arr)

''' Adding in Array '''

# from numpy import *
# arr = array([1,2,3,4,5])
# arr = arr + 5
# print(arr)

''' Adding 2 Arrays '''

# from numpy import *
# arr1 = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,10])
# arr3 = arr1 + arr2
# print(arr3)

''' Mathematical Operations '''

# from numpy import *
# arr1 = ([30,40,60,90,0])
# print(sin(arr1))
# print(cos(arr1))
# print(log(arr1))
# print(sqrt(arr1))
# print(sum(arr1))
# print(min(arr1))
# print(max(arr1))

''' Concatenate in array '''

# from numpy import *
# arr1 = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,10])

# print(concatenate([arr1,arr2]))

''' Copying in arrays '''

''' id same hogi '''
# from numpy import *
# arr1 = array([1,2,3,4,5])
# arr2 = arr1
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

''' id different hogi '''

# from numpy import *
# arr1 = array([2,6,8,1,3])
# arr2 = arr1.view()

# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

''' 1. Shallow Copy '''

# from numpy import *
# arr1 = array([2,6,8,1,3])
# arr2 = arr1.view()
# arr1[1] = 7
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

''' 2. Deep Copy '''

# from numpy import *
# arr1 = array([2,6,8,1,3])
# arr2 = arr1.copy()

# arr2[1] = 7
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

''' Matrix in Python '''

# from numpy import *
# arr1 = array([
#                 [1,2,3],
#                 [4,5,6]

#             ])
# print(arr1)
# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)

''' flatten() changes the array into 1D array '''

# from numpy import *
# arr1 = array([

#                 [1,2,3],
#                 [4,5,6]         
            
#             ])
# arr2 = arr1.flatten()
# print(arr2)

''' reshape changes array in different dimensios '''

# from numpy import * 
# arr1 = array([
#                 [1,2,3,4,5,6],
#                 [7,8,9,10,11,12]    
#             ])
# arr2 = arr1.flatten()
# arr3 = arr2.reshape(4,3)
# arr3 = arr2.reshape(2,3,2)
# print(arr3)

''' Matrices in Python '''

# from numpy import *

# m = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
# print(m)
# print(diagonal(m))
# print(m.min())
# print(m.max())

''' Adding 2 Matrices '''

# from numpy import *
# m1 = matrix('1 2 3 ; 4 5 6')
# m2 = matrix('7 8 9 ; 10 11 12')
# m3 = m1 + m2
# print(m3) 

''' Multiplying 2 Matrices '''

from numpy import *
m1 = matrix('1 2 3 ; 4 5 6 ; 9 8 7')
m2 = matrix('7 8 9 ; 10 11 12 ; 13 14 15')
m3 = m1 * m2
print(m3)