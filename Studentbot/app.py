from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

# Gemini model setup
generation_config = {
    "temperature": 0.5,
    "top_p": 0.9,
    "top_k": 50,
    "max_output_tokens": 1024,
}

system_instruction = """
You are a helpful Study Scheduler Bot.
Ask users their subjects, total days left for preparation, and daily study hours.
Then generate a realistic, well-balanced study schedule in bullet points.
Spread subjects evenly, give revision time, and avoid overloading. Encourage them at the end!
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction
)

chat_session = model.start_chat(history=[])

@app.route("/", methods=["GET", "POST"])
def index():
    schedule = ""
    if request.method == "POST":
        name = request.form["name"]
        subjects = request.form["subjects"]
        days = request.form["days"]
        hours = request.form["hours"]

        prompt = (
            f"My name is {name}. I have {days} days to prepare. "
            f"I can study {hours} hours per day. My subjects are: {subjects}. "
            "Create a daily or weekly study plan with subject-wise time split and revision time. "
            "Make it friendly, motivating, and well-balanced. Use bullet points."
        )

        response = chat_session.send_message(prompt)
        schedule = response.text

    return render_template("index.html", schedule=schedule)

if __name__ == "__main__":
    app.run(debug=True)
