# app/routes/auth_routes.py

from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from backend.models import User
from backend import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)


# Register works
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']
        hashed_password = generate_password_hash(password)
        

        user = User(email=email, password_hash=hashed_password, user_type=user_type, is_active=True)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

# Login works
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            user.is_authenticated = True
            session['user_id'] = user.user_id
            flash('Login successful!')
            # login_user(user)
            print("Next page:", request.args.get('next'))
            
            return redirect(url_for('job.list_jobs'))
        else:
            flash('Login failed. Please check your email and password.')
    return render_template('login.html')

# Logout should work but not tested
@auth_bp.route('/logout')
def logout():
    # logout_user()
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))
