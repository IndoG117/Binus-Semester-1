# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 06:33:00 2019

@author: Gadtardi Wongkaren
"""

#%%
#Task 1: Simple Calculator
firstNum = input("enter first number:")
secNum = input("enter second number:")

def addition(num_1, num_2):
    return eval(num_1) + eval(num_2)

print (addition(firstNum,secNum))

def subtraction(num_1, num_2):
    return eval(num_1) - eval(num_2)


print (subtraction(firstNum,secNum))

def multiplication(num_1, num_2):
    return eval(num_1)*eval(num_2)

print (multiplication(firstNum,secNum))

def division(num_1, num_2):
    return eval(num_1)/eval(num_2)

print (division(firstNum,secNum))

#%%
#Task 2: Factorial Calculation
def factorial(number):
    if (number > 1):
        print(number)
        return number*factorial(number-1)
    else:
        return number
#%%
#Task 3: Fibonacci
def fibonacci(n):
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
  

#%%
#Task 4: Counting elements in a string
def findinlist(x,li_input):
    for i in range(len(li_input)):
        if x == li_input[i]:
            return i

def countletter(str_input):
    a=[]
    b=[]
    for i in str_input:
        if i not in a:
            a.append(i)
            b.append(1)
        else:
            x=findinlist(i,a)
            b[x]+=1
    for i in range(len(a)):
        print(a[i],"=",b[i])


#%%
#Task 5: anagrams
def anagram(x,y):
    s1 = x
    s2 = y
    if (sorted(x.lower())==sorted(y.lower())):
        print('is anagram')
    else:
        print('not anagram')
#%%
#Task 6.1: Roman to Arabic
    romabdict = {"I" : 1,
    'II' : 2,
    'III' : 3,
    'IV' : 4,
    'V'  : 5,
    'VI' : 6,
    'VII' : 7,
    'VIII' : 8,
    'IX' : 9,
    'X' : 10,
    'XI' : 11,
    'XII' : 12,
    'XIII' : 13,
    'XIV' : 14,
    'XV' : 15,
    'XVI' : 16,
    'XVII' : 17,
    'XVIII' : 18,
    'XIX' : 19,
    'XX' : 20}
    
    def roman_to_arabic(x):
        y=''
        y = romabdict[x]
        print(y)

#%%
#Task 6.2: Arabic to Roman
def arab_to_roman(x):
    arab_list=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_list=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    i=0
    while(x!=0):
        if(x>=arab_list[i]):
            x-=arab_list[i]
            print(roman_list[i],end='')
        else:
            i+=1