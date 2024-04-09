import bcrypt
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from.models import User, house
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import requests
auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])


def login():


    if request.method == "POST":


        username = request.form.get('username')


        password = request.form.get('password')


        remember_me = request.form.get('remember_me')


        user = User.query.filter_by(username=username).first()


        if user:


            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):


                session['username'] = user.username


                if remember_me == 'on':


                    session.permanent = True


                session['message'] = None


                return redirect(url_for('auth.dashboard'))


            else:


                flash('Incorrect password')


                session['message'] = None


        else:


            flash('User not found')


            session['message'] = None


    return render_template("login.html")



@auth.route('/Signup', methods=['GET','POST'])


def Signup():


    if request.method ==  "POST":


        firstName = request.form.get('f_name')


        username= request.form.get('username')


        lastName = request.form.get('l_name')


        phonenumber = request.form.get('p_number')


        email = request.form.get('email')


        password = request.form.get('password')


        confirm_password =  request.form.get('confirm_password')


        existing_user = User.query.filter_by(username=username).first()


        existing_email = User.query.filter_by(email=email).first()


        if existing_user or existing_email:


            flash('Account Already Exists!!')


            return redirect(url_for('auth.Signup'))


        if password!= confirm_password:


            flash('Passwords do not match!!')


            return redirect(url_for('auth.Signup'))


        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


        new_user = User(email=email, firstName= firstName, lastName=lastName,username=username,phonenumber=phonenumber, password= password_hash)


        db.session.add(new_user)


        db.session.commit()


        flash('Account Created!!')


        return redirect(url_for('auth.login'))


    return render_template("signup.html")



@auth.route('/dashboard')


def dashboard():


    if 'username' in session:


        flash_message = session.pop('message', None)


        if flash_message:


            flash(flash_message)


        return render_template("finder.html")


    else:


        flash('Please log in to see this page')


        return redirect(url_for('auth.login'))



@auth.route('/logout')


def logout():


    session.pop('username', None)


    flash('Logged out successfully')


    return redirect(url_for('views.home'))



@auth.before_request

def check_if_logged_in():


    if request.endpoint == 'auth.login' or request.endpoint == 'auth.Signup':


        if 'username' in session:


            return redirect(url_for('auth.dashboard'))


    if request.endpoint == 'auth.dashboard':


        if 'username' not in session:


            return redirect(url_for('auth.login'))

@auth.route('/house/<int:house_id>')
def house(house_id):
    house = house.query.get_or_404(house_id) 
    return render_template('house.html', house=house)


