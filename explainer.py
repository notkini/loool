def generate_explanation(student_id, reasons, confidence):
    prompt = f"""
You are an education support assistant.
Your role is to explain early disengagement signals ethically and clearly.

Student ID: {student_id}
Confidence Level: {confidence}

Observed signals:
{chr(10).join(reasons)}

Explain:
1. What pattern is changing
2. Why this matters early
3. Keep tone supportive and non-judgmental

Then suggest 2 gentle, human-led interventions.
Do not label the student negatively.
"""

    explanation = f"""
Early engagement insight for Student {student_id}

Summary:
Recent learning activity shows a noticeable change compared to the student’s usual engagement pattern. Activity gaps have increased, which can indicate early disengagement if left unaddressed.

Why this matters:
Behavioral changes often appear weeks before academic impact. Identifying this early allows supportive action before performance is affected.

Confidence level:
{confidence}

Suggested next steps:
- A short, supportive mentor check-in to understand any challenges
- Review workload pacing or learning schedule flexibility
"""

    return explanation.strip()
