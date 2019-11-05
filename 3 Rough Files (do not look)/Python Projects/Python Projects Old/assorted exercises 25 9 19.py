# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:20:53 2019

@author: Gadtardi Wongkaren
"""

#1.
def tuple_maker():
    x=[]
    xlist=(input('input list:'))
    x = xlist.split(',')
    print(x)
    print(tuple(x))

#%%
#2.
def translate(text):
    trans=''
    for letter in text:
        if(letter not in 'AEIOUaeiou '):
            trans += letter + 'o' + letter
        else:
            trans += letter
    return print(trans)
#%%
#3

#%%
#4

#%%
#5

#%%
#6
def histogram(lst):
   for i in lst:
       print('*' * i) 

#%%
#7

#%%
#8

#%%
#9
def filter_long_words(lwords, n):
    return [i for i in lwords if len(i) > n]

print(filter_long_words(['one', 'two', 'three'], 2))

#%%
#10

#%%
#11

#%%
#12
def shiftalp(chr_value,num):
    z=ord(chr_value)
    if(123>z>96):
        z+=num
        if (z>122):
            z-=26
        return chr(z)
    

#%%
#13

#%%
#14

