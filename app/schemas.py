from pydantic import BaseModel


class WorkoutRequest(BaseModel):
    name: str
    user_id: str
    age: int
    weight: float
    fitness_goal: str
    intensity: str


class FeedbackRequest(BaseModel):
    user_id: str
    feedback: str