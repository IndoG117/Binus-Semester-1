#%%

class Account:
    __balance = 0
    
    def __init__(self,balance):
        self.__balance = balance
    
    def getbal(self): #returns a balance statement to the user
        desc = "Account Balance: Rp. %s" % (self.__balance)
        return desc
    
    def deposit(self, dep): #returns True or False if process is doable
            try:
                if dep <= 0:
                    return False
                else:
                    self.__balance  += dep
                    return True
            except TypeError:
                return False

    def withdraw(self, amt): #returns True or False if process is doable
            try:
                if amt <= 0:
                    return False
                elif amt > self.__balance:
                    return False
                else:
                    self.__balance  -= amt
                    return True
            except TypeError:
                return False
    
    def export(self): #returns the balance
        return self.__balance

class Customer:
    __firstName = ''
    __lastName = ''
    __account = Account(5000)
    
    def __init__(self, fname, lname):
        self.__firstName = fname
        self.__lastName = lname
    
    def getname(self): #greets the user
        desc = 'Welcome to our service %s %s, we hope you enjoy it!' % (self.__firstName, self.__lastName)
        return desc
    
    def bye(self): #says goodbye to the user
        desc = 'Thank you for using our services %s, we hope to see you soon!' % (self.__lastName)
        return desc
    
    def makeaccount(self, bal): #makes a new account for the user
        self.__account = Account(bal)
        
    def getaccount(self): #returns the generated account
        return self.__account

class Bank:
    __customer = []
    __bankName = ''
    
    def __init__(self,name):
        self.__bankName = name
    
    def addcustom(self, fname, lname, password): #appends new customer data
        name = '%s %s' % (fname, lname)
        self.__customer.append({
                "name": name,
                "balance": 5000,
                "password": password
                })
    
    def balupdateadd(self, name, add): #updates bals when depositing
        for i in self.__customer:
            if i["name"] == name:
                i["balance"] = customerdata.getcustomer(prompt).getaccount().export() + add
            else:
                pass

    def balupdatesub(self, name, sub): #updates bal when withdrawing
        for i in self.__customer:
            if i["name"] == name:
                i["balance"] = customerdata.getcustomer(prompt).getaccount().export() - sub
            else:
                pass
            
    def getcustomer(self, name): #gets generated class object Customer()
        for i in customers:
            if i["name"] == name:
                name = name.split()
                customer = Customer(name[0], name[1])
                customer.makeaccount(i["balance"]) #makes a new acc with updated balance
                return customer
        else:
            pass
        
    def loadcustomers(self, cus): #loads a list of dictionaries with customer data
        for i in cus:             
            self.__customer.append(i)
            
    def exportcustomers(self): #returns the newly updated data
        return self.__customer
            
    def customers(self): #returns a list of customers, password and balance
        cus = []         #are ommited
        for i in self.__customer:
           cus.append(i["name"])
        return cus

import json

filename = "banks.json"
banks = []
customers = []

with open(filename) as f_obj:
    bank = json.loads(f_obj.read())
    banks = bank["banks"]        
            
def newbank(name, password): #updates the database of banks to be exported
    banks.append({           #to the banks database
            "name": name,
            "password": password
            })
    with open(filename, 'w') as f_obj:
        f_obj.write(json.dumps({"banks": banks}, indent=2))
        
def newcustomer(name, balance): #updates the database of customers to
    customers.append({          #be exported to the customer database
            "name": name,
            "balance": balance
            })
    with open(database, 'w') as f_obj:
        f_obj.write(json.dumps({"customers": customers}, indent=2))

guest = False
admin = False
login = False

while True:
    logintype = str(input("Login as an:\n1. User\n2. Admin\n>>> "))
    if logintype.lower() in ("admin", "2"):
        admin = True
        break
    elif logintype.lower() in ("user", "guest", "1"):
        guest = True
        break
    else:
        continue

program = False
program2 = False

