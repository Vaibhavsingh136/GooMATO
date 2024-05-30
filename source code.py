import mysql.connector as ms
from colorama import Fore,Back,Style,init
import random
from os import system
from datetime import date

#start Here
def welcome():
    print("Welcome to Food Ordering Project")
    x=int(input("1. Login \t 2. Register \t 3.Exit: "))
    if(x==1):
        loginc()
    elif(x==2):
        add()
    else:
        exit()

#ORDER HERE
def menu(cust,crt):
    system('cls')
    con = ms.connect(host = "localhost" , database="menu" , user = "root" , password = "")
    b = int(input("PRESS 1 FOR BREAKFAST\n"
                  "PRESS 2 FOR LUNCH\n"
                  "PRESS 3 FOR DINNER\n"
                  "PRESS 4 FOR DESERTS\n"
                  "PRESS 5 FOR BEVRAGES\n"
                  "PRESS 6 TO VIEW CART\n"
                  "PRESS 7 FOR Previous Orders\n"
                  "PRESS 0 TO LOG-OUT\n"
                       "="))
    system('cls')
    if b==0:
        crt=""
        cst=0
        welcome()
        
    if b==1:
        c = int(input("PRESS 1 FOR VEG" "\n" 
        "PRESS 2 FOR NON-VEG" "\n"
        "PRESS 3 FOR NO PREFERENCE" "\n"
        "="))
        if c==1:
            cur = con.cursor()
            cur.execute("select * from breakfast where type = 'VEG'" )
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"

        if c==2:
            cur = con.cursor()
            cur.execute("select * from breakfast where type = 'NON-VEG'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
        if c==3:
            cur = con.cursor()
            cur.execute("select * from breakfast")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"


    if b==2:
        c = int(input("PRESS 1 FOR VEG" "\n"
        "PRESS 2 FOR NON-VEG" "\n"
        "PRESS 3 FOR NO PREFERENCE" '\n'
        "="))
        if c==1:
            cur = con.cursor()
            cur.execute("select * from lunch where type = 'VEG'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"

        if c==2:
            cur = con.cursor()
            cur.execute("select * from lunch where type = 'NON-VEG'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
        if c==3:
            cur = con.cursor()
            cur.execute("select * from lunch")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])   
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"

    if b==3:
        c = int(input("PRESS 1 FOR VEG" "\n"
        "PRESS 2 FOR NON-VEG" "\n"
        "PRESS 3 FOR NO PREFERENCE" "\n"
        "="))
        if c==1:
            cur = con.cursor()
            cur.execute("select * from dinner where type = 'VEG'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
        if c==2:
            cur = con.cursor()
            cur.execute("select * from dinner where type = 'NON-VEG'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
        if c==3:
            cur = con.cursor()
            cur.execute("select * from dinner")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])                    
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
    if b==4:
        c = int(input("PRESS 1 FOR HOT" "\n"
        "PRESS 2 FOR COLD" "\n"
        "PRESS 3 FOR NO PREFERENCE" "\n"
        "="))
        if c==1:
            cur = con.cursor()
            cur.execute("select * from desserts where type = 'HOT'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"

        if c==2:
            cur = con.cursor()
            cur.execute("select * from desserts where type = 'cold'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"

        if c==3:
            cur = con.cursor()
            cur.execute("select * from desserts")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])   
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
    if b==5:
        c = int(input("PRESS 1 FOR HOT" "\n"
        "PRESS 2 FOR COLD" "\n"
        "PRESS 3 FOR NO PREFERENCE" "\n"
        "="))
        if c==1:
            cur = con.cursor()
            cur.execute("select * from beverages where type = 'HOT'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
        if c==2:
            cur = con.cursor()
            cur.execute("select * from beverages where type = 'cold'")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
        if c==3:
            cur = con.cursor()
            cur.execute("select * from beverages")
            value = cur.fetchall()
            n=0
            for x in value:
                n+=1
                if(len(x[0])<6):
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2]) 
                else:
                    print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2])               
            sel=int(input("Choose Item No. to Order,   0 to Go Back"))
            if(sel==0):
                pass
            else:
                crt+=value[sel-1][0]+"--"+str(value[sel-1][1])+"##"
                
    if b==6:
        amt=0
        if(len(crt)==0):
            print("CART Empty")
        else:            
            for x in crt.split("##"):
                print(x)
                if(len(x)>0):
                    amt=amt+int(x.split("--")[1])
            print("Total Amount : ",amt)
            c=int(input("Press 1. To Choose More\n      2. Order Confirm\n      3. Clear Cart : "))
            if(c==1):
                pass
            elif(c==2):
                odate = date.today()
                con = ms.connect(host = "localhost" , database="info" , user = "root" , password = "")
                cur = con.cursor()
                x="insert into orders values (%s,'%s','%s',%s)" %(cust,odate,crt,amt)
                cur.execute(x)
                con.commit()
                crt=""
                print("\n\tOrder Placed on Date:",odate,"\tTotal Bill:",amt)
            elif(c==3):
                crt=""
        x=input('\n_______________________Press ENTER to Continue_____________________________')

    if b==7:
        con = ms.connect(host = "localhost" , database="info" , user = "root" , password = "")
        cur = con.cursor()
        cur.execute("select * from orders where CustomerId="+str(cust))
        prv=cur.fetchall()
        for x in prv:
            print(x[1],"\t",x[2].replace("##"," , "),"\b\b\b   ",x[3])
        x=input('\n_______________________Press ENTER to Continue_____________________________')
        
    return (cust,crt)

######################################################################################################################        

