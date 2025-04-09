SHL Assessment Recommender
This is a take-home assignment submission for SHL's AI team. The solution includes a recommendation system that suggests relevant assessments based on job descriptions or natural language queries.

🚀 Live Links
🔗 Streamlit Tool:
https://shlrecommenderupdated-2fslen9zza8j66drxu7gxf.streamlit.app/

🧠 API Base URL:
https://shl-recommender-updated-1.onrender.com

📄 1-Page Report:
https://docs.google.com/document/d/1D7b_3lhB8V6taD3ud0nhzoTVCY8wY16mRrZgo_xOp_I/edit?usp=sharing

📦 API Endpoints
1. Health Check
URL: /health

Method: GET

Response:

json
Copy
Edit
{
  "status": "healthy"
}
2. Assessment Recommendation
URL: /recommend

Method: POST

Body:

json
Copy
Edit
{
  "query": "Looking for a Python developer test"
}
Response:

json
Copy
Edit
{
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
🛠️ Technologies Used
Python

FastAPI

Streamlit

Render (API deployment)

Streamlit Cloud (Web App deployment)

📂 How to Run Locally
bash
Copy
Edit
# Clone the repository
git clone https://github.com/Msrinadh/shl_recommender_updated.git
cd shl_recommender_updated

# Create virtual environment and activate
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app
uvicorn main:app --reload

# OR run Streamlit app
streamlit run app.py
