
import mysql.connector
from datetime import date
from tabulate import tabulate

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
        print("Add consumer selected")
        consumerCode = input("Enter the consumer code: ")
        consumerName = input("Enter the consumer name: ")
        consumerPhone = input("Enter the consumer phone: ")
        consumerAddress = input("Enter the consumer address: ")
        sql = "INSERT INTO `consumer`(`consumerCode`, `consumerName`, `consumerPhone`, `consumerAddress`) VALUES (%s,%s,%s,%s)"
        data = (consumerCode,consumerName,consumerPhone,consumerAddress)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data inserted successfully")

    elif(choice==2):

        print("Search Consumer selected")
        searchOption = input("Enter the Consumer Code/Name/Phone to search: ")
        sql = "SELECT `consumerCode`, `consumerName`, `consumerPhone`, `consumerAddress` FROM `consumer` WHERE `consumerCode` ='"+searchOption+"'  OR `consumerName`='"+searchOption+"' OR `consumerPhone` ='"+searchOption+"' "
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice==3):
        print("Delete Consumer Selected")
        consumerCode = input("Enter the consumer code to delete: ")
        sql = "DELETE FROM `consumer` WHERE `consumerCode` = "+consumerCode
        mycursor.execute(sql)
        mydb.commit()
        print("Data deleted successfully.")
 

    elif(choice==4):

        
        print("Update Consumer selected")
        consumerCode = input("Enter the consumer code to update consumer: ")
        consumerName = input("Enter the consumer name to update: ")
        consumerPhone = input("Enter the consumer phone to update: ")
        consumerEmail = input("Enter the consumer email id to update: ")
        consumerAddress = input("Enter the consumer address to update: ")
        sql = "UPDATE `consumer` SET `consumerName`='"+consumerName+"',`consumerPhone`='"+consumerPhone+"',`consumerAddress`='"+consumerAddress+"' WHERE `consumerCode` = "+consumerCode
        mycursor.execute(sql)
        mydb.commit()
        print(" Consumer Data updated successfully")

    elif(choice==5):
       
       print("View All Consumer selected")
       sql = "SELECT `consumerCode`, `consumerName`, `consumerPhone`, `consumerAddress` FROM `consumer` "
       mycursor.execute(sql)
       result = mycursor.fetchall()
       for i in result:
            print(i)
       

    elif(choice==6):
        print('generate bill selected')
        dates = date.today()
        year = dates.year
        month = dates.month
        sql="DELETE FROM `bill` WHERE `month`='"+str(month)+"' AND `year`= '"+str(year)+"'"
        mycursor.execute(sql)
        mydb.commit()

        sql="SELECT `id` FROM `bill`"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            a=i[0]
            print(a)
            
            sql="SELECT SUM(unit) FROM `usage` WHERE `consumercode`='"+str(a)+"' AND MONTH(datetime)='"+str(month)+"' AND YEAR(datetime)='"+str(year)+"' "
            mycursor.execute(sql)
            result=mycursor.fetchone()
            unit=(result[0])
            print(result)
            #print(i)
            total_bill=int(str(result[0])) * 5
            print(total_bill)
            #date= datetime.today().strftime('%Y-%m-%d')
            sql="INSERT INTO `bill`(`consumercode`, `month`, `year`, `bill`, `billdate`, `billstatus`, `totalunit`) VALUES (%s,%s,%s,%s,%s,now(),%s,now()+interval 14 day)"
            data = (str(a),str(month),str(year),total_bill,'0',unit)
            mycursor.execute(sql,data)
            mydb.commit()
            print("Bill inserted successfully.")
        
    elif(choice==8):
      print("Exit")
    break
 