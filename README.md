# 🏋️ FitBuddy – AI Fitness Plan Generator

FitBuddy is an AI-powered personal fitness web application that generates personalized workout plans and nutrition guidance based on the user's fitness profile.

## Features

- 👤 User profile management
- 🤖 AI-generated personalized 7-day workout plans
- 🥗 AI-generated nutrition and recovery tips
- 💬 Workout feedback and plan updates
- 📊 Fitness progress dashboard
- 🔥 Streak tracking
- 🏆 Achievement tracking
- 👥 All users page
- 📱 Mobile-friendly web application
- 🌐 Online deployment using Render

## Technologies Used

- Python
- FastAPI
- Jinja2
- SQLAlchemy
- Google Gemini API
- HTML
- CSS
- Git
- GitHub
- Render

## Requirements

- Python 3.10+
- Google Gemini API Key
- Git

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/dharshu33666-debug/Fit-Buddy-AI-Fitness-Plan-Generator.git
```

### 2. Open the Project Folder

```bash
cd Fit-Buddy-AI-Fitness-Plan-Generator
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment File

Create a `.env` file in the project root directory.

Add your Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

> ⚠️ Never upload your `.env` file or expose your Gemini API key publicly.

### 5. Run the Application

```bash
python -m uvicorn app.main:app --reload
```

### 6. Open in Browser

Open:

```text
http://127.0.0.1:8000
```

## AI Integration

FitBuddy uses the Google Gemini API to generate:

- 🏋️ Personalized workout plans
- 🥗 Nutrition recommendations
- 😴 Recovery guidance
- 💬 Updated workout plans based on user feedback

The Gemini API key is stored securely using environment variables.

## Fitness Dashboard

The dashboard provides:

- 🏋️ Workout progress
- 🎯 Weekly goal progress
- 🔥 Workout streak
- 🏆 Achievements
- 💪 Fitness motivation

## Personalized Feedback

Users can provide feedback about their workout plan.

FitBuddy uses the feedback to generate an updated workout plan based on the user's requirements.

## Project Structure

```text
FitBuddy/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── schemas.py
│   ├── gemini_client.py
│   ├── gemini_generator.py
│   ├── gemini_flash_generator.py
│   └── updated_plan.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── dashboard.html
│   └── all_users.html
│
├── static/
│   └── images/
│       └── fitness.jpg
│
├── tests/
│   └── test_gemini_retry.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Deployment

FitBuddy is deployed as a FastAPI web application using Render.

The application can be accessed from both desktop and mobile devices.

## Security

The Gemini API key is stored in the `.env` file.

The `.env` file is excluded from Git using `.gitignore`.

**Never commit API keys or other sensitive information to GitHub.**

## Future Improvements

- 🔐 User authentication
- 📈 Real-time progress tracking
- 🏋️ Workout completion tracking
- 📅 Workout history
- 📊 Advanced progress charts
- 🔥 Real streak calculation
- 🏆 More achievements
- 🥗 Advanced nutrition tracking
- 📱 Improved mobile UI

## Author

**Dharshini**

GitHub:

https://github.com/dharshu33666-debug

## Project

FitBuddy is an AI-powered fitness assistant designed to help users create personalized workout and nutrition plans using AI technology.