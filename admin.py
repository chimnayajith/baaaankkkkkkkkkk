import pickle,time
import menus

def client_list():
    try:
        clientlist=open('clients.dat','rb')
        header="""
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛"""
        print("\n")
        print(header)
        try:
            while True:
                data=pickle.load(clientlist)
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
        except:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            clientlist.close()
        choice=input("\nPress [ENTER] to continue...")
        print('\n'*10)
        menus.admin_menu()
    except:
        print("\nUh Oh! An error popped up...Try again another time")
        print("\nRedirecting to main menu...")
        time.sleep(2)
        menus.main_menu()

def search_acc():
    flag=False
    file_sr=open('clients.dat','rb')
    sracc_no=int(input("\n\nEnter A/c No. to search : "))
    try:
        while 1:
            data=pickle.load(file_sr)
            if data['acc_no']==sracc_no:
                flag=True
                print("""\n\nSEARCH RESULTS
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
    
    except:
        file_sr.close()
        if flag==False:
            print("\nNo Accounts found...\n")
            input("Press [ENTER] to continue..")
            menus.search_menu()
        else:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            input("Press [ENTER] to continue..")
            menus.search_menu()

def search_name():
    flag=False
    search=open('clients.dat','rb')
    search_name=input("\n\nEnter A/c Holder Name to search : ")
    try:
        while 1:
            data=pickle.load(search)
            if data['name'].lower()==search_name.lower():
                flag=True
                print("""\n\nSEARCH RESULTS\n
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
    
    except:
        if flag==False:
            print("\nNo accounts found...\n")
            input("Press [ENTER] to continue..")
            menus.search_menu()
        else:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            input("Press [ENTER] to continue..")
            menus.search_menu()

def search_username():
    flag=False
    search=open('clients.dat','rb')
    search_username=input("\n\nEnter A/c username to search : ")
    try:
        while 1:
            data=pickle.load(search)
            if data['username'].lower()==search_username.lower():
                flag=True
                print("""\n\nSEARCH RESULTS\n
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
    
    except:
        if flag==False:
            print("\nNo accounts found...\n")
            input("Press [ENTER] to continue..")
            menus.search_menu()
        else:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            input("Press [ENTER] to continue..")
            menus.search_menu()

def search_acc_edit():
    flag=False
    file_sr=open('clients.dat','rb')
    sracc_no=int(input("\n\nEnter A/c No. to search : "))
    try:
        while 1:
            data=pickle.load(file_sr)
            if data['acc_no']==sracc_no:
                flag=True
                print("""\n\nSEARCH RESULTS
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
    
    except:
        file_sr.close()
        if flag==False:
            print("\nNo Accounts found...\n")
            input("Press [ENTER] to continue..")
            menus.admin_edit_search()
        else:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            choice = input("\nIs this the Account you want to edit?[Y/N] :: ")
            if choice in 'yY':
                menus.admin_edit(data)
            else:
                menus.admin_edit_search()

def search_name_edit():
    flag=False
    search=open('clients.dat','rb')
    search_name=input("\n\nEnter A/c Holder Name to search : ")
    try:
        while 1:
            data=pickle.load(search)
            if data['name'].lower()==search_name.lower():
                flag=True
                print("""\n\nSEARCH RESULTS\n
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
    
    except:
        if flag==False:
            print("\nNo accounts found...\n")
            input("Press [ENTER] to continue..")
            menus.admin_edit()
        else:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            choice = input("\nIs this the Account you want to edit?[Y/N] :: ")
            if choice in 'yY':
                menus.admin_edit(data)
            else:
                menus.admin_edit_search()

def search_username_edit():
    flag=False
    search=open('clients.dat','rb')
    search_username=input("\n\nEnter A/c username to search : ")
    try:
        while 1:
            data=pickle.load(search)
            if data['username'].lower()==search_username.lower():
                flag=True
                print("""\n\nSEARCH RESULTS\n
╒═════════════╤══════════════════╤═══════════════╤═══════════════╤══════════════════╤══════════════════╕
│ Account no. │ Name             │ Username      │ Contact       │ Alt contact      │ Acc Balance      │
╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛""")
                details1 = "│{}│{}│{}│{}│{}│{}│".format((str(data['acc_no'])).ljust(13),(data['name']).ljust(18),(data['username']).ljust(15),(str(data['mob_no'])).ljust(15),(str(data['alternate'])).ljust(18),(str(data['bal'])).ljust(18))
                print(details1)
    
    except:
        if flag==False:
            print("\nNo accounts found...\n")
            input("Press [ENTER] to continue..")
            menus.admin_edit()
        else:
            print("╘═════════════╧══════════════════╧═══════════════╧═══════════════╧══════════════════╧══════════════════╛")
            choice = input("\nIs this the Account you want to edit?[Y/N] :: ")
            if choice in 'yY':
                menus.admin_edit(data)
            else:
                menus.admin_edit_search()
