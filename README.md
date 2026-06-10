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

## Project Structure

### users_app
- Custom User Model
- Post Model
- Login/Logout
- Post Creation

### products
- Product Model
- Product Listing

## Database Architecture

Default Database:
- User
- Post

Products Database:
- Product

Database routing is implemented using Django Database Router.

## Assignment Requirements Covered

- Two Django Apps
- Custom User Model
- Product Model
- Post Model
- Multiple Databases
- Authentication
- Authenticated Post Creation
- Admin Registration