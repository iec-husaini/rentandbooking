from flask import Flask, render_template, flash, request, redirect, url_for
#from data import Items
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

# Items = Items()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

#Connect to Database and create database session
engine = create_engine('sqlite:///rat.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#landing page that will display all the books in our database
#This function operate on the Read operation.
@app.route('/')
@app.route('/things')
def showThings():
   things = session.query(Thing).all()
   return render_template("things.html", things=things)


######The following routes mentioning /books all need to be changed#######

#This will let us Create a new book and save it in our database
@app.route('/books/new/',methods=['GET','POST'])
def newBook():
   if request.method == 'POST':
       newBook = Book(title = request.form['name'], author = request.form['author'], genre = request.form['genre'])
       session.add(newBook)
       session.commit()
       return redirect(url_for('showBooks'))
   else:
       return render_template('newBook.html')


#This will let us Update our books and save it in our database
@app.route("/books/<int:book_id>/edit/", methods = ['GET', 'POST'])
def editBook(book_id):
   editedBook = session.query(Book).filter_by(id=book_id).one()
   if request.method == 'POST':
       if request.form['name']:
           editedBook.title = request.form['name']
           return redirect(url_for('showBooks'))
   else:
       return render_template('editBook.html', book = editedBook)

#This will let us Delete our book
@app.route('/books/<int:book_id>/delete/', methods = ['GET','POST'])
def deleteBook(book_id):
   bookToDelete = session.query(Book).filter_by(id=book_id).one()
   if request.method == 'POST':
       session.delete(bookToDelete)
       session.commit()
       return redirect(url_for('showBooks', book_id=book_id))
   else:
       return render_template('deleteBook.html',book = bookToDelete)
       

#@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/submit')
def submit():
    return render_template('items.html', items = Items)

@app.route('/item/<string:id>')
def item(id):
    return render_template('item.html', id=id)

# @app.route('/register')
# def register():
#     return render_template('register.html')

# App config.
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# # Automatically reload the application upon a template file change
app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
# class ReusableForm(Form):
#     name = TextField('Name:', validators=[validators.required()])
#     email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
#     password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
#     
#     @app.route("/register", methods=['GET', 'POST'])
#     def register():
#         form = ReusableForm(request.form)
#     
#         print form.errors
#         if request.method == 'POST':
#             name=request.form['name']
#             password=request.form['password']
#             email=request.form['email']
#             print name, " ", email, " ", password
#     
#         if form.validate():
#         # Save the comment here.
#             flash('Thanks for registration ' + name)
#         else:
#             flash('Error: All the form fields are required. ')
#     
#         return render_template('register.html', form=form)


