##mysql connection
import mysql.connector
msql=mysql.connector.connect(host="localhost",user="root",\
                             passwd="mpire",database="smartres")
m=msql.cursor()

##Main table creation
m.execute("create table orders(Table_no int(5),Flavor varchar(30),Food varchar(30),\
Quantity int(5),Amount float(5),Total_amount float(50))")

##Sub table creation
m.execute("create table flavor(s_no int(5),flavor varchar(20))")
m.execute("create table food(No int(5),food varchar(20))")
m.execute("create table _food_(flavor varchar(20),food varchar(20))")
m.execute("create table price(food varchar(20),price float(5))")
m.execute("create table quantity(food varchar(20),quantity float(5))")

##Dictionaries
import json
dict0={1:"Indian",2:"American",3:"Chinese"}
dict1={"Indian":{1:'Biriyani',2:'Thali meals',3:'Masala dosa'},\
       "American":{4:'Maccaroni and cheese',5:'Pizza',6:'Corned beef'},\
       "Chinese":{7:'Noodles',8:'Dumplings',9:'Tofu'}}
dict2={'Biriyani':180,'Thali meals':120,'Masala dosa':70,\
       'Maccaroni and cheese':580,'Pizza':300,'Corned beef':620,\
       'Noodles':50,'Dumplings':100,'Tofu':120}
dict3={'Biriyani':40,'Thali meals':10,'Masala dosa':4,\
       'Maccaroni and cheese':50,'Pizza':30,'Corned beef':20,\
       'Noodles':50,'Dumplings':10,'Tofu':20}

##Lists
lst0=list(dict0.keys())
lst00=list(dict0.values())
lst1=list(dict1.keys())
lst11=list(dict1.values())
lst2=list(dict2.keys())
lst22=list(dict2.values())
lst3=list(dict3.keys())
lst33=list(dict3.values())

##Functions
def flavor():
    for i in range(len(lst0)):
        data=(lst0[i],lst00[i])
        qry=("insert into flavor values(%s,%s)")
        m.execute(qry,data)
        msql.commit()
    m.execute("select * from flavor")
    mrec=m.fetchall()
    print("+-------------+-------------+")
    print("|   Number    |   Flavor    |")
    print("+-------------+-------------+")
    for i in range(len(mrec)):
        print("|",mrec[i][0]," "*(10-len(str(mrec[i][0]))),"|",mrec[i][1]," "*(10-len(mrec[i][1])),"|")
    print("+-------------+-------------+")

def _food_():
    for i in range(len(lst11)):
        for j in range(len(lst11[i])):
            a=list(lst11[i].values())
            data=(lst1[i],a[j])
            qry=("insert into _food_ values(%s,%s)")
            m.execute(qry,data)
            msql.commit()
    m.execute("select * from _food_")
    mrec=m.fetchall()
    print("+-------------+-----------------------+")
    print("|   Flavor    |          Food         |")
    print("+-------------+-----------------------+")
    for i in range(len(mrec)):
        print("|",mrec[i][0]," "*(10-len(mrec[i][0])),"|",mrec[i][1]," "*(20-len(mrec[i][1])),"|")
    print("+-------------+-----------------------+")

def select_food(n):
    for i in dict0:
        if n==i:
            for j in lst11[i-1]:
                data=(j,lst11[i-1][j])
                qry=("insert into food values(%s,%s)")
                m.execute(qry,data)
                msql.commit()
            m.execute("select * from food")
            mrec=m.fetchall()
            print("+-------------+-----------------------+")
            print("|   Number    |         Food          |")
            print("+-------------+-----------------------+")
            for i in range(len(mrec)):
                print("|",mrec[i][0]," "*(10-len(str(mrec[i][0]))),"|",mrec[i][1]," "*(20-len(mrec[i][1])),"|")
            print("+-------------+-----------------------+")

def price():
    for i in lst2:
        data=(i,dict2[i])
        qry=("insert into price values(%s,%s)")
        m.execute(qry,data)
        msql.commit()
    m.execute("select * from price")
    mrec=m.fetchall()
    print("+-----------------------+---------------+")
    print("|         Food          |     Price     |")
    print("+-----------------------+---------------+")
    for i in range(len(mrec)):
        print("|",mrec[i][0]," "*(20-len(mrec[i][0])),"|",mrec[i][1]," "*(12-len(str(mrec[i][1]))),"|")
    print("+-----------------------+---------------+")

def quantity():
    for i in lst3:
        data=(i,dict3[i])
        qry=("insert into quantity values(%s,%s)")
        m.execute(qry,data)
        msql.commit()
    m.execute("select * from quantity")
    mrec=m.fetchall()
    print("+-----------------------+---------------+")
    print("|         Food          |   Quantity    |")
    print("+-----------------------+---------------+")
    for i in range(len(mrec)):
        print("|",mrec[i][0]," "*(20-len(mrec[i][0])),"|",mrec[i][1]," "*(12-len(str(mrec[i][1]))),"|")
    print("+-----------------------+---------------+")

def clear():
    m.execute("delete from flavor")
    m.execute("delete from food")

##Graph creation
import matplotlib.pyplot as p
x1=[]
values1=[]
x2=[]
values2=[]

def Pgraph():
    for i in lst2:
        x2.append(i)
        values2.append(dict2[i])
    p.plot(x2,values2,'r',linewidth=2,linestyle="solid",marker='*',markersize=5,markeredgecolor='k')
    p.title("Food Price",color='r')
    p.xlabel("Food",color='r')
    p.ylabel("Price",color='r')
    p.xlim(0,5)
    p.show()
    