#CUSTOMER
# LOGIN
def loginc():
    x=1
    cust=int(input("Enter Customer ID: "))
    con = ms.connect(host = "localhost" , database="info" , user = "root" , password = "")
    cur = con.cursor()
    cur.execute("select * from customer where CustomerId="+str(cust))
    b=cur.fetchone()
    if(b != None):
        crt=""
        while(x==1):
            cust,crt=menu(cust,crt)            
    else:
        x=input("No such User Found")
        exit()

# ADD                    
def add():
    con = ms.connect(host = "localhost" , database="info" , user = "root" , password = "")
    n = input(Back.BLACK+Fore.CYAN+Style.BRIGHT+"ENTER YOUR NAME = ")
    a = input(Back.BLACK+Fore.CYAN+Style.BRIGHT+"ENTER YOUR ADDRESS = ")
    p = input(Back.BLACK+Fore.CYAN+Style.BRIGHT+"ENTER YOUR PHONE NO. = ")
    c = str(random.randint(100,999))
    print("Your Customer ID is: ",c)
    cur = con.cursor()
    x="insert into customer values ('%s','%s','%s',%s)" %(n,a,p,c)
    cur.execute(x)
    con.commit()
    x=input('\n_______________________Press ENTER to Continue_____________________________')
    loginc()

#VIEW
def details():
    con = ms.connect(host = "localhost" , database="info" , user = "root" , password = "")

    cur = con.cursor()
    con.commit()
    b="select * from customer"
    cur.execute(b)
    value = cur.fetchall()
    for x in value:
        if(len(x[0])<6):
            print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2],"\t",x[3]) 
        else:
            print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2],"\t",x[3])

#EDIT
def detailsp():
    con = ms.connect(host = "localhost" , database="info" , user = "root" , password = "")

    cur = con.cursor()
    con.commit()
    b="select * from customer where CustomerId = c"
    cur.execute(b)
    value = cur.fetchall()
    for x in value:
        if(len(x[0])<6):
            print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t\t",x[1],"\t",x[2],"\t",x[3]) 
        else:
            print(Back.BLACK+Fore.CYAN+Style.BRIGHT+str(n)+"\t"+x[0],"\t",x[1],"\t",x[2],"\t",x[3])


#MENU EDIT
def edit():
    con = ms.connect(host = "localhost" , database="menu" , user = "root" , password = "")

    a = int(input("PRESS 1 TO ADD ITEM "       "\n"    "PRESS 2 TO REMOVE ITEM "       "\n"        "="))

    if a==1:
        t = int(input("PRESS 1 FOR BREAKFAST" "\n"  "PRESS 2 FOR LUNCH"    "\n"  "PRESS 3 FOR DINNER"    "\n"    "PRESS 4 FOR DESERT"     "\n"    "PRESS 5 FOR BEVRAGES"   "\n"  "="))
        if t==1:
            n = input("ENTER FOOD ITEM NAME:-")            
            p = int(input("ENTER PRICE = "))
            i = input("ENTER TYPE = ")

            cur = con.cursor()
            x="insert into BREAKFAST values ('%s',%s,'%s')" %(n,p,i)
            cur.execute(x)
            con.commit()

        if t==2:
            n = input("ENTER FOOD ITEM NAME:-")            
            p = int(input("ENTER PRICE = "))
            i = input("ENTER TYPE = ")

            cur = con.cursor()
            x="insert into LUNCH values ('%s',%s,'%s')" %(n,p,i)
            cur.execute(x)
            con.commit()

        if t==3:
            n = input("ENTER FOOD ITEM NAME:-")            
            p = int(input("ENTER PRICE = "))
            i = input("ENTER TYPE = ")

            cur = con.cursor()
            x="insert into DINNER values ('%s',%s,'%s')" %(n,p,i)
            cur.execute(x)
            con.commit()

        if t==4:
            n = input("ENTER FOOD ITEM NAME:-")            
            p = int(input("ENTER PRICE = "))
            i = input("ENTER TYPE = ")

            cur = con.cursor()
            x="insert into desserts values ('%s',%s,'%s')" %(n,p,i)
            cur.execute(x)
            con.commit()

        if t==5:
            n = input("ENTER FOOD ITEM NAME:-")            
            p = int(input("ENTER PRICE = "))
            i = input("ENTER TYPE = ")

            cur = con.cursor()
            x="insert into beverages values ('%s',%s,'%s')" %(n,p,i)
            cur.execute(x)
            con.commit()   


    if a==2:
        t = int(input("PRESS 1 FOR BREAKFAST" "\n"
                "PRESS 2 FOR LUNCH" "\n"
                "PRESS 3 FOR DINNER" "\n"
                "PRESS 4 FOR DESERT" "\n"
                "PRESS 5 FOR BEVRAGES" "\n"
                "="))                   

        if t==1:
            d = input("ENTER ITEM NAME TO DELETE: ")  
            cur = con.cursor()
            x="delete from breakfast where item='%s'" %(d)
            cur.execute(x)
            con.commit()

        if t==2:
            d = input("ENTER ITEM NAME TO DELETE: ")  
            cur = con.cursor()
            x="delete from lunch where item='%s'" %(d)
            cur.execute(x)
            con.commit()

        if t==3:
            d = input("ENTER ITEM NAME TO DELETE: ")  
            cur = con.cursor()
            x="delete from dinner where item='%s'" %(d)
            cur.execute(x)
            con.commit()

        if t==4:
            d = input("ENTER ITEM NAME TO DELETE: ")  
            cur = con.cursor()
            x="delete from desserts where item='%s'" %(d)
            cur.execute(x)
            con.commit()

        if t==5:
            d = input("ENTER ITEM NAME TO DELETE: ")  
            cur = con.cursor()
            x="delete from beverages where item='%s'" %(d)
            cur.execute(x)
            con.commit()

###################################################################################
welcome()
