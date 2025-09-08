from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import CORS_ORIGINS
from routers.course import router as course_router


# FastAPI App
app = FastAPI()

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

@app.get("/")
def root():
    return {"message": "Welcome to Workiy Academy API! Use /docs for API documentation."}
