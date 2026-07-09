from fastapi import FastAPI
from app.storage.results_store import init_db
from app.api.routes import router

# Initialize the database
init_db()

app = FastAPI(
    title="Multi-Agent Research Assistant",
    description="AI-powered research with CrewAI + RAG",
    version="1.0.0"
)

# Include the research routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Research Assistant API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}