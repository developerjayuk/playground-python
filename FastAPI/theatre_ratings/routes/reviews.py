from typing import Annotated

from database import get_session
from models import Review, ReviewCreate, ReviewRead, ReviewUpdate
from sqlmodel import Session, func, select

from fastapi import APIRouter, Depends, HTTPException, Query, status

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


@router.get("/", response_model=list[ReviewRead])
def list_reviews(
    session: SessionDep,
    play_name: str | None = Query(None, description="Filter by play name"),
    skip: int = Query(0, ge=0, description="Number of reviews to skip"),
    limit: int = Query(10, ge=1, le=50, description="Max reviews to return"),
):
    query = select(Review)

    if play_name:
        query = query.where(Review.play_name == play_name)

    query = query.offset(skip).limit(limit)
    return session.exec(query).all()


@router.get("/average/{play_name}")
def get_average_rating(play_name: str, session: SessionDep):
    no_review_exception = HTTPException(
        status_code=404, detail=f"No review found for {play_name}"
    )

    result = session.exec(
        select(func.avg(Review.rating), func.count(Review.id)).where(
            Review.play_name == play_name
        )
    ).first()

    if result is None:
        raise no_review_exception

    avg_rating, total_reviews = result

    if total_reviews == 0:
        raise no_review_exception

    return {
        "play_name": play_name,
        "average_rating": round(avg_rating, 2),
        "total_reviews": total_reviews,
    }


@router.get("/{review_id}", response_model=ReviewRead)
def get_review(review_id: int, session: SessionDep):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail=f"No review found for {review_id}")

    return review


@router.patch("/{review_id}", response_model=ReviewRead)
def patch_review(review_id: int, update: ReviewUpdate, session: SessionDep):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail=f"No review found for {review_id}")

    update_data = update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(review, key, value)

    session.add(review)
    session.commit()
    session.refresh(review)
    return review


@router.put("/{review_id}", response_model=ReviewRead)
def replace_review(review_id: int, review: ReviewCreate, session: SessionDep):
    db_review = session.get(Review, review_id)

    if db_review is None:
        raise HTTPException(status_code=404, detail=f"No review found for {review_id}")

    db_review.sqlmodel_update(review.model_dump())

    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review


@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int, session: SessionDep):
    review = session.get(Review, review_id)

    if not review:
        raise HTTPException(status_code=404, detail=f"No review found for {review_id}")

    session.delete(review)
    session.commit()
