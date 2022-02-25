import client , admin
import time,sys
username={'admin':'admin'}#default admin username and password

def main_menu():
    time.sleep(0.5)
    print('\n'*5)
    hehe ="""
     MAIN MENU
╒═════════════════╕
│ [1] Client Menu │
│ [2] Admin Menu  │
│ [3] Exit/Quit   │
╘═════════════════╛"""
    print(hehe)
    choice=int(input("Select [1-3] : "))
    if choice==1:
        username1=input("\nUsername      : ")
        if username1 in username:
            password=input("Password      : ")
            if password==username[username1]:
                print ("\nPlease Wait...")
                time.sleep(0.5)
                print("\nSuccesfully Logged In !!")
                time.sleep(0.5)
                admin_menu()
            else:
                time.sleep(0.5)
                print("\nIncorrect password!\n")
                main_menu()
        else:
            print("User does not exist!")
            main_menu()
    elif choice==2:
        client_menu()
    elif choice==3:
        exit()
    elif choice==4:
        pass
    else:
        print("\nInvalid input! Please Try Again..")
        main_menu()

def admin_menu():
    print("""\n\n
                    ADMIN MENU
╒══════════════════════════════════════════════════════╕
│ [1] Client List                [4] Back to Main Menu │
│ [2] Search Client              [5] Quit/Exit         │
│ [3] Edit Client Details                              │
╘══════════════════════════════════════════════════════╛""")
    choice=int(input("Select option [1-7] : "))
    if choice == 1:
        admin.client_list()
    if choice == 2:
        search_menu()
    if choice == 3:
        admin_edit_search()
    if choice == 4:
        main_menu()
    if choice == 5:
        exit()        
    elif choice not in [1,2,3,4,5,6]:
        print('\nInvalid input try again')
        admin_menu()

def client_menu():
    print('''\n\n
        CLIENT MENU
╒════════════════════════╕
│ [1] Client Login       │
│ [2] Create New Account │
│ [3] Back to Main Menu  │
│ [4] Quit/Exit          │
╘════════════════════════╛

''')
    choice=int(input("Select [1-5] : "))
    if choice == 1:
        client.client_login()
    if choice == 2:
        choice=input("Do you want to open a new account?[Y/N] : ")
        if choice in 'yY':
            client.new_client()
        elif choice in 'nN':
            print("\nBack to Client Menu")
            time.sleep(0.5)
            client_menu()
    if choice == 3:
        main_menu()
    if choice == 4:
        exit()
    elif choice not in [1,2,3,4]:
        print('\nInvalid input try again')
        client_menu()

def client_menu2(user,data):
    print("\n\n")
    print('                WELCOME ',user)
    print('''╒══════════════════════════════════════════════════════════╕
│ [1] Check Balance             [5] Edit account details   │
│ [2] Withdraw money            [6] Close/Delete Account   │
│ [3] Deposit money             [7] Log out                │
│ [4] Transfer money            [8] Quit/Exit              │
╘══════════════════════════════════════════════════════════╛''')
    choice=int(input("Select [1-8] : "))
    if choice==1:
        client.client_bal(data)
    elif choice ==2:
        client.withdraw(data)
    elif choice==3:
        client.deposit(data)
    elif choice==4:
        client.transfer(data)
    elif choice==5:
        edit_menu(data)
    elif choice==6:
        pass
    elif choice==7:
        print("\nLogging out...")
        time.sleep(0.5)
        print("\nLogged out..Have a nice day!")
        time.sleep(1)
        client_menu()
    elif choice==8:
        exit()
    elif choice not in [1,2,3,4,5,6,7,8]:
        print("Invlaid input... Try Again!")
        time.sleep(0.5)
        client_menu2(user)

def search_menu():
    print("\n\nHow do you want to search?")
    print("""╒═════════════════════╕
│ [1] Account Number  │
│ [2] A/c Holder Name │
│ [3] Username        │
│ [4] Cancel          │
╘═════════════════════╛
    """)
    choice=int(input("Enter your choice > "))
    if choice == 1:
        admin.search_acc()
    elif choice == 2:
        admin.search_name()
    elif choice ==3:
        admin.search_username()
    elif choice ==4:
        admin_menu()

def edit_menu(data):
    print("""
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
    details1 = "│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18))
    print(details1)
    print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
    print("\n\nWhich value do you want to change ? :: ")
    print("""         EDIT MENU
╒══════════════════════════════════════════╕
│ [1] A/c Holder Name  [5] Alt. Contact No.│
│ [2] Username         [6] Cancel          │
│ [3] Password                             │
│ [4] Contact No.                          │
╘══════════════════════════════════════════╛""")
    choice=int(input("Enter your choice >"))
    if choice == 1:
        client.edit_name(data)
    elif choice == 2:
        client.edit_username(data)
    elif choice == 3:
        client.edit_password(data)
    elif choice == 4:
        client.edit_phno(data)
    elif choice == 5:
        client.edit_altph(data)
    elif choice == 6:
        client_menu2(data['name'],data)

def admin_edit_search():
    print("\n\nHow do you want to search account?")
    print("""╒═════════════════════╕
│ [1] Account Number  │
│ [2] A/c Holder Name │
│ [3] Username        │
│ [4] Cancel          │
╘═════════════════════╛
    """)
    choice=int(input("Enter your choice > "))
    if choice == 1:
        admin.search_acc_edit()
    elif choice == 2:
        admin.search_name_edit()
    elif choice ==3:
        admin.search_username_edit()
    elif choice ==4:
        admin_menu()

def admin_edit(data):
    print("""     ADMIN EDIT MENU
╒════════════════════════════════════════╕
│ [1] A/c Holder Name  [5] Alt. Phone no.│
│ [2] Username         [6] Cancel        │
│ [3] Password                           │
│ [4] Phone no.                          │
╘════════════════════════════════════════╛""")
    choice=int(input("=> Choose option [1-6] :: "))
    if choice == 1:
        client.edit_name(data)
    if choice == 2:
        client.edit_username(data)
    if choice == 3:
        client.edit_password(data)
    if choice == 4:
        client.edit_phno(data)
    if choice == 5:
        client.edit_altph(data)
    if choice == 6:
        admin_menu()
    elif choice not in [1,2,3,4,5,6]:
        print("Invalid Input..Try Again!!")
        admin_edit(data)

def exit():
    choice=input("\n\nAre you sure you want to exit/quit? [Y/N]")
    if choice in 'yY':
        print("\n\nThank You...Have a nice day.")
        time.sleep(1)
        sys.exit()
    elif choice in 'nN':
        main_menu()
    elif choice not in 'NYny':
        print("Invalid input. Redirecting to Main Menu")
        main_menu()
