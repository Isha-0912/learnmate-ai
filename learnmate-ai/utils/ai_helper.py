import os
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def _chat(system_prompt: str, user_prompt: str, max_tokens: int = 1500) -> dict:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()
        if content.startswith("```"):
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        return json.loads(content)
    except json.JSONDecodeError as e:
        return {"error": f"Failed to parse AI response: {str(e)}"}
    except Exception as e:
        err = str(e)
        if "api_key" in err.lower() or "authentication" in err.lower():
            return {"error": "Invalid or missing Groq API key. Please check your .env file."}
        return {"error": f"AI service error: {err}"}


def generate_study_plan(subject: str, level: str, days: int) -> dict:
    system = (
        "You are an expert educational planner. You create structured, actionable study plans. "
        "Always respond with valid JSON only — no markdown, no extra text."
    )
    user = f"""Create a {days}-day study plan for "{subject}" at {level} level.
Return ONLY this JSON structure:
{{
  "subject": "{subject}",
  "level": "{level}",
  "days": {days},
  "overview": "A 2-sentence overview of what the student will achieve",
  "daily_plan": [
    {{
      "day": 1,
      "title": "Day title",
      "topics": ["Topic 1", "Topic 2"],
      "activities": ["Activity description"],
      "resources": ["Resource suggestion"],
      "duration_hours": 2
    }}
  ],
  "tips": ["Tip 1", "Tip 2", "Tip 3"]
}}
Make sure daily_plan has exactly {days} entries."""
    return _chat(system, user, max_tokens=2500)


def ask_tutor(question: str, subject_context: str = "") -> dict:
    system = (
        "You are LearnMate AI, a world-class patient tutor. Explain concepts clearly with examples. "
        "Always respond with valid JSON only — no markdown, no extra text."
    )
    context_line = f" The student is studying: {subject_context}." if subject_context else ""
    user = f"""Answer this student question:{context_line}

Question: {question}

Return ONLY this JSON structure:
{{
  "question": "{question}",
  "explanation": "Clear, detailed explanation (3-5 paragraphs)",
  "key_points": ["Key point 1", "Key point 2", "Key point 3"],
  "example": "A concrete real-world example",
  "follow_up_topics": ["Related topic 1", "Related topic 2", "Related topic 3"]
}}"""
    return _chat(system, user, max_tokens=1200)


def generate_quiz(topic: str, num_questions: int, difficulty: str) -> dict:
    system = (
        "You are a quiz generator. Create clear, educational multiple-choice questions. "
        "Always respond with valid JSON only — no markdown, no extra text."
    )
    user = f"""Generate {num_questions} {difficulty}-difficulty multiple-choice questions about "{topic}".

Return ONLY this JSON structure:
{{
  "topic": "{topic}",
  "difficulty": "{difficulty}",
  "questions": [
    {{
      "id": 1,
      "question": "Question text?",
      "options": {{
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D"
      }},
      "correct_answer": "A",
      "explanation": "Why this answer is correct"
    }}
  ]
}}
Make sure there are exactly {num_questions} questions."""
    return _chat(system, user, max_tokens=2000)


def get_recommendations(subjects: list) -> dict:
    system = (
        "You are a learning path advisor. Suggest logical next steps for learners. "
        "Always respond with valid JSON only — no markdown, no extra text."
    )
    subjects_str = ", ".join(subjects)
    user = f"""A student has been studying: {subjects_str}.
Suggest next learning topics.

Return ONLY this JSON structure:
{{
  "recommendations": [
    {{
      "topic": "Topic name",
      "reason": "Why this is a good next step",
      "difficulty": "Beginner/Intermediate/Advanced",
      "estimated_hours": 10,
      "category": "Category name"
    }}
  ]
}}
Provide 4-5 recommendations."""
    return _chat(system, user, max_tokens=800)
