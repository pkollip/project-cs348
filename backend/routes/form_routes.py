# app/routes/form_routes.py

from flask import Blueprint, request, render_template, redirect, url_for
from backend.models import ApplicationForm
from backend import db

form_bp = Blueprint('form', __name__)

@form_bp.route('/create', methods=['GET', 'POST'])
def create_form():
    if request.method == 'POST':
        company_id = request.form['company_id']
        form_name = request.form['form_name']
        form_structure = request.form['form_structure']  # Assume JSON structure passed as a string

        form = ApplicationForm(company_id=company_id, form_name=form_name, form_structure=form_structure)
        db.session.add(form)
        db.session.commit()
        return redirect(url_for('form.view_form', form_id=form.form_id))
    
    return render_template('create_form.html')

@form_bp.route('/<int:form_id>', methods=['GET'])
def view_form(form_id):
    form = ApplicationForm.query.get_or_404(form_id)
    return render_template('form_details.html', form=form)
