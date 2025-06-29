from fastapi import FastAPI, Request, Body
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from app.image_generator import generate_images
from app.models import GenerateRequest
import uuid, os

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

@app.post("/generate")
@limiter.limit("5/minute")
async def generate(request: Request, data: GenerateRequest = Body(...)):
    prompt = data.prompt.strip()
    images = await generate_images(prompt, data.num_images, data.width, data.height)

    os.makedirs("outputs/images", exist_ok=True)
    response_paths = []
    for img in images:
        img_id = str(uuid.uuid4()) + ".png"
        path = f"outputs/images/{img_id}"
        img.save(path)
        response_paths.append(path)
    
    return {"images": response_paths}
