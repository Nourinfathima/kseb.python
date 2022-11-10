
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'ksebdb')

mycursor = mydb.cursor()
while True:

    print("select an option from menu")

    print("1 add consumer")

    print("2 search a consumer")

    print("3 delete the consumer")

    print("4 update a consumse")
    
    print("5 view the consumer")

    print("6 genarate the consumerbill")

    print("7 view consumerbill")

    print("8 exit")
    choice = int(input("Enter an option: "))

    if(choice==1):

        print("add consumer selected")

    elif(choice==2):

        print("search  consumer selected")

    elif(choice==3):

        print("delete employe selected")

    elif(choice==4):

        print("update employe selected")

    elif(choice==5):
        print("view employe selected")

    elif(choice==6):
        print("generate the consumerbill ")

    elif(choice==7):
        print("view bill")

    elif(choice==8):
        print("Exit")

        break