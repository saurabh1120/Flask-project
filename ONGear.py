from flask import Flask, render_template
from sqlalchemy import MetaData
from flask_mysqldb import MySQL
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect
from flask_mail import Mail

app=Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/ongear'
# db = SQLAlchemy(app) 
 
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="Ongear"
# app.config['']=""
mysql = MySQL(app)

@app.route("/index",methods=['POST','GET'])
def index():
    if(request.method=='POST'):
        
        name = request.form['name']
        email = request.form['email']
        number = request.form['Phone']

        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO request(name,email,number)VALUES (%s,%s,%d),(name,email,number)")

        
    return render_template('index.html')

@app.route("/Login")
def Login():    
    return render_template('Login.html')

@app.route("/details", methods=['GET','POST'])
def details():
    return render_template('details.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route("/services")
def service():    
    return render_template('services.html')


@app.route("/about")
def about():    
    return render_template('about.html')


@app.route("/payment")
def payment():  
    return render_template('payment.html')




if __name__=="__main__":
    app.run(debug=True)