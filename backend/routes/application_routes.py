# app/routes/application_routes.py

from flask import Blueprint, request, render_template, redirect, url_for
from backend.models import Application
from backend import db

app_bp = Blueprint('application', __name__)

@app_bp.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):
    if request.method == 'POST':
        user_id = request.form['user_id']
        resume_id = request.form.get('resume_id')
        application_data = request.form.get('application_data')

        application = Application(job_id=job_id, user_id=user_id, resume_id=resume_id,
                                  application_data=application_data)
        db.session.add(application)
        db.session.commit()
        return redirect(url_for('application.view_application', app_id=application.application_id))
    
    return render_template('application_form.html', job_id=job_id)

@app_bp.route('/<int:app_id>', methods=['GET'])
def view_application(app_id):
    application = Application.query.get_or_404(app_id)
    return render_template('application_details.html', application=application)
