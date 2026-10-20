from fastapi import FastAPI, File, UploadFile
import uuid
from pathlib import Path


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

@app.post("/videos")
async def upload_video(video: UploadFile):
    video_id = uuid.uuid4()
    extension = Path(video.filename).suffix
    path = Path(f"data/uploads/{video_id}{extension}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb", ) as file:
        for chunk in iter(lambda: video.file.read(1024 * 1024), b""):
            file.write(chunk)
    return {
        "filename": video.filename,
        "id": video_id
    }