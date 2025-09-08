
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import CORS_ORIGINS
from routers.course import router as course_router
from routers.courseDetails import router as course_details_router
from routers.newsletter import router as newsletter_router
from routers.enquiry import router as enquiry_router
from database import Base, engine


# FastAPI App

app = FastAPI()

# Automatically create all tables on startup
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# Add CORS middleware using config
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(course_router)
app.include_router(course_details_router)
app.include_router(newsletter_router)
app.include_router(enquiry_router)

@app.get("/")
def root():
    return {"message": "Welcome to Workiy Academy API! Use /docs for API documentation."}
