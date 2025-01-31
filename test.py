from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load BERT model for NLP-based similarity
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample Analyst Data
analysts = pd.DataFrame([
    {"AnalystID": "A001", "Name": "John Doe", "Skills": "Financial Fraud, AML, Risk Analysis", "Experience": 5, "Availability": True, "CasesResolved": 30, "SuccessRate": 90},
    {"AnalystID": "A002", "Name": "Jane Smith", "Skills": "Insider Trading, Regulatory Compliance", "Experience": 7, "Availability": False, "CasesResolved": 40, "SuccessRate": 85},
    {"AnalystID": "A003", "Name": "Robert Lee", "Skills": "Data Privacy, Cybersecurity", "Experience": 3, "Availability": True, "CasesResolved": 20, "SuccessRate": 88},
    {"AnalystID": "A004", "Name": "Emily Davis", "Skills": "Financial Fraud, Money Laundering", "Experience": 6, "Availability": True, "CasesResolved": 35, "SuccessRate": 92}
])

# Function to compute skill similarity using BERT embeddings
def calculate_skill_match_nlp(analyst_skills, case_type):
    analyst_embedding = bert_model.encode(analyst_skills)
    case_embedding = bert_model.encode(case_type)
    
    similarity = cosine_similarity([analyst_embedding], [case_embedding])[0][0]
    return round(similarity * 100, 2)  # Convert to percentage

# API Endpoint to recommend analysts
@app.route('/recommend_analyst', methods=['POST'])
def recommend_analyst():
    data = request.get_json()
    case_type = data.get("AllegationType", "")

    recommendations = []

    for _, analyst in analysts.iterrows():
        skill_match = calculate_skill_match_nlp(analyst["Skills"], case_type)
        
        # Weighted score (Skill match 50%, Experience 30%, Availability 20%)
        weighted_score = (
            (skill_match * 0.5) +
            (analyst["Experience"] * 3) +  # Convert experience to a 0-30 scale
            (20 if analyst["Availability"] else 0)  # Bonus for availability
        )

        recommendations.append({
            "AnalystID": analyst["AnalystID"],
            "Name": analyst["Name"],
            "SkillMatch": skill_match,
            "Experience": analyst["Experience"],
            "Availability": analyst["Availability"],
            "WeightedScore": weighted_score
        })

    # Sort by highest weighted score
    recommendations = sorted(recommendations, key=lambda x: x["WeightedScore"], reverse=True)

    return jsonify({"recommendations": recommendations})

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)