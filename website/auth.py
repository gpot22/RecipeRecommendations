from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Log in success!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Sorry, wrong password.', category='error')
        else:
            flash('Sorry, account does not exist. Try signing up!', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Sorry, account already exists. Try logging in.', category='error')
        elif len(email) < 5:
            flash('Sorry, email must be more than 4 characters.', category='error')
        elif len(name) < 2:
            flash('Sorry, name must be longer than 1 character.', category='error')
        elif len(password1) < 8:
            flash('Sorry, password must be minimum 7 characters.', category='error')
        elif password1 != password2:
            flash('Sorry, your passwords don\'t match.', category='error')
        else:
            new_user = User(email=email, first_name=name, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Hurray, account created!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        
    return render_template('signup.html', user=current_user)