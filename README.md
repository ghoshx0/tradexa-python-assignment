# Tradexa Technologies Assignment

## Features

- Custom User Model
- Post Model
- Product Model
- Authentication (Login/Logout)
- Authenticated Post Creation
- Multiple Databases
- Django Admin

## Setup

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

python manage.py migrate --database=products_db

Create superuser:

python manage.py createsuperuser

Run server:

python manage.py runserver