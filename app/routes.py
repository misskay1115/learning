from flask import render_template, url_for, flash, redirect
from app import app 
from app.forms import LoginForm, RegistrationForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title ='Home', user=user, posts=posts)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}!')
        return redirect( url_for('index'))
    return render_template('register.html',title = 'Sign In', form=form )

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'{form.email.data} has been logged in!')
        return redirect( url_for('index'))
    return render_template('login.html',title = 'Log In', form=form )
