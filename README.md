
# 🚀 TeamFlow - Collaborative Project Management Platform

![Django](https://img.shields.io/badge/Django-5.x-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Database](https://img.shields.io/badge/Database-SQLite-orange)
![UI](https://img.shields.io/badge/UI-AdminLTE%203-purple)

## 📌 Project Overview

**TeamFlow** is a full-stack collaborative project management platform designed for software engineering teams to plan, organize, execute, and track their work efficiently.

The application provides a centralized workspace where teams can manage multiple projects, create and assign tasks, monitor progress, collaborate through comments, receive notifications, and visualize deadlines using an interactive calendar.

The goal of TeamFlow is to simplify software project management by combining task tracking, team collaboration, scheduling, and progress analytics into a single platform.



# ✨ Features Implemented

## 🔐 Authentication & User Management

* User login and logout
* Secure Django authentication system
* User assignment for tasks
* Admin user management



# 📊 Dashboard

The dashboard provides a quick overview of the entire workspace.

Features:

* Total project count
* Total task count
* Pending tasks
* In-progress tasks
* Completed tasks
* Overdue task tracking
* Task status visualization
* Project task analytics
* Upcoming deadlines



# 📁 Project Management

Users can manage projects efficiently.

Features:

* Create projects
* View projects
* Update project details
* Delete projects
* Track project-related tasks

Each project acts as a container for related tasks.



# ✅ Task Management

TeamFlow provides complete task lifecycle management.

Features:

* Create tasks
* Edit tasks
* Delete tasks
* Assign tasks to team members
* Update task status
* Set priority levels
* Add descriptions
* Set deadlines
* Create parent/sub-task relationships

### Task Status Workflow

```
Pending
   ↓
In Progress
   ↓
Completed
```



# 👥 Task Assignment

Tasks can be assigned to registered users.

Assignment information includes:

* Assigned user
* Project
* Priority
* Deadline
* Current status

This helps teams understand ownership and responsibility.

# 💬 Collaboration System

Team members can communicate directly inside tasks.

Features:

* Add comments
* Display commenter username
* Display comment timestamp
* Delete comments
* Maintain activity history

Example activity:

```
RamaKrishna added a comment
RamaKrishna updated task details
RamaKrishna deleted a comment
```


# 🔔 Notification System

TeamFlow provides notifications for important actions.

Implemented notifications:

* Task assignment notifications
* Activity-based notifications



# 📅 Calendar Management

An interactive calendar is integrated for task scheduling.

Features:

* Monthly view
* Weekly view
* Daily view
* Display tasks based on due dates
* Drag and drop task date update

### Calendar Filters

Users can filter tasks by:

* Project
* Status
* Priority
* Assigned user



# 📈 Reports & Analytics

The system provides visual insights using charts.

Implemented:

* Task status chart
* Project task distribution chart
* Dashboard statistics



# 🛠️ Technology Stack

## Backend

* Python
* Django Framework
* Django ORM

## Database

* SQLite

## Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

## UI Framework

* AdminLTE 3

## Libraries

* Chart.js
* FullCalendar



# 🏗️ Project Architecture

TeamFlow follows Django's **Model-View-Template (MVT)** architecture.

Project structure:

```
TeamFlow/
│
├── TeamFlow/
│   ├── settings.py
│   ├── urls.py
│
├── projects/
│   ├── models.py
│   ├── views.py
│
├── tasks/
│   ├── models.py
│   ├── views.py
│
├── calendar_app/
│   ├── views.py
│
├── notifications/
│   ├── models.py
│
├── templates/
│
├── static/
│
├── manage.py
│
├── requirements.txt
│
└── README.md
```



# ⚙️ Installation and Setup

## 1. Clone Repository

```bash
git clone <repository-url>
```

Move into project directory:

```bash
cd TeamFlow
```



## 2. Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv

source venv/bin/activate
```



## 3. Install Dependencies

```bash
pip install -r requirements.txt
```



## 4. Apply Database Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```



## 5. Create Admin Account

```bash
python manage.py createsuperuser
```

Enter:

```
Username
Email
Password
```



## 6. Run Development Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```



# 🔑 Environment Variables

Currently TeamFlow uses SQLite and does not require external environment variables.

For production deployment:

Create:

```
.env
```

Example:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_database_url
```



# 📦 Requirements

Generate dependencies:

```bash
pip freeze > requirements.txt
```

Install:

```bash
pip install -r requirements.txt
```



# ⚠️ Assumptions

* Users are managed using Django authentication.
* SQLite is used for simplicity and easy setup.
* Tasks belong to projects.
* Users can only manage features according to available permissions.
* Email services are not configured.



# 🚧 Known Limitations

* Email notifications are not implemented.
* Real-time collaboration using WebSockets is not included.
* File attachments are not supported.
* Advanced role permissions are limited.
* SQLite is not optimized for very large-scale production usage.


# 🔮 Future Enhancements

Possible improvements:

* Email notification system
* Real-time chat
* File attachments
* Advanced user roles
* PostgreSQL migration
* Cloud deployment
* Mobile application support



# 👨‍💻 Author

**Rama Krishna**

Computer Science Engineering



# 📄 License

This project is created for educational and demonstration purposes.

# TeamFlow
A full-stack project management platform built with Django, SQLite, and AdminLTE 3 for managing projects, tasks, team collaboration, notifications, dashboards, and calendar scheduling.

