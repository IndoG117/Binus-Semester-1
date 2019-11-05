name = input("Enter your name >> ")
#%%

age = eval(input("Enter your age >>"))
type(age)
#%%
Feet = eval(input("Enter your height in feet >>"))
Inches = eval(input("Enter your height remainder in inches >>"))
# 12 inches in a foot
# 2.54 cm in an inch
print("Suggested Board Length is:",((Inches*2.54 + Feet*12*2.54)/100)*88)
#%%
# F = m x a
# find a
mass, force = eval(input("Enter mass in kg and force in N >>"))
print("the acceleration is",(force/mass))
#%%
print("Hello, how would u like ur name to be displayed?")
print("1 - All lowercase")
print("2 - All uppercase")
print("3 - First letter capitalized")
name = input("Enter your name to see the options >>")
options = f"1 {name.lower()} 2 {name.upper()} 3 {name.title()}"
print("le options:", options)
choice = input("so, which number do you choose?")
if(choice == "1"): 
    print(f"Well hello {name.lower()}")
if(choice == "2"):
    print(f"Well hello {name.upper()}")
if(choice == "3"):
    print(f"Well hello {name.title()}")
#%%
print("Enter a password")
print("Password must be at least 8 characters in length")
password = input("Your Password >>")
password = password.replace("a","x")
password = password.replace("e","x")
password = password.replace("i","x")
password = password.replace("o","x")
password = password.replace("u","x")
password = password.replace("A","x")
password = password.replace("E","x")
password = password.replace("I","x")
password = password.replace("O","x")
password = password.replace("U","x")
if(len(password)<8):
    print("Password not valid.")
elif("xx" in password):
    print("Password not valid.")
elif("XX" in password): 
    print("Password not valid.")
else:
    print("here is your new password:" ,password)
