from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash

from app.database import (
    save_user,
    save_plan,
    get_original_plan,
    update_plan,
    SessionLocal,
    User
)

from app.updated_plan import update_workout_plan


router = APIRouter()

templates = Jinja2Templates(directory="templates")


# =========================================================
# GENERATE FITNESS PLAN
# =========================================================

@router.post("/generate-workout")
def generate_workout(
    request: Request,

    name: str = Form(...),

    user_id: str = Form(...),

    age: int = Form(...),

    weight: float = Form(...),

    fitness_goal: str = Form(...),

    intensity: str = Form(...)
):

    # Generate Workout using Gemini

    workout_plan = generate_workout_gemini(
        name,
        age,
        weight,
        fitness_goal,
        intensity
    )


    # Generate Nutrition using Gemini

    nutrition_tip = generate_nutrition_tip_with_flash(
        fitness_goal,
        weight
    )


    # Save user

    save_user(
        name,
        user_id,
        age,
        weight,
        fitness_goal,
        intensity
    )


    # Save workout plan

    save_plan(
        user_id,
        workout_plan
    )


    # Show result page

    return templates.TemplateResponse(
        request=request,

        name="result.html",

        context={

            "name": name,

            "user_id": user_id,

            "age": age,

            "weight": weight,

            "fitness_goal": fitness_goal,

            "intensity": intensity,

            "workout_plan": workout_plan,

            "nutrition_tip": nutrition_tip
        }
    )


# =========================================================
# UPDATE WORKOUT USING FEEDBACK
# =========================================================

@router.post("/submit-feedback")
def submit_feedback(

    request: Request,

    user_id: str = Form(...),

    feedback: str = Form(...)
):

    # Get original plan

    original_plan = get_original_plan(
        user_id
    )


    # Generate updated plan

    updated_plan = update_workout_plan(
        original_plan,
        feedback
    )


    # Save updated plan

    update_plan(
        user_id,
        updated_plan
    )


    # Show updated result

    return templates.TemplateResponse(

        request=request,

        name="result.html",

        context={

            "user_id": user_id,

            "workout_plan": updated_plan,

            "nutrition_tip": "",

            "name": "",

            "age": "",

            "weight": "",

            "fitness_goal": "",

            "intensity": ""
        }
    )


# =========================================================
# ALL USERS
# =========================================================

@router.get("/all-users")
def all_users(request: Request):

    db = SessionLocal()

    users = db.query(User).all()

    db.close()


    return templates.TemplateResponse(

        request=request,

        name="all_users.html",

        context={

            "users": users

        }
    )


# =========================================================
# PROGRESS DASHBOARD
# =========================================================

@router.get("/dashboard")
def dashboard(request: Request):

    # Demo progress values
    # Later these can be connected
    # to actual workout completion data.

    streak = 7

    completed_workouts = 5

    weekly_goal = 7

    progress = 71


    achievements = [

        "🔥 7 Day Streak",

        "💪 5 Workouts Completed",

        "🎯 Weekly Goal Progress",

        "⭐ Fitness Journey Started"

    ]


    return templates.TemplateResponse(

        request=request,

        name="dashboard.html",

        context={

            "streak": streak,

            "completed_workouts":
                completed_workouts,

            "weekly_goal":
                weekly_goal,

            "progress":
                progress,

            "achievements":
                achievements

        }
    )