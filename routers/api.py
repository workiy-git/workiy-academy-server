from fastapi import APIRouter
from .course import router as course_router
from .courseDetails import router as course_details_router
from .newsletter import router as newsletter_router
from .enquiry import router as enquiry_router
from .internship import router as internship_router

api_router = APIRouter(prefix="/api")
api_router.include_router(course_router, prefix="/courses", tags=["Courses"])
api_router.include_router(course_details_router, prefix="/course-details", tags=["Course Details"])
api_router.include_router(newsletter_router, prefix="/newsletter", tags=["Newsletter"])
api_router.include_router(enquiry_router, prefix="/enquiry", tags=["Enquiry"])
api_router.include_router(internship_router, prefix="/internship", tags=["Internship"])
