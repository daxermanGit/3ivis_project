# 3IVIS Project

This is a Django-based project for the 3IVIS application. It includes both a web application with a D3 chart rendering after login and a REST API for data fetching.

## Features

- **Web Application**: Login functionality with D3 chart rendering upon successful authentication.
- **REST API**: A REST API that allows fetching data for the D3 chart after successful authentication.
- **Data Visualization**: The project integrates Django with D3.js for data visualization.

## Requirements

- Python 3.10.1
- Django 3.x
- PostgreSQL (optional depending on your database configuration)
- D3.js (used for rendering the chart)

## Setup Instructions

Follow the steps below to get the project running in your local development environment.

### 1. Install Python and Dependencies

Make sure you have [Python](https://www.python.org/downloads/) installed (preferably version 3.10 or higher).

Set up a virtual environment for the project:

```bash
python -m venv 3IVIS_venv
```

Activate the virtual environment:

On Windows:

```bash
3IVIS_venv\Scripts\activate
```
On macOS/Linux:

```bash
source 3IVIS_venv/bin/activate
```
Then install the dependencies:

```bash
pip install -r requirements.txt
```

### 2. Set Up the Database
If you're using PostgreSQL, make sure you have it installed and running. Update your settings.py for the database connection. You can use SQLite for development if preferred.

### 3. Run Migrations
Apply the migrations to set up the database:

```bash
python manage.py migrate
```

### 4. Create a Superuser
To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```

The server should now be running at http://127.0.0.1:8000/. You can access the web application and the Django admin interface (at /admin) with the superuser credentials.