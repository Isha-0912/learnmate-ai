# 🎓 LearnMate AI — Personalized Learning Dashboard

> An AI-powered learning companion that generates study plans, quizzes, tutor responses, and tracks your progress — all in one beautiful dashboard.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square&logo=flask)
![Groq](https://img.shields.io/badge/AI-Groq%20LLaMA%203.3-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Features

| Feature | Description |
|---|---|
| 📚 **Study Plan Generator** | Enter any subject, skill level, and number of days — get a full day-by-day roadmap |
| ❓ **Quiz Generator** | AI-generated multiple-choice quizzes with live scoring and explanations |
| 💬 **AI Tutor** | Ask any learning question and get a structured explanation with examples |
| 📊 **Progress Tracker** | Track completed study days with interactive progress bars |
| 🚀 **Smart Recommendations** | Get personalized suggestions for what to study next |

---

## 🖥️ Screenshots

### Dashboard
> Modern dark dashboard with stats, feature cards, and active plan tracking.

### Study Plan
> Day-by-day timeline with topics, activities, resources, and duration.

### Quiz
> Interactive MCQ quiz with instant feedback and score display.

### AI Tutor
> Structured explanations with key points, examples, and follow-up topics.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI:** Groq API (LLaMA 3.3 70B)
- **Fonts:** DM Serif Display + DM Sans

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Git
- A free [Groq API key](https://console.groq.com)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/learnmate-ai.git
cd learnmate-ai
```

**2. Create a virtual environment**
```bash
python -m venv venv
```

Activate it:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up your API key**

Create a `.env` file in the project root:
```
GROQ_API_KEY=your-groq-api-key-here
SECRET_KEY=learnmate2024
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

**5. Run the app**
```bash
python app.py
```

Open your browser and go to: **http://localhost:5000**

---

## 📁 Project Structure

```
learnmate-ai/
│
├── app.py                  ← Flask app and all routes
├── requirements.txt        ← Python dependencies
├── .env.example            ← Environment variable template
│
├── templates/
│   ├── base.html           ← Master layout with sidebar
│   ├── index.html          ← Dashboard homepage
│   ├── study_plan.html     ← Study plan generator
│   ├── quiz.html           ← Quiz generator
│   ├── tutor.html          ← AI tutor
│   └── progress.html       ← Progress tracker
│
├── static/
│   ├── style.css           ← Dark dashboard theme
│   └── script.js           ← Animations and interactions
│
└── utils/
    └── ai_helper.py        ← All Groq AI API calls
```

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key (get it free at console.groq.com) |
| `SECRET_KEY` | Flask session secret key (any random string) |

---

## 💡 How It Works

1. User submits a form (subject, level, days)
2. Flask routes the request to `ai_helper.py`
3. Groq's LLaMA 3.3 70B model generates structured JSON
4. Flask renders the response into beautiful HTML templates
5. Progress is tracked using Flask sessions

---

## 🏆 Built For

This project was built for a **hackathon** to demonstrate the power of AI in personalized education. LearnMate AI makes quality learning accessible to everyone by providing instant, personalized study resources on any topic.

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [Groq](https://groq.com) for the blazing fast free AI API
- [Flask](https://flask.palletsprojects.com) for the lightweight backend
- [Google Fonts](https://fonts.google.com) for DM Serif Display and DM Sans
