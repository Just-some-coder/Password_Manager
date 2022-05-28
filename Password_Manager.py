import random
import csv
import mysql.connector
import string
import sys

key = {'0': 'b7v', '1': 'Qb2', '2': 'EuP', '3': 'm16', '4': 'CXq', '5': 'TTA', '6': 'Usx', '7': 'Ahi', '8': '4nS', '9': 'ipo', 'a': 'Hsb', 'b': 'DCp', 'c': 'FMu', 'd': 'Ks0', 'e': '6tX', 'f': 'lEZ', 'g': 'aok', 'h': '6rL', 'i': '3YG', 'j': 'Qn6', 'k': 'LSm', 'l': 'GSI', 'm': 'Pzl', 'n': 'diQ', 'o': '8cv', 'p': 'KPf', 'q': 'M5d', 'r': 'Ata', 's': 'C4Q', 't': 'RLo', 'u': 'GdM', 'v': 'hkQ', 'w': 'pma', 'x': 'CSC', 'y': 'SfP', 'z': 'YVg', 'A': 'c00', 'B': 'dsz', 'C': 'JHO', 'D': 'UzW', 'E': 'lT1', 'F': 'Yzz', 'G': 'f94', 'H': 'ogF', 'I': 'bgS', 'J': 's5a', 'K': '3V4', 'L': 'Dyv', 'M': 'JmW', 'N': '09z', 'O': '6Z5', 'P': 'Kjx', 'Q': 'v1m', 'R': 'I1H', 'S': 'N0Z', 'T': 'oJz', 'U': '5zX', 'V': 'gEz', 'W': 'Wsu', 'X': 'gan', 'Y': '82M', 'Z': 'SP8', '!': 'rZE', '"': 'INT', '#': 'o5H', '$': 'Mt3', '%': 'qAY', '&': 'PO8', "'": 'BdH', '(': 'j8w', ')': '3Wu', '*': 'yjP', '+': '9Z6', ',': 'DB8', '-': 'Zbg', '.': 'jPS', '/': 'lKN', ':': 'hB8', ';': '1gY', '<': 'PGI', '=': 'P8W', '>': '7m6', '?': 'AqC', '@': 'TqX', '[': 'jwh', '\\': '2Wa', ']': 'Q05', '^': 'm56', '_': 'xvE', '`': 'MKQ', '{': 'EfP', '|': 'Cue', '}': 'Z2V', '~': '4Pm'}

def login():
    mycon=mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    cur=mycon.cursor()
    cur.execute("select * from idpass;")
    data = cur.fetchall()
    uid = str(input("Enter Your ID "))
    password = str(input("Enter Your Password "))
    for i in data:        
        if decoder(i[0])==uid and decoder(i[1])==password:
            print("Logged in")
            return uid
            break
    else:
        print("No record exists")
        sys.exit()
def encoder(upass):
    epass=''
    for i in upass:
        epass+=key[i]
    return(epass)

def decoder(epass):
    dpass = ''
    for i in range(0,len(epass),3):
        for j in key:
            if key[j]== epass[i:i+3]:
                dpass += j
    return(dpass)

def access():
    mycon = mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    cur = mycon.cursor()
    cur.execute("select * from "+uid+";")
    data = cur.fetchall()
    x = str(input("Search By Keyword(kwd) or by exact email(eem) ?"))
    if x=='kwd':
        y= str(input("Enter The Keyword "))
        for i in data:
            if y in decoder(i[0]):
                print(decoder(i[0]),decoder(i[1]))
    elif x=='eem':
        y= str(input("Enter The Email "))
        for i in data:
            if y==decoder(i[0]):
                print(decoder(i[0]),decoder(i[1]))
                
def Delete():
    mycon=mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    cur=mycon.cursor()
    print("Enter the ID ,you would like to delete ? ")
    x = str(input())
    cur.execute("Select * from "+uid)
    data=cur.fetchall()
    for i in data:
        if str(decoder(i[0]))==x:
            x='"'+encoder(x)+'"'
            temp="delete from "+uid+" where User_ID="+x+";"
            cur.execute(temp)
            mycon.commit()
            print("Record deleted")
    mycon.close()

def cng():
    mycon=mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    cur=mycon.cursor()
    print("Enter the ID ,you would like to change ? ")
    x = str(input())
    y = str(input("Enter updated email id "))
    z = str(input("Enter updated password "))
    cur.execute("Select * from "+uid)
    data=cur.fetchall()
    for i in data:
        if str(decoder(i[0]))==x:
            y='"'+encoder(y)+'"'
            z='"'+encoder(z)+'"'
            x='"'+encoder(x)+'"'
            temp="update "+uid+" set User_ID="+y+",User_password="+z+" where User_ID="+x+";"
            cur.execute(temp)
            mycon.commit()
            print("Updated succesfully ")
    mycon.close()

def add():
    mycon=mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    cur=mycon.cursor()
    x = str(input("Enter your Email-ID "))
    y = str(input("Enter your password "))
    x = '"'+encoder(x)+'"'
    y = '"'+encoder(y)+'"'
    temp = "insert into "+uid+" values("+x+","+y+");"
    cur.execute(temp)
    mycon.commit()
    mycon.close()
    print("Sucessfully Added")

def upd():
    mycon=mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    cur=mycon.cursor()
    print("Would you like to make changes or add a new record? ")
    x = str(input("Change(cng) or Add(add) ? "))
    if x.lower()=='cng':
        cng()
    elif x.lower()=='add':
        add()
    else:
        print("Unknown function")

