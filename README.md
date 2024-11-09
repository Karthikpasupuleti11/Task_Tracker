# Task Tracker

### [Watch the Demo Video](https://youtu.be/tW_FleHEnB0)

## Description

**Task Tracker** is a simple web-based application built using Python, Flask, and SQLAlchemy. This app helps users create, update, and manage their tasks. It includes user authentication (registration and login), allowing users to securely access their task lists. Tasks can be assigned different priorities, due dates, and statuses. Users can view their task list, mark tasks as complete, and delete them when no longer needed.

### Features:
- **User Registration & Login**: Users can register for an account, log in, and view their personalized tasks.
- **Add, Update, and Delete Tasks**: Users can add tasks with a title, description, due date, and priority. Tasks can be marked as complete or incomplete and deleted when necessary.
- **Priority & Status Management**: Users can set task priorities (Low, Medium, High) and mark tasks as completed.
- **User Authentication**: Secure login with hashed passwords.

---

## Brief Working 

### 1. **Registration:**
   - New users must create an account by providing a username and password.
   - The password is hashed using `pbkdf2:sha256` for secure storage in the database.
   - Once registered, users can log in to access their tasks.

### 2. **Login:**
   - Existing users can log in with their credentials.
   - Upon successful login, users are redirected to their personal task homepage.

### 3. **Task Management:**
   - Users can add tasks by entering a title, description, due date, and priority.
   - Once a task is added, it will appear on the user's homepage.
   - Users can update the status of tasks (mark as complete/incomplete).
   - Users can delete tasks from the list.

### 4. **Logout:**
   - Users can log out at any time, which will end their session and redirect them to the login page.

---

## How the Program Works
## File Descriptions:

### 1. **app.py**:
   - **Description**: This is the main Python file that runs the Flask web application. It handles the routing of requests and responses, user authentication, task management, and database interactions.
   - **Features**:
     - **User Authentication**: Handles the registration (`/register`), login (`/login`), and logout (`/logout`) routes. Passwords are hashed and stored securely in the database using `Werkzeug`.
     - **Task Management**: Routes like `/add_task`, `/update_task/<task_id>`, and `/delete_task/<task_id>` manage the creation, updating (mark as complete/incomplete), and deletion of tasks.
     - **Database Operations**: Uses SQLAlchemy to interact with an SQLite database (`tasktracker.db`). The `User` and `Task` models are defined here, with relationships set between users and their tasks.
     - **Session Management**: Sessions are used to keep track of logged-in users, ensuring that users can only access their own tasks.
     - **Error Handling**: Includes basic error handling to notify users in case of issues with registration, login, or task operations.

### 2. **home.html**:
   - **Description**: This is the HTML template for the homepage, which is displayed after a user successfully logs in. It lists all tasks for the logged-in user and provides options to manage them.
   - **Features**:
     - Displays each task with its title, description, due date, priority, and current status (Completed or Incomplete).
     - **Task Actions**: Each task includes buttons to mark it as complete/incomplete and delete it.
     - **Task Form**: A form at the top of the page allows users to add new tasks with details like title, description, due date, and priority.
     - **Logout Option**: A button is provided for users to log out, which will end the session and redirect them to the login page.

### 3. **login.html**:
   - **Description**: This HTML template renders the login page where users can enter their credentials to access their task list. It is used for authenticating users.
   - **Features**:
     - **Login Form**: Users can input their username and password. The form uses the `POST` method to send the data to the `/login` route in the Flask app.
     - **Error Handling**: Displays an error message if the login credentials are invalid (incorrect username or password).
     - **Navigation to Registration**: If the user does not have an account, a link is provided to navigate to the registration page (`/register`).

### 4. **register.html**:
   - **Description**: This is the registration page where new users can sign up for the application by providing a username and password.
   - **Features**:
     - **Registration Form**: Users input a username and password, which are sent via a `POST` request to the `/register` route in `app.py`.
     - **Password Hashing**: The user's password is securely hashed using the `pbkdf2:sha256` algorithm before being stored in the database.
     - **Redirection**: After a successful registration, the user is redirected to the login page (`/login`), where they can then log in with their newly created credentials.
     - **Error Handling**: Displays a message if the username is already taken or another issue occurs during registration.

### 5. **style.css**:
   - **Description**: This is the CSS file used to style the HTML templates and improve the overall appearance of the web pages. It ensures that the web app is user-friendly and visually appealing.
   - **Features**:
     - **General Layout**: Provides a clean and minimalistic design for the pages, using a simple color scheme and responsive layout.
     - **Forms and Buttons**: Styles the input fields, text areas, and buttons to make them consistent and easy to use.
     - **Task List**: Styles the task list items, including the display of task details (e.g., title, description, due date).
     - **Responsive Design**: Ensures the application looks good on both desktop and mobile screens.

### 6. **requirements.txt**:
   - **Description**: This text file lists all the Python libraries required to run the application. It ensures that all necessary dependencies are installed when setting up the project.
   - **Libraries Included**:
     - `Flask`: The web framework for building the application.
     - `Flask-SQLAlchemy`: An extension for Flask to work with SQLAlchemy for database operations.
     - `Werkzeug`: A library used for securely hashing passwords.
     - `SQLAlchemy`: The ORM for interacting with the SQLite database.
   
   - **Usage**: To install the required dependencies, run:
     ```bash
     pip install -r requirements.txt
     ```

### 7. **tasktracker.db**:
   - **Description**: This is the SQLite database used to store user data (usernames, passwords) and tasks (task title, description, due date, status, etc.).
   - **Structure**: 
     - `User` table stores user information, including the `id`, `username`, and `password` (hashed).
     - `Task` table stores task details, including the `id`, `title`, `description`, `due_date`, `priority`, `status`, and the `user_id` (to associate tasks with users).
   - **Creation**: The database is automatically created when you run the app for the first time with `db.create_all()`.

---

## How to Run the Program Locally

### Prerequisites:
- Python 3.x
- Flask
- SQLAlchemy
- Werkzeug

### Setup Instructions:
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/task-tracker.git

2. Install the required Python libraries:
    bash
    opy code
    cd task-tracker
    pip install -r requirements.txt

3. Create the SQLite database:
    bash
    Copy code
    python
    >>> from app import db
    >>> db.create_all()
    >>> exit()

4. Run the Flask application:
    bash
    Copy code
    python app.py

5. Open your browser and navigate to http://127.0.0.1:5000 to access the application.

### Technologies Used:
- Python: Backend programming language.
- Flask: Web framework for Python.
- SQLAlchemy: ORM for database interactions.
- HTML/CSS: Frontend structure and styling.
- SQLite: Database used for storing tasks and user data.

### [GitHub Repository](https://github.com/Karthikpasupuleti11/Task_Tracker.git)
    