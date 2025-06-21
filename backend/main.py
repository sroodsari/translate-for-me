from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import translate

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow everything
    allow_credentials=False,  # ❌ must be False if origins = "*"
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(translate.router)

print("Translate router loaded")