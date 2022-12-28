import mysql.connector
class person():
    def __init__(self,name,last_name,age,nationalcode):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.nationalcode = nationalcode
    def getInfo(self):
        return (self.name,self.last_name,self.age,self.nationalcode,self.education_Id)


def TableList(cursor,tablename):
    cursor.execute("select * from {}".format(tablename))
    return cursor.fetchall()
     
def SavePerson(person,numbers):
    try:
        sqlCommand = "insert into person (number,person_Id) values(%s,%s)"
        value = person.getInfo()
        cursor.execute(sqlCommand,value)
        id = cursor.lastrowid
        
        for number in numbers:
            sqlCommand ="insert into person (name,last_name,age,nationalcod,education_Id) values(%s,%s,%s,%s,%s)"
            value = (number,id)
            cursor.execute(sqlCommand,value)
            
        connection.commit()
    except mysql.connector.Error as e:
        print(e)
        connection.rollback()
       
connection = mysql.connector.connect(host="localhost",user="root", password = "123456" , database = "seconddatabase")
cursor = connection.cursor()

name = input("enter your name")
last_name = input("enter your lastname ")
age = input("enter your age")
nationalcode = input("enter your nationalcode")

result = TableList(cursor,"education")

for item in result:
    print(item)
    
education_Id = input("enter your education")

p1 = person(name,last_name,age,nationalcode)
p1.education_Id = education_Id


numbers = []

hasNumber = input("do you have number? y/n")

if hasNumber =="y":
    end ="y"
    while end == "y":
         number = input("enter your number")
         numbers.append(number)
         end = input("do you have another number?y/n")
         
         
SavePerson(p1,numbers)
    
         

        
    