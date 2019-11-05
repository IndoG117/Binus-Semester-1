#%%
def encrypt1(param, keys):
    comb = ""
    for ch, key in zip(param,keys):
        comb += str(chr(ord(ch)+key))
        print(ch,key)
    return comb

param = "Hi there"
keys = [33,45,55,67,74,88,90,100,110]

comb = encrypt(param,keys)
print(comb)

tkst = input("Enter sentence to encrypt in numbering: ")
tkst_list = []
for i in range(len(tkst)):
    tkst_list.append(ord(tkst[i]))
print("".join(map(str, tkst_list)))


def filter_long_words(lwords, n):
    return [i for i in lwords if len(i) > n]

print(filter_long_words(['one', 'two', 'three'], 2))


def histogram(lst):
   for i in lst:
       print('*' * i)
        
histogram([4,9,7])
#%%
def translate(txt):
    vowels = "aeiou"
    ret = ""
    for c in txt:
        ret += c
        if c.isalpha() and c.lower() not in vowels: 
            ret += 'o' + c
    return ret

#%%
val = (input('Enter a key: '))
list_2 = ['a','b','c',1,2,3]
def is_member(val):
    n=(-1)
    while val != list_2[n]:
        n += 1
        if val == list_2[n]:
            print(True)
            break
        elif n == (len(list_2)-1):
            print(False)
            break
is_member(val)

def n7():
    val = input("Enter thingy : ")
    result = list(map(len,val.split()))
    print(val.split())
    print(result)
n7()
#%%

import string

def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = list(string.ascii_lowercase)
    for i in sentence:
        if i in alphabet:
            alphabet.remove(i)
    return len(alphabet) == 0

print(is_pangram('The quick brown fox jumps over the lazy dog'))
#%%