from flask import Flask, render_template
from data import Items

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

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