def Qgraph():
    for i in lst3:
        x1.append(dict3[i])
        values1.append(i)
    lst=["k","k","k","k","k","k","k","k","k"]
    for i in range(len(x1)):
        if x1[i]<=10:
            lst[i]="r"
        elif x1[i]>10 and x1[i]<=30:
            lst[i]="y"
        else:
            lst[i]="g"
    p.pie(x1,labels=values1,autopct="%2d%%",colors=lst,explode=[0.05]*len(x1),shadow=True,radius=1.1)
    p.title("Food Quantity",color='r')
    p.show()    

##Main Program
while True:
    print("\t\t\t\t\t\tSmart Restaurant")
    print("\t\t\t\t\t\t----------------")
    print("\t\t\t'To serve someone is beautiful, when you do it with whole heart'")
    print("\t\t\t----------------------------------------------------------------")
    print("\t\t\t\t\tWelcome to Restaurant : Cuisine love")
    print("\t\t\t\t\t\t\t\tContact : 9445666111")
    print("\t\t\tCheck out the site for more details : 'www.smartres4cuisinelove.com'")
    print("\t\t\t--------------------------------------------------------------------")
    print("1 - Take order")
    print("2 - See flavor and food")
    print("3 - See food_price")
    print("4 - See food_price graph")
    print("5 - See food_quantity")
    print("6 - See food_quantity graph")
    print("7 - Order history")
    print("8 - Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        while True:
            strt=input("Begin order? (Press 'Y' for yes and 'N' for no):")
            if strt=='Y' or strt=='y':
                while True:
                    print("Which flavor do you have in mind? We have")
                    flavor()
                    cnte0=input("Do you want to continue?(Y/N):")
                    if cnte0=='Y' or cnte0=='y':
                        chflno=int(input("Choose flavor number:"))
                        if chflno not in lst0:
                            print("Invalid")
                            clear()
                            continue
                        for i in range(len(dict1)):
                            if lst1[i]==dict0[chflno]:
                                a=lst11[i]
                                print("Good choice!")
                                while True:
                                    print("In",dict0[chflno],"flavor, we have these dishes:")
                                    select_food(chflno)
                                    cnte=input("Do you want to continue?(Y/N):")
                                    if cnte=='Y' or cnte=='y':
                                        chfono=int(input("Choose food number:"))                                                                                
                                        if chfono not in list(a.keys()):
                                            print("Invalid")
                                            clear()
                                            continue
                                        elif dict3[a[chfono]]==0:
                                            print("Not available right now.")
                                            clear()
                                            continue
                                        else:
                                            print("Nice choice!")
                                            t=int(input("Enter the table no.:"))
                                            print("The price for",a[chfono],"is Rs",dict2[a[chfono]])
                                            print("Available:",dict3[a[chfono]])
                                            d=int(input("How many?:"))
                                            if d>dict3[a[chfono]]:
                                                print(d,a[chfono],"not available")
                                                clear()
                                            elif d<=dict3[a[chfono]]:                                                
                                                print("The total amount is",d*dict2[a[chfono]])                                                
                                                dict3[a[chfono]]-=d
                                                clear()
                                            cnfrmordr=input("Confirm order(Y/N):")
                                            if cnfrmordr=='Y' or cnfrmordr=='y':
                                                while True:
                                                    print("You have ordered",d,a[chfono],"from",dict0[chflno],"flavor")
                                                    print("Your meal's on the way. Please wait...")
                                                    qry=("insert into orders values(%s,%s,%s,%s,%s,%s)")
                                                    table=t
                                                    flav=dict0[chflno]
                                                    food=a[chfono]
                                                    qty=d
                                                    amount=dict2[a[chfono]]
                                                    total_amount=qty*amount
                                                    data=(table,flav,food,qty,amount,total_amount)
                                                    m.execute(qry,data)
                                                    msql.commit()
                                                    break
                                            elif cnfrmordr=='N' or cnfrmordr=='n':
                                                print("OK")
                                                clear()
                                                continue
                                            else:
                                                print("Invalid")
                                                clear()
                                                continue
                                    elif cnte=='N' or cnte=='n':
                                        print("OK")
                                        clear()
                                        break
                                    else:
                                        print("Invalid")
                                        clear()
                    elif cnte0=='N' or cnte0=='n':
                        print("OK")
                        clear()
                        break
                    else:
                        print("Invalid")
                        clear()
            elif strt=='N' or strt=='n':
                print("Have a nice day! Thank you for using me!")
                break
            else:
                print("Invalid")
    elif ch==2:
        _food_()
    elif ch==3:
        price()
    elif ch==4:
        Pgraph()
    elif ch==5:
        quantity()
    elif ch==6:
        Qgraph()
    elif ch==7:
        print()
        m.execute("select * from orders")
        mrec=m.fetchall()
        print("+-------------+-------------+-----------------------+---------------+---------------+------------------+")
        print("|Table number |   Flavor    |          Food         |   Quantity    |    Amount     |   Total amount   |")
        print("+-------------+-------------+-----------------------+---------------+---------------+------------------+")
        for i in range(len(mrec)):
            print("|",mrec[i][0]," "*(10-len(str(mrec[i][0]))),"|",mrec[i][1]," "*(10-len(mrec[i][1])),\
                  "|",mrec[i][2]," "*(20-len(mrec[i][2])),"|",mrec[i][3]," "*(12-len(str(mrec[i][3]))),\
                  "|",mrec[i][4]," "*(12-len(str(mrec[i][4]))),"|",mrec[i][5]," "*(15-len(str(mrec[i][5]))),"|")
        print("+-------------+-------------+-----------------------+---------------+---------------+------------------+")
    elif ch==8:
        break
    else:
        print("Invalid")
