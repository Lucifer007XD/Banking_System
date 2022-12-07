# The class takes all the parameters needed to make the user account
class User:
    #Importing dill module
    import json
    #Loading data from Info.txt to Info      
    Info=json.load(open("Info.json","r"))
    @classmethod
    def __init__(self,username:str,password:str,usertype:str,address:list,account:list):
        import json
        self.__username=username
        self.__password=password
        self.__usertype=usertype
        self.__address=address
        self.__account=account
        if self.__usertype=='customer' or self.__usertype=='Customer' or self.__usertype=='CUSTOMER':
            noofcurrentaccount=0
            lenght=len(self.__account)
            for i in range (0,lenght):
                if self.__account[i][1]=='Current':
                    noofcurrentaccount=noofcurrentaccount+1
            if noofcurrentaccount>=2:
                print('User can only have one current account this detail will not be saved. Try Again!!')
            elif noofcurrentaccount==1 or noofcurrentaccount==0:
                self.__info={self.__username:[self.__username,self.__password,self.__usertype,self.__address,self.__account]}
        elif self.__usertype=='admin':
            self.__info={self.__username:[self.__username,self.__password,self.__usertype,self.__address,self.__account]}
        #Using all the parameters a dictionary was made which is updated to Info
        User.Info.update(self.__info)
        #Saving that dictionary to Info.txt
        json.dump(User.Info,open("Info.json","w"),indent=6)   
    
    def displayforuser(self):#This Function is used to display options for user
        print("Please select an option:")
        print("  1 - View account")
        print("  2 - View summary")
        print("  3 - Quit")
    def displayforadmin(self):#This Function is used to dispaly options for admin
        print("Please select an option:")
        print("  1 - Customer Summary")
        print("  2 - Financial Forecast")
        print("  3 - Transfer Money - GUI")
        print("  4 - Account management - GUI")

class TransferWindow:
    def __init__(self):
        try:
            import tkinter as tk
            self.tw=tk.Tk()
            self.tw.title("Transfer Window")
            self.frame=tk.Frame(self.tw,background="White")
            self.frame.pack()
        
            self.username_label=tk.Label(self.frame,text="Username: ",font=("Poppins"),background="white")
            self.username_entry=tk.Entry(self.frame,width=30)
            self.username_label.grid(row=1,column=1)
            self.username_entry.grid(row=1,column=2)
        
            self.fromaccount_label=tk.Label(self.frame,text="From Account: ",font=("Poppins"),background="white")
            self.fromaccount_entry=tk.Entry(self.frame,width=30)
            self.fromaccount_label.grid(row=2,column=1)
            self.fromaccount_entry.grid(row=2,column=2)
        
        
            self.tousername_label=tk.Label(self.frame,text="To Username: ",font=("Poppins"),background="white")
            self.tousername_entry=tk.Entry(self.frame,width=30)
            self.tousername_label.grid(row=6,column=1)
            self.tousername_entry.grid(row=6,column=2)
        
            self.toaccount_label=tk.Label(self.frame,text="To Account: ",font=("Poppins"),background="white")
            self.toaccount_entry=tk.Entry(self.frame,width=30)
            self.toaccount_label.grid(row=7,column=1)
            self.toaccount_entry.grid(row=7,column=2)
        
            self.amount_label=tk.Label(self.frame,text="Amount: ",font=("Poppins"),background="white")
            self.amount_entry=tk.Entry(self.frame,width=30)
            self.amount_label.grid(row=10,column=1)
            self.amount_entry.grid(row=10,column=2)
        
            self.result=tk.StringVar()
            self.result_label=tk.Label(self.frame, textvariable=self.result)
            self.result_label.grid(row=12,column=2)
        
            self.transfer_button=tk.Button(self.frame,text="Transfer",command=self.transfermoney,font=("Poppins"))
            self.cancel_button=tk.Button(self.frame,text="Cancel",command=self.tw.destroy,font=("Poppins"))
            self.transfer_button.grid(row=14,column=2)
            self.cancel_button.grid(row=14,column=3)
        
            tk.mainloop()
        except:
            print("Error: Invalid Input")
    
    def transfermoney(self):
       try: 
        self.username=self.username_entry.get()
        self.fromaccount=int(self.fromaccount_entry.get())
        self.tousername=self.tousername_entry.get()
        self.toaccountno=int(self.toaccount_entry.get())
        self.amount=float(self.amount_entry.get())
        self.__Info=User.Info
        for i in self.__Info:
            if i==self.username:
                self.useraccounts=self.__Info[i][4]
                for account in self.useraccounts:
                    if account[0]==self.fromaccount:
                        length=len(self.useraccounts)
                        for l in range(0,length):
                            if User.Info[i][4][l][0]==self.fromaccount:
                                User.Info[i][4][l][3]-=self.amount
                                import json
                                json.dump(User.Info,open("Info.json","w"),indent=6)
                        for name in self.__Info:
                            if name==self.tousername:
                                self.user2accounts=self.__Info[name][4]
                                for account2 in self.user2accounts:
                                    if account2[0]==self.toaccountno:
                                        lenght2=len(self.user2accounts)
                                        for l2 in range (0,lenght2):
                                            if User.Info[name][4][l2][0]==self.toaccountno:
                                                User.Info[name][4][l2][3]+=self.amount
                                                json.dump(User.Info,open("Info.json","w"),indent=6)
                                                print("Money Transfered")
                                                self.result.set("Transfered")
                                                self.tw.destroy
                                            else:
                                                print("Error: account no. not found")
                                                

                
       except:

           self.result.set("Error: Invalid data type")
           


