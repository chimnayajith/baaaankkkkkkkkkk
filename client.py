import menus
import pickle,time,random,os
from datetime import datetime

def new_client():
    new_cli=open('clients.dat','ab+')
    client={}
    client['acc_no']=random.randint(100000,999999)
    print("\nRandom Generated Account Number : ",client['acc_no'])
    client['name']=input("Enter Name :: ")
    client['username']=input("Enter username :: ")
    client['password']=input("Password:: ")
    confirm=input("Confirm Password:: ")
    if (confirm!=client['password']):
        print("\nPasswords does not match ! Try Again !")
        new_client()
    client['mob_no']=input("Mobile Number :: ")
    client['alternate']=input("Alternate Contact :: ")
    print("\nPlease Wait...")
    time.sleep(0.5)
    print("\nNew Client Succesfully Created!!")
    choice=input("\nPress [ENTER] to continue...")
    while choice=='':
        dep=int(input("\nEnter the amount to be deposited initially : "))
        if dep<1500:
            print("\n!!!ABC Bank requires a minimum account balance of Rs.1500!!!")
            continue
        else:
            client['bal']=dep
            print("\nProcessing Account Details... Please Wait!")
            time.sleep(0.5)
            print('\n₹{} deposited into account.'.format(dep))
            break
    pickle.dump(client,new_cli)
    new_cli.close()
    menus.client_menu()       

def client_login():
    cli_det =open('clients.dat','rb')
    client=input("\nEnter Username   : ")
    flag=True
    try:
        while True:
            data=pickle.load(cli_det)
            while True:
                if data['username']==client:
                    client_pass = input("Enter Password   : ")
                    if data['password']==client_pass:
                        flag=True
                        print("\nLogged in as ",data['name'])
                        cli_det.close()
                        menus.client_menu2(data['name'],data)
                    else:
                        print("Incorrect Password")
                else:
                    flag=False
                    break
    except: 
         cli_det.close()
    if flag==False:
        print("User not found...Try again")
        client_login()

def client_bal(data1):
    cli_bal = open('clients.dat','rb')
    try:
        while True:
            balance = pickle.load(cli_bal)
            if balance['acc_no']==data1['acc_no']:
                data=balance
    except:
        cli_bal.close()
    now = datetime.now()
    now_date = now.strftime("%m/%d/%Y")
    now_time=now.strftime("%H:%M:%S")
    print("+--------------------------------------+")
    print("│               ABC BANK               │")
    print("│            BALANCE ENQUIRY           │\n│ {}│\n│{} │\n│                                      │".format((now_date).rjust(37),(now_time).rjust(37)))
    print("│ Acc. Number  :: {}│\n│ Acc. Holder  :: {}│\n│ Acc. Balance :: ₹ {}│".format((str(data['acc_no'])).ljust(21),(data['name']).ljust(21),(str(data['bal'])).ljust(19)))
    print("+--------------------------------------+")
    input('Press [ENTER] to continue..')
    menus.client_menu2(data['name'],data)

def withdraw(data):
    now = datetime.now()
    now_date = now.strftime("%m/%d/%Y")
    now_time=now.strftime("%H:%M:%S")
    try:
        cli_with =open('clients.dat','rb')
        cli_withnew = open("temp.dat",'wb')
        search = data['acc_no']
        while 1:
            file=pickle.load(cli_with)
            if file['acc_no']==search:
                logined = file
                amount=int(input("Enter the amount you want to withdraw(in ₹) :: "))
                balance = file['bal']
                if (balance > amount):
                    confirm=input('Are you sure you want to withraw ₹{} ? [y/n] :: '.format(amount))
                    if confirm in 'yY':
                        passconfirm = input("Confirm your password :: ")
                        if passconfirm == file['password']:
                            file['bal']=balance-amount
                            print("+--------------------------------------+")
                            print("│               ABC BANK               │")
                            print("│          WITHDRAWAL RECEIPT          │\n│ {}│\n│{} │\n│                                      │".format((now_date).rjust(37),(now_time).rjust(37)))
                            print('│A/c No.                 :: XXX{}│\n│Amount withdrawn        :: ₹{}│\n│Current Account balance :: ₹{}│'.format((str(file['acc_no'])[3:]).ljust(8),(str(amount)).ljust(10),(str(file['bal'])).ljust(10)))
                            print("+--------------------------------------+")
                            input('Press [ENTER] to continue..')
                        else:
                            print("Incorrect password! Try again")
                            withdraw(file)
                        pickle.dump(file,cli_withnew)
                    else:
                        cli_with.close()
                        cli_withnew.close()
                        os.remove('temp.dat')
                        print("Transaction Cancelled! Redirecting to Menu")
                        time.sleep(0.7)
                        menus.client_menu2(data['name'],data)

                else:
                    print('\n\nThe amount you specified is more than your account balance.Try again..\n\n')
                    cli_with.close()
                    cli_withnew.close()
                    os.remove('temp.dat')
                    time.sleep(0.5)
                    withdraw(data)
            else:
                pickle.dump(file,cli_withnew)

    except:
        cli_with.close()
        cli_withnew.close()
        os.remove('clients.dat')
        os.rename('temp.dat','clients.dat')
        menus.client_menu2(logined['name'],logined)

