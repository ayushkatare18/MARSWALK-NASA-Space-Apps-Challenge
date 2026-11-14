import uvicorn, asyncio, sys
from app.main import app

if __name__ == "__main__":
    # Disable reload to avoid multiprocessing issues
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
