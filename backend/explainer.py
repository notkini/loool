import vertexai
from vertexai.preview.generative_models import GenerativeModel

PROJECT_ID = "silent-disengagement-cloud"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

model = GenerativeModel("gemini-1.5-flash")

def generate_explanation(student_id, reasons, confidence):
    reasons_text = "\n".join(reasons)

    prompt = f"""
You are an education support assistant.

Explain early disengagement signals clearly and ethically.

Rules:
- No negative labels
- No surveillance language
- Human-first tone
- Supportive and calm explanation

Student ID: {student_id}
Confidence level: {confidence}

Observed behavioral changes:
{reasons_text}

Explain:
1. What is changing
2. Why early awareness matters
3. Two gentle, human-led intervention suggestions
"""

    response = model.generate_content(prompt)
    return response.text.strip()
