
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

## 1. Clone the Repository

```bash
git clone https://github.com/RamaKrishna173/TeamFlow.git
cd TeamFlow
```

---

## 2. Verify the Project Files

Ensure you are in the project directory by running:

```bash
dir
```

You should see files and folders similar to the following:

```text
README.md
DATABASE_SCHEMA.md
ARCHITECTURE.md
requirements.txt
manage.py
db.sqlite3
accounts/
calendar_app/
dashboard/
notifications/
projects/
reports/
static/
tasks/
templates/
TeamFlow/
```

---

## 3. Install Required Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

## 4. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

If the server starts successfully, you will see output similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

Open your browser and navigate to:

```text
http://127.0.0.1:8000/
```

---

# 🔑 Demo Login Credentials

The repository includes a preconfigured SQLite database (`db.sqlite3`) with sample data and demo accounts.

## Application Login

Open:

```text
http://127.0.0.1:8000/login/
```

**Demo User**

**Username:**

```text
RamaKrishna
```

**Password:**

```text
Rama123@
```

---

## Django Admin Login

Open:

```text
http://127.0.0.1:8000/admin/
```

**Administrator**

**Username:**

```text
bajoj
```

**Password:**

```text
bajoji
```

---

# 📦 Demo Data

The included SQLite database contains sample:

* Projects
* Tasks
* Task Assignments
* Comments
* Activity History
* Notifications
* Calendar Events

This allows reviewers to explore the application's functionality immediately without creating additional data.

---

# 📌 Notes

* The project uses **SQLite** as the database.
* The repository already includes a preconfigured **db.sqlite3** file with demo data.
* No additional database configuration is required to run the application.
* If you wish to start with a fresh database, delete `db.sqlite3` and run:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
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

