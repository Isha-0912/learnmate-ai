from flask import Flask, render_template, request, jsonify, session
from utils.ai_helper import (
    generate_study_plan,
    ask_tutor,
    generate_quiz,
    get_recommendations
)
import os
from dotenv import load_dotenv
load_dotenv(override=True)


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "learnmate-secret-2024")


@app.route("/")
def index():
    if "progress" not in session:
        session["progress"] = {}
    if "subjects" not in session:
        session["subjects"] = []
    return render_template("index.html",
                           progress=session.get("progress", {}),
                           subjects=session.get("subjects", []))


@app.route("/study-plan", methods=["GET", "POST"])
def study_plan():
    plan = None
    error = None
    form_data = {}

    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        level = request.form.get("level", "Beginner")
        days = request.form.get("days", "7")
        form_data = {"subject": subject, "level": level, "days": days}

        if not subject:
            error = "Please enter a subject."
        else:
            plan = generate_study_plan(subject, level, int(days))
            if plan and "error" not in plan:
                # Track subject in session
                subjects = session.get("subjects", [])
                if subject not in subjects:
                    subjects.append(subject)
                    session["subjects"] = subjects
                # Init progress
                progress = session.get("progress", {})
                key = f"{subject}_{level}"
                if key not in progress:
                    progress[key] = {"completed": 0, "total": int(days), "subject": subject, "level": level}
                    session["progress"] = progress
            elif plan and "error" in plan:
                error = plan["error"]
                plan = None

    return render_template("study_plan.html", plan=plan, error=error, form_data=form_data)


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    quiz_data = None
    error = None
    form_data = {}

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        num_questions = request.form.get("num_questions", "5")
        difficulty = request.form.get("difficulty", "Medium")
        form_data = {"topic": topic, "num_questions": num_questions, "difficulty": difficulty}

        if not topic:
            error = "Please enter a topic."
        else:
            quiz_data = generate_quiz(topic, int(num_questions), difficulty)
            if quiz_data and "error" in quiz_data:
                error = quiz_data["error"]
                quiz_data = None

    return render_template("quiz.html", quiz_data=quiz_data, error=error, form_data=form_data)


@app.route("/tutor", methods=["GET", "POST"])
def tutor():
    response = None
    error = None
    question = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        subject_context = request.form.get("subject_context", "").strip()

        if not question:
            error = "Please enter a question."
        else:
            response = ask_tutor(question, subject_context)
            if response and "error" in response:
                error = response["error"]
                response = None

    return render_template("tutor.html", response=response, error=error, question=question,
                           subjects=session.get("subjects", []))


@app.route("/progress")
def progress():
    progress_data = session.get("progress", {})
    subjects = session.get("subjects", [])
    recommendations = []

    if subjects:
        recs = get_recommendations(subjects)
        if recs and "error" not in recs:
            recommendations = recs.get("recommendations", [])

    return render_template("progress.html",
                           progress_data=progress_data,
                           subjects=subjects,
                           recommendations=recommendations)


@app.route("/api/update-progress", methods=["POST"])
def update_progress():
    data = request.json
    key = data.get("key")
    completed = data.get("completed", 0)

    progress = session.get("progress", {})
    if key in progress:
        progress[key]["completed"] = completed
        session["progress"] = progress
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Key not found"}), 404


@app.route("/api/reset-progress", methods=["POST"])
def reset_progress():
    session["progress"] = {}
    session["subjects"] = []
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
