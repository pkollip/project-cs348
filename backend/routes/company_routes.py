# app/routes/company_routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from backend.models import Company
from backend import db

company_bp = Blueprint('company', __name__)

@company_bp.route('/create', methods=['GET', 'POST'])
def create_company():
    print(request.form)
    if request.method == 'POST':
        company_name = request.form['company_name']
        description = request.form.get('description')
        website = request.form.get('website')
        location = request.form.get('location')
        industry = request.form.get('industry')

        company = Company(company_name=company_name, description=description,
                          website=website, location=location, industry=industry)
        db.session.add(company)
        db.session.commit()
        return redirect(url_for('company.view_company', company_id=company.company_id))
    
    return render_template('create_company.html')

@company_bp.route('/<int:company_id>', methods=['GET'])
def view_company(company_id):
    company = Company.query.get_or_404(company_id)
    print(company.company_name)
    return render_template('company_profile.html', company=company)

@company_bp.route('/<int:company_id>/edit', methods=['GET', 'POST'])
def edit_company(company_id):
    # Fetch the company or return a 404 if it doesn't exist
    company = Company.query.get_or_404(company_id)
    
    if request.method == 'POST':
        # Update company details from the form
        company.company_name = request.form['company_name']
        company.description = request.form.get('description')
        company.website = request.form.get('website')
        company.location = request.form.get('location')
        company.industry = request.form.get('industry')
        
        # Commit the changes to the database
        db.session.commit()
        
        # Redirect to the company's profile page
        return redirect(url_for('company.view_company', company_id=company.company_id))
    
    # Render the edit form with the current company details
    return render_template('edit_company.html', company=company)

@company_bp.route('/<int:company_id>/delete', methods=['POST'])
def delete_company(company_id):
    # Fetch the company or return a 404 if it doesn't exist
    company = Company.query.get_or_404(company_id)

    # Delete the company
    db.session.delete(company)
    db.session.commit()

    # Redirect to a relevant page (e.g., company listings or home page)
    return redirect(url_for('company.list_companies'))  # Update to your company listing route
