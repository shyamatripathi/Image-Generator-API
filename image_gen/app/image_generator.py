# app/image_generator.py
import asyncio
from PIL import Image
from app.config import model

async def generate_images(prompt, num_images=1, width=512, height=512):
    loop = asyncio.get_event_loop()
    results = await loop.run_in_executor(None, lambda: model(prompt, num_inference_steps=30, height=height, width=width, num_images_per_prompt=num_images))
    return results.images
