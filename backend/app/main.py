from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Backend API for monitoring data pipelines, quality checks, incidents, and deployments.",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "DataOps Control Center API",
        "status": "running",
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
    }