import pandas as pd
import os

class accountCreate:
    def __init__(self, name, account_no, pin):
        self.name = name
        self.account_no = account_no
        self.pin = pin

    def save_to_file(self):
        try:
            df_existing = pd.read_csv('atm_pro_data.csv')
            data_storage_account = {
                'Name': df_existing['Name'].tolist(),
                'account1': df_existing['account1'].astype(str).tolist(),
                'pin': df_existing['pin'].astype(str).tolist()
            }
        except FileNotFoundError:
            data_storage_account = {'Name': [], 'account1': [], 'pin': []}

        if self.account_no in data_storage_account['account1']:
            print('Account number already exists. Please use a different one.')
            return

        if self.pin in data_storage_account['pin']:
            print('Pin already exists. Please use a different one.')
            return

        data_storage_account['Name'].append(self.name)
        data_storage_account['account1'].append(self.account_no)
        data_storage_account['pin'].append(self.pin)
        print("Account created successfully")

        df = pd.DataFrame(data_storage_account)
        df.to_csv('atm_pro_data.csv', index=False)
        print("Account created successfully and saved to atm_pro_data.csv")
        
def create_new_account():
    try:
        name=input("enter your name")
        account_no=input("enter your account")
        if len(account_no) != 10 or not account_no.isdigit():
            print("enter 10 digit no and only numeric value")
            return
        pin=input("enter four digit pin")
        if len(pin) != 4 or not pin.isdigit():
            return
    except ValueError:
        print("enter numeric value")    
    new_account=accountCreate(name, account_no, pin)
    new_account.save_to_file()       

def atm_menu():
    print("1.","check your bank balence")
    print("2. change pin")
    print("3.","widrwal your ammount")
    print("4.","deposit your money")
    print("5. check transiction history ")
    print("6.","create new account")
    print("7.","exit from atm")

def new_pin_atm(current_data,df_existing):
    try:
        current_pin=int(input("enter current pin"))
        if current_pin != current_data['pin'] :
            print("enter correct pin") 
            return current_data['pin']
        
        new_pin=int(input("enter new pin"))
        confirm_pin=int(input("enter confirm pin")) 
        if new_pin != confirm_pin :
            print("do not match pin")
            return current_data['pin']
        if new_pin in df_existing['pin'].values:
            print(" new pin existing pls use different pin")
            return current_data['pin']
    
        current_data['pin'] = new_pin
        print("successful update pin") 
        return new_pin
    except ValueError:
        print(" use only numeric value")
        return current_data['pin']
            
     
def login_and_run():
    try:
        df_existing = pd.read_csv('atm_pro_data.csv')
        df_existing['pin'] = df_existing['pin'].astype(int)
    except FileNotFoundError:
        print("No existing accounts found. Please create a new account.")
        return    
        
        
    attempt = 0
    max_attempt = 3
    print(" welcom to my atm ")
    while attempt < max_attempt:
        try:
           user_pin=int(input("enter your pin number"))
        except ValueError:
            print(" pls enter numeric digit")
            continue  
        if user_pin in df_existing['pin'].values: 
            print(" successfull login")
            current_data= df_existing[df_existing['pin'] == user_pin].iloc[0].to_dict()
            current_user = {
                'name': current_data['Name'],
                'account_no': current_data['account1'],
                'pin': current_data['pin'],
                'bank_balance': 0,  # Initialize with zero, will be updated later
                'transaction_history': []
            }
            break
        else:
            attempt += 1
            print(f'your login attempt left {max_attempt - attempt}')
    if attempt == max_attempt:
        print("you have used all attempt ! account are lockeed")  
        return         
    while True:
          atm_menu()
          check=input("enter your choice bt 1 to 6 :")
          if check=='1':
             print(f"your bank balence here {current_user['bank_balance']}")
             current_user['transaction_history'].append(f"checked balance history {current_user['bank_balance']}")
          elif check == '2':
               new_pin = new_pin_atm(current_user, df_existing)
               if new_pin != current_user['pin']:
                   df_existing.loc[df_existing['pin'] == user_pin, 'pin'] = new_pin
                   df_existing.to_csv('atm_pro_data.csv', index=False)
                   user_pin = new_pin  # Update user_pin to the new pin
          elif check=='3':
               ammount=float(input("enter your ammount"))
               if 0 < ammount <= current_user['bank_balance']:
                current_user['bank_balance'] -= ammount
                current_user['transaction_history'].append(f'withdraw amount {ammount}')
                print(f'{ammount} is successfull withdrawn')
               else:
                print("pls enter valid ammount")
          elif check=='4':
                deposit=float(input("enter amount"))
                if deposit>0:
                  current_user['bank_balance'] += deposit
                  current_user['transaction_history'].append(f' deposit amount {deposit}')
                  print(f'{deposit} is deposit successfully')
                else:
                   print("pls enter valid ammount")
          elif check=='5':
            if current_user['transaction_history'] :
               print("\n transaction history" )  
               for entry in current_user['transaction_history']:
                   print(entry) 
            else:
                 print("no traction ")
                       
          elif check == '6':
                print(" congratulation for using my atm. thanku")
                break
          else:
                print(" invalid opition pls choice 1 to  no")
                
 

def atm():
    try:
        print("\\WELCOME TO MY ATM\\")
        print("1. Login to existing account")
        print("2. Create a new account")
        print("3. Exit")

        choice = input("enter your choice: ")

        if choice == '1':
          login_and_run()
        elif choice == '2':
          create_new_account()
        elif choice == '3':
           print("Thank you for using the ATM")
           return
        else:
           print("Invalid choice. Please enter 1,2or 3.")
    except ValueError:
        print("enter only numeriv values")   
atm()  
                  


    
