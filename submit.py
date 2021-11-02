#! C:\Python36\python.exe
import MySQLdb as mysql
import cgi
import cgitb;cgitb.enable()
from student import * #importing Student Class from the student module

print("")
form=cgi.FieldStorage()
def getinputvalue(fieldname):
    if fieldname in form:
        return form[fieldname].value
if "submitted" in form:
  fname=getinputvalue("fname")
  lname=getinputvalue("lname")
  email=getinputvalue("email")
  gender=getinputvalue("gender")
  address=getinputvalue("address")
  phone=getinputvalue("phone")
  course=getinputvalue("course")
  Student1 = Student(fname,lname,email,gender,address,phone,course) #creating Student1 object from the Student Class
  Student1.add() #calling add function from the Student Class                                                                                                                                                          
            
