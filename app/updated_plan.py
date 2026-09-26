import os
from dotenv import load_dotenv
from google import genai

from app.gemini_client import generate_text_with_retry

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def update_workout_plan(original_plan, feedback):

    prompt = f"""
Here is the original workout plan:

{original_plan}

The user gave this feedback:

{feedback}

Create an updated 7-day workout plan based on the user's feedback.

Keep the plan simple, safe, and personalized.
Return only the updated workout plan.
"""

    return generate_text_with_retry(
        client=client,
        model_name="gemini-3.5-flash",
        prompt=prompt,
        fallback_text=(
            "Your plan update is temporarily unavailable because the AI service is busy. "
            "Please try again in a few minutes."
        ),
    )