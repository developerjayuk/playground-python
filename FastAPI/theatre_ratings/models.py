from datetime import datetime

from sqlmodel import Field, SQLModel


class Review(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    play_name: str = Field(index=True)
    reviewer_name: str
    rating: int = Field(ge=1, le=5)
    comment: str
    created_at: datetime = Field(default_factory=datetime.now)


class ReviewCreate(SQLModel):
    play_name: str
    reviewer_name: str
    rating: int = Field(ge=1, le=5)
    comment: str


class ReviewRead(SQLModel):
    id: int
    play_name: str
    reviewer_name: str
    rating: int
    comment: str
    created_at: datetime = Field(default_factory=datetime.now)


class ReviewUpdate(SQLModel):
    rating: int | None = Field(default=None, ge=1, le=5)
    comment: str | None = None
