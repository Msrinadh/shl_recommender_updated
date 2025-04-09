import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

import os
model_path = os.path.join(os.path.dirname(__file__), 'pretrained_model')
model = SentenceTransformer(model_path)
df = pd.read_csv("shl_catalog.csv")
df['combined_text'] = df[['assessment_name', 'description', 'test_type']].fillna('').agg(' '.join, axis=1)
catalog_embeddings = model.encode(df['combined_text'].tolist())

def get_recommendations(query: str, top_k: int = 10):
    input_embedding = model.encode([query])
    scores = cosine_similarity(input_embedding, catalog_embeddings)[0]
    top_n = scores.argsort()[-top_k:][::-1]
    return df.iloc[top_n]