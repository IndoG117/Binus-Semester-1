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
print("4 - play Thermonuclear Warfare and destroy the world *jk*")
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
flag = 0
if(len(password)<8):
    flag = -1
if flag ==-1:
    print("Password not valid.")
    

    