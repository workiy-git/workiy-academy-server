# Workiy Academy Server

This is a FastAPI-based backend for the Workiy Academy platform. It follows enterprise standards for modularity, maintainability, and scalability.

## Project Structure

```
├── config.py
├── database.py
├── main.py
├── requirements.txt
├── crud/
│   ├── course.py
│   ├── courseDetails.py
│   ├── enquiry.py
│   ├── internship.py
│   ├── newsletter.py
├── models/
│   ├── course.py
│   ├── courseDetails.py
│   ├── enquiry.py
│   ├── internship.py
│   ├── newsletter.py
├── routers/
│   ├── api.py
│   ├── course.py
│   ├── courseDetails.py
│   ├── enquiry.py
│   ├── internship.py
│   ├── newsletter.py
├── schemas/
│   ├── course.py
│   ├── courseDetails.py
│   ├── enquiry.py
│   ├── internship.py
│   ├── newsletter.py
├── services/
│   ├── course_service.py
└── tests/
```

## Key Features

- **Centralized Routing:** All API endpoints are registered in `routers/api.py` and included in `main.py`.
- **Modular Design:** CRUD logic, models, schemas, and routers are separated for maintainability.
- **Database:** Uses SQLAlchemy ORM for database models and operations.
- **Validation:** Pydantic schemas for request/response validation.
- **CORS:** Configurable origins for secure cross-origin requests.

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
3. Access API docs:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

- `/courses` - Course management
- `/course-details` - Course details
- `/enquiries` - Enquiry management
- `/internships` - Internship applications
- `/newsletter` - Newsletter subscriptions

## Configuration
- CORS origins are set in `config.py`.
- Database connection is managed in `database.py`.

## Extending the Application
- Add new models in `models/`.
- Add new schemas in `schemas/`.
- Add new CRUD logic in `crud/`.
- Register new routers in `routers/api.py`.

## Testing
- Place your tests in the `tests/` directory.

## License
MIT
