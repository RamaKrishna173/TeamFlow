# Database Schema

## Overview

TeamFlow uses **SQLite** as the relational database and **Django ORM** for all database operations. The database schema is defined through Django migration files located in each application.

## Migration Files

### Accounts

* accounts/migrations/0001_initial.py

### Projects

* projects/migrations/0001_initial.py

### Tasks

* tasks/migrations/0001_initial.py
* tasks/migrations/0002_task_due_date_task_parent_task_task_priority_and_more.py
* tasks/migrations/0003_activitylog_comment.py

### Notifications

* notifications/migrations/0001_initial.py
* notifications/migrations/0002_notification_event_key_and_more.py

These migration files create and update the database schema automatically using Django's migration framework.

## Main Database Tables

### User (Django Authentication)

Stores user account information.

* id
* username
* email
* password
* first_name
* last_name

### Project

Stores project information.

* id
* name
* description
* created_at

### Task

Stores task details.

* id
* title
* description
* status
* priority
* due_date
* project (Foreign Key → Project)
* assigned_to (Foreign Key → User)
* parent_task (Self Foreign Key)

### Comment

Stores comments added to tasks.

* id
* task (Foreign Key → Task)
* user (Foreign Key → User)
* message
* created_at

### ActivityLog

Stores task activity history.

* id
* task (Foreign Key → Task)
* action
* created_at

### Notification

Stores user notifications.

* id
* user (Foreign Key → User)
* message
* is_read
* created_at

## Entity Relationships

* One Project can contain multiple Tasks.
* One User can be assigned to multiple Tasks.
* One Task can have multiple Comments.
* One Task can have multiple Activity Logs.
* One Task can optionally have a Parent Task.
* One User can receive multiple Notifications.

## Database Technology

* Database: SQLite
* ORM: Django ORM
* Migration Framework: Django Migrations
