from typing import Annotated

from database import get_session
from models import Review, ReviewCreate, ReviewRead, ReviewUpdate
from sqlmodel import Session

from fastapi import APIRouter, Depends

router = APIRouter(prefix="/review", tags=["reviews"])

# Module-level singleton so `Depends(...)` is not called in a function's
# argument defaults (see https://docs.astral.sh/ruff/rules/function-call-in-default-argument/)
SessionDep = Annotated[Session, Depends(get_session)]


@router.post("/", response_model=ReviewRead)
def create_review(review: ReviewCreate, session: SessionDep):
    db_review = Review.model_validate(review)
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review
