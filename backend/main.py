from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auto_research
from starlette import status
from starlette.responses import RedirectResponse


app = FastAPI()

origins = [
    "http://localhost:3000",  # React/Next.js dev server
    "http://127.0.0.1:3000",  # Alternate localhost address
    "https://your-production-domain.com"  # Production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies or credentials
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root(): 
  return RedirectResponse(url="/financial_analysis")

app.include_router(auto_research.router)