class AccountManagement:
    def __init__(self):
       try: 
        import tkinter as tk
        
        self.am=tk.Tk()
        self.am.title("Account Management")
        
        self.frame=tk.Frame(self.am,background="white")
        self.frame.pack()
        
        self.username_label=tk.Label(self.frame,text="Username: ",background="white",font=("Poppins"))
        self.username_entry=tk.Entry(self.frame,width=30)
        self.username_label.grid(row=1,column=1)
        self.username_entry.grid(row=1,column=2)
        
        self.add_button=tk.Button(self.frame,text="Add Account",font=("Poppins"),command=self.addaccount)
        self.add_button.grid(row=3,column=2)
        
        self.delete_button=tk.Button(self.frame,text="Delete Account",font=("Poppins"),command=self.deleteaccount)
        self.delete_button.grid(row=3,column=3)
        
        self.cancel_button=tk.Button(self.frame,text="Cancel",font=("Poppins"),command=self.am.destroy)
        self.cancel_button.grid(row=3,column=4)
        
        self.result=tk.StringVar()
        self.result_label=tk.Label(self.frame, textvariable=self.result)
        self.result_label.grid(row=2,column=2)
        
        tk.mainloop()
       except:
           print("Error:Invalid Username")
    
    def addaccount(self):
        import tkinter as tk
        self.username=self.username_entry.get()
        for name in User.Info:
            if name==self.username:
                self.am.destroy
                self.add=tk.Tk()
                self.add.title("Add Account")
                
                self.frame1=tk.Frame(self.add,background="white")
                self.frame1.pack()
                
                self.account_type_label=tk.Label(self.frame1,text="Account Type Current/Saving? ",font=("Poppins"),background="white")
                self.account_type_entry=tk.Entry(self.frame1,width=30)
                self.account_type_label.grid(row=1,column=1)
                self.account_type_entry.grid(row=1,column=2)
                
                self.balance_label=tk.Label(self.frame1,text="Balance: ",font=("Poppins"),background="white")
                self.balance_entry=tk.Entry(self.frame1,width=30)
                self.balance_label.grid(row=2,column=1)
                self.balance_entry.grid(row=2,column=2)
                
                self.ol_ir_label=tk.Label(self.frame1,text="Overdraft Limit(Current)/Interest Rate(Saving): ",font=("Poppins"),background="white")
                self.ol_ir_entry=tk.Entry(self.frame1,width=30)
                self.ol_ir_label.grid(row=3,column=1)
                self.ol_ir_entry.grid(row=3,column=2)
                
                
                
                self.add_account_button=tk.Button(self.frame1,text="Add",font=("Poppins"),command=self.addaccountprogram)
                self.add_account_button.grid(row=5,column=2)
                
                self.cancel_button1=tk.Button(self.frame1,text="Cancel",font=("Poppins"),command=self.add.destroy)
                self.cancel_button1.grid(row=5,column=3)
                
                tk.mainloop()
            else:
                self.result.set("Invalid Username")
      
    
               
    
    def addaccountprogram(self):
        import json
        self.username=self.username_entry.get()
        self.account_type=self.account_type_entry.get()
        self.balance=float(self.balance_entry.get())
        self.ol_ir=float(self.ol_ir_entry.get())
        for name in User.Info:
            if self.username==name:
                self.accounts=User.Info[name][4]
                if self.account_type=="Current" or self.account_type=="current":
                    for account in self.accounts:
                         self.noofcurrentaccount=0
                         if account[1]=="Current":
                             self.noofcurrentaccount+=1
                    if self.noofcurrentaccount>=1:
                         print("One user can only")
                    elif self.noofcurrentaccount==0:
                        self.newaccount=Account("Current",self.ol_ir,self.balance).aslist()
                        User.Info[name][4].append(self.newaccount)
                        json.dump(User.Info,open("Info.json","w"),indent=6)
                        print("Your Account has been Added")
                        print("Account info: {}".format(self.newaccount))
                        self.add.destroy
                elif self.account_type=="Saving" or self.account_type=="saving":
                    self.newaccount=Account("Saving",self.ol_ir,self.balance).aslist()
                    User.Info[name][4].append(self.newaccount)
                    json.dump(User.Info,open("Info.json","w"),indent=6)
                    print("Your Account has been Added")
                    self.result.set("Account has been Added")
                    print("Account info: {}".format(self.newaccount))
                    self.add.destroy
                else:
                    print("Invalid Account Type")
                    
                        
        
                
    def deleteaccount(self):
        import tkinter as tk
        self.username=self.username_entry.get()
        for name in User.Info:
            if name==self.username:
                self.am.destroy
                self.delt=tk.Tk()
                self.delt.title("Delete Account")
                
                self.frame2=tk.Frame(self.delt,background="white")
                self.frame2.pack()
                
                self.account_no_label=tk.Label(self.frame2,text="Account no.: ",font=("Poppins"),background="white")
                self.account_no_entry=tk.Entry(self.frame2,width=30)
                self.account_no_label.grid(row=1,column=1)
                self.account_no_entry.grid(row=1,column=2)
                
                
                
                
                self.delt_account_button=tk.Button(self.frame2,text="Delete",font=("Poppins"),command=self.delete)
                self.delt_account_button.grid(row=3,column=2)
                
                self.cancel_button2=tk.Button(self.frame2,text="Cancel",font=("Poppins"),command=self.delt.destroy)
                self.cancel_button2.grid(row=3,column=3)
                
                tk.mainloop()
    def delete(self):
        self.username=self.username_entry.get()
        self.accountno=int(self.account_no_entry.get())
        for name in User.Info:
            if name==self.username:
                self.accounts=User.Info[name][4]
                lenght=len(self.accounts)
                for l in range(0,lenght):
                    if User.Info[name][4][l][0]==self.accountno:
                            self.index=l
                j=0
                for n in self.accounts:
                    j+=1
                if j==1:
                    self.index=None
                
                try:
                    del User.Info[name][4][self.index]
                    import json
                    json.dump(User.Info,open("Info.json","w"),indent=6)
                    print("Account Deleted")
                    self.result.set("Account deleted")
                    self.delt.destroy
                except:
                    print("Account cannot be deleted")
                    
                
                        
                        

                
                
        
        
           
                
                                        
                                
       
                                
    
    
        

        
        
        
            
        
        
        
      
