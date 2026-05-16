# ✈️ SkyReserve: Premium Aviation Fleet Management Platform

![SkyReserve Banner](https://images.unsplash.com/photo-1542296332-2e4473faf563?auto=format&fit=crop&q=80&w=2000)

**SkyReserve** is an enterprise-grade, full-stack flight management and booking platform designed for premium private aviation services. Built with production-ready architecture, it provides complete fleet operations oversight, intelligent booking workflows, and an immersive user experience optimized for high-end aviation businesses.

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Database Schema](#-database-schema)
- [Development Workflow](#-development-workflow)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🏢 Admin Operations Control Center
- **Fleet Management**: Complete CRUD operations for flight routes with real-time availability tracking
- **Advanced Booking Management**: Multi-status workflow (Pending → Accepted/Rejected) with seat capacity management
- **Route Optimization**: Add, modify, and decommission flights with cascading data integrity
- **Dashboard Analytics**: Visualize pending bookings and active fleet status
- **Cascade Delete Protection**: Intelligent foreign key relationships with `cascade='all, delete-orphan'` to prevent orphaned records

### 👤 Client Portal
- **User Authentication**: Secure JWT-based session management with password hashing (PBKDF2:SHA256)
- **Flight Discovery**: Real-time fleet availability with dynamic pricing and capacity display
- **Smart Booking System**: One-click booking requests with automatic approval workflow
- **Booking History**: Track all journeys with status indicators (Pending, Accepted, Rejected)
- **E-Ticket Generation**: Download acceptance confirmations as verified PNG tickets
- **Responsive Design**: Seamless experience across desktop, tablet, and mobile devices

### 🎨 Premium User Interface
- **Cinematic Design Language**: Glassmorphism effects with smooth micro-animations
- **Adaptive Theming**: Dark-first design with optimized contrast and readability
- **Dynamic Flight Images**: Unique aircraft imagery per flight route (8-image rotation)
- **Real-time Feedback**: Toast notifications for all user actions
- **AOS Animations**: Staggered entrance animations for professional presentation

---

## 🏗 Architecture

### MVC Pattern Implementation
```
SkyReserve/
├── Models (Business Logic)
│   └── User, Flight, Booking, Contact entities with relationships
├── Views (Presentation Layer)
│   └── Jinja2 templates with Tailwind CSS + vanilla JavaScript
└── Controllers (Route Handlers)
    └── Flask blueprints for auth, user, and admin operations
```

### Data Flow
```
User Request → Route Handler → Model/Database → Template Rendering → HTTP Response
```

---

## 🛠 Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Flask 2.x | Lightweight WSGI web framework |
| **ORM** | SQLAlchemy | Database abstraction and relationship management |
| **Database** | SQLite | File-based relational database (dev/prod) |
| **Authentication** | Flask-Login | Session management and user authentication |
| **Security** | Werkzeug | Password hashing and cryptographic utilities |
| **Frontend** | Tailwind CSS | Utility-first CSS framework for responsive design |
| **Icons** | Lucide Icons | Modern, crisp SVG icon library |
| **Typography** | Google Fonts | Inter (primary), Montserrat (display) |
| **Animations** | CSS3 + JavaScript | Hardware-accelerated transitions |
| **Image Processing** | Pillow | Python Imaging Library for ticket generation |

---

## 📁 Project Structure

```
SkyReserve-Flask/
│
├── app.py                          # Main Flask application & route handlers
├── models/
│   ├── __init__.py
│   └── models.py                  # SQLAlchemy ORM models (User, Flight, Booking, Contact)
│
├── templates/                      # Jinja2 templates
│   ├── base.html                  # Base layout with navigation
│   ├── user/
│   │   ├── home.html              # Landing/dashboard page
│   │   ├── flights.html           # Available flights with booking interface
│   │   └── my_bookings.html       # User's booking history & ticket downloads
│   ├── admin/
│   │   ├── dashboard.html         # Booking management interface
│   │   └── add_flight.html        # Flight creation/editing form
│   └── auth/
│       ├── login.html             # Login form with credentials validation
│       └── register.html          # User registration with email verification
│
├── static/
│   └── css/
│       └── style.css              # Custom design tokens & premium styling
│
├── instance/                       # SQLite database & instance data
│
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git exclusion rules
└── README.md                      # Documentation (this file)
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip or conda
- Git
- 4GB RAM (minimum)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/SkyReserve-Flask.git
cd SkyReserve-Flask
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database
```bash
# Database initializes automatically on first app run
# Default admin account is created:
# Email: admin123@gmail.com
# Password: admin12345
```

### Step 5: Launch Application
```bash
python app.py
```

Application runs at: **http://localhost:5000**

---

## ⚙️ Configuration

### Environment Variables
Create `.env` file in root directory:
```bash
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
SQLALCHEMY_DATABASE_URI=sqlite:///skyreserve.db
```

### Database Configuration
Located in `app.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skyreserve.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

---

## 📖 Usage

### Admin Workflow
1. Navigate to `/admin` (requires admin authentication)
2. **Add Flight**: Click "Add Flight" → Enter route details
3. **Manage Bookings**: Review pending requests → Accept/Reject
4. **Monitor Fleet**: View active routes and capacity

### User Workflow
1. **Register** at `/register` or **Login** at `/login`
2. **Browse Flights** at `/flights` with real-time availability
3. **Book Flight**: Click "Initialize Booking Request"
4. **Track Bookings**: View status at `/my-bookings`
5. **Download Ticket**: After admin acceptance, download e-ticket

### Test Credentials
```
Admin Account:
Email: admin123@gmail.com
Password: admin12345
```

---

## 🔌 API Endpoints

### Authentication Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/register` | User registration |
| GET/POST | `/login` | User login |
| GET | `/logout` | Session termination |

### User Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/flights` | List all available flights |
| POST | `/book/<flight_id>` | Submit booking request |
| GET | `/my-bookings` | User's booking history |
| GET | `/download-ticket/<booking_id>` | Download e-ticket (PNG) |

### Admin Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin` | Operations dashboard |
| GET/POST | `/add-flight` | Create new flight |
| GET/POST | `/edit-flight/<flight_id>` | Modify flight details |
| POST | `/delete-flight/<flight_id>` | Decommission flight |
| POST | `/admin/booking/<booking_id>/<action>` | Manage bookings (accept/reject) |

---

## 💾 Database Schema

### Users Table
```sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL,
    role VARCHAR(20) DEFAULT 'user'  -- 'admin' or 'user'
);
```

### Flights Table
```sql
CREATE TABLE flight (
    id INTEGER PRIMARY KEY,
    flight_number VARCHAR(20) UNIQUE NOT NULL,
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    seats_available INTEGER NOT NULL,
    price FLOAT NOT NULL
);
```

### Bookings Table
```sql
CREATE TABLE booking (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL FOREIGN KEY,
    flight_id INTEGER NOT NULL FOREIGN KEY,
    status VARCHAR(20) DEFAULT 'pending',  -- 'pending', 'accepted', 'rejected'
    seats_booked INTEGER DEFAULT 1,
    booking_date DATETIME DEFAULT NOW()
);
```

---

## 🔄 Development Workflow

### Adding a New Feature

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement Changes**
   - Follow existing code patterns
   - Update models if database changes required
   - Add corresponding template updates

3. **Test Thoroughly**
   - Test all user paths
   - Verify admin functions
   - Check responsive design

4. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: descriptive commit message"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request** on GitHub

### Code Standards
- **Python**: PEP 8 compliance, docstrings for complex functions
- **HTML/CSS**: BEM naming, Tailwind utilities
- **JavaScript**: ES6+, event delegation, no global variables
- **Comments**: Inline comments for business logic only

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'flask'`
**Solution**: Ensure virtual environment is activated and dependencies installed
```bash
.venv\Scripts\activate  # or: source .venv/bin/activate
pip install -r requirements.txt
```

### Issue: `IntegrityError: NOT NULL constraint failed: booking.flight_id`
**Solution**: Ensure Flight model has cascade delete configured
```python
bookings = db.relationship('Booking', backref='flight', lazy=True, cascade='all, delete-orphan')
```

### Issue: Port 5000 already in use
**Solution**: Run on different port
```bash
python app.py --port=5001
```

### Issue: Database corruption or needs reset
**Solution**: Delete `instance/skyreserve.db` and restart app
```bash
rm instance/skyreserve.db
python app.py
```

---

## 📝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📊 Current Implementation Status

### ✅ Completed
- [x] User authentication (Login/Register)
- [x] Flight CRUD operations
- [x] Booking workflow (Pending → Accept/Reject)
- [x] Admin dashboard
- [x] Dynamic flight imagery (8-rotation system)
- [x] E-ticket generation (PNG format)
- [x] Status-based ticket download controls
- [x] Responsive mobile/tablet design
- [x] Dark mode optimization
- [x] Cascade delete for data integrity
- [x] Flash message system with color coding

### 🔄 In Progress
- [ ] Payment integration (Stripe/PayPal)
- [ ] Multi-currency support
- [ ] Advanced analytics dashboard
- [ ] Email confirmation notifications

### 📋 Planned
- [ ] 3D flight route visualization
- [ ] Real-time seat map
- [ ] Booking cancellation workflow
- [ ] PDF ticket export
- [ ] Customer support chat

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👨‍💼 Author

**Emad Ahmed**
- GitHub: [@Emad-Ahmed6699](https://github.com/Emad-Ahmed6699)
- Email: emademad880800@gmail.com

---

## 🙏 Acknowledgments

- **Flask Community** for the excellent web framework
- **Tailwind Labs** for the CSS framework
- **Unsplash** for premium aircraft imagery
- **Lucide Icons** for beautiful iconography

---

## 📞 Support

For issues, questions, or suggestions:
1. Check existing [GitHub Issues](https://github.com/yourusername/SkyReserve-Flask/issues)
2. Create new issue with detailed description
3. Contact: emademad880800@gmail.com

---

**Last Updated**: May 16, 2026  
**Status**: Active Development  
**Version**: 1.0.0-beta
