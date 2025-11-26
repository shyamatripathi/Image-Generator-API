from fastapi import FastAPI, Request, Body
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from app.image_generator import generate_images
from app.models import GenerateRequest
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import uuid
import os

# Create app
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

# Static files for image hosting
app.mount("/static", StaticFiles(directory="outputs/images"), name="static")


@app.post("/generate")
@limiter.limit("5/minute")
async def generate(request: Request, data: GenerateRequest = Body(...)):
    prompt = data.prompt.strip()
    images = await generate_images(prompt, data.num_images, data.width, data.height)

    # Ensure output directory exists
    os.makedirs("outputs/images", exist_ok=True)

    response_paths = []

    for img in images:
        img_id = f"{uuid.uuid4()}.png"
        save_path = f"outputs/images/{img_id}"
        img.save(save_path)

        # Public URL returned to frontend
        url = f"{request.base_url}static/{img_id}"
        response_paths.append(url)

    return {"images": response_paths}
