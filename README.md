# Stable Diffusion Image Generator API

## Overview

A FastAPI-based application to generate AI images from text prompts using Stable Diffusion.

## Features

- FastAPI application
- API documentation (auto-generated at `/docs`)
- Asynchronous image generation
- Request validation using Pydantic
- Rate limiting (5 requests per minute)
- 20+ sample generated images
- Simple deployment instructions

## Requirements
Install dependencies:
pip install -r requirements.txt
requirements.txt
### Running the Server
uvicorn app.main:app --reload
## API Usage
Endpoint
POST /generate
Request Headers
Content-Type: application/json
JSON Body
{
  "prompt": "A magical forest at twilight",
  "num_images": 1,
  "width": 512,
  "height": 512
}
Response
json

{
  "images": [
    "outputs/images/<uuid>.png"
  ]
}
Swagger UI
Access interactive API docs at:
http://127.0.0.1:8000/docs
### Folder Structure
project-root/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── image_generator.py
│   └── config.py
├── outputs/
│   └── images/
├── generate_samples.py
├── requirements.txt
└── README.md
### Deployment
git clone <repo-url>
cd <repo-folder>
pip install -r requirements.txt
uvicorn app.main:app --reload