#To add Address to the User class this Address class is made which take two inputs house no. and street name                       
class Address:
    def __init__(self,number:str,streetname:str):
        self.__hnumber=number
        self.__street=streetname
    def aslist(self):
        self.list=[self.__hnumber,self.__street]
        return self.list
    
    
#To Add accounts to User class This Account class can be used     
class Account:
    accountno=0
    @classmethod
    def __init__(self,accounttype:str,rateorlimit:float,balance:float):
        self.__accounttype=accounttype
        if self.__accounttype=='Current':
            if rateorlimit<=1000 and rateorlimit>=0:
                self.__rateorlimit=rateorlimit
                self.__balance=balance
            else:
                print('Overdraft limit should be between 0 to 1000')
        elif self.__accounttype=='Saving':
            if rateorlimit<=5 and rateorlimit>=0.01:
                self.__rateorlimit=rateorlimit
                self.__balance=balance
        else:
            print('Please enter account type Current/Saving')
        Account.accountno+=1
        import random
        self.accountno=random.randint(Account.accountno+1,500000000)
    def aslist(self):
        self.list=[self.accountno,self.__accounttype,self.__rateorlimit,self.__balance]
        return self.list
    

        
        
            
    
    
#To add a user by customer manually by asking input from the customer this class can be used    
class AddaUser:
    def __init__(self):
        try:
            self.username=input('Add a Username: ')
            self.password=input('Add a Password: ')
            self.usertype='customer'
            self.hnumber=input('Add your house number: ')
            self.street=input('Add your street name:')
            
            ask=True
            self.accounts=[]
            while ask==True:
                try:
                
                
                    self.accounttype=str(input('please enter the type of account (Current/Saving): '))
                    self.rateorlimit=float(input('If Current account enter the overdraft limit and if Saving enter interest rate: '))
                    self.balance=float(input('Enter the balance of the account: '))
                    self.select=input('Want to add another account to this username y/n: ')
                    self.account=[Account(self.accounttype,self.rateorlimit,self.balance).aslist()]
                    self.accounts=self.accounts+self.account

                    if self.select=='Y' or self.select=='y':
                        ask=True
                    elif self.select=='N' or self.select=='n':
                        ask=False
                    else:
                        print('Invalid Input')
                        ask=False
                    User(self.username,self.password,self.usertype,Address(self.hnumber,self.street).aslist(),self.accounts)
                except:
                    print("Invalid Input")
                    ask=False
        except:
            print("Invalid Input")
                
                

                
        
            
            
