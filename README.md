### 🧳 TravelBook API

A full-featured travel booking backend built with Django REST Framework, supporting property listing, room & rate management bookings, and payment mock integrations.

### Features

- JWT Authentication (Register, Login)

- Property listing with amenities

- Room types & rate plans

- Booking creation & quote calculation

- Mock Payment Intent & Confirm endpoints

- Docker support for easy deployment

- Environment variables & secret management

- CI/CD pipeline using GitHub Actions & Render

### Installation

1. Clone project

```
git clone https://github.com/tushar-3549/TravelBook-API
cd TravelBook-API
```

2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies: `pip install -r requirements.txt`

4. Run migrations: `python manage.py migrate`

5. Create superuser: `python manage.py createsuperuser`

- Run Locally: `python manage.py runserver`

Server runs on: http://127.0.0.1:8000

### 🐳 Docker Support

1. Build & Run with Docker Compose: `docker compose up -d --build`

Containers:

- `web` — Django application

- `db` — PostgreSQL database

2. Stop containers: `docker compose down`

### Some API Endpoints:

| Method | Endpoint                         | Description                    | Auth Required |
| ------ | -------------------------------- | ------------------------------ | ------------- |
| POST   | `/api/v1/auth/register/`         | User registration              | ❌            |
| POST   | `/api/v1/auth/login/`            | User login (JWT)               | ❌            |
| GET    | `/api/v1/properties/`            | List properties                | ❌            |
| GET    | `/api/v1/properties/{id}/`       | Property details               | ❌            |
| POST   | `/api/v1/bookings/quote/`        | Get booking quote              | ❌            |
| POST   | `/api/v1/bookings/`              | Create booking                 | ✅            |
| GET    | `/api/v1/bookings/{code}/`       | Booking details                | ✅            |
| POST   | `/api/v1/payments/intent/`       | Create payment intent (mock)   | ✅            |
| POST   | `/api/v1/payments/{id}/confirm/` | Confirm payment (mock success) | ✅            |

- Postman Link: https://surl.li/wusqgb

#### Running Test

To run tests using Pytest:

`pytest`

### CI / Deployment

- GitHub Actions runs tests on PRs and pushes.

- Deployment: Render — include build & environment variable setup.

Deploy Link: https://travelbook-api.onrender.com/swagger/


### ER Diagram

![alt text](<nol_api - public.png>)


