#%%

from useronly_module import User

class Admin(User):
    
    def __init__(self,first_name,last_name,dob,fav_color):
        super().__init__(first_name,last_name,dob,fav_color)
        self.privileges = Privileges()
        
    

class Privileges():
    
    def __init__(self):
        self.privilegeslist = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print("this admin can " + str(self.privilegeslist))