from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Request model
class QueryRequest(BaseModel):
    query: str

# Response model
class Assessment(BaseModel):
    url: str
    adaptive_support: str  # "Yes" or "No"
    description: str
    duration: int
    remote_support: str  # "Yes" or "No"
    test_type: List[str]

class RecommendationResponse(BaseModel):
    recommended_assessments: List[Assessment]

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/recommend", response_model=RecommendationResponse)
def recommend(query: QueryRequest):
    # Dummy response (replace with your model logic)
    return {
        "recommended_assessments": [
            {
                "url": "https://example.com/python-test",
                "adaptive_support": "No",
                "description": "Test for Python devs",
                "duration": 60,
                "remote_support": "Yes",
                "test_type": ["Knowledge & Skills"]
            }
        ]
    }
