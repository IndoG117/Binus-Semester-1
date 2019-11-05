# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:19:31 2019

@author: Gadtardi Wongkaren

"""
#%%
#Problem 2: Deck of Cards
#Shuffle a deck of cards and print all of its content


from random import shuffle

def printCard():
    shape = ["heart", "spade", "diamond", "club"]
    numbers = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    decklist = []
    for a_shape in shape:
        for a_number in numbers:
             decklist.append(a_shape + " " + a_number)
             shuffle(decklist)
    print(decklist)

printCard()

#%%
#Problem 3: Hangman

def hangman():
    hangword = input("What word/phrase for the hangman game?:")
    print("let the game begin")
    display = []
    used = []
    display.extend(hangword)
    used.extend(display)
    for i in range(len(display)):
        display[i] = '_'
    print(' '.join(display))
    print()
    count = 0
    while count < len(hangword):
       guess = input('please guess a letter:')
       guess = guess.lower()
       print (count)
       for i in range(len(hangword)):
        if hangword[i] == guess and guess in used:
            display[i] = guess
            count = count + 1
            used.remove(guess)
        if guess not in display:
            print('wrong guess!')
       print('you have guessed:',count,'correct letters.')
       print(' '.join(display))
       print()
       if count == len(hangword):
         break
    print('well done, fin')

#%%
#Problem 1: Chess position
    
           

