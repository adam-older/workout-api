from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
from typing import List

from sqlmodel import Session, select, insert

from app.repositories.database import get_sqlmodel_session
from app.models.WorkoutModel import WorkoutModel

router = APIRouter(
    prefix="/workout",
    tags=""
)


# Route to get all workouts
@router.get("/", response_model=List[WorkoutModel])
def read_workouts(skip: int = 0, limit: int = 100, db: Session = Depends(get_sqlmodel_session)):
    workouts = db.exec(select(WorkoutModel).offset(skip).limit(limit)).all()
    return workouts


# Route to create a new workout
@router.post("/", response_model=WorkoutModel)
def create_workout(workout: WorkoutModel, db: Session = Depends(get_sqlmodel_session)):
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

# Route to create a new workout
@router.post("/bulk", response_model=List[WorkoutModel])
def create_bulk_workout(workouts: List[WorkoutModel], db: Session = Depends(get_sqlmodel_session)):
    # result = db.scalars(insert(WorkoutModel).returning(WorkoutModel), workouts)
    db.bulk_save_objects(workouts)
    db.commit()
    result = db.exec(select(WorkoutModel)).all()
    return result


# Route to get a specific workout by ID
@router.get("/{workout_id}", response_model=WorkoutModel)
def read_workout(workout_id: int, db: Session = Depends(get_sqlmodel_session)):
    workout = db.query(WorkoutModel).filter(WorkoutModel.workout_id == workout_id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


# Route to update a specific workout by ID
@router.put("/{workout_id}", response_model=WorkoutModel)
def update_workout(workout_id: int, workout: WorkoutModel, db: Session = Depends(get_sqlmodel_session)):
    db_workout = db.query(WorkoutModel).filter(WorkoutModel.workout_id == workout_id).first()
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    update_data = workout.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_workout, key, value)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout


# Route to delete a specific workout by ID
@router.delete("/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(get_sqlmodel_session)):
    workout = db.query(WorkoutModel).filter(WorkoutModel.workout_id == workout_id).first()
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    db.delete(workout)
    db.commit()
    return {"message": "Workout deleted successfully"}
