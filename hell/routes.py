from flask import render_template, url_for, flash, redirect, request
from hell.forms import RegistrationForm, LoginForm
from hell.models import User, Post
from hell import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Chris Kovalev',
        'title': 'Blog Post 1',
        'content': 'First post content bla bla bla!',
        'date': 'December 22, 2020'
    },
    {
        'author': 'Paul Blart',
        'title': 'Blog supremecy 1',
        'content': 'mall cop man',
        'date': 'April 12, 1512'
    }
]

@app.route("/")
@app.route("/home")

def homePage():
    return render_template('home.html', posts = posts)

@app.route("/about")

def aboutPage():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def registerPage():
    if  current_user.is_authenticated:
        return redirect(url_for('homePage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now login!', 'success')
        return redirect(url_for('loginPage'))
    return render_template('register.html', title='Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def loginPage():
    if  current_user.is_authenticated:
        return redirect(url_for('homePage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('homePage'))
        else:
            flash('Login Unsuccessful. Please check', 'danger')
    return render_template('login.html', title='Login', form = form)

@app.route("/logout")
def logoutPage():
    logout_user()
    return redirect(url_for('homePage'))

@app.route("/account")
@login_required
def accountPage():
    return render_template('account.html', title='Account')