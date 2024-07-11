# Tutor App

Tutor App is a Django-based application that provides an educational content dashboard. It includes features such as user authentication, course management, and question submission.

## Features

- User authentication using JWT (JSON Web Tokens)
- Course management with video links, details, transcripts, and images
- Multiple-choice questions with variable choices
- Submission of answers with validation

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/tutor_app.git
    cd tutor_app
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database**:

    Create a PostgreSQL database and update the `DATABASES` setting in `tutor_app/settings.py` with your database credentials.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Run migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py makemigrations course_tutor
    python manage.py migrate
    ```

6. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

8. **Access the application**:

    Open your web browser and navigate to `http://127.0.0.1:8000/admin/` to access the Django admin panel. Login with the superuser credentials created in previous steps.

## API Endpoints

### Obtain JWT Token

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

### Refresh JWT Token

```bash
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
     -H "Content-Type: application/json" \
     -d '{"refresh": "your_refresh_token_here"}'
```

### Get List of Courses (Limited Fields)

```bash
curl -X GET http://127.0.0.1:8000/api/courses/ \
     -H "Authorization: Bearer your_access_token_here"
```

### Get Details of a Specific Course

```bash
curl -X GET http://127.0.0.1:8000/api/courses/1/ \
     -H "Authorization: Bearer your_access_token_here"
```

### Submit an Answer

```bash
curl -X POST http://127.0.0.1:8000/api/submissions/ \
     -H "Authorization: Bearer your_access_token_here" \
     -H "Content-Type: application/json" \
     -d '{
           "question": 1,
           "selected_choice": "A JavaScript library"
         }'
```

## Link for sample CRUD queries
https://github.com/varungidwani91/tutor_app/blob/main/crud_queries.md

## Link for database schema diagram
https://github.com/varungidwani91/tutor_app/blob/main/database_schema_diagram.png

## Link for demo video of how to insert the data via admin portal
https://drive.google.com/drive/u/2/folders/1rsMVjiAS3V95BDhvlAzIw-4Shdq2tODn

## Repository link for frontend react application
https://github.com/prabeer451/courseapp_frontend.git

## Link for demo video of frontend react application
https://drive.google.com/file/d/1Ctmzbt9eJoBvroGfv-XYNktMtEzC-2wm/view?usp=sharing
