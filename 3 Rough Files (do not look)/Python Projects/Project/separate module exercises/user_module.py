#%%


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
        print("this admin can " + str(self.privilegeslist))

