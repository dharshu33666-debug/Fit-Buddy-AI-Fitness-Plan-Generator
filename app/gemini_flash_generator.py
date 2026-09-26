import os
from dotenv import load_dotenv
from google import genai

from app.gemini_client import generate_text_with_retry

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_nutrition_tip_with_flash(fitness_goal, weight):

    prompt = f"""
Create a personalized nutrition and recovery tip for a fitness user.

Fitness Goal: {fitness_goal}
Weight: {weight} kg

Give:
- 5 simple nutrition tips
- Hydration advice
- Recovery advice
- Sleep advice
- Simple healthy food suggestions

Keep it practical, beginner-friendly, and easy to follow.
Do not give extreme diet recommendations.

Return the answer with clear headings.
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