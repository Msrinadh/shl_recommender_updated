from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Request model for recommendation
class RecommendRequest(BaseModel):
    query: str

# Response model for assessments
class Assessment(BaseModel):
    url: str
    adaptive_support: str
    description: str
    duration: int
    remote_support: str
    test_type: List[str]

class RecommendResponse(BaseModel):
    recommended_assessments: List[Assessment]

# Recommend endpoint
@app.post("/recommend", response_model=RecommendResponse)
def recommend_assessments(req: RecommendRequest):
    # Dummy data for example
    return {
        "recommended_assessments": [
            {
                "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
                "adaptive_support": "No",
                "description": "Multi-choice test for Python knowledge.",
                "duration": 11,
                "remote_support": "Yes",
                "test_type": ["Knowledge & Skills"]
            }
        ]
    }
