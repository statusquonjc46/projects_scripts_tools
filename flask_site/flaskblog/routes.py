#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import SendEmail, EditorLogin
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/contact")
def contact():
    form = SendEmail()
    return render_template('contact.html', title='Contact Me', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_form():
    form = EditorLogin()
    if form.validate_on_submit():
        if form.email.data == 'editor@flaskblog.com' and form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed, check username and/or password', 'danger')
    return render_template('login.html', title='Login', form=form)
