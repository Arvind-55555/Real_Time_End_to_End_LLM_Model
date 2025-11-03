# Entry point placeholder for FastAPI application
import uvicorn
from .api import app
from .config import settings

if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT, log_level="info")
