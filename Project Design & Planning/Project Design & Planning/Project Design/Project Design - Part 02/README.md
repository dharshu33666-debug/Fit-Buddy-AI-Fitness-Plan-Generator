# Project Design - Part 02

## Application Flow

1. User enters fitness details.
2. FastAPI receives the user input.
3. The backend sends the details to Google Gemini.
4. Gemini generates a personalized workout plan.
5. Nutrition and recovery guidance is generated.
6. The result is displayed using Jinja2 templates.
7. User feedback is used to update the workout plan.
8. User and workout data are stored in SQLite.

## Expected Result

The system provides a personalized fitness plan
and allows the user to update the plan using feedback.