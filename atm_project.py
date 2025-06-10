users={
    6545 : {'bank_balance':1000,'transaction_history':[ ]},
    1234 : {'bank_balance':2000,'transaction_history':[ ]},
    8811 : {'bank_balance':4599,'transaction_history':[ ]},
    5456 : {'bank_balance':2879,'transaction_history':[ ]}
}

def atm_menu():
    print("1.","check your bank balence")
    print("2. change pin")
    print("3.","widrwal your ammount")
    print("4.","deposit your money")
    print("5. check transiction history ")
    print("6.","exit from atm")

def new_pin_atm(user_pin):
    try:
        current_pin=int(input("enter current pin"))
        if current_pin != user_pin :
            print("enter correct pin") 
            return user_pin
        new_pin=int(input("enter new pin"))
        confirm_pin=int(input("enter confirm pin")) 
        if new_pin != confirm_pin :
            print("do not match pin")
            return user_pin
        if new_pin in users :
            print(" new pin existing pls use different pin")
            return user_pin
        users[new_pin] = users.pop(user_pin)
        user_pin = new_pin
        print("successful update pin") 
        return new_pin
    except ValueError :
        print(" use only numeric value")   
        return user_pin             
            
     
def atm():
    attempt = 0
    max_attempt = 3
    print(" welcom to my atm ")
    while attempt < max_attempt:
        try:
           user_pin=int(input("enter your pin number"))
        except ValueError:
            print(" pls enter numeric digit")
            continue
        if user_pin in users:
            print(" successfull login")
            current_user=users[user_pin]
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
             print(f'your bank balence here {current_user['bank_balance']}')
             current_user['transaction_history'].append(f'checked balance history{current_user['bank_balance']}')
          elif check == '2':
               new_pin_atm(user_pin)
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
                print(" invalid opition pls choice 1 to 5 no")
                
atm()   
                  


    