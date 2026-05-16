# ✈️ SkyReserve: Premium Aviation Fleet Management Platform

![SkyReserve Banner](https://images.unsplash.com/photo-1542296332-2e4473faf563?auto=format&fit=crop&q=80&w=2000)

SkyReserve is a next-generation fleet management and booking platform for premium private aviation services. Built with a focus on cinematic aesthetics, operational efficiency, and seamless user experience.

---

## ✨ Key Features

### 🏢 Admin Control Center
- **Fleet Management**: Complete CRUD operations for flight routes
- **Booking Management**: Multi-status workflow (Pending → Accepted/Rejected)
- **Route Optimization**: Add, modify, and decommission flights
- **Dashboard**: Real-time pending bookings and fleet overview

### 👤 User Portal
- **User Authentication**: Secure login/register with password hashing
- **Flight Discovery**: Real-time availability with dynamic pricing
- **Smart Booking**: One-click booking requests
- **E-Ticket Generation**: Download PNG tickets for accepted bookings
- **Booking History**: Track all journeys with status indicators
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile

---

## 🛠 Technology Stack

| Component | Technology |
|-----------|-----------|
| Backend | Flask 2.x + SQLAlchemy |
| Database | SQLite |
| Authentication | Flask-Login |
| Frontend | Tailwind CSS + Vanilla JS |
| Icons | Lucide Icons |
| Image Processing | Pillow |

---

## 📁 Project Structure

```
SkyReserve-Flask/
├── app.py                    # Main Flask application
├── models/
│   ├── __init__.py
│   └── models.py            # SQLAlchemy ORM models
├── templates/
│   ├── base.html
│   ├── user/                # User pages
│   ├── admin/               # Admin pages
│   └── auth/                # Auth pages
├── static/css/
│   └── style.css
└── requirements.txt
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. **Clone repository**:
   ```bash
   git clone https://github.com/Emad-Ahmed6699/SkyReserve-Flask.git
   cd SkyReserve-Flask
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run application**:
   ```bash
   python app.py
   ```

Access at: **http://localhost:5000**

---

## 🔐 Test Credentials

```
Admin Account:
Email: admin123@gmail.com
Password: admin12345
```

---

## 📖 User Workflow

### For Users
1. **Register** at `/register`
2. **Browse Flights** at `/flights`
3. **Book Flight** - Submit booking request
4. **Track Bookings** at `/my-bookings`
5. **Download Ticket** - After admin acceptance

### For Admin
1. Access `/admin` dashboard
2. **Manage Bookings** - Accept or reject requests
3. **Add Flights** - Create new routes
4. **Monitor Fleet** - View all active flights

---

## 🔌 API Endpoints

### Authentication
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET /logout` - Logout

### User Routes
- `GET /flights` - List all flights
- `POST /book/<flight_id>` - Book a flight
- `GET /my-bookings` - View bookings
- `GET /download-ticket/<booking_id>` - Download e-ticket

### Admin Routes
- `GET /admin` - Dashboard
- `GET/POST /add-flight` - Create flight
- `GET/POST /edit-flight/<id>` - Edit flight
- `POST /delete-flight/<id>` - Delete flight
- `POST /admin/booking/<id>/<action>` - Manage booking

---

## 💾 Database Models

### User
- Email (unique)
- Password (hashed)
- Role (admin/user)
- Bookings (relationship)

### Flight
- Flight number (unique)
- Origin/Destination
- Departure/Arrival times
- Seats available
- Price
- Bookings (relationship with cascade delete)

### Booking
- User reference
- Flight reference
- Status (pending/accepted/rejected)
- Seats booked
- Booking date

---

## 🎨 Features Highlights

- **Dynamic Flight Images**: 8-image rotation per flight
- **Status-based Ticket Control**: Download only for accepted bookings
- **Cascade Delete Protection**: Prevents orphaned booking records
- **Responsive Mobile Design**: Full functionality on mobile devices
- **Real-time Feedback**: Toast notifications for all actions
- **Smooth Animations**: AOS entrance animations and transitions

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Activate venv: `.venv\Scripts\activate` |
| Port 5000 in use | Run: `python app.py --port=5001` |
| Database issues | Delete `instance/skyreserve.db` and restart |
| Missing packages | Run: `pip install -r requirements.txt` |

---

## 📝 Contributing

1. Fork repository
2. Create feature branch: `git checkout -b feature/name`
3. Commit changes: `git commit -m "feat: description"`
4. Push branch: `git push origin feature/name`
5. Create Pull Request

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👨‍💼 Author

**Emad Ahmed**
- GitHub: [@Emad-Ahmed6699](https://github.com/Emad-Ahmed6699)
- Email: emademad880800@gmail.com

---

## 🙏 Acknowledgments

- Flask community
- Tailwind Labs
- Unsplash (imagery)
- Lucide Icons

---

**Version**: 1.0.0 | **Status**: Active Development | **Last Updated**: May 16, 2026
