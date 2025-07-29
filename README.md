
# 📅 Study Scheduler Bot

A simple AI-powered chatbot that helps users generate personalized daily or weekly **study plans** based on their inputs using **Gemini (Google Generative AI)**.

Built with **Flask** and the **Gemini 1.5 Flash API**, this bot asks for your subjects, number of preparation days, and daily study hours, then returns a motivational and well-balanced schedule.

---


## ✨ Features

- 🌟 Personalized study plans with daily/weekly breakdown.
- 🧠 Powered by Gemini 1.5 Flash from Google.
- 📝 Takes name, subjects, available days, and daily study time.
- 📄 Clean UI using HTML & CSS via Flask templates.


---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (via Flask templates)
- **Backend**: Python (Flask)
- **AI**: Google Generative AI (Gemini)
- **Environment**: dotenv for API key config

---

## 📁 Project Structure

```

student\_bot/
├── app.py
├── .env
├── requirements.txt
├── templates/
│   └── index.html
└── README.md

```

---

## 🧑‍💻 Getting Started

### 🔐 1. Get a Gemini API Key

- Visit: [Google AI Studio](https://aistudio.google.com/app/apikey)
- Generate an API key
- Copy it to a `.env` file in your project folder:

```

GEMINI\_API\_KEY=your\_gemini\_api\_key\_here

````

---

### 🧩 2. Install Dependencies

```bash
pip install -r requirements.txt
````

---

### ▶️ 3. Run the App

```bash
python app.py
```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## 📄 Example Usage

**Input:**

```
Name: Aanya
Subjects: Physics, Chemistry, Biology
Days: 25
Hours per day: 4
```

**Output:**

```
📅 Aanya's 25-Day Study Plan

📌 Week 1–2:
- 1.5 hrs Physics
- 1.5 hrs Chemistry
- 1 hr Biology

📌 Week 3–4:
- Alternate topics daily
- Include past paper practice
- Light revision weekends

✨ Stay focused. You’re doing great!
```

---

## ✅ requirements.txt

```txt
flask
python-dotenv
google-generativeai
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📌 To Do / Future Ideas

* [ ] Add PDF download of study plan
* [ ] Add user authentication
* [ ] Add persistent chat history
* [ ] Deploy using Render or Replit





