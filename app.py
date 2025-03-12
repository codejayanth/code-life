from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from datetime import datetime
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data['id']
        self.email = user_data['email']
        self.user_type = None  # Will be set to 'student' or 'company'
        self.profile = None

@login_manager.user_loader
def load_user(user_id):
    try:
        # Check if user is a student
        response = supabase.table('students').select('*').eq('id', user_id).execute()
        if response.data:
            user = User({'id': user_id, 'email': response.data[0]['email']})
            user.user_type = 'student'
            user.profile = response.data[0]
            return user

        # Check if user is a company
        response = supabase.table('companies').select('*').eq('id', user_id).execute()
        if response.data:
            user = User({'id': user_id, 'email': response.data[0]['email']})
            user.user_type = 'company'
            user.profile = response.data[0]
            return user

    except Exception as e:
        print(f"Error loading user: {e}")
        return None

@app.route('/')
def index():
    try:
        # Fetch all projects with student information
        response = supabase.table('projects').select(
            '*,students(name,university)'
        ).execute()
        projects = response.data
        return render_template('index.html', projects=projects)
    except Exception as e:
        flash(f"Error loading projects: {str(e)}", 'error')
        return render_template('index.html', projects=[])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            if response.user:
                user = User(response.user)
                login_user(user)
                return redirect(url_for('index'))
        except Exception as e:
            flash('Login failed. Please check your credentials.', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']
        
        try:
            # Create auth user
            response = supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            
            if response.user:
                user_id = response.user.id
                
                if user_type == 'student':
                    # Create student profile
                    supabase.table('students').insert({
                        'id': user_id,
                        'name': request.form['name'],
                        'university': request.form['university'],
                        'field': request.form['field'],
                        'bio': request.form.get('bio', '')
                    }).execute()
                else:
                    # Create company profile
                    supabase.table('companies').insert({
                        'id': user_id,
                        'name': request.form['name'],
                        'industry': request.form['industry'],
                        'description': request.form.get('description', ''),
                        'website': request.form.get('website', '')
                    }).execute()
                
                flash('Registration successful! Please log in.', 'success')
                return redirect(url_for('login'))
                
        except Exception as e:
            flash(f'Registration failed: {str(e)}', 'error')
            
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    try:
        if current_user.user_type == 'student':
            # Fetch student's projects
            response = supabase.table('projects').select('*').eq('student_id', current_user.id).execute()
            projects = response.data
            return render_template('profile.html', user=current_user, projects=projects)
        else:
            # Fetch company's interested projects
            response = supabase.table('project_interests').select(
                '*,projects(*,students(name,university))'
            ).eq('company_id', current_user.id).execute()
            interests = response.data
            return render_template('profile.html', user=current_user, interests=interests)
    except Exception as e:
        flash(f"Error loading profile: {str(e)}", 'error')
        return render_template('profile.html', user=current_user)

@app.route('/post-project', methods=['GET', 'POST'])
@login_required
def post_project():
    if current_user.user_type != 'student':
        flash('Only students can post projects.', 'error')
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        try:
            project_data = {
                'student_id': current_user.id,
                'title': request.form['title'],
                'description': request.form['description'],
                'category': request.form['category'],
                'image_url': request.form['image_url'],
                'tags': request.form['tags'].split(','),
            }
            
            # Handle presentation file upload if provided
            if 'presentation' in request.files:
                file = request.files['presentation']
                if file:
                    response = supabase.storage.from_('project-files').upload(
                        f"presentations/{datetime.now().timestamp()}_{file.filename}",
                        file.read()
                    )
                    if response.data:
                        project_data['presentation_url'] = supabase.storage.from_('project-files').get_public_url(response.data['path'])
            
            # Create project
            supabase.table('projects').insert(project_data).execute()
            flash('Project posted successfully!', 'success')
            return redirect(url_for('profile'))
            
        except Exception as e:
            flash(f'Error posting project: {str(e)}', 'error')
            
    return render_template('post_project.html')

@app.route('/express-interest/<project_id>', methods=['POST'])
@login_required
def express_interest(project_id):
    if current_user.user_type != 'company':
        return jsonify({'error': 'Only companies can express interest'}), 403
        
    try:
        supabase.table('project_interests').insert({
            'company_id': current_user.id,
            'project_id': project_id,
            'message': request.form.get('message', '')
        }).execute()
        return jsonify({'message': 'Interest expressed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)