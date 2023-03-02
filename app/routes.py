from flask import render_template, flash, redirect
from app import app, db
from app.forms import RegisterForm, LoginInForm, BlogForm, CarForm
from app.models import User, Car, Blog


@app.route('/', methods=['GET', 'POST'])
def car():
    form=CarForm()
    if form.validate_on_submit():
        year = form.year.data
        make = form.make.data
        model = form.model.data
        color = form.color.data
        price = form.price.data
        description = form.description
        flash(f'Car information sent!')
    return render_template('index.html.jinja', car_form=form, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form =RegisterForm()
    if form.validate_on_submit():
        username=form.username.data
        email= form.email.data
        password=form.password.data
        first_name= form.first_name.data
        last_name= form.last_name.data
        u = User(username=username, email=email, password=password, first_name=first_name,last_name=last_name)
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email)
        if user_match:
            flash(f'Username {username} already exists, try again! ')
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already exists, try again!')
            return redirect('/register')
        else:
            u.commit()
            flash(f'Request to register {username} successful!')
            return redirect('/')
    return render_template('register.jinja', form=form)

@app.route('/login', methods=['GET','POST'])
def log_in():
    form=LoginInForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} successfully signed in!')
        return redirect('/')
    return render_template('login.jinja', log_in_form=form)

@app.route('/blog', methods=['GET','POST'])
def blog():
    form=BlogForm()
    if form.validate_on_submit():
        blogblock=form.blogblock.data  
        flash(f'Successfully sent a Blog!')
    return render_template('blog.jinja', blog_form=form)

