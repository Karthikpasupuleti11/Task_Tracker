from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = 'your_secret_key'

# Config for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasktracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500))
    due_date = db.Column(db.String(50))
    priority = db.Column(db.String(50), default='Low')
    status = db.Column(db.Boolean, default=False)  # False means incomplete, True means completed
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Change the hash method to 'pbkdf2:sha256'
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        except:
            flash("There was an issue creating your account. Try again.", "danger")
            return redirect(url_for('register'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            # If login is successful, store the user ID in the session
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            # If login fails, show an error message
            return render_template('login.html', error="Invalid credentials. Please try again.")

    return render_template('login.html')



@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    page = request.args.get('page', 1, type=int)  # Get page number from URL args
    tasks = Task.query.filter_by(user_id=user.id).paginate(page=page, per_page=5, error_out=False)  # Corrected

    return render_template('home.html', tasks=tasks.items, pagination=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        flash("You must be logged in to add a task.", "danger")
        return redirect(url_for('login'))

    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    priority = request.form['priority']
    user_id = session['user_id']

    new_task = Task(title=title, description=description, due_date=due_date, priority=priority, user_id=user_id)

    try:
        db.session.add(new_task)
        db.session.commit()
        flash("Task successfully added!", "success")
        return redirect(url_for('home'))
    except:
        flash("There was an issue adding your task.", "danger")
        return redirect(url_for('home'))

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get(task_id)
    task.status = not task.status  # Toggle task status

    try:
        db.session.commit()
        flash("Task status updated successfully.", "success")
        return redirect(url_for('home'))
    except:
        flash("There was an issue updating your task.", "danger")
        return redirect(url_for('home'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)

    try:
        db.session.delete(task)
        db.session.commit()
        flash("Task successfully deleted.", "success")
        return redirect(url_for('home'))
    except:
        flash("There was an issue deleting your task.", "danger")
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Clear the session
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