while admin == True:
    name = str(input("Username: "))
    password = str(input("Password: "))
    for i in banks:
        if i["name"] == name and i["password"] == password:
            database = name + '.json'
            with open(database) as f_obj:
                dataset = json.loads(f_obj.read())
                customers = dataset["customers"]
            customerdata = Bank(name)
            customerdata.loadcustomers(customers)
            program = True
            admin = False
        else:
            continue
            
    if program != True:
        new = str(input("Would you like to make a new account? [Y/N]:\n>>> "))
        if new.lower() in ('y', '1', 'yes'):
            newbank(name, password)           
            customerdata = Bank(name)
            database = name + '.json'
            program = True
            admin = False
            
while program == True:
    command = str(input("Here are a list of commands:\n1. Add Customer\n2. List of Customers\n3. Exit \n>>> "))
    if command.lower() in ('1', 'add', 'add customers'):
        cfname = str(input("First Name: ")) 
        clname = str(input("Last Name: "))
        pword = str(input("Set a password: "))
        customerdata.addcustom(cfname, clname, pword)
        fullname = "%s %s" % (cfname, clname)
        newcustomer(fullname, 5000)
        done = "%s %s has been registered" % (cfname, clname)
        print(done)
    elif command.lower() in ('2', 'list', 'customers'):
        print(customerdata.customers())
    elif command.lower() in ('3', 'quit', 'exit'):
        with open(database, 'w') as f_obj:
            f_obj.write(json.dumps({"customers": customerdata.exportcustomers()}, indent=2))
        print("Goodbye!")
        program = False

while guest == True:
    bankname = str(input("What bank do you go to:\n>>> "))
    for i in banks:
        if i["name"] == bankname:
            database = bankname + '.json'
            with open(database) as f_obj:
                dataset = json.loads(f_obj.read())
                customers = dataset["customers"]
            customerdata = Bank(bankname)
            customerdata.loadcustomers(customers)
            guest = False
            program2 = True
            login = True
        else:
            continue

while login == True:
    prompt = str(input("Please login (Full Name):\n>>> "))
    pword = str(input("Please input your password:\n>>> "))
    for i in customerdata.exportcustomers():
        if i["name"] == prompt and i["password"] == pword:
            print(customerdata.getcustomer(prompt).getname())
            login = False
        else:
            continue
    
while program2 == True:        
    command = str(input("Here are a list of commands:\n1. Balance Inquiry\n2. Deposit\n3. Withdraw\n4. Exit\n>>> "))
    if command.lower() in ('1', 'balance', 'balance inquiry'):
        print(customerdata.getcustomer(prompt).getaccount().getbal())
    elif command.lower() in ('2', 'deposit'):
        dep = int(input("How much would you like to deposit?\n>>> "))
        confirm = str(input("Are you sure? [Y/N]\n>>> "))
        if confirm.lower() in ('y', '1', 'yes'):
            if customerdata.getcustomer(prompt).getaccount().deposit(dep):
                customerdata.balupdateadd(prompt, dep)
                print("You have deposited Rp.", dep)
                print(customerdata.getcustomer(prompt).getaccount().getbal())
            else:
                pass
        else:
            continue
    elif command.lower() in ('3', 'withdraw'):
        withdraw = int(input("How much would you like to withdraw?\n>>> "))
        confirm = str(input("Are you sure? [Y/N]\n>>> "))
        if confirm.lower() in ('y', '1', 'yes'):
            if customerdata.getcustomer(prompt).getaccount().withdraw(withdraw):
                customerdata.balupdatesub(prompt, withdraw)
                print("You have withdrawn Rp.", withdraw)
                print(customerdata.getcustomer(prompt).getaccount().getbal())
            else:
                print("Error, Can't withdraw beyond your total balance!")
        else:
            continue
    elif command.lower() in ('4', 'quit', 'exit'):
        with open(database, 'w') as f_obj:
            f_obj.write(json.dumps({"customers": customerdata.exportcustomers()}, indent=2))
        print(customerdata.getcustomer(prompt).bye())
        program2 = False