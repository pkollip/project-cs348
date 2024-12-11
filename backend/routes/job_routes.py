# app/routes/job_routes.py

from flask import Blueprint, request, render_template, redirect, url_for
from backend.models import JobPosting
from backend import db
from flask_login import login_required

job_bp = Blueprint('job', __name__)


@job_bp.route('/', methods=['GET'])
def list_jobs():
    conn = db.engine.raw_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM fetch_job_listings()")  # Call the function
        jobs = cursor.fetchall()
        cursor.close()
    finally:
        conn.close()
    return render_template('job_listings.html', jobs=jobs)

@job_bp.route('/<int:job_id>', methods=['GET'])
def view_job(job_id):
    job = JobPosting.query.get_or_404(job_id)
    return render_template('job_details.html', job=job)

@job_bp.route('/create', methods=['GET', 'POST'])
def create_job():
    print(request.form)
    if request.method == 'POST':
        company_name = request.form['company']
        title = request.form['title']
        description = request.form['description']
        location = request.form.get('location')
        employment_type = request.form['employment_type']
        salary_range = request.form.get('salary_range')
        application_deadline = request.form.get('application_deadline')

        job = JobPosting(company_name=company_name, title=title, description=description, location=location,
                         employment_type=employment_type, salary_range=salary_range,
                         application_deadline=application_deadline)
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('job.list_jobs'))
    
    return render_template('create_job.html')

@job_bp.route('/<int:job_id>/edit', methods=['GET', 'POST'])
def edit_job(job_id):
    # Fetch the job or return a 404 if it doesn't exist
    job = JobPosting.query.get_or_404(job_id)
    
    if request.method == 'POST':
        # Update job details from the form
        job.company_name = request.form['company']
        job.title = request.form['title']
        job.description = request.form['description']
        job.location = request.form.get('location')
        job.employment_type = request.form['employment_type']
        job.salary_range = request.form.get('salary_range')
        job.application_deadline = request.form.get('application_deadline')
        
        # Commit the changes to the database
        db.session.commit()
        
        # Redirect to the job details page
        return redirect(url_for('job.view_job', job_id=job.job_id))
    
    # Render the edit form with the current job details
    return render_template('edit_job.html', job=job)

@job_bp.route('/<int:job_id>/delete', methods=['POST'])
def delete_job(job_id):
    # Fetch the job or return a 404 if it doesn't exist
    job = JobPosting.query.get_or_404(job_id)

    # Delete the job
    db.session.delete(job)
    db.session.commit()

    # Redirect to the job listings page
    return redirect(url_for('job.list_jobs'))