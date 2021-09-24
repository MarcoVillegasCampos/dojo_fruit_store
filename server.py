from flask import Flask, render_template, request, redirect
app = Flask(__name__)  
fruits=[
    
        
        
        
    {"name": "apple", 
     "quantity": "0"},
    {"name": "blackberry", 
     "quantity": "0"},
    {"name": "strawberry", 
     "quantity": "0"}
   
        ]
personalInfo=[
    
        
        
        
    {"firstName": "n/a", 
     "lastName": "n/a",
     "studentId": "n/a"},
 
   
        ]


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    firstName=request.form['first_name']
    lastName=request.form['last_name']
    studentId=request.form['student_id']
    strawberry=request.form['strawberry']
    raspberry=request.form['raspberry']
    apple=request.form['apple']
    sumFruits= int(strawberry)+int(raspberry)+ int(apple)
    message="Charging "+firstName+ " for "+ str(sumFruits)+ " fruit(s)"
    return render_template("checkout.html",message=message, firstName=firstName, lastName=lastName, studentId=studentId,strawberry=strawberry,raspberry=raspberry,apple=apple)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    