#%%
degrees = input("angle in degrees >>")
print("radians is",eval(degrees)*(3.14/180))
#%%
student1 = input("score of student 1:")
student2 = input("score of student 2:")
student3 = input("score of student 3:")
print(student1)
print(student2)
print(student3)
average = ((eval(student1)+eval(student2)+eval(student3))//3)
print("average is:",average)
#%%
#classes 32 45 51, groups 5 7 6
class1 = input("class 1 size:")
class2 = input("class 2 size:")
class3 = input("class 3 size:")
print(class1)
print(class2)
print(class3)

print(eval(class1)//5)
print(eval(class2)//7)
print(eval(class3)//6)

print(eval(class1)%5)
print(eval(class2)%7)
print(eval(class3)%6)
#%%
# velo 343 freq 256
velocity = input("velocity:")
frequency = input("frequency:")
wavelength = (eval(velocity)/eval(frequency))

print("velocity:",velocity)
print("frequency:",frequency)
print("wavelength:",wavelength)
#%%
# function version problem 2
x = 80
y = 90
z = 66.5

def studaverage(x,y,z):
    average = ((x+y+z)//3)
    print(average)
    
studaverage(x,y,z)
#%%
x=32
xr=5
#5
y=45
yr=7
#7
z=51
zr=6
#6

def memrem(x,xr,y,yr,z,zr):
    a,b=divmod(x,xr)
    print("members:",a,"reminder:",b)
    a,b=divmod(y,yr)
    print("members:",a,"reminder:",b)
    a,b=divmod(z,zr)
    print("members:",a,"reminder:",b)
    
memrem(x,xr,y,yr,z,zr)
#%%

f=256
v=343

def findwavel(f,v):
    print(v/f)

    
    
findwavel(f,v)
#%%
def f(x):
    return x + 2,x*2

x,y=f(5)
print(x+y)
#%%
def calc_q1(x):
    q=4*x+1  
    return q

calc_q1(5)
print(q)
#%%
def calc_q2(x):
    q=4*x+1
    
print(q)
q=calc_q2(5)
#%%
q=20 
def calc_q3(x):
    q=4*x+1
    return q

q=calc_q3(5)
print(q)
#%%
def calc_q4(x):
    q=4*x+1
print(calc_q4(5))
#%%
def=5 + 6 % 7
print(def)
#%%
def get_input():
    x=float
#%%

def get_days(a,b,c):
    print("days:", round((a*60*60 + b*60 + c)/86400, 4))

def convert_to_days():
    hours=eval(input("Enter hours:"))
    minutes=eval(input("Enter minutes:"))
    seconds=eval(input("Enter seconds:"))
    get_days(hours,minutes,seconds)
   
    
#%%
a = range (1,100,5)
b = [1,2,3,4]
for element in b:
    element = element + 1
    print(element)
#%%
#boodoo
a = range (1,50)
for element in a:
    if ((element % 3) == 0):
#%%
b = [38,39,63,18] 
print(sum(b)/len(b))
#%%
b = [38,39,63,18] 
print(max(b))
#%%
#output=equivweight
#input=earthweight,planetgravity
#earthw = mass*9.8
#mass = earthw / 9.8
#equivw = mass*gravity
#equivw = (earthw/9.8)*plgrav
#return equivw

def calc_weight_on_planet(earthw,plgrav=None):
    if plgrav is None:
        print((earthw/9.8)*23.1)
    else:
        equivw = (earthw/9.8)*plgrav
        return equivw
#%%
#output=number of atoms in n grams of element x (default gold)
#inputs=ngramsofelement, optional atomic weight
def num_atoms(grams,atomw=None):
    avog = (6.02*10**23)
    if atomw is None:
        print((grams / 196.97)*avog)
    else:
        print((grams / atomw)*avog)
#%%
#output=new height to preserve aspect ratio
#input=old width, old height, new width
#variables= ratio number(oldwith/oldheight)
#result=deswidth/rationumber
        
def calc_new_height():
    oldwidth = eval(input("enter old witdth:"))
    oldheight = eval(input("enter old height:"))
    deswidth = eval(input("enter desired width:"))
    ratio = oldwidth / oldheight
    print("the new height should be:",(deswidth/ratio))
#%%
#convert_temp(),convert_to_celcius(f),convert_to_kelvin(c)
#celcius=(5/9)*(f-32)
#kelvin=c+273.15

def convert_to_celsius(y):
    cels = ((5/9)*(y-32))
    print(cels)
    
def convert_to_kelvin(x):
    kelv = (x + 273.15)
    print(kelv)
    
    

def convert_temp():
    fahr = eval(input("enter temp in fahrenheit:"))
    def convert_to_celsius(fahr):
        cels = ((5/9)*(y-32))
        print(cels)
        def convert_to_kelvin(cels):
            kelv = (x + 273.15)
            print(kelv)
#%%

n = str(input("what is my name? :"))
while (n != "gadtardi"):
    print(n, "is not my name, try again")
    n = str(input("what is my name? :"))
    
print("okay, correct guess")
#%%
#Flow Control Exercises
#def max(x,y)
def Max(x,y):
    if x >= y:
        print(x)
    else:
        print(y)
#%%
def max_of_three(x,y,z):
    if x >= y and x >= z:
        print(x)
    elif y > z and y > x:
        print(y)
    else:
        print(z)
#%%
def Len(string):
    x = 0
    for elements in string:
        x = x + 1
    print(x)
#%%
def vowel(letter):
    if letter in ["a","e","i","o","u"]:
        print(True)
    else:
        print(False)
#%%
#Score Grade

score = float(input("input score:"))
if (score < 0.0 and score > 1.0):
    print("error")
elif (score >= 0.9):
    print("A")
elif (score >= 0.8):
    print("B")
elif (score >= 0.7):
    print("C")
elif (score >= 0.6):
    print("D")
elif (score < 0.6):
    print("F")
    
#%%
w = ['B','A','D'] + ['a','b','c']
l = len(w)
a = w.sort(reverse = True)
print(w)

#%%
def multiply_list(start,stop):
    product = 1
    for element in range(start,stop):
        product = product*element
    return product
x = multiply_list(1,4)
#%%
def f3(x,y):
    print(x,y)
    return[x,y]
#%%
def f5(x,y):
    return [x,y]
    print([x,y])
#%%
xlist = [3,2,1,0]
for item in xlist:
    print(item,end=" ")
#%%
a = 1
b = 2
xlist = [a,b,a+b]
a = 0
b = 0
print(xlist)
#%%
def encrypt(param, keys):
    comb = ""
    for ch, key in zip(param,keys):
        comb += chr(ord(ch)+key)
        print(ch,key)
    return comb

def decrypt(param, keys):
    comb = ""
    for ch, key in zip(param,keys):
        comb += chr(ord(ch)-key)
        print(ch,key)
    return comb

param = 'Hi there'
keys = [33,45,55,67,74,88,89,90]
#%%
def encrypt(param, keys):
    comb = ""
    for ch, key in zip(param,keys):
        comb += chr(ord(ch)+key)
        print(ch,key)
    return comb

param = 'Hi there'
keys = [33,45,55,67,74,88,89,90]
#%%
#simple calculator
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

#%%
def factorial(number):
    if (number > 1):
        print(number)
        return number*factorial(number-1)
    else:
        return number

print (factorial(4))

#%%
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
  

  
print(fibonacci(9)) 
#%%
def fibonacci2(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibonacci2(n-1) + fibonacci2(n-2))  
nterms = int(input("How many terms? "))  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for n in range(nterms):  
       print(fibonacci2(n))  
#%%
def findinlist(x,li_input):
    for i in range(len(li_input)):
        if x==li_input[i]:
            return 1

def count:
#%%
# anagrams
def anagram(x,y):
    s1 = x
    s2 = y
    if (sorted(x.lower())==sorted(y.lower())):
        print('is anagram')
    else:
        print('not anagram')
#%%

#def roman_to_arabic():
   # x=print(input("enter roman numeral:"))
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

#%%
#1
def tuple_maker():
    x=[]
    xlist=(input('input list:'))
    x = xlist.split(',')
    print(x)
    print(tuple(x))

    
#%%
#2
def translate(text):
    trans=''
    for letter in text:
        if(letter not in 'AEIOUaeiou '):
            trans += letter + 'o' + letter
        else:
            trans += letter
    return print(trans)
#%%
s = "Jane Doe"
print(s[1])
#%%
def main():
      msg = input("Enter a phrase: ")
      for w in msg.split():
               print(w[0], end="")
main()
#%%
for x in "Mississippi".split("i"):
        print(x, end="")
#%%
s = "absense makes the brain shrink"
x = s.find("s")
y = s.find("s", x + 1)
print(s[x : y])
#%%
phrase = input("Enter a phrase: ")
ascii_sum = 0 # accumulator for the sum
for ch in phrase:
       ascii_sum = ascii_sum + ord(ch)
print(ascii_sum)

#%%
positiondict = {A1,A2,A3,A4,A5,A6,A7,A8}

#%%
def chess():
    chessboard = 8,8,8,8,8,8,8,8,
    for i in chessboard:
        chessresult = print(('- ')*i)
        
def positioning():
    xaxislist = 'ABCDEFGH'
    li
#%%
#30-9-19
def wordcatcher():
    string = input('input a long string of words:')
    dictionary = {}
    print(string.split())
    
    for word in string.split():
        dictionary[word] = dictionary.get(word,0)+1
    
    for key in dictionary:
        print(dictionary[key], key)
        
#%%
def wordcatcher():
    string = input('input a long string of words:')
    dictionary = {}
    for word in string.split():
        if word not in dictionary:
            dictionary[word] = 1
    print(dictionary)

#%%

#Exercise 1
#Try to do the following:
# Add a key to inventory called 'pocket'.
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# .sort()the items in the list stored under the 'backpack' key.
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key.
#Terranexus
#metrona

inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
pocketlist = ['seashell', 'strange berry', 'lint']
inventory['pocket'] = pocketlist
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
    
print(inventory)

#%%

fruitmenu = {}
fruitmenu['banana'] = 4,1
fruitmenu['apple'] = 2,2
fruitmenu['orange'] = 1.5,3
fruitmenu['pear'] = 3,4
print(fruitmenu)
total = ''
for fruit in fruitmenu:
    print(fruit)
    print('price:', fruitmenu[fruit][0])
    print('stock:', fruitmenu[fruit][1])
    print('total:',fruitmenu[fruit][0]*fruitmenu[fruit][1])
for fruit in fruitmenu:
fruittotal = fruit

#%%
# 1.
keylist = ['apples','oranges','peaches','lemons']
mydict = {'apples': 0,'oranges': 0,'peaches': 0,'avocados':0}

def removekeys(mydict,keylist):
    for ele in keylist:
        if ele in mydict:
            del mydict[ele]
            
    print(mydict)
#%%
# 2.
users = {'gadtardi':'henl0','mika':'roblox','stanly':'Godeater'}


def accept_login(users,username,password):
    username = input('enter username:')
    password = input('enter password:')
    if users.get(username) == password:
        print('login successful') 
    else:
        print('login unsuccessful, please try again')

#%%

import random

dollaramt = [1000,5000,10000,25000,50000,75000,100000,200000,
             300000,400000,500000,750000,1000000]
random.shuffle(dollaramt)

briefcases = dict()

index = 1
for amt in dollaramt:
    briefcases[index] = amt
    index = index + 1

print (briefcases)


while (len(briefcases) > 1):
  selection = int(input('select which briefcase:'))
  print(briefcases.keys())
  if selection in briefcases:
     print(briefcases[selection])
     del briefcases[selection]
     offer = ((sum(briefcases.values()))/(len(briefcases)))
     print("the banker offers:",offer)
  else:
      print('briefcase already chosen/not valid number')

  
print(briefcases)

#%%

#bruh moment generator

import matplotlib

import pylab

x = [1,2,3,4]
y = [1,2,3,4]

from pylab import plot, show



plot(x,y,marker="*")

jaktemp2019 = [30.5,30.5,31.5,32.5,30.5,30.5,31.5,32.5,30.5,30.5,31.5,32.5,]

months = range(1,13)

plot(months, jaktemp2019,marker="*")

#%%

import csv
import matplotlib.pyplot as plt
filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\death_valley_2014.csv'

reader = csv.reader(filename)
highs,lows =[],[]
high,low = 0,0
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    print(headerRow[0])
    nextRow = next(reader)
    print(nextRow[0])
except ValueError:
    
    
    for row in reader:
        low = float(row[0])
        high = float(row[1])
        lows.append(low)
        highs.append(high)
    print(lows)
    print(highs)

plt.plot(highs, label='highs')
plt.plot(lows, label='lows')
plt.title('jak temp highs lows 2018')
plt.xlabel('month')
plt.ylabel('temperature (C)')
plt.fill_between(range(1,366),highs,lows,facecolor = 'green', alpha = 0.3)
plt.legend(loc = 'upper left')


plt.show

#%%

import json

filename = r'C:\Users\Djagad P. Dwialam\Documents\color.json'
list_of_color = []
with open(filename) as f:
        color_json = json.load(f)
        list_of_color = color_json['colors']
print (list_of_color)

#def find_a_color(color_name):

     

#choice = input('find a color:')
#print (find_a_color(choice))

#find color
#find by rgb
#save new color
#save to json file

#def find_a_color(color_name):
    #for a_color in list_of_color:
        #if (a_color["color"] == color_name):
            #return a_color

#def find_a_color_by_rgb (r,g,b):
    #how

#def find_a_similar_color(color):
 # e.g. blue and sky blue
 
 
#developer.twitter.com
#json formatter
    
#%%
import json

filename = r'C:\Users\Djagad P. Dwialam\Documents\color.json'
list_of_color = []
with open(filename) as f:
        color_json = json.load(f)
        list_of_color = color_json['colors']
        print (list_of_color)
        
def find_a_color():
    color_name = input('find a color:')
    for a_color in list_of_color:
        if(a_color["color"] == color_name):
            return a_color

def find_by_rgb():
    rgbselect = []

#%%

import json
from datetime import datetime

with open(r'C:\Users\Djagad P. Dwialam\Documents\tweet1.txt') as json_file:
    data_list = json.load(json_file)

print(data_list)
timestamp = time.time()
dt_object = datetime.fromtimestamp(timestamp)

newtweet = input('insert new tweet:')
data_list['text'] = newtweet
data_list['created_at'] = str(dt_object)


with open(r'C:\Users\Djagad P. Dwialam\Documents\tweetout.txt', 'w+') as outfile:
    json.dump(data_list, outfile, indent = 4)

#%%
from datetime import datetime
import time

timestamp = time.time()
dt_object = datetime.fromtimestamp(timestamp)
print("dt_object =", dt_object)
#%%

filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\sitka_weather_07-2014.csv'

with open(filename) as data_source:
    data_inside = data_source.read()
    print(data_inside)

#%%
import csv
from matplotlib import pyplot as plt


filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\sitka_weather_07-2014.csv'

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    header_row = next(reader)
    print(header_row)
    

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)
    
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs, c='blue')

plt.title('daily high temps, jul 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('temp (f)',fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()

#%%
from datetime import datetime
first_date = datetime.strptime('20-09-1995', '%d-%m-%Y')
print(first_date)

#%%
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\sitka_weather_07-2014.csv'

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    header_row = next(reader)
    print(header_row)
    
    
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    print(highs)
    
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='blue')

plt.title('daily high temps, jul 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('temp (f)',fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()

#%%

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\sitka_weather_2014.csv'

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    header_row = next(reader)
    print(header_row)
    
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        
        high = int(row[1])
        highs.append(high)
        
        low = int(row[3])
        lows.append(low)

    print(highs)
    
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='blue', alpha=0.5)
plt.plot(dates, lows, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('daily high and low temps, 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('temp (f)',fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()

#%%
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\death_valley_2014.csv'

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    header_row = next(reader)
    print(header_row)
    
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    
    
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='blue', alpha=0.5)
plt.plot(dates, lows, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('daily high and low temps, 2014', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('temp (f)',fontsize=16)
plt.tick_params(axis='both', which='major',labelsize=16)

plt.show()

#%%
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\activity.csv'

with open(filename) as csvfile:
    reader = csv.reader(csvfile)
    header_row = next(reader)
    print(header_row)

    steps = []
    for row in reader:
        steps.append(row[0])
    print(steps)

#%%
    
import matplotlib.pyplot as plt
import numpy as np
import statistics
import csv

file = open(r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\activity.csv')
csvReader = csv.reader(file)


def getStepsPerDay(file, reader):
    next(reader)
    steps = []
    stepsToday = 0
    acc = 0
    while True:
        try:
            acc += 1
            step = next(reader)[0]
            stepsToday += int(step) if step != "NA" else 0
            if acc % 288 == 0:
                steps.append(stepsToday)
                stepsToday = 0
        except StopIteration:
            break
    file.seek(0)
    return steps


def getMedianMeanPerDay(file, reader):
    next(reader)
    medianPerDay = []
    meanPerDay = []
    stepToday = []
    acc = 0
    while True:
        try:
            acc += 1
            step = next(reader)[0]
            stepToday.append(int(step) if step != "NA" else 0)
            if acc % 288 == 0:
                stepToday.sort()
                medianPerDay.append(statistics.median(stepToday))
                meanPerDay.append(statistics.mean(stepToday))
                stepToday = []
        except StopIteration:
            break
    file.seek(0)
    return medianPerDay, meanPerDay


def makePlot(steps, median, mean):
    x = [x+1 for x in range(len(steps))]
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Activity')
    ax1.set_title("Steps")
    ax1.plot(x, steps)
    ax2.set_title("Median")
    ax2.plot(x, median)
    ax3.set_title("Mean")
    ax3.plot(x, mean)
    plt.tight_layout()
    plt.show()


steps = getStepsPerDay(file, csvReader)
median, mean = getMedianMeanPerDay(file, csvReader)
# print(mean)

makePlot(steps, median, mean)

#%%
import csv
import datetime as dt
import statistics as st
import matplotlib.pyplot as plt


filename = r'C:\Users\Djagad P. Dwialam\Downloads\201910080755170860002405_CSVFiles\activity.csv'

dict = {}
dictInterval = {}
dictIntervalweekDays = {}
dictIntervalWeekEnds = {}


with open (filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        if (steps != 'NA'):
            date = row[1]
            date2 = int(dt.datetime.strptime(date, '%Y-%m-%d').day)
            interval = int(row[2])
            
            dict.setdefault(str(date),[])
            dict[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps))
            
            

            
listDate = []
listTotal = []
listAve = []

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))
    
plt.hist(listTotal)
plt.show()

print(dictInterval)



#%%

import matplotlib.pyplot as p

string = 'indonesia raya merdeka merdeka'
string_list = string.split()
string_dict = {}

print (string_list)

for word in string_list:
    if word in string_dict:
        string_dict[word] = string_dict[word] + 1
    else:
        string_dict[word] = 1

print(string_dict)

count_list = string_dict.values()
indentation = list(range(1,len(count_list)+1))
#if invoked at the same time, then values and keys will be in order
#check matplotlib.pyplot library functions
b1 = p.bar(indentation, count_list)
p.xticks(indentation, string_dict.keys())
p.show()

#%%

import matplotlib.pyplot as p


with open(r'C:\Users\Djagad P. Dwialam\Documents\hello there.txt') as file_object:
     contents = file_object.read()

string = contents
string_list = string.split()
string_dict = {}

print (string_list)

for word in string_list:
    if word in string_dict:
        string_dict[word] = string_dict[word] + 1
    else:
        string_dict[word] = 1

print(string_dict)

count_list = string_dict.values()
indentation = list(range(1,len(count_list)+1))
#if invoked at the same time, then values and keys will be in order
#check matplotlib.pyplot library functions
b1 = p.bar(indentation, count_list)
p.xticks(indentation, string_dict.keys())
p.show()
#%%
class dog():
#%%
import math
def combination(n,r):
    nf = math.factorial(n)
    rf = math.factorial(r)
    nrf = math.factorial(n-r)
    #x = (math.factorial(n))/(math.factorial(r))*(math.factorial(n-r))
    return nf / rf * nrf

# sir stavin wa 08111099302
#%%
#23-24 nov
# - IDR 350
# Wombat Comserv
#%%
class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self,name,age):
        """initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(self.name.title() + "rolled over!")

#%%
import pygame
from pygameship import Ship

class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.ship = Ship(self)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False    
            
    
    def _update_screen(self):
        self.screen.fill((0,0,0))
        self.ship.blitme()
        pygame.display.flip()
        
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

if __name__ == "__main__":
    mg = MainGame()
    mg.run_game()
















