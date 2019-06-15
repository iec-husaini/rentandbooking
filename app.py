from flask import Flask, render_template, flash, request
from data import Items
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

Items = Items()

@app.route('/')
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

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    
    @app.route("/register", methods=['GET', 'POST'])
    def register():
        form = ReusableForm(request.form)
    
        print form.errors
        if request.method == 'POST':
            name=request.form['name']
            password=request.form['password']
            email=request.form['email']
            print name, " ", email, " ", password
    
        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
    
        return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
