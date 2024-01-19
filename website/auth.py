from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "x"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 5:
            flash('Sorry, email must be more than 4 characters.', category='error')
        elif len(name) < 2:
            flash('Sorry, name must be longer than 1 character.', category='error')
        elif len(password1) < 8:
            flash('Sorry, password must be minimum 7 characters.', category='error')
        elif password1 != password2:
            flash('Sorry, your passwords don\'t match.', category='error')
        else:
            flash('Hurray, account created!', category='success')
        
    return render_template('signup.html')