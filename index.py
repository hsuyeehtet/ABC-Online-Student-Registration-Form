#! C:\Python36\python.exe
import MySQLdb as mysql
import cgi
import cgitb;cgitb.enable()#enable to track cgi error. cgi tb request for debugging
print("Content-type:text/html\n\n")

form=cgi.FieldStorage()
class database: #database class is the super class or base class  
    #defining connect database as a method in the super class
    def connect_db(self):
        db = mysql.connect(host = "localhost",user="root",password="lithanmyanmar",db="pythondemo")
        return db
    
class coursemaster(database): #coursemaster class is the sub class inherited from the database class 
        
    #retrieve courses from database and populate dropdown list    
    def get_AllCourses(self):
        cursor.execute("select courseid,Name from coursemaster")
        row = cursor.fetchone()
        while row is not None:
            row = cursor.fetchone()

#create C1 object from the coursemaster class  
C1=coursemaster() #sending two arguments to the coursemaster class  
db=C1.connect_db() #calling connect_db method from the super class: database class  
cursor=db.cursor() #prepare a cursor object using cursor method 
#C1.add() #calling add function// It is the porlymorphism because we use the same name of method in the coursemaster class and Student class. But the operations are different.
C1.get_AllCourses() #calling get_AllCourses method from the coursemaster class

print("""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="img/book.png">

    <title>Student Registration</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <!-- Custom styles for-->
    <link href="css.css" rel="stylesheet">
  </head>

  <body class="bg-light">

    <div class="container">
      <div class="py-5 text-center">
        <h2><b>Student Registration Form</b></h2>
       <hr>
      </div>

      <div class="row">
        <div class="col">
          <form class="needs-validation" action="submit.py" method="post" novalidate>
            
              <div class="mb-3">
                <label for="firstName"><h4>First Name</h4></label>
                <div class="input-group">
                <input type="text" maxlength="50" class="form-control" placeholder="Enter First Name" name='fname' id="fn" onkeypress="return chkAplha(event,'error')" onblur="chkblnk('fn','error')" required />
                <div class="input-group-prepend">
                  <button type="button" class="btn btn-secondary input-group-text" data-toggle="tooltip" data-placement="top" title="Max length is 50 and Only Alphabet">
                      &#x2754;
                   </button>
                </div>
                </div>
                <div class="col" id="error" style="color:red"></div>
                <div class="invalid-feedback">
                  Valid first name is required.
                </div>
              </div>
              
              
              <div class="mb-3">
                  <label for="LastName"><h4>Last Name</h4></label>
                  <div class="input-group">
                  <input type="text" maxlength="50" class="form-control"  placeholder="Enter Last Name (Max length is: 50)" name='lname' id="ln" onkeypress="return chkAplha(event,'error1')" onblur="chkblnk('ln','error1')" required />
                  <div class="input-group-prepend">
                    <button type="button" class="btn btn-secondary input-group-text" data-toggle="tooltip" data-placement="top" title="Max length is 50 and Only Alphabet">
                        &#x2754;
                     </button>
                  </div>
                </div>
                  <div class="col" id="error1" style="color:red"></div>
                  <div class="invalid-feedback">
                    Valid first name is required.
                  </div>
                </div>
              
            

            <div class="mb-3">
              <label for="email"><h4>Email</h4></label>
              <div class="input-group">
              <input type="email" class="form-control" maxlength="30" name='email' id="e" onblur="chkeid()" placeholder="Example@gmail.com (Max length is: 30)" required>
            <div class="input-group-prepend">
                    <button type="button" class="btn btn-secondary input-group-text" data-toggle="tooltip" data-placement="top" title="Max length is 30 and Use Email Format include (@)(.) ">
                        &#x2754;
                     </button>
                  </div>
            </div>
              <div id="error2" style="color:red"></div>
              <div class="invalid-feedback">
                Please enter a valid email address .
              </div>
            </div>

            <div class="mb-3">
                <label for="phone"><h4>Contact Number</h4></label>
                <div class="input-group">
                  <input type="text" onkeypress="return isNumberKey(event);" class="form-control" id="phone" name='phone' placeholder="Example = 123-456-7890" onblur="chkblnk('phone','error3')"required>
                  <div class="input-group-prepend">
                    <button type="button" class="btn btn-secondary input-group-text" data-toggle="tooltip" data-placement="top" title="Max length is 11 and Only Number(0-9) ">
                        &#x2754;
                     </button>
                  </div>
                </div>
                  <div id="error3" style="color:red"></div>
                <div class="invalid-feedback">
                  Please enter a valid Phone Number .
                </div>
              </div>

              <div class="mb-3">
                <label for="Courses"><h4>Courses</h4></label>
                <div class="input-group">
                <select class="custom-select" id="course" name='course' onblur="chkblnk('course','error4')" required>
""")
for (courseid, Name) in cursor:
    print('<option value="'+ str(courseid)+'">'+ Name +'</option>')
print("""
			   
               </select>
                <div class="input-group-prepend">
                        <button type="button" class="btn btn-secondary input-group-text" data-toggle="tooltip" data-placement="top" title="Choose the Course that you want to attent ">
                            &#x2754;
                         </button>
                      </div>
                </div>
                <div id="error4" style="color:red"></div>
                <div class="invalid-feedback">
                  Please select a valid Courses.
                </div>
            </div>

            <div class="input-group">
            <h4 class="mb-3">Gender</h4>
            
            <div class="d-block my-3">
              <div class="custom-control custom-radio">
                <input id="Male" name="gender" type="radio" value='male' class="custom-control-input"  required>
                <label class="custom-control-label" for="Male">Male</label>
              </div>
              <div class="custom-control custom-radio">
                <input id="Female" name="gender" type="radio" value='female' class="custom-control-input"  required>
                <label class="custom-control-label" for="Female">Female</label>
              </div>
            </div>
            
            </div>
            <div id="error6" style="color:red"></div>
            <div class="input-group-prepend">
              <button type="button" class="btn btn-secondary input-group-text" data-toggle="tooltip" data-placement="top" title="Plz Choose One ">
                  &#x2754;
               </button>
            </div>

            <hr class="mb-4">

            <div class="mb-3  ">
              <label for="address"><h4>Address</h4></label>
              <div class="input-group-prepend">
              <textarea  class="form-control" id="address" name='address' maxlength="255" onblur="chkblnk('address','error6')" rows="5" placeholder="Example = 631/ 5E, Pyay Road, Kamayut Township, Junction of Pyay Road & Inya Road, Yangon" required ></textarea>
              <div class="input-group-prepend">
                    <button type="button" class="btn btn-secondary input-group-text" data-toggle="tooltip" data-placement="top" title="Word Limit = 255 ">
                        &#x2754;
                     </button>
                  </div>
            </div>
              <div id="error6" style="color:red"></div>
              <div class="invalid-feedback">
                Please enter your address.
              </div>
            </div>

            <hr class="mb-4">

           
              <input type="submit" class="btn btn-primary" name="SubmitButton" value="Submit" onClick="ValidateForm(this.form)">
              <input type="hidden" name="submitted" value="1">

              <input class="btn btn-primary " type="button" value="Clear" onClick="document.location.reload(true)">
          </form>
        </div>
      </div>
      
      <footer class="my-5 pt-5 text-muted text-center text-small">
      </footer>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    
    <!--Custom Javascript -->
    <script src="js.js"></script>
  </body>
</html>

""")

db.close() #disconnect from the server
