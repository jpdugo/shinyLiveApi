from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the 'site' directory to serve the Shinylive application
app.mount("/", StaticFiles(directory="site", html=True), name="shinylive")

# Optionally, you can add other routes or API endpoints here