from fastapi import FastAPI
from pydantic import BaseModel
from recommend_core import get_recommendations

app = FastAPI()

class QueryInput(BaseModel):
    query: str
    top_k: int = 10

@app.post("/recommend")
def recommend(data: QueryInput):
    results = get_recommendations(data.query, data.top_k)
    return {
        "query": data.query,
        "recommendations": results[[
            'assessment_name', 'url', 'remote_testing',
            'adaptive_support', 'duration', 'test_type'
        ]].to_dict(orient="records")
    }