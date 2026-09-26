from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./fitbuddy.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(String, unique=True, index=True)
    age = Column(Integer)
    weight = Column(Float)
    fitness_goal = Column(String)
    intensity = Column(String)


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    plan = Column(Text)


Base.metadata.create_all(bind=engine)


def save_user(name, user_id, age, weight, fitness_goal, intensity):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.user_id == user_id
    ).first()

    if existing_user:
        existing_user.name = name
        existing_user.age = age
        existing_user.weight = weight
        existing_user.fitness_goal = fitness_goal
        existing_user.intensity = intensity
    else:
        user = User(
            name=name,
            user_id=user_id,
            age=age,
            weight=weight,
            fitness_goal=fitness_goal,
            intensity=intensity
        )

        db.add(user)

    db.commit()
    db.close()


def save_plan(user_id, plan):
    db = SessionLocal()

    workout_plan = WorkoutPlan(
        user_id=user_id,
        plan=plan
    )

    db.add(workout_plan)
    db.commit()
    db.close()


def get_user(user_id):
    db = SessionLocal()

    user = db.query(User).filter(
        User.user_id == user_id
    ).first()

    db.close()

    return user


def get_original_plan(user_id):
    db = SessionLocal()

    workout_plan = db.query(WorkoutPlan).filter(
        WorkoutPlan.user_id == user_id
    ).first()

    db.close()

    if workout_plan:
        return workout_plan.plan

    return None


def update_plan(user_id, new_plan):
    db = SessionLocal()

    workout_plan = db.query(WorkoutPlan).filter(
        WorkoutPlan.user_id == user_id
    ).first()

    if workout_plan:
        workout_plan.plan = new_plan
        db.commit()

    db.close()