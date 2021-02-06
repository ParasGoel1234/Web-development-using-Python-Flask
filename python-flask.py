from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/paras-blogger'
db = SQLAlchemy(app)


class Contacts(db.Model):
   SNo = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   Phone_number = db.Column(db.String(12), nullable=False)
   Message = db.Column(db.String(120),  nullable=False)
   Email = db.Column(db.String(20),  nullable=False)
   date = db.Column(db.String(12),  nullable=True)

@app.route("/")
def home():
   return render_template('index.html')
@app.route("/about")
def about():
   return render_template('about.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contacts():
   if(request.method == 'POST'):
      '''add entry to the database'''
      name = request.form.get('name')
      email = request.form.get('email')
      phone = request.form.get('phone')
      message = request.form.get('message')
      #  contact(name=name,email=email,phone_no=phone,date=datetime.now(), message=message)
      entry = contacts(name=name, Phone_number=phone, Message=message, Email=email)
      db.session.add(entry)
      db.session.commit()

   return render_template('contact.html')

@app.route("/post")
def Post():
   return render_template('post.html')

app.run(debug =True)
