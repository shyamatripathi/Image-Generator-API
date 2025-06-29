# Stable Diffusion Image Generator API

## Overview

A FastAPI-based application to generate AI images from text prompts using Stable Diffusion.

## Features

- FastAPI application
- API documentation 
- Asynchronous image generation
- Request validation using Pydantic
- Rate limiting

## Requirements
Install dependencies:
pip install -r requirements.txt
requirements.txt
```markdown
### Running the Server

```bash
uvicorn app.main:app --reload
```

## API Usage

### Endpoint

**POST** `/generate`

### Request Headers

```
Content-Type: application/json
```

### JSON Body

```json
{
  "prompt": "A magical forest at twilight",
  "num_images": 1,
  "width": 512,
  "height": 512
}
```

### Response

```json
{
  "images": [
    "outputs/images/<uuid>.png"
  ]
}
```

## Swagger UI

Access interactive API docs at:

```
http://127.0.0.1:8000/docs
```

### Folder Structure

```
project-root/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── image_generator.py
│   └── config.py
├── outputs/
│   └── images/
├── requirements.txt
└── README.md
```

### Deployment

```bash
git clone <repo-url>
cd <repo-folder>
pip install -r requirements.txt
uvicorn app.main:app --reload
```

