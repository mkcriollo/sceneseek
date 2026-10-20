from fastapi import FastAPI

app = FastAPI(
    title="SceneSeek API",
    description="AI powered semantic video search engine",
    version="0.1.0"
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "sceneseek"
    }