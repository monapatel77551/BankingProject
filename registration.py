
from mysqlconnector import mycursor,mydb
import random
SpecialSym =['$', '@', '#', '%']
def remove(str):
    # This Method is for removing all space from string
        return str.replace(" ", "")


class CreateAccount():

    def enrich(self):
        print("\n")
        print("___________________________________________________________________________")
        print("********************  Welcome To Banking System *************************")
        print("___________________________________________________________________________")
        print("\n")
        self.user_name()
        self.password()
        self.name()
        self.type()
        self.opening_amount()
        self.address()
        self.phone_number()
        self.aadhar_number()
        self.credit_card_allot()
        self.debit_card_allot()
        self.add_beneficiaries()
        print("\n\nCongrats! New Account Created")
        print("\n\n")
        self.showAccount()

    def user_name(self):
        while True:
                try: 
                    ut1 = input("Enter user name Here : ")
                    # ut2 = ut1.strip()
                    self.user_name = ut1.strip()
                    # ut = remove(ut1)
                    if ut1.isalnum() and ut1[0].isalpha() :
                        break
                    else:
                        raise TypeError 
                except TypeError:
                    print("spaces, first letter is Numeric or Special Character are not allowed like . , @ # < > ? / ; ")
        return self

    def password(self):
        while True:        
                try:
                    z = input("Enter Your Password : ")
                    self.password = z
                    if (len(z)<6):
                        raise ValueError (" Password should contain at least 6 character ")
                    if not any(char.isdigit() for char in z):
                        raise ValueError ("Password should atleast a number")
                    if not any(char.isupper() for char in z):
                        raise KeyError ()
                    if not any(char.islower() for char in z):
                        raise KeyError
                    if not any(char in SpecialSym for char in z ):
                        raise KeyError
                    break
                except ValueError:
                    print("Password should contain atleast 1 upper case, 1 Lower Case ,1 Numeric , 1 Special Character  and Password Must Contain atleast 7 character")
                except KeyError:
                    print("Password should contain atleast 1 upper case, 1 Lower Case ,1 Numeric , 1 Special Character  and Password Must Contain atleast 7 character")
        return self

    def name(self):
        while True:
            try: 
                ut1 = input("Enter Your Name Here : ")
                # ut2 = ut1.strip()
                self.name = ut1.strip()
                ut = remove(ut1)
                if ut.isalpha() :
                    break
                else:
                    raise TypeError 
            except TypeError:
                print("Numeric or Special Character are not allowed like . , @ # < > ? / ; ")
        return self

    def type(self):
        while True:
            try:
                u = input('Enter the type of account (for saving type S and for current type C) :')
                if u in ['S','C']:
                    self.type = u
                    break
                else:
                     raise TypeError      
            except TypeError:
                print("Enter right input")
                  
            
        #self.type = input("Enter the type of account [C/S] : ")
        return self

    def opening_amount(self):
        while True:
                try:
                    try:
                        k=int(input("Enter the Amount of money you want to deposit : "))
                        self.opening_amount = k
                    except:
                        print("Please Enter the value ! \U0001F642 ")
                    if (k<=0) :
                        print('\n')
                        print("Amount less than Zero is not exist in the real world only you can think! \U0001F642 ")
                        print('\n') 
                    else:
                        break              
                except:
                    print("Please write correct value !")
        return self

    def address(self):
        self.address = input("Enter Your Address : ")
        return self

    def phone_number(self):
        while True:
                try:
                    d=int(input("Enter Your Phone Number : "))
                    self.phone_number = d
                    if (len(str(d))!=10) or (str(d).isalpha()) or (str(d)[0] not in ['6','7','8','9']) :
                        raise ValueError("Pls enter a valid 10 digit Number and number should be start from 6,7,8,9.")
                    break
                except ValueError as m:
                    print(m)

        return self

    def aadhar_number(self):
        while True:
                try:
                    f=int(input("Enter Your 12 Digit Aadhar Number Without putting space  : "))
                    self.aadhar_number = str(f)
                    if(len(str(f))!=12) or (str(f).isalpha()):
                        raise ValueError ("Please Enter a valid 12 digit aadhar Number")
                    break
                except ValueError as m:
                    print(m)

        return self

    def credit_card_allot(self):
        # Generate a random 16-digit number
        self.credit_card_no = random.randint(10**15, (10**16)-1)
        self.credit_type = 'credit'
        self.credit_pin = random.randint(1000,9999)
        self.credit_cvv = random.randint(100,999)

    def debit_card_allot(self):
        # Generate a random 16-digit number
        self.debit_card_no = random.randint(10**15, (10**16)-1)
        self.debit_type = 'debit'
        self.debit_pin = random.randint(1000,9999)
        self.debit_cvv = random.randint(100,999)

    def add_beneficiaries(self):
        while True:
            try: 
                ut1 = input("Enter Your benficiarie Name here : ")
                # ut2 = ut1.strip()
                self.beneficairy_name = ut1.strip()
                ut = remove(ut1)
                if ut.isalpha() :
                    break
                else:
                    raise TypeError 
            except TypeError:
                print("Numeric or Special Character are not allowed like . , @ # < > ? / ; ")
                
        while True:
                try:
                    f=int(input("Enter Your 12 Digit beneficiary_account_number Without putting space  : "))
                    self.beneficiary_account_number = f
                    if(len(str(f))!=12) or (str(f).isalpha()):
                        raise ValueError ("Please Enter a valid 12 digit beneficiary_account_number")
                    break
                except ValueError as m:
                    print(m)

        return self

    def showAccount(self):
        q="insert into account_details (user_name,password,name,type,balance,address,mobile,aadhar) values('{}','{}','{}','{}',{},'{}',{},{})".format(self.user_name,self.password,self.name,self.type,self.opening_amount,self.address,self.phone_number,self.aadhar_number)
        mycursor.execute(q)
        mydb.commit()
        ad="select account_number from account_details where user_name='{}' and password ='{}' ".format(self.user_name,self.password)
        mycursor.execute(ad)
        a=mycursor.fetchone()[0]
        cc = "insert into card (account_number, card_number,card_type,pin, cvv) values ({},{},'{}',{},{})".format(a,self.credit_card_no,self.credit_type,self.credit_pin,self.credit_cvv)
        mycursor.execute(cc)
        mydb.commit()
        dc = "insert into card (account_number, card_number,card_type,pin, cvv) values ({},{},'{}',{},{})".format(a,self.debit_card_no,self.debit_type,self.debit_pin,self.debit_cvv)
        mycursor.execute(dc)
        mydb.commit()
        ba = "insert into beneficiaries (account_number, beneficiary_name,beneficiary_account_number) values ({},'{}','{}')".format(a,self.beneficairy_name,self.beneficiary_account_number)
        mycursor.execute(ba)
        mydb.commit()


        print("user name  : ",self.user_name)
        print("account number : ",a)
        print("Account Holder Name : ", self.name)
        print("Type of Account : ",self.type)
        print("Balance : ",self.opening_amount)
        print("address : ", self.address)
        print("phone_number : ", self.phone_number)
        print("addhar number : ",self.aadhar_number)
        print("credit_card number : ",self.credit_card_no)
        print("credit_card_cvv : ",self.credit_cvv)
        print("credit_card_pin : ",self.credit_pin)
        print("debit_card_no : ",self.debit_card_no)
        print("debit_card_cvv : ",self.debit_cvv)
        print("debit_card_pin : ",self.debit_pin)
        print("beneficiary_name : ",self.beneficairy_name)
        print("beneficiary_account_number : ",self.beneficiary_account_number)