#%%

class Dog():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!")
        
my_dog = Dog('willie', 6)

print("my dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)

print("your dog's name is " + your_dog.name.title() + ".")
print("your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

#%%

#9-1

class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("the resto is called " + self.restaurant_name + " and it serves " + self.cuisine_type)
        
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")
        
restaurant = Restaurant('Mcd','american')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('Hokben','Japanese')
restaurant3 = Restaurant('bensu','indonesian')

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

#%%

class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('this car has ' + str(self.odometer_reading) + ' miles on it.')
        
    
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#%%

class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
        else:
            print('u cant  reverse an odometer!')
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def get_descriptive_name(self):
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('this car has ' + str(self.odometer_reading) + ' miles on it.')
        
    
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()





#%%

class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
        else:
            print('u cant  reverse an odometer!')
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def get_descriptive_name(self):
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('this car has ' + str(self.odometer_reading) + ' miles on it.')
        
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print('this car has a ' +str(self.battery_size) + ' -kWh battery.')
             
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = 'this car can go approximately '+ str(range)
        message += ' miles on a full charge.'
        print(message)



class ElectricCar(Car):
    
    def fill_gas_tank():
        print('this car doesnt need a gas tank!')
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
    
        

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#%%

#9-1

class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("the resto is called " + self.restaurant_name + " and it serves " + self.cuisine_type)
        
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")
        
restaurant = Restaurant('Mcd','american')

restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2

restaurant2 = Restaurant('Hokben','Japanese')
restaurant3 = Restaurant('bensu','indonesian')

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

#%%
#9-3

class User():
    
    def __init__(self,first_name,last_name,dob,fav_color):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.fav_color = fav_color
        
    def describe_user(self):
        print("the user's name is " + self.first_name + " " + self.last_name)
        print("the user's date of birth is " + self.dob)
        print("the user's favorite color is " + self.fav_color)
        
    def greet_user(self):
        print("hello " + self.first_name + ", the weather outside is feeling kinda " + self.fav_color + " isnt it?")

gadtardi = User('Gadtardi','Wongkaren','20/09/95','blue')

gadtardi.describe_user()

gadtardi.greet_user()


#%%

#9-4

class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
        
    def describe_restaurant(self):
        print("the resto is called " + self.restaurant_name + " and it serves " + self.cuisine_type)
        
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")
    
    def see_number_served(self):
        print(self.restaurant_name + " currently has " + str(self.number_served) + " people served." )
    
    def set_number_served(self,numserved):
        self.number_served = numserved
        
    def increment_number_served(self,newserved):
        self.number_served += newserved
    
    
        
#        
        
mcd = Restaurant('Mcd','american')

mcd.see_number_served()
mcd.set_number_served(30)
mcd.see_number_served()
mcd.increment_number_served(3)
mcd.see_number_served()

#%%

#9-5

class User():
    
    def __init__(self,first_name,last_name,dob,fav_color):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.fav_color = fav_color
        self.login_attempts = 0
        
    def describe_user(self):
        print("the user's name is " + self.first_name + " " + self.last_name)
        print("the user's date of birth is " + self.dob)
        print("the user's favorite color is " + self.fav_color)
        
    def greet_user(self):
        print("hello " + self.first_name + ", the weather outside is feeling kinda " + self.fav_color + " isnt it?")

    def see_login_attempts(self):
        print("there are " + str(self.login_attempts) + " login attempts")

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        






gadtardi = User('Gadtardi','Wongkaren','20/09/95','blue')

gadtardi.increment_login_attempts()
gadtardi.increment_login_attempts()

gadtardi.see_login_attempts()


gadtardi.reset_login_attempts()
gadtardi.see_login_attempts()


#%%

#9-6

class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
        
    def describe_restaurant(self):
        print("the resto is called " + self.restaurant_name + " and it serves " + self.cuisine_type)
        
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")
    
    def see_number_served(self):
        print(self.restaurant_name + " currently has " + str(self.number_served) + " people served." )
    
    def set_number_served(self,numserved):
        self.number_served = numserved
        
    def increment_number_served(self,newserved):
        self.number_served += newserved
        
        
class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'chocolate', 'matcha']
    
    def listflavors(self):
        print("available flavors are " + str(self.flavors))
        

benNjerrys = IceCreamStand("Ben and Jerry's","liberal american")

benNjerrys.listflavors()  

#%%

#9-7

class User():
    
    def __init__(self,first_name,last_name,dob,fav_color):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.fav_color = fav_color
        self.login_attempts = 0
        
    def describe_user(self):
        print("the user's name is " + self.first_name + " " + self.last_name)
        print("the user's date of birth is " + self.dob)
        print("the user's favorite color is " + self.fav_color)
        
    def greet_user(self):
        print("hello " + self.first_name + ", the weather outside is feeling kinda " + self.fav_color + " isnt it?")

    def see_login_attempts(self):
        print("there are " + str(self.login_attempts) + " login attempts")

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
        
        
class Admin(User):
    
    def __init__(self,first_name,last_name,dob,fav_color):
        super().__init__(first_name,last_name,dob,fav_color)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print(" admin can " + str(self.privileges))
        


gadtardi = Admin('Gadtardi','Wongkaren','20/09/95','blue')

gadtardi.show_privileges()

#%%

#9-8

class User():
    
    def __init__(self,first_name,last_name,dob,fav_color):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.fav_color = fav_color
        self.login_attempts = 0
        
    def describe_user(self):
        print("the user's name is " + self.first_name + " " + self.last_name)
        print("the user's date of birth is " + self.dob)
        print("the user's favorite color is " + self.fav_color)
        
    def greet_user(self):
        print("hello " + self.first_name + ", the weather outside is feeling kinda " + self.fav_color + " isnt it?")

    def see_login_attempts(self):
        print("there are " + str(self.login_attempts) + " login attempts")

    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
        
        
class Admin(User):
    
    def __init__(self,first_name,last_name,dob,fav_color):
        super().__init__(first_name,last_name,dob,fav_color)
        self.privileges = Privileges()
        
    

class Privileges():
    
    def __init__(self):
        self.privilegeslist = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print( "this admin can " + str(self.privilegeslist))

gadtardi = Admin('Gadtardi','Wongkaren','20/09/95','blue')

gadtardi.privileges.show_privileges()

#%%

#9-9

class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
        else:
            print('u cant  reverse an odometer!')
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def get_descriptive_name(self):
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print('this car has ' + str(self.odometer_reading) + ' miles on it.')
        
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print('this car has a ' +str(self.battery_size) + ' -kWh battery.')
             
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = 'this car can go approximately '+ str(range)
        message += ' miles on a full charge.'
        print(message)
        
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85



class ElectricCar(Car):
    
    def fill_gas_tank():
        print('this car doesnt need a gas tank!')
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

#%%

#9-10

class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
        
    def describe_restaurant(self):
        print("the resto is called " + self.restaurant_name + " and it serves " + self.cuisine_type)
        
    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")
    
    def see_number_served(self):
        print(self.restaurant_name + " currently has " + str(self.number_served) + " people served." )
    
    def set_number_served(self,numserved):
        self.number_served = numserved
        
    def increment_number_served(self,newserved):
        self.number_served += newserved
        
        
class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'chocolate', 'matcha']






















