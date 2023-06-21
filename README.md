# BANKING MANAGEMENT SYSTEM APPLICATION USING PYTHON AND MYSQL

# About-:  

  In this project I have created Online Banking system  using Python and MySQL. Data entered by the user are stored in MYSQL database in tabular form. 
  Here I have used the OOPS concept like class and multiple methods inside the class
  Also i have implemented the concept of Exception handling(Try raise  except) which will handle and resove various functionality 

  This project is basically designed to create or open an account and after account has been created  the user can see their record their is also beneficiaries 
  record to whom they can transfer fund for ,also how to change the pin number like debit card and credit card two types of card allotted to user.
  
  If someone is not having Login Id, password he/she could make a new id. Further it can also check overall record of a local customer or full detail of a single 
  a/c as per transactions, create a new record for new customer, Update an old customer record. Python is used as Front End and MySQL is used as Back End.

# Prerequisite-:

  Here basic knowledge of python is required with good command on exceptionl handlinh
  Basic commands of git 
  For database MySql 
  
# Requirements-: 

1.Visual Studio Code 
2 Python Latest Version(3.8.10)
3.MySql(8.0.30)
4.Python MySql connector : Most Important

# MySql Details-: 
# Database -:
 Here I have created database named as  'Banking_Project' .This will store all the table records.
 
# Tables inside Database 'Banking_Project'
 
 1-account_details 
   Feilds in it   (account_number,user_name,password,name,type,balance,address,mob  ile,adhar)
2-beneficiaries
   Feilds in it
  (account_number,beneficiary_name,beneficiary_account_number)

3-card
    Feilds in it
   (account_number,card_number,card_type,pin,cvv)
   
# Python Code files-:
 1-: main.py
      This is the main file where i have imported all the files to be run where we can see the result of all the functions 
      
 2-: login.py
      This is the files where login class is defined and inside which i have imported the method of registration function and we can 
      call different function of login and registration
      
 3-: mysqlconnector.py
      In this file i have created the mysql login credential like host name,user-name,password and database name to connect with it

 4-:registration.py
      In this file i have defined  the class create account  inside this class defined function like user_name,beneficary_details,card,password,adhar ,mobile 
      address etc

  # Note -:
       To see the output just run the main.py file 
 
 


 

  
