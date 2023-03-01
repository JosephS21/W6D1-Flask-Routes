from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm


@app.route('/')
def index():
    cdn={
        'instructors':('lucas', 'dylan'),
        'students':['blane','ashmike','abe','zi','connor','martin','noah','erm']
    }
    return render_template('index.html.jinja',cdn=cdn, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form =RegisterForm()
    return redirect('/')
    return render_template('register.jinja', form=form)

@app.route('/login')
def login():
    return render_template('login.jinja')

@app.route('/blog')
def blog():
    return render_template('blog.jinja')
