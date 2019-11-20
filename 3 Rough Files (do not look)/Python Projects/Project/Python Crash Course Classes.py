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
restaurant3 = Restaurant('ben)