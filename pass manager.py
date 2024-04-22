from cryptography.fernet import Fernet
import mysql.connector as con
db=con.connect(host='localhost',user='root',password='harish123',database='passwords')
if db.is_connected():
    print('connection established')
mycursor=db.cursor()
mycursor.execute("CREATE DATABASE if not exists password_manager")
mycursor.execute("CREATE TABLE if not exists info(username VARCHAR(100),encrypted_password VARCHAR(100),site_name VARCHAR(100),email VARCHAR(100),key1 VARCHAR(100),PRIMARY KEY(site_name,email))")
mycursor.execute("CREATE TABLE if not exists mpass1(epass VARCHAR(100),key2 VARCHAR(100),secret VARCHAR(100))")

def menu():
    print('-'*30)
    print(('-'*13) + 'PASSWORD MANAGER'+ ('-' *13))
    print('1. Create new password')
    print('2. Find a password for a site or app')
    print('3. Create new master password')
    print('4. Get Master password')
    print('5. Exit')
    print('-'*30)
menu()

def selection():
    global sel
    sel=int(input("Enter your choice :"))
selection()


def master():
    secr=str(input('Please enter secret code to get master password :'))
    mycursor.execute("select epass from mpass1 where secret=%s",(secr,))
    resu= mycursor.fetchall()
    resu1=''.join([str(x) for x in resu])
    resu2=bytes(resu1, 'utf-8')
    mycursor.execute("select key2 from mpass1 where secret=%s",(secr,))
    resu3=mycursor.fetchall()
    j=''.join([str(i) for i in resu3])
    j1=bytes(j, 'utf-8')
    f3= Fernet(j1)
    uncipherpass=(f3.decrypt(resu2))
    master=bytes(uncipherpass).decode("utf-8")
    print("Your masterpassword is :", master)


if sel==1:
    site=input("Enter the site name/URL :")
    usern=input("Enter your username :")
    passw=input("Enter you password :")
    email=input("Enter your email id :")
    pass1=bytes(passw, encoding='utf8')
    key = Fernet.generate_key()
    f= Fernet(key)
    epass = f.encrypt(pass1)
    sql= "INSERT INTO info(username,encrypted_password,site_name,email,key1) VALUES(%s,%s,%s,%s,%s)"
    val= (usern,epass,site,email,key)
    mycursor.execute(sql,val)
    db.commit()
    print('Your data has been added successfully')

elif sel==2:
    chek=input("Enter masterpassword to continue :")
    if chek==secr:
        site=str(input('Please proivide the name of the site or app you want to find the password to :'))
        mycursor.execute("select encrypted_password from info where site_name=%s",(site,))
        result = mycursor.fetchall()
        res=''.join([str(x) for x in result])
        res1=bytes(res, 'utf-8')
        mycursor.execute("select key1 from info where site_name=%s",(site,))
        res2= mycursor.fetchall()
        k = ''.join([str(v) for v in res2])
        k1=bytes(k, 'utf-8')
        f1= Fernet(k1)
        uncipher_text =(f1.decrypt(res1))
        fpass = bytes(uncipher_text).decode("utf-8") #convert to string
        print("Your password is :", fpass)
    else:
        print("oops...masterpassword incorrect")
                                        
elif sel==3:
    mycursor.execute("select * from mpass1")
    al=mycursor.fetchall()
    if al==[]:
        mps=input('enter your new masterpassword :')
        mp=input("Enter secret code for this masterpassword :")
        print("You'll need this secret code in the future to get the masterpassword...dont forget it")
        ps1=bytes(mps, encoding='utf8')
        key1 = Fernet.generate_key()
        f2= Fernet(key1)
        empass= f2.encrypt(mps1)
        mpl= "INSERT INTO mpass1(epass,key2,secret) VALUES(%s,%s,%s)"
        vpl= (empass,key1,mp)
        mycursor.execute(mpl,vpl)
        db.commit()
        print('Your masterpassword has been changed successfully')
    else:
        print("masterpassword already exists")


elif sel==4:
    master()
    
else:
    print("BYE :)")






    





  
