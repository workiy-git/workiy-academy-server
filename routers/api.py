from fastapi import APIRouter
from .course import router as course_router
from .courseDetails import router as course_details_router
from .enquiry import router as enquiry_router
from .internship import router as internship_router
from .newsletter import router as newsletter_router

api_router = APIRouter()

api_router.include_router(course_router, prefix="/courses")
api_router.include_router(course_details_router, prefix="/course-details")
api_router.include_router(enquiry_router, prefix="/enquiries")
api_router.include_router(internship_router, prefix="/internships")
api_router.include_router(newsletter_router, prefix="/newsletter")
