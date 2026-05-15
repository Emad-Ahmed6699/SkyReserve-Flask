from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Flight, Booking, Contact
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'skyreserve-secret-key-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skyreserve.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize Database and Admin User
with app.app_context():
    db.create_all()
    # Check if admin exists
    admin = User.query.filter_by(email='admin123@gmail.com').first()
    if not admin:
        hashed_password = generate_password_hash('admin12345', method='pbkdf2:sha256')
        admin = User(name='Admin', email='admin123@gmail.com', password=hashed_password, role='admin')
        db.session.add(admin)
        db.session.commit()

# --- Public Routes ---

@app.route('/')
def home():
    return render_template('user/home.html')

@app.route('/flights')
def flights():
    all_flights = Flight.query.all()
    return render_template('user/flights.html', flights=all_flights)

# --- Auth Routes ---

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))
        
        new_user = User(
            name=name, 
            email=email, 
            password=generate_password_hash(password, method='pbkdf2:sha256'),
            role='user'
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'error')
    return render_template('auth/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# --- User Routes ---

@app.route('/book/<int:id>', methods=['POST'])
@login_required
def book_flight(id):
    flight = Flight.query.get_or_404(id)
    if flight.seats_available <= 0:
        flash('No seats available.', 'error')
        return redirect(url_for('flights'))
    
    new_booking = Booking(user_id=current_user.id, flight_id=flight.id, status='pending')
    db.session.add(new_booking)
    db.session.commit()
    flash('Booking request submitted! Waiting for admin approval.', 'success')
    return redirect(url_for('my_bookings'))

@app.route('/my-bookings')
@login_required
def my_bookings():
    user_bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.booking_date.desc()).all()
    return render_template('user/my_bookings.html', bookings=user_bookings)

# --- Admin Routes ---

def admin_required(f):
    def wrap(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('Admin access required.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    pending = Booking.query.filter_by(status='pending').all()
    all_flights = Flight.query.all()
    return render_template('admin/dashboard.html', pending_bookings=pending, flights=all_flights)

@app.route('/add-flight', methods=['GET', 'POST'])
@login_required
@admin_required
def add_flight():
    if request.method == 'POST':
        departure_time = datetime.strptime(request.form.get('departure_time'), '%Y-%m-%dT%H:%M')
        arrival_time = datetime.strptime(request.form.get('arrival_time'), '%Y-%m-%dT%H:%M')
        
        new_flight = Flight(
            flight_number=request.form.get('flight_number'),
            origin=request.form.get('origin'),
            destination=request.form.get('destination'),
            departure_time=departure_time,
            arrival_time=arrival_time,
            seats_available=int(request.form.get('seats_available')),
            price=float(request.form.get('price'))
        )
        db.session.add(new_flight)
        db.session.commit()
        flash('Flight added successfully.', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/add_flight.html', flight=None)

@app.route('/edit-flight/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_flight(id):
    flight = Flight.query.get_or_404(id)
    if request.method == 'POST':
        flight.flight_number = request.form.get('flight_number')
        flight.origin = request.form.get('origin')
        flight.destination = request.form.get('destination')
        flight.departure_time = datetime.strptime(request.form.get('departure_time'), '%Y-%m-%dT%H:%M')
        flight.arrival_time = datetime.strptime(request.form.get('arrival_time'), '%Y-%m-%dT%H:%M')
        flight.seats_available = int(request.form.get('seats_available'))
        flight.price = float(request.form.get('price'))
        db.session.commit()
        flash('Flight updated.', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/add_flight.html', flight=flight)

@app.route('/delete-flight/<int:id>', methods=['POST'])
@login_required
@admin_required
def delete_flight(id):
    flight = Flight.query.get_or_404(id)
    db.session.delete(flight)
    db.session.commit()
    flash('Flight deleted.', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/booking/<int:id>/<action>', methods=['POST'])
@login_required
@admin_required
def handle_booking(id, action):
    booking = Booking.query.get_or_404(id)
    if action == 'accept':
        if booking.flight.seats_available > 0:
            booking.status = 'accepted'
            booking.flight.seats_available -= 1
            flash(f'Booking for {booking.user.name} accepted.', 'success')
        else:
            flash('No seats available to accept this booking.', 'error')
    elif action == 'reject':
        booking.status = 'rejected'
        flash(f'Booking for {booking.user.name} rejected.', 'success')
    
    db.session.commit()
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
