# Deployment Guide

This guide outlines the steps to deploy the Django project for the HR Management System using SQLite.

## Prerequisites

- Python 3.12.x installed
- Virtual environment tool (like `venv` or `virtualenv`)
- Git installed

## Steps to Deploy

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/brightkan/trial_hr_system.git
   cd trial_hr_system

2. **Create Virtual Environment**:
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Add .env variables**:
   ```bash
   cp .env.example .env
   # Update the .env file with your own values
   # set DEBUG=1 for development and DEBUG=0 for production
   # set SECRET_KEY to a unique string for secure token generation and session management

4. **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    
   
5. **Run Migrations**:
   ```bash
    python manage.py migrate
   
6. **Create Superuser**:
    ```bash
     python manage.py createsuperuser
   
7. **Collect Static Files**:
    ```bash
    python manage.py collectstatic
   
8. **Run Server**:
    ```bash
    gunicorn project.wsgi:application

9. **Access the Application**:
    Visit `http://localhost:8000` in your browser.

10. **API documentation**:
    Visit `http://localhost:8000/api/v1/swagger/` in your browser.

11. **Admin Panel**:
    Visit `http://localhost:8000/admin` in your browser.

12. ***API Performance View On this link***:
    Visit `http://localhost:8000/admin/api_performance/apirequestlog/summary_view/` in your browser.
    You can also visit the Admin panel and click on the API Performance and click on summary to view the API performance.


