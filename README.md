# 🚀 Insightlytics Backend API Service

**Thank you for reviewing my Flask backend implementation!**  
This is a production-ready API service featuring secure authentication and dynamic data endpoints for a modern analytics dashboard.


##  Table of Contents
- [ Key Features](#-key-features)
- [ Technology Stack](#-technology-stack)
- [ Development Setup](#️-development-setup)
- [ Production Deployment](#-production-deployment)
- [ Database Schema](#️-database-schema)
- [ Contact](#-contact)

---

##  Key Features
- Secure **JWT token-based authentication**
- **PostgreSQL** database integration
- ORM support using **Flask-SQLAlchemy**
- **CORS** configuration for cross-origin requests
- Environment-based config via `.env` file


## Technology Stack

| Component        | Technology            |
|------------------|------------------------|
| Framework        | Flask 2.3              |
| Database ORM     | SQLAlchemy 3.0         |
| Authentication   | Flask-JWT-Extended 4.4 |
| Server (Prod)    | Gunicorn               |

---

##  Development Setup

###  Prerequisites
- Python 3.8+
- PostgreSQL 12+

###  Installation Steps

##  From the Git
```bash
git clone https://github.com/sbasavam/Insightlytics-Backend.git
cd Insightlytics-Backend  # if inside the main project folder

python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

pip install -r requirements.txt


#  Create .env file 

# Use this for local development
DATABASE_URL=postgresql://insightlytics_backend_user:hRIUlSj6O6sH1mM4G0HtMIcpg0wn4VsF@dpg-d1q03tmr433s73ds6fmg-a.oregon-postgres.render.com/insightlytics_backend

# Use this in production deployment
DATABASE_URL=postgresql://insightlytics_backend_user:hRIUlSj6O6sH1mM4G0HtMIcpg0wn4VsF@dpg-d1q03tmr433s73ds6fmg-a/insightlytics_backend

JWT_SECRET_KEY=your-secure-key-here


# Database Setup
flask db init
flask db migrate -m "Initial tables"
flask db upgrade

#  Run the Application

 flask run

# For any questions or support, reach out at:

 sanganabasavam1999@gmail.com