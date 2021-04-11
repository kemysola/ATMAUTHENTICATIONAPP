import random
import datetime
database ={}

#init function
def init():
    print('Welcome to Apy Bank')
    isValidatedOptionSelected = False
    while isValidatedOptionSelected == False:
        haveAccount =int(input("Do you have an account number with us: 1(yes) 2(no) \n\t"))
        if(haveAccount ==1):
            isValidatedOptionSelected = True
            login()
        elif(haveAccount ==2):
            isValidatedOptionSelected = True
            register()
        else:
            print("You have selected a wrong option")
            login()

#login function......           
def login():
    accountNumber =input('Kindly enter your account number \n')
    #if(name in allowedUsers):
    password =input('Kindly enter your password \n')
    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumber:
            if(password == userDetails[3]):
                transactionDate =datetime.datetime.now()
                print('Login Sucessful!')
                print(transactionDate)
                print('******************')
                print("******************")
                operations(userDetails)
    print('Invalid Account or Password!')
    init()
#register function...........
def register():
    print('*********** Kindly register ************')
    email =input('Please enter your email: \n')
    first_name=input('Kindly enter your first name: \n')
    last_name=input('Kindly enter your  last name: \n')
    password = input('Create a password \n')
    accountNumber = generateAccountNumber()
    database[accountNumber] = [ first_name , last_name, email, password ]
    print('**********************************')
    print('**** Your account number has been created ****')
    print("Your account number is: %d"  % accountNumber)
    print("*****************************************")
    login()
#.....Account generation function......  
def generateAccountNumber():
    return random.randrange(1111111111, 9999999999) 
#operation function.........
def operations(user):
    print('*********************')
    print("Welcome",user[0].upper(), user[1].upper())
    print('**********************')
    print('*********************')
    print('This are the available options')  
    print('1.Withdrawal')
    print('2.Deposit')
    print('3.Transfer')
    print('4.Complaints')
    selectedOptions = int(input('Please select an option: \n'))
    if(selectedOptions == 1):
        withdraw()

    elif(selectedOptions ==2):
        deposit()
    elif(selectedOptions ==3):
        transfer()
    elif(selectedOptions ==4):
        complaints()
    else:
        print('Enter a valid amount')
        login()
#withdraw function
def withdraw():
    users_amount = input('How much would you like to withdraw ? \n')
    print('Please take your cash')
    print('Will you like to continue? 1(yes) 2(No) \n\t')
    more_options()
    
#deposit function.....    
def deposit():
    users_deposit =input('How much would you like to deposit? \n')
    print(f'Your available balance is {users_deposit}')
    print('Will you like to continue? 1(yes) 2(No) \n\t')
    more_options()
#transfer function......    
def transfer():
    print('1.To same bank')
    print('2.Other Banks')
    transfers =int(input('Kindly select an option: \n'))
    if(transfers ==1):
        
        users_acct = input('Kindly enter the account number: \n')
        transfer_account = (input("Kindly enter the amount? \n"))
        print("****************")
        print(f'you have transfered {transfer_account} to {users_acct}')
        print('Will you like to continue? 1(yes) 2(No) \n\t')
        more_options()
        
    elif(transfers ==2):
        print('Other Banks')
    else:
        print('Kindly enter a valid option')
        transfer()
#options function......        
def more_options():
    print("1.Yes 2.No")
    selectedOptions = int(input('Please select an option: \n'))
    if(selectedOptions == 1):
        login()
    elif(selectedOptions ==2):
        print('Thank you,Kindly exit')
    else:
        print('Kindly enter a valid option')
        more_options()
#user complaints function----     
def complaints():
    user_message = input('Kindly enter your complaint \n\t')
    print('Thank you, we will be in touch.')
    print("****************")
    print('Would you like to continue?')
    more_options()
    
    
init()