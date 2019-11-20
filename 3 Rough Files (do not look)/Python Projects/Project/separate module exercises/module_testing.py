#%%

#9-10

from restaurant_module import Restaurant


bensu = Restaurant('ayam geprek bensu','ayam geprek',)

bensu.describe_restaurant()

#%%

#9-11

from user_module import User,Admin,Privileges

gadtardi = Admin('Gadtardi','Wongkaren','20/09/95','blue')

gadtardi.privileges.show_privileges()

#%%

#9-12

from useronly_module import User
from admin_privileges_module import Admin,Privileges




gadtardi = Admin('Gadtardi','Wongkaren','20/09/95','blue')

gadtardi.privileges.show_privileges()