def deposit(data):
    now = datetime.now()
    now_date = now.strftime("%m/%d/%Y")
    now_time=now.strftime("%H:%M:%S")
    try:
        cli_with =open('clients.dat','rb')
        cli_withnew = open("temp.dat",'wb')
        search = data['acc_no']
        while 1:
            file=pickle.load(cli_with)
            if file['acc_no']==search:
                logined = file
                amount=int(input("Enter the amount you want to deposit(in ₹) :: "))
                balance = file['bal']
                confirm=input('Are you sure you want to deposit ₹{} ? [y/n] :: '.format(amount))
                if confirm in 'yY':
                    passconfirm = input("Confirm your password :: ")
                    if passconfirm == file['password']:
                        file['bal']=balance+amount
                        print("+--------------------------------------+")
                        print("│               ABC BANK               │")
                        print("│           DEPOSIT RECEIPT            │\n│ {}│\n│{} │\n│                                      │".format((now_date).rjust(37),(now_time).rjust(37)))
                        print('│A/c No.                 :: XXX{}│\n│Amount deposited        :: ₹{}│\n│Current Account balance :: ₹{}│'.format((str(file['acc_no'])[3:]).ljust(8),(str(amount)).ljust(10),(str(file['bal'])).ljust(10)))
                        print("+--------------------------------------+")
                        input('Press [ENTER] to continue..')
                    else:
                        print("Incorrect password! Try again")
                        withdraw(data)
                    pickle.dump(file,cli_withnew)
                else:
                    cli_with.close()
                    cli_withnew.close()
                    os.remove('temp.dat') 
                    print("Transaction Cancelled! Redirecting to Menu")
                    time.sleep(0.7) 
                    menus.client_menu2(data['name'],data) 
            else:
                pickle.dump(file,cli_withnew)

    except:
        cli_with.close()
        cli_withnew.close()
        os.remove('clients.dat')
        os.rename('temp.dat','clients.dat')
        menus.client_menu2(logined['name'],logined)

def transfer(data):
    now = datetime.now()
    now_date = now.strftime("%m/%d/%Y")
    now_time=now.strftime("%H:%M:%S")
    flag = False
    try:
        transferacc = int(input("A/c No. to which you want to transfer money to :: "))
        tocheck = open('clients.dat','rb')
        while 1:
            file = pickle.load(tocheck)
            if file['acc_no'] == transferacc:
                print("\n\nMake Sure this is the A/c you want to tranfer to ::")
                print("""
╒══════════════════════╤══════════════════════════╤═════════════════════════╕
│ A/c No.              │ Name                     │ Username                │
╘══════════════════════╧══════════════════════════╧═════════════════════════╛""")
                print("│{:<21} │{:<25} │{:25}│".format(file['acc_no'],file['name'],file['username']))
                print('╘══════════════════════╧══════════════════════════╧═════════════════════════╛')
                confirm = input("Enter [Y/N] >")
                if confirm in 'yY':
                    flag=True
                    tocheck.close()
                    break
                else:
                    tocheck.close()
                    transfer(data)

        transferee = open('clients.dat','rb')
        temp = open('temp.dat','wb')
        search = data['acc_no']
        while 1:
            file = pickle.load(transferee)
            if file['acc_no'] == search:
                logined = file
                amount=int(input("Enter the amount you want to transfer(in ₹) :: ")) 
                if amount < file['bal']:
                    file['bal']=file['bal']-amount
                    transferee.seek(0)
                    while 1:
                        acc = pickle.load(transferee)
                        if acc['acc_no'] == transferacc:
                            sed=acc
                            acc['bal']=acc['bal'] + amount
                            pickle.dump(file,temp)
                            pickle.dump(acc,temp)
                            print("\n\nMoney transferred Succesfully!!\n\nGenerating slip..Please wait\n\n")
                            time.sleep(0.75)
                            print("+--------------------------------------+")
                            print("│               ABC BANK               │")
                            print("│           TRANSFER RECIEPT           │\n│ {}│\n│{} │\n│                                      │".format((now_date).rjust(37),(now_time).rjust(37)))
                            print("│ A/c Number      :: {}│\n│ A/c Holder      :: {}│\n│ Current Balance :: ₹ {}│\n│ Transferred To  :: {}│\n│ Amount          :: ₹ {}│".format((str(file['acc_no'])).ljust(18),(file['name']).ljust(18),(str(file['bal'])).ljust(16),(sed['name']).ljust(18),(str(amount)).ljust(16)))
                            print("+--------------------------------------+")
                        elif acc['acc_no'] != search:
                            pickle.dump(acc,temp)
                else:
                    print('\n\nThe amount you specified is more than your account balance.Try again..\n\n')
                    transferee.close()
                    temp.close()
                    os.remove('temp.dat')
                    time.sleep(0.5)
                    transfer(logined)
    except:
        if flag == False:
            tocheck.close()
            print("\n\nEnter a valid A/c No. to transfer to!!\n\n")
            time.sleep(0.5)
            transfer(data)
        else:
            transferee.close()
            temp.close()
            os.remove('clients.dat')
            os.rename('temp.dat', 'clients.dat')
            input('Press [ENTER] to continue..')
            print('\n'*10)
            menus.client_menu2(file['name'],file)

