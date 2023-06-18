from curses.ascii import isalpha
from login import log_in

from registration import CreateAccount
# from Banking_project.proj1_login import log_in
# from Banking_project.proj1_registration import CreateAccount
# from mysql_connector import mydb, mycursor
# SpecialSym =['$', '@', '#', '%']


while True:
    print("\n")
    print("___________________________________________________________________________")
    print("********************  Welcome To  Banking System  *************************")
    print("___________________________________________________________________________")
    print("\n")
    print("Press 1 For Registration ")
    print("Press 2 For Log In  ")
    print("Press 3 For Exit  ")
    try:
        ch=int(input("Enter the Key : "))
        if(isalpha(ch)) or (ch>=4) or (ch<1) :
            raise Exception ("Oops!  That was not a valid number.  Try again...  :( ")
        elif(ch==1):
            reg = CreateAccount()
            reg.enrich()
        elif(ch==2):
            login = log_in()
            login.enrich()
        elif(ch==3):
            print("Thank You For Visiting! \U0001f60A ")
            break
    except Exception:
        print("\n")
        print("Oops! Something went wrong ")
        print("_________________________________________________")
        print("\n")