from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import SignUpForm

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods = ["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Your address has been added!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phonenum = form.phonenum.data
        address = form.address.data
        print(first_name, last_name, phonenum, address)

        flash("You have successfully signed up!", "success")

        # redirect back to home
        return redirect(url_for('index'))
    return render_template('signup.html', form = form)