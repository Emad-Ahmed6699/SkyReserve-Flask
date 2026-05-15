# ✈️ SkyReserve | Premium Aviation Management

![SkyReserve Banner](https://images.unsplash.com/photo-1540962351504-03099e0a754b?q=80&w=2000&auto=format&fit=crop)

SkyReserve is a cutting-edge, cinematic private aviation booking platform built for the global elite. It combines precision engineering with luxury aesthetics to provide a seamless flight scheduling experience.

---

## ✨ Key Features

*   **🌑 Dynamic Theming**: Full Light/Dark mode support with fluid GSAP transitions.
*   **🛂 Dual-Role Architecture**:
    *   **Elite Client**: Browse fleet schedules, manage itineraries, and request bookings.
    *   **Operations Commander (Admin)**: Full control over flight routes, aircraft allocation, and payload valuation.
*   **🎨 Cinematic UI**: Built with Vanilla CSS variables, Tailwind CSS, and Lucide Icons for a premium SaaS feel.
*   **🛡️ Secure Protocols**: Robust authentication and role-based access control.
*   **📱 Precision-Responsive**: Optimized for high-resolution displays and mobile devices.

---

## 🛠️ Tech Stack

*   **Backend**: Python / Flask
*   **Database**: SQLite (SQLAlchemy ORM)
*   **Frontend**: HTML5 / CSS3 / JavaScript
*   **Styling**: Tailwind CSS & Vanilla CSS Variables
*   **Animations**: GSAP & AOS (Animate On Scroll)
*   **Icons**: Lucide Icons

---

## 📂 Project Structure

```text
SkyReserve-Flask/
├── models/             # Database Schemas (SQLAlchemy)
│   ├── __init__.py
│   └── models.py
├── static/             # Assets & Styling
│   ├── css/
│   │   └── style.css
│   └── js/
├── templates/          # Jinja2 HTML Viewports
│   ├── admin/          # Operations Terminal
│   ├── auth/           # Secure Access
│   ├── user/           # Client Interface
│   └── base.html       # Global Architecture
├── app.py              # Main Flight Controller
└── requirements.txt    # System Dependencies
```

---

## 🚀 Quick Start

1.  **Clone the Hangar**:
    ```bash
    git clone https://github.com/Emad-Ahmed6699/SkyReserve-Flask.git
    cd SkyReserve-Flask
    ```

2.  **Initialize Environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Engines**:
    ```bash
    python app.py
    ```

---

## 👤 Credentials

| Role | Email | Password |
| :--- | :--- | :--- |
| **Admin** | `admin123@gmail.com` | `admin12345` |
| **User** | Register any account | Any |

---

<p align="center">
  <i>© 2026 SkyReserve Systems. Precision in Every Departure.</i>
</p>
