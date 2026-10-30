from sqlmodel import Session, SQLModel, create_engine

# usually kept in env variable
DATABASE_URL = "sqlite:///theatre_ratings.db"

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    """Create all tables defined by the SQLModel Class"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency that provides a database session per request"""
    with Session(engine) as session:
        # yield similar to using in other languages, keeps it alive so it can be used later
        yield session
