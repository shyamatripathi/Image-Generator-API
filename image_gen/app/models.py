# app/models.py
from pydantic import BaseModel, Field
from typing import Optional

class GenerateRequest(BaseModel):
    prompt: str = Field(..., max_length=300)
    num_images: Optional[int] = 1
    width: Optional[int] = 512
    height: Optional[int] = 512