def Import():
    filename= str(input("Enter the name of your file "))
    mycon=mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    cur=mycon.cursor()
    f=open(filename+".csv",'r',newline='\r\n')
    reader=csv.reader(f)
    for i in reader:
        x = encoder(i[0])
        y = encoder(i[1])
        cur.execute("insert into "+uid+" values('%s','%s');"%(x,y))
        mycon.commit()
    mycon.close()
    print('file Imported')
    f.close()


def export():
    name=str(input("Name your file "))
    mycon=mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    f = open(name+".csv","a",newline='\r\n')
    cur = mycon.cursor()
    writer=csv.writer(f)
    cur.execute("select * from "+uid)
    r=cur.fetchall()
    for i in r:
        writer.writerow([decoder(i[0]),decoder(i[1])])
    print("Exporting Completed")
    mycon.close()
    f.close()


def GAK():
    asc=list(string.printable)
    asc=asc[0:94]
    code=[]
    while len(code)<94:
        x = random.choice(asc[0:62])+random.choice(asc[0:62])+random.choice(asc[0:62])
        if x not in code:
            code.append(x)
    key={}
    for i in range(94):
        key[asc[i]]=code[i]
    return key

def GAP():
    password = ''
    special_chars = list(string.printable[62:94])
    numbers = list(string.printable[0:10])
    alphabetsC = list(string.printable[36:62])
    alphabestS = list(string.printable[10:36])
    n = random.choice(numbers[4:9])
    for i in range(int(n)):
        password = password+random.choice(alphabetsC)
        password = password+random.choice(alphabestS)
        password = password+random.choice(special_chars)
        password = password+str(random.choice(numbers))
    return "Here is a randomly Generated password " + password

def CPS():
    u,l,n,s,g=0,0,0,0,0
    up = str(input("Enter Your Password "))
    if len(up)>=16:
        for i in up:
            if i.isupper():
               u+=1
            elif i.islower():
                l+=1
            elif i.isnumeric():
                n+=1
            else:
                s+=1
        if u>=4:
            g+=1
        if l>=4:
            g+=1
        if n>=4:
            g+=1
        if s>=4:
            g+=1
        if g==4:
            print("Very Strong Password")
        elif g==3:
            print("Moderate Password")
        else:
            print("Weak Password")
    else:
        print("Weak Password")

def Signin():
    uid = str(input("Enter Your id: "))
    upass = str(input("Enter Your Password: "))
    upass1= str(input("Re-Enter Your Password: "))
    while upass!=upass1:
        print("Passwords do not match, Retry")
        upass = str(input("Enter Your Password: "))
        upass1= str(input("Re-Enter Your Password: "))  
    mycon = mysql.connector.connect(host='localhost',user='root',password='123456',database='idpass')
    cur=mycon.cursor()
    temp="create table "+uid+"(User_ID varchar(2000), User_password varchar(2000));"
    cur.execute(temp)
    uid = '"'+encoder(uid)+'"'
    upass = '"'+encoder(upass)+'"'
    cur.execute("insert into idpass values("+uid+","+upass+")")
    mycon.commit()
    mycon.close()
    return decoder(uid)
    
res = str(input('''Type lgn to Login
Type sgu to Sign IN
Type anything else to close
'''))

if res=='sgu':
    uid=Signin()
elif res=='lgn':
    uid = login()
else:
    sys.exit()

print("""
=============================================================================                                                                                                                                                                                          
|    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗    |  
|    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗   |
|    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║   |
|    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║   | 
|    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝   | 
|    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝    |                                                                                                                                                          
|    ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗         | 
|    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗        | 
|    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝        | 
|    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗        |
|    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║        |
|    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝        |
=============================================================================

1.Update                        (UPD)   
2.Access                        (ACC)   
3.Delete                        (DEL)   
4.Import                        (IMP)   
5.Export                        (EXP)            
6.Generate a password           (GAP)   
7.Generate a key                (GAK)   
8.Check password strength       (CPS)   
9.Quit                          (QUT)   
10.Help                         (HLP)    

""")
y = 'y'

while y == 'y':    
    x = str(input("Which function do you want to use ? Type the keyword next to the function  "))
    if x.upper() == 'UPD':    #1
        upd()
        
    elif x.upper()=='ACC':    #2
        access()
        
    elif x.upper()=='DEL':    #3
        Delete()
        
    elif x.upper()=='IMP':    #4
        Import()
        
    elif x.upper()=='EXP':    #5
        export()
            
    elif x.upper()=='GAP':    #6
        print(GAP())
        
    elif x.upper()=='GAK':    #7
        print(GAK())
        
    elif x.upper()=='CPS':    #8
        CPS()
        
    elif x.upper()=='QUT':    #9
        break

    elif x.upper()=='HLP':    #10
        
        Y='y'
        
        while Y=='y':
            z = str(input("Which function do you need to know about? "))
            
            if z.upper() == 'UPD':              #1
                print("This function will allow you to make any changes in your database")
                
            elif z.upper()=='ACC':              #2
                print("This function will allow you to fetch data from the database")
                
            elif z.upper()=='DEL':              #3
                print("This function will allow you to delete an entry from the database")
                
            elif z.upper()=='IMP':              #4
                print("This function will allow you to import your own password file to the database")
                
            elif z.upper()=='EXP':              #5
                print("This function will allow you to export the saved database")

            elif z.upper()=='GAP':              #6
                print("This function will generate a complex password for you to use")
                
            elif z.upper()=='GAK':              #7
                print("This function will generate a key for you to do your own encryption")
                
            elif z.upper()=='CPS':              #8
                print("This function will check if the password you've entered is strong or weak")
                
            elif z.upper()=='QUT':              #9
                print("Using this function will instantly close the program")
                
            Y = str(input("Do you want more help? (Y)")) 
    else:
        print("No such function exist\n")
        
    y = str(input("Use another function? (Y)"))
    
print("Quitting program")
