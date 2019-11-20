#%%

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
        
