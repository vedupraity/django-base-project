Django - Base Project
=====================

This simple Django project includes environment based settings and pre-configured logging following the best design patterns.

---

## Getting started

These instructions will get you a copy of this project up and running on your machine for development and testing purposes.

### System Requirements

- [python](https://www.python.org/) - 3.7

### Project dependencies

- [django](https://www.djangoproject.com/) - 3.0
- [django-configurations](django-configurations) - 2.2
- [dj-database-url](https://github.com/jacobian/dj-database-url) - 0.5.0
- [python-decouple](https://github.com/henriquebastos/python-decouple) - 3.3

### Project setup

Create a virtual environment and after activating run the following command to install required python packages:

```sh
pip install -r requirements.txt
```

Set environment variables required to run the project

```sh
export $(cat ./env/development.env)
```

Override environment variables if required

```sh
export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
export LOGGING_LEVEL=DEBUG
```

Apply migrations to synchronize the database state with the current set of models and migrations.

```sh
python manage.py migrate
```

Collect all static files from each application

```sh
python manage.py collectstatic
```

Create superuser who can login to the admin site

```sh
python manage.py createsuperuser
```

### Run the project

```sh
$ python manage.py runserver
```

---

### Authors:

- Vedprakash Upraity - [GitHub](https://github.com/vedupraity) | [Linkedin](https://in.linkedin.com/in/vedupraity)
