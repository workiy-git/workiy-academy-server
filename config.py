import os
from dotenv import load_dotenv

# Determine environment and load appropriate .env file
env = os.getenv("ENV", "prod")
if env == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env.local")

DATABASE_URL = os.getenv("DATABASE_URL")
# Parse CORS_ORIGINS from comma-separated string
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "").split(",") if os.getenv("CORS_ORIGINS") else []
