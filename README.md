# 🧳 TravelBook API

A comprehensive travel booking backend built with **Django REST Framework**. This API supports property listings, room & rate management, booking workflows, and integrated payment mocks.

---

## 🚀 Features

- **JWT Authentication**: Secure user registration and login.
- **User Profiles**: Manage personal information and account status.
- **Property Management**: Detailed property listings with amenities and photos.
- **Inventory & Pricing**: Room types, rate plans, and dynamic pricing.
- **Booking Engine**: Quote calculation, booking creation, and status tracking.
- **Payment Integration**: Mock endpoints for Payment Intent and Confirmation.
- **Standardized API**: Support for GET, POST, PUT, PATCH, and DELETE across core resources.
- **Documentation**: Interactive Swagger UI for API exploration.
- **Scalable Infrastructure**: Dockerized setup, Environment-based configuration, and CI/CD ready.

---

## 🛠️ Tech Stack

- **Framework**: Django 4.2+, Django REST Framework
- **Database**: PostgreSQL (Prod), SQLite (Local)
- **Auth**: SimpleJWT
- **Docs**: drf-yasg (Swagger)
- **DevOps**: Docker, Docker Compose, GitHub Actions, Render
- **Testing**: Pytest, Factory Boy

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/tushar-3549/TravelBook-API
cd TravelBook-API
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory and configure it (see `.env.example` if available, or use the project defaults).

### 3. Run with Docker (Recommended)
The easiest way to get started is using Docker Compose:
```bash
docker compose up -d --build
```
The API will be available at `http://localhost:8000`.

### 4. Manual Local Setup
If you prefer running without Docker:
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

---

## � API Documentation

The interactive API documentation is available at:
- **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Redoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

### Core Endpoints

| Resource | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Auth** | POST | `/api/v1/auth/register/` | Register a new user |
| | POST | `/api/v1/auth/login/` | Login and receive JWT tokens |
| **User** | GET/PUT/PATCH/DELETE | `/api/v1/me/` | Manage your profile |
| **Properties** | GET | `/api/v1/accommodations/` | List all properties |
| | GET/PUT/PATCH/DELETE | `/api/v1/accommodations/{id}/` | Manage property details |
| **Bookings** | POST | `/api/v1/bookings/quote/` | Get a pricing quote |
| | POST | `/api/v1/bookings/` | Create a new booking |
| | GET/PATCH/DELETE | `/api/v1/bookings/{code}/` | Manage specific booking |
| **Reviews** | POST | `/api/v1/reviews/{prop_id}/create/` | Add a review |
| | GET/PUT/PATCH/DELETE | `/api/v1/reviews/review/{id}/` | Manage specific review |
| **Payments** | POST | `/api/v1/payments/intent/` | Create payment intent |
| | POST | `/api/v1/payments/{id}/confirm/` | Confirm payment success |

---

## 🧪 Testing

To run the automated test suite:
```bash
pytest
```

To run with coverage:
```bash
pytest --cov=.
```

---

## 🚢 CI/CD & Deployment

- **CI**: GitHub Actions runs tests on every push and pull request.
- **Deployment**: Automatic deployment to Render for the `main` branch.
- **Live Demo**: [https://travelbook-api.onrender.com/swagger/](https://travelbook-api.onrender.com/swagger/)

---

## 📊 Database Schema

![Database Schema](screenshoots/nol_api%20-%20public.png)

---

## 📄 License & Contact

Developed by **Tushar**.
- **Postman Collection**: [View on Postman](https://surl.li/wusqgb)
