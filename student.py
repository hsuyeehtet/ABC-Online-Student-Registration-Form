#! C:\Python36\python.exe
import MySQLdb as mysql
import cgi
import cgitb;cgitb.enable()#enable to track cgi error. cgi tb request for debugging

print("Content-type:text/html\n\n")
class Student: #creating Student class
    def __init__(self,fname,lname,email,gender,address,phone,course): #initialization method
        self.fname = fname
        self.lname = lname
        self.email = email
        self.gender = gender
        self.address = address
        self.phone = phone
        self.course= course

    #inserting students into the database
    def add(self): #It is using Polymorphism features. Because add method from this class is the same as the coursemaster class.
        db = mysql.connect("localhost","root","0000161502","pythondemo") #open database connection
        sql="insert into studentmaster(student_firstname, student_lastname, email, gender, residential_address, contact_no, courseid) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(self.fname,self.lname,self.email,self.gender,self.address,self.phone,self.course)
                                                                                                                                                                       
        cursor=db.cursor() #prepare a cursor object using cursor method 
        try:
            cursor.execute(sql)
            db.commit()
            print("""
<!DOCTYPE html>
<html>
<div class=content>
  <div class="wrapper-1">
    <div class="wrapper-2">
      <h1>Thank you !</h1>
	  <p> Dear
	  <span>
	  
 """)
            print(self.fname,self.lname)
            print("""
	  </span> Thanks for subscribing to our Registration Form  </p>
      <p>you should receive a confirmation email to this mail address: 
	  <span>
	   """)
            print(self.email)
            print("""
	  </span>
	  or we will sent SMS to this Phone number: 
<span>  """)
            print(self.phone)
            print("""
	  </span>
	  </p>
      <button class="go-home" onclick="location.href='index.py'" >
      Back
      </button>
    </div>
    <div class="footer-like">
      
    </div>
</div>
</div>

<link href="https://fonts.googleapis.com/css?family=Kaushan+Script|Source+Sans+Pro" rel="stylesheet">
    <link href="style.css" rel="stylesheet">


""")
        except Exception as e:
            print(str(e))                                                                                                                                                                
            db.rollback()
        db.close