#To add a admin by customer manually by asking input from customer this class can be used          
class AddaAdmin:
    def __init__(self):
        try:
            self.username=input('Add a Username: ')
            self.password=input('Add a Password: ')
            self.usertype='admin'
            self.address=None
            self.account=None
            User(self.username,self.password,self.usertype,self.address,self.account)
        except:
            
            print('Invalid Input')
    
    
#This is the main class where all the class are used to run a Banking System
class BankingSystem:  
    @classmethod
    def __init__(self):
       
        import json            
        self.__Info=json.load(open("Info.json","r"))
        
    def run_app(self):
        from banking_system import User
        import json
        try:
            error=True
            print("Welcome to the Banking system, please login first")
            while error==True:
         
              self.uname=input("Enter the Username: ")
              for name in self.__Info:
                  if self.uname==name:
                      print("Username Found")
                      self.pswrd=input("Enter the Password: ")
                      if self.pswrd==self.__Info[self.uname][1]:
                          print("You have now logged in, {}".format(self.__Info[self.uname][0]))
                          if self.__Info[self.uname][2]=='customer'or self.__Info[self.uname][2]=='Customer' or self.__Info[self.uname][2]=='CUSTOMER':
                              self.accounts=self.__Info[self.uname][4]
                              isit=True
                              while isit==True:
                                  for i in self.accounts:
                                      print('{}--{} account'.format(i[0],i[1]))
                                  User.displayforuser(self)
                                  option=input('Enter a number to select your option: ')
                                  if option=='1':
                                     print("--Account list--")
                                     print("Please select an option:")
                                     j=0
                                     for i in self.accounts:
                                         j=j+1
                                         print("  {} - {} account: ${}".format(j,i[1],i[3]))
                                     j=0
                                
                                     option1=input("Enter a number to select your option: ")
                                     for i in self.accounts:
                                         j+=1
                                         if option1=='{}'.format(j):
                                             print("You selected {} - {} account: ${}.".format(j,i[1],i[3]))
                                             print("Please select an option:")
                                             print("  1 - Deposit")
                                             print("  2 - Withdraw")
                                             print("  3 - Go back")
                                             option2=input("Enter the number to select your option: ")
                                             if option2=='1':
                                                 try:
                                                     self.deposit=float(input("Enter the amount you want to deposit: "))
                                                 except:
                                                     print("Invalid amount enter a number no character allowed")
                                                 self.accounts[j-1][3]=i[3]+self.deposit
                                                 self.__Info[self.uname][4]=self.accounts
                                                 User.Info.update(self.__Info)
                                                 json.dump(User.Info,open("Info.json","w"),indent=6)
                                                 print ("Amount:{} Added to the account".format(self.deposit))
                                                 
                                                 isit=False
                                                 error=False
                                             elif option2=='2':
                                                 try:
                                                     self.withdraw=float(input("Enter the amount you want to Withdraw: "))
                                                 except:
                                                     print("Invalid amount enter a number no character allowed")
                                                 if self.withdraw<=self.accounts[j-1][3]:
                                                    self.accounts[j-1][3]=i[3]-self.withdraw
                                                    self.__Info[self.uname][4]=self.accounts
                                                    User.Info.update(self.__Info)
                                                    json.dump(User.Info,open("Info.json","w"),indent=6)
                                                    print("Amount: {} withdrawn".format(self.withdraw))
                                                    isit=False
                                                    error=False
                                                 else:
                                                    print("Insufficient Balance")
                                             elif option2=='3':
                                                 isit=True
                                             else:
                                                 print("Invalid Option")
                                                 print("Try Again!!")
                                                 isit=True
                                
                                  elif option=='2':
                                      j=0
                                      for i in self.accounts:
                                          k=0+i[3]
                                          j=j+1
                                      print("Total number of account: {}".format(j))
                                      print("Total balance of all accounts: {}".format(k))
                                      self.address=self.__Info[self.uname][3]
                                      print("Address: {},{}".format(self.address[0],self.address[1]))
                                      isit=False
                                      error=False
                                  elif option=='3':
                                      print("Bye!!!")
                                      isit=False
                                      error=False
                                  else:
                                      print("Invalid Option entered")
                                      print("Please Only enter a number")
                                      print("Try Again!!")
                                      isit=True
                          elif self.__Info[self.uname][2]=='admin' or self.__Info[self.uname][2]=='Admin' or self.__Info[self.uname][2]=='ADMIN': 
                              isit=True
                              while isit==True:
                                  User.displayforadmin(self)
                                  option=input("Enter a number to select your option:")
                                  if option=='1':
                                      for i in self.__Info:
                                          self.accounts=self.__Info[i][4]
                                          self.address=self.__Info[i][3]
                                          if self.__Info[i][2]=='customer' or self.__Info[i][2]=='Customer' or self.__Info[i][2]=='CUSTOMER':
                                              print('-'*40)
                                              print('Name: {}'.format(i))
                                              print('Address: {}, {}'.format(self.address[0],self.address[1]))
                                              print('--Accounts--')
                                              for j in self.accounts:
                                                  if j[1]=='Current':
                                                      print('{} - {} account -- balance: ${}, Over-draft limit: {}'.format(j[0],j[1],j[3],j[2]))
                                                  elif j[1]=='Saving':
                                                      print('{} - {} account -- balance: ${}, Interest rate: {}%'.format(j[0],j[1],j[3],j[2]))
                                                  else:
                                                      print('Error: Occured')
                                              print('-'*40)
                                
                                          else:
                                              pass
                                          isit=False
                                          error=False
                                  elif option=='2':
                                      print('-'*40)
                                      for i in self.__Info:
                                          if self.__Info[i][2]=='customer' or self.__Info[i][2]=='Customer' or self.__Info[i][2]=='CUSTOMER':
                                 
                                              print('Name: {}'.format(i))
                                              j=0
                                              totalafteryear=0
                                              total=0
                                              self.accounts=self.__Info[i][4]
                                              for k in self.accounts:
                                                  j=j+1
                                                  total=total+k[3]
                                                  if k[1]=='Saving':
                                                      forcast=k[3]-(k[3]*(k[2]/100))
                                                      totalafteryear=totalafteryear+forcast
                                                  elif k[1]=='Current':
                                                      totalafteryear=totalafteryear+k[3]
                                                  else:
                                                      print('Unexpected Error')
                                              print('Total number of bank accounts: {}'.format(j))
                                              print('Total money in the bank: ${}'.format(total))
                                              print('Total money after a year forcast: ${}'.format(totalafteryear))
                                              print('-'*40)
                                 
                                          else:
                                              pass
                                          isit=False
                                          error=False
                                  elif option=='3':
                                      from banking_system import TransferWindow as tw
                                      tw()
                                  
                                      isit=False
                                      error=False
                                         
                                         
                                 
                             
                                  elif option=='4':
                                      from banking_system import AccountManagement as am
                                      am()
                                      isit=False
                                      error=False
                                  else:
                                      print("Invalid Input")
                                      print("Please enter a number shown at side the option")
                                      print('Try Again!')
                                      isit=True
                                      error=False
                         
                                  
                             
                          else:
                              print("Invalid UserType")
                              print("Usertype should not be in Capital letters")
                      else:
                          print("Error:Invalid Password")
                          error=True
                  else:
                      pass
        
      
              
      
        except:
                print("Error: Invalid Info")
                                
                                 

                                  
                                 
                      