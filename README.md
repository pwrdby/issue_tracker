# Easy issue tracker
Easy issue tracker for managing issues with categories.

Feel free to fork.

# Instalation
After download:
> pip install requirements.txt

# Usage
Run migrations:
> python manage.py migrate

Create Your own superuser:
> python manage.py superuser

Run dev server:
> python manage.py runserver

In Your browser:
> localhost:8000/tracker/

On this page, You can find login, and authenticate Yourself like superuser. Then You can manage the content.
On admin site, You can create `staff` users, who can only read issues.
