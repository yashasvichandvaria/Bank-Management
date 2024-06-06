import mysql.connector

mydb=mysql.connector.connect(user="root",
                             passwd="123456",
                             host="localhost",
                             database="BankDB"
                             )

mycursor=mydb.cursor()
#Created Database BankDB
#Function to display the menu
def Menu():             #Function to Display the main menu
  print("*"*140)
  print( "\t\t*******************************MAIN MENU*****************************")
  print("\t\t\t 1. Create new Account")
  print("\t\t................................................................................................................")
  print("\t\t\t 2. Display Records")
  print("\t\t\t     a. Sorted as per account number")
  print("\t\t\t     b. Sorted as per Customer Name")
  print("\t\t\t     c.Exit")
  print("\t\t................................................................................................................")
  print("\t\t\t 3. Search record details as per the account number")
  print("\t\t................................................................................................................")
  print("\t\t\t 4. Update Records")
  print("\t\t................................................................................................................")
  print("\t\t\t 5. Delete Records")
  print("\t\t................................................................................................................")
  print("\t\t\t 6. Transactions Debit\Withdrawl from the account")
  print("\t\t\t     a.  Debit\Withdrawl from the account.")
  print("\t\t\t     b.  Credit into the account.")
  print("\t\t\t     c.  Exit.")
  print("\t\t................................................................................................................")
  print("\t\t\t 7.  Exit")
  print("*"*140)
def Menu_sort():
  print("\t\t a.Sorted as per account number")
  print("\t\t b.Sorted as per Customer name.")
  print("\t\t c.Back")
def MenuTransaction():
  print("\t\t      a.  Debit\Withdrawl from account")
  print("\t\t      b.  Credit into the account")
  print("\t\t      c.  Back")
def Create():
  try:
    mycursor.execute("create table bank(ACC_NO varchar(10),NAME varchar(20),MOBILE varchar(10),EMAIL varchar(20),ADDRESS varchar(20),CITY varchar(10),COUNTRY varchar(20),BALANCE integer(15))")
    print("Table Created")
    Insert()
  except:
    print("Table Exist")
    Insert()
def Insert():          
  while True:                        #Loop for accepting records.
    Acc=input("Enter account no")
    Name=input("Enter Name")
    Mob=input("Enter Mobile")
    email=input("Enter Email")
    Add=input("Enter Address")
    City=input("Enter City")
    Country=input("Enter your Country")
    Bal=float(input("Enter Balance"))
    Rec=[Acc,Name,Mob,email,Add,City,Country,Bal]
    Cmd="insert into BANK values (%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(Cmd,Rec)
    mydb.commit()
    ch=input("Do you want to enter more records, Enter Y/N")
    if ch=='N' or ch=='n':
      print("Records inserted succesfully")
      break

    
def DispSortAcc():             #Display records as per ascending order of acc no.
  try:
    cmd="select*from BANK order by ACC_NO"
    mycursor.execute(cmd)
    S=mycursor.fetchall()
    F="%15s %15s %15s %15s %15s %15s %15s %15s"
    print(F % ("ACCNO", "NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
    print("="*120)
    for i in S:
      for j in i:
        print("%16s" % j,end=' ')
      print()
    print("="*120)
  except:
    print("Table doesn't exist")
    
def DispSortName():                #Function to Display Records as per ascending order of Name.
  try:
    cmd="select* from BANK order by NAME"
    mycursor.execute(cmd)
    S=mycursor.fetchall()
    F="%15s %15s %15s %15s %15s %15s %15s %15s"
    print(F %("ACCNO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
    print("="*120)
    for i in S:
      for j in i:
        print("%16s" %j,end=' ')
      print()
    print("="*120)
  except:
    print("Table doesn't exist")
    
          
def DispSearchAcc():        #Function to search for the record from the file with respect to account number
  try:
    cmd="select*from Bank"
    mycursor.execute(cmd)
    S=mycursor.fetchall()
    ch=input("Enter the account no to be searched")
    for i in S:
      if i[0]==ch:
        print("="*120)
        F="%15s %15s %15s %15s %15s %15s %15s %15s "
        print(F%("ACCNO","NAME","MOBILE","EMAIL ADD","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*120)
        for j in i:
          print("%14s" %j,end=' ')
        print()
        break
    else:
      print("Record not found")
  except:
    print("Table doesn't exist")

    
def Update():             #Function to change the details of a customer
  try:
    cmd="select*from Bank"
    mycursor.execute(cmd)
    S=mycursor.fetchall()
    A=input("Enter the account no whose details to be changed")
    for i in S:
      i=list(i)
      if i[0]==A:
        ch=input("Change Name(Y/N)")
        if ch=='y' or ch=='Y':
          i[1]=input("Enter Name")

        ch=input("Change Mobile(Y/N)")
        if ch=='y' or ch=='Y':
          i[2]=input("Enter mobile")

        ch=input("Change Email(Y/N)")
        if ch=='y' or ch=='Y':
          i[3]=input("Enter email")

        ch=input("Change Address(Y/N)")
        if ch=='y' or ch=='Y':
          i[4]=input("Enter Address")
          

        ch=input("Change City(Y/N)")
        if ch=='y' or ch=='Y':
          i[5]=input("Enter city")
         
        ch=input("Change Country(Y/N)")
        if ch=='y' or ch=='Y':
          i[6]=input("Enter Country")
         
        ch=input("Change Balance(Y/N)")
        if ch=='y' or ch=='Y':
          i[7]=int(input("Enter Balance"))
        cmd="update Bank set NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s where ACC_NO=%s"
        val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
        mycursor.execute(cmd,val)
        mydb.commit()
        print("Account Updated")
        break
    else:
      print("Record not Found")
  except:
    print("No such Table")

def Delete():               #Function to delete the details of a customer.
  try:
    cmd="select*from Bank"
    mycursor.execute(cmd)
    S=mycursor.fetchall()
    A=input("Enter the account no whose account to be deleted")
    for i in S:
      i=list(i)
      if i[0]==A:
        cmd="delete from Bank where acc_no=%s"
        val=(i[0],)
        mycursor.execute(cmd,val)
        mydb.commit()
        print("Account Deleted")
        break
    else:
      print("Record not Found")
  except:
    print("No such Table")

    

def Debit():                      #Function to withdrawl the amount by assuring the min balance of Rs5000
  try:
    cmd="select * from Bank"
    mycursor.execute(cmd)
    S=mycursor.fetchall()
    print("Please Note that the Money can be debited if min balance of Rs5000 exists")
    acc=input("Enter the account no from which money is to be debited")
    for i in S:
      i=list(i)
      if i[0]==acc:
        Amt=float(input("Enter the amount to be withdrawn"))
        if i[7]-Amt>=5000:
          i[7]-=Amt
          cmd="update bank set BALANCE=%s where ACC_NO=%s"
          val=(i[7],i[0])
          mycursor.execute(cmd,val)
          mydb.commit()
          print("Amount Debited")
          break
        else:
          print("There must be min Balance of Rs5000")
          break
    else:
      print("Record Not Found")
  except:
    print("table Doesn,t Exist")

    
def Credit():         #Function to Withdrawl amount by assuring the min balance of Rs5000
  try:
    cmd="select*from Bank"
    mycursor.execute(cmd)
    S=mycursor.fetchall()
    acc=input("Enter the account no from which the money to be deposited")
    for i in S:
      i=list(i)
      if i[0]==acc:
        Amt=float(input("Enter the amount to be credited"))
        i[7]+=Amt
        cmd="update bank set BALANCE=%s where ACC_NO=%s"
        val=(i[7],i[0])
        mycursor.execute(cmd,val)
        mydb.commit()
        print("Amount Credited")
        break
    else:
      print("Record not found")
  except:
    print("Table does not exist")


    
while True:
  Menu()
  ch=input("Enter your Choice")
  if ch=="1":
    Create()
  elif ch=="2":
    while True:
      Menu_sort()
      ch1=input("Enter choice a /b /c")
      if ch1 in ['a','A']:
        DispSortAcc()
      elif ch1 in['b','B']:
        DispSortName()
      elif ch1 in['c','C']:
        print("Back to main Menu")
        break
      else:
        print("Invalid choice")
  elif ch=="3":
    DispSearchAcc()
  elif ch=="4":
    Update()
  elif ch=="5":
    Delete()
  elif ch=="6":
    while True:
      MenuTransaction()
      ch1=input("Enter choice a/b/c")
      if ch1 in ['a','A']:
        Debit()
      elif ch1 in ['b','B']:
        Credit()
      elif ch1 in ['c','C']:
        print("Back to main menu")
        break
      else:
        print("Invalid Choice")
  elif ch=="7":
    print("Exiting...........")
    break
  else:
    print("!!!!Wrong Choice!!!!")
      
                  
                            
  
  
        
      
  
  
    
    
  
                        
