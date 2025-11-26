# app/config.py
from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
import torch

def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Use a scheduler that runs better on limited GPU
    model = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None,           # Faster + avoids HF warnings
    )

    # Use memory-optimized scheduler
    model.scheduler = EulerAncestralDiscreteScheduler.from_config(model.scheduler.config)

    # Enable memory efficient attention
    if device == "cuda":
        model.enable_xformers_memory_efficient_attention()

    return model.to(device)

model = load_model()