def edit_name(data):
    file_edit=open('clients.dat','rb')
    temp = open('temp.dat','wb')
    try:
        while 1:
            each=pickle.load(file_edit)
            if each['acc_no']==data['acc_no']:
                new_name = input("Enter the new name > ")
                each['name'] = new_name
                print("New data : ")
                print("""╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│".format((str(each['acc_no'])).ljust(13),(each['name']).ljust(18),(each['username']).ljust(15),(str(each['mob_no'])).ljust(15),(str(each['alternate'])).ljust(18))
                print(details1)
                print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
                confirmation = input("Are you sure you want to edit the name [Y/N] ? : ")
                if confirmation in 'yY':
                    pass_confirm = input("Confirm your password to edit :: ")
                    if pass_confirm == each['password']:
                        hehe=each
                        pickle.dump(each,temp)
                        continue
                    else:
                        print("Incorrect password..Try Again!")
                        file_edit.close()
                        temp.close()
                        os.remove('temp.dat')
                        time.sleep(0.7)
                        menus.client_menu2(each['name'],each)
                else:
                    print("Cancelling edits...")
                    file_edit.close()
                    temp.close()
                    os.remove('temp.dat')
                    time.sleep(0.7)
                    menus.client_menu2(each['name'],each)
            else:
                pickle.dump(each,temp)
    except:
        file_edit.close()
        temp.close()
        os.remove('clients.dat') 
        os.rename('temp.dat','clients.dat')
        print("\n\nData edited succesfully!!\n\n")
        time.sleep(0.7)
        menus.client_menu2(hehe['name'],hehe)

def edit_username(data):
    file_edit=open('clients.dat','rb')
    temp = open('temp.dat','wb')
    try:
        while 1:
            each=pickle.load(file_edit)
            if each['acc_no']==data['acc_no']:
                new_username = input("Enter your new username > ")
                each['username'] = new_username
                print("New data : ")
                print("""╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│".format((str(each['acc_no'])).ljust(13),(each['name']).ljust(18),(each['username']).ljust(15),(str(each['mob_no'])).ljust(15),(str(each['alternate'])).ljust(18))
                print(details1)
                print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
                confirmation = input("Are you sure you want to edit the username [Y/N] ? : ")
                if confirmation in 'yY':
                    pass_confirm = input("Confirm your password to edit :: ")
                    if pass_confirm == each['password']:
                        hehe=each
                        pickle.dump(each,temp)
                        continue
                    else:
                        print("Incorrect password..Try again!")
                        file_edit.close()
                        temp.close()
                        os.remove('temp.dat')
                        time.sleep(0.7)
                        menus.client_menu2(each['name'],each)
                else:
                    print("Cancelling edits...")
                    file_edit.close()
                    temp.close()
                    os.remove('temp.dat')
                    time.sleep(0.7)
                    menus.client_menu2(each['name'],each)
            else:
                pickle.dump(each,temp)
    except:
        file_edit.close()
        temp.close()
        os.remove('clients.dat') 
        os.rename('temp.dat','clients.dat')
        print("\n\nData edited succesfully!!\n\n")
        time.sleep(0.7)
        menus.client_menu2(hehe['name'],hehe)

def edit_password(data):
    file_edit=open('clients.dat','rb')
    temp = open('temp.dat','wb')
    try:
        while 1:
            each=pickle.load(file_edit)
            if each['acc_no']==data['acc_no']:
                pass_confirm = input("Confirm your password to edit > ")
                if pass_confirm == each['password']:
                    new_password = input("Enter your new password > ")
                    each['password'] = new_password
                    confirm = input("Confirm your password > ") 
                    if confirm == new_password:  
                        hehe=each
                        pickle.dump(each,temp)
                        continue
                    else:
                        print("\nPasswords don't match!")
                        file_edit.close()
                        temp.close()
                        os.remove('temp.dat')
                        time.sleep(0.7)
                        menus.client_menu2(each['name'],each)
                else:
                    print("\n\nIncorrect password!\n\n")
                    file_edit.close()
                    temp.close()
                    os.remove('temp.dat')
                    time.sleep(0.7)
                    menus.client_menu2(each['name'],each)
            else:
                pickle.dump(each,temp)
    except:
        file_edit.close()
        temp.close()
        os.remove('clients.dat') 
        os.rename('temp.dat','clients.dat')
        print("\n\nData edited succesfully!!\n\n")
        time.sleep(0.7)
        menus.client_menu2(hehe['name'],hehe)

def edit_phno(data):
    file_edit=open('clients.dat','rb')
    temp = open('temp.dat','wb')
    try:
        while 1:
            each=pickle.load(file_edit)
            if each['acc_no']==data['acc_no']:
                ph_no = input("Enter the Contact number > ")
                each['contact'] = ph_no
                print("New data : ")
                print("""╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│".format((str(each['acc_no'])).ljust(13),(each['name']).ljust(18),(each['username']).ljust(15),(str(each['mob_no'])).ljust(15),(str(each['alternate'])).ljust(18))
                print(details1)
                print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
                confirmation = input("Are you sure you want to edit Contact No. [Y/N] ? : ")
                if confirmation in 'yY':
                    pass_confirm = input("Confirm your password to edit :: ")
                    if pass_confirm == each['password']:
                        hehe=each
                        pickle.dump(each,temp)
                        continue
                    else:
                        print("Incorrect password..Try Again!")
                        file_edit.close()
                        temp.close()
                        os.remove('temp.dat')
                        time.sleep(0.7)
                        menus.client_menu2(each['name'],each)
                else:
                    print("Cancelling edits...")
                    file_edit.close()
                    temp.close()
                    os.remove('temp.dat')
                    time.sleep(0.7)
                    menus.client_menu2(each['name'],each)
            else:
                pickle.dump(each,temp)
    except:
        file_edit.close()
        temp.close()
        os.remove('clients.dat') 
        os.rename('temp.dat','clients.dat')
        print("\n\nData edited succesfully!!\n\n")
        time.sleep(0.7)
        menus.client_menu2(hehe['name'],hehe)

def edit_altph(data):
    file_edit=open('clients.dat','rb')
    temp = open('temp.dat','wb')
    try:
        while 1:
            each=pickle.load(file_edit)
            if each['acc_no']==data['acc_no']:
                alternate = input("Enter the Contact number > ")
                each['alternate'] = alternate
                print("New data : ")
                print("""╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│".format((str(each['acc_no'])).ljust(13),(each['name']).ljust(18),(each['username']).ljust(15),(str(each['mob_no'])).ljust(15),(str(each['alternate'])).ljust(18))
                print(details1)
                print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
                confirmation = input("Are you sure you want to edit Alt. Contact No. [Y/N] ? : ")
                if confirmation in 'yY':
                    pass_confirm = input("Confirm your password to edit :: ")
                    if pass_confirm == each['password']:
                        hehe=each
                        pickle.dump(each,temp)
                        continue
                    else:
                        print("Incorrect password..Try Again!")
                        file_edit.close()
                        temp.close()
                        os.remove('temp.dat')
                        time.sleep(0.7)
                        menus.client_menu2(each['name'],each)
                else:
                    print("Cancelling edits...")
                    file_edit.close()
                    temp.close()
                    os.remove('temp.dat')
                    time.sleep(0.7)
                    menus.client_menu2(each['name'],each)
            else:
                pickle.dump(each,temp)
    except:
        file_edit.close()
        temp.close()
        os.remove('clients.dat') 
        os.rename('temp.dat','clients.dat')
        print("\n\nData edited succesfully!!\n\n")
        time.sleep(0.7)
        menus.client_menu2(hehe['name'],hehe)

def close_account(data):
     print("""╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛""")
     details1 = "│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18))
     print(details1)
     print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╛")
     choice = input("Are you sure you want delete your account?")
     if choice in 'yY':
         passconfirm = input("Enter your Password to continue :: ")
         if passconfirm == data['password']:
            file_del=open('clients.dat','rb')
            temp = open('temp.dat','wb')
            try:
                while True:
                    each = pickle.load(file_del)
                    if each == data:
                        continue
                    else:
                        pickle.dump(each,temp)
            except:
                os.remove('clients.dat')
                os.rename('temp.dat' , 'clients.dat')
                print("\nDeleting Account..")
                time.sleep(0.5)
                print("\nAccount Deleted!!")
                menus.client_menu()
                
