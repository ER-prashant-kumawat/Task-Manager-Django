# Task Manager

A Django-based Task Manager web application with user authentication and task management features.

## Features

- User Authentication (Signup/Login)
- Task CRUD Operations
- Task Priority and Status Management
- Due Date Tracking
- Filter Tasks by Priority, Status, and Date
- Admin Panel for Management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

- Access the application at: http://localhost:8000
- Access the admin panel at: http://localhost:8000/admin

## Technologies Used

- Django 5.0.2
- Bootstrap 5
- SQLite Database
- Crispy Forms 