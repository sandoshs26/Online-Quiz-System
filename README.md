# Online Quiz System

A full-stack web-based Online Quiz System built with **Python Django** and **MySQL**.

The application provides role-based access for **Students, Teachers, and Administrators**, allowing users to participate in quizzes, create and manage quizzes, evaluate results, and view leaderboard information through a responsive Bootstrap-based interface.

## Features

### Student

- Student Registration and Login
- Student Dashboard
- View Available Quizzes
- View Quiz Details
- Attempt Quizzes
- Submit Quiz Answers
- Automatic Score Calculation
- Percentage Calculation
- View Quiz Results
- View Result History
- View Leaderboard
- Logout

### Teacher

- Teacher Login
- Teacher Dashboard
- Create Quiz
- Edit Quiz
- Add Questions
- Edit Questions
- View Questions
- View Student Results
- View Leaderboard
- Logout

### Administrator

- Admin Dashboard
- Manage Users
- User Management
- Role-based Access Control

## Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Django

### Database
- MySQL

### Development & Version Control
- Visual Studio Code
- Git
- GitHub

## User Roles

| Role | Responsibilities |
|------|------------------|
| Student | Attempt quizzes, submit answers, view results, result history and leaderboard |
| Teacher | Create and manage quizzes, questions and view student results |
| Admin | Manage users and access administrative functions |

## Application Workflow

```text
User Registration / Login
          │
          ▼
    Role Identification
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
 Student Teacher Admin
    │      │      │
    ▼      ▼      ▼
  Quiz   Quiz   Manage
 Attempt Management Users
    │      │
    ▼      ▼
 Results  Questions
    │      │
    └──┬───┘
       ▼
   Leaderboard

## Project Structure

Online-Quiz-System/
│
├── authentication/
├── config/
├── dashboard/
├── quiz/
├── subject/
├── static/
│   └── css/
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.x
- Django
- MySQL
- MySQL Connector / MySQL Client
- Web Browser

## Installation & Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required dependencies.
4. Configure the MySQL database.
5. Apply Django migrations.
6. Create a superuser if required.

## Run the Project

```bash
python manage.py runserver
```


### Database

```markdown
## Database

This project uses MySQL as the database management system.

The database is used to store:
- User information
- Subjects
- Quizzes
- Questions
- Quiz results
- Student performance data
```

## Testing

The application was tested for:

- User Registration and Login
- Student Dashboard
- Teacher Dashboard
- Quiz Creation
- Quiz Attempt
- Result Calculation
- Result History
- Leaderboard
- Admin/User Management

## Future Enhancements

- Email notifications
- Advanced analytics and performance reports
- Timer-based quizzes
- Question randomization
- Improved leaderboard features
- Deployment to a cloud platform

## Project Status

Completed

The Online Quiz System has been developed and tested successfully.

## Author

**Sandosh S**

GitHub: [sandosh26](https://github.com/sandosh26)
