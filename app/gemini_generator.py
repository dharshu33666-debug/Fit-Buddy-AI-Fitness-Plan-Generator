import os
from dotenv import load_dotenv
from google import genai

from app.gemini_client import generate_text_with_retry

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_workout_gemini(name, age, weight, fitness_goal, intensity):

    prompt = f"""
Create a personalized 7-day workout plan for:

Name: {name}
Age: {age}
Weight: {weight} kg
Fitness Goal: {fitness_goal}
Intensity: {intensity}

Give a simple day-by-day workout plan.

For each day include:
- Exercises
- Sets/reps or duration
- Rest days when appropriate

Make the plan personalized based on the user's age, weight,
fitness goal, and selected intensity.

Keep it practical and beginner-friendly.
"""

    return generate_text_with_retry(
        client=client,
        model_name="gemini-3.5-flash",
        prompt=prompt,
        fallback_text=(
            "Gemini API daily limit has been reached. "
            "Please try again after the quota resets."
        ),
    )