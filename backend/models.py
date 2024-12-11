from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin

# User class is good
class User(db.Model):
    __tablename__ = 'Users'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.TIMESTAMP, default=db.func.now())
    last_login = db.Column(db.TIMESTAMP, nullable=True)

    # Relationships
    company_id = db.Column(db.Integer, db.ForeignKey('Companies.company_id'), nullable=True) # nullable for applicants
    applications = db.relationship('Application', backref='user', lazy=True)

    def get_id(self):
        return str(self.user_id)

class Company(db.Model):
    __tablename__ = 'Companies'

    company_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    website = db.Column(db.String(255))
    location = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    # Relationships
    job_postings = db.relationship('JobPosting', backref='company', lazy=True)
    application_forms = db.relationship('ApplicationForm', backref='company', lazy=True)

class JobPosting(db.Model):
    __tablename__ = 'Job_Postings'
    
    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String, db.ForeignKey('Companies.company_name'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255))
    employment_type = db.Column(db.String(255), nullable=False)
    salary_range = db.Column(db.String(50))
    posted_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    application_deadline = db.Column(db.Date, nullable=True)
    form_id = db.Column(db.Integer, db.ForeignKey('Application_Forms.form_id'))

    # Relationships
    applications = db.relationship('Application', backref='job_posting', lazy=True)


class ApplicationForm(db.Model):
    __tablename__ = 'Application_Forms'
    
    form_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id = db.Column(db.Integer, db.ForeignKey('Companies.company_id'), nullable=False)
    form_name = db.Column(db.String(255), nullable=False)
    form_structure = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    # Relationships
    job_postings = db.relationship('JobPosting', backref='application_form', lazy=True)

class Application(db.Model):
    __tablename__ = 'Applications'
    
    application_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_id = db.Column(db.Integer, db.ForeignKey('Job_Postings.job_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    application_data = db.Column(db.JSON)
    status = db.Column(db.String(255), default='Submitted')
    applied_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Replace with your user lookup logic