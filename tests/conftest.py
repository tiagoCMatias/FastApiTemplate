# tests/conftest.py
import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, scoped_session
from fastapi.testclient import TestClient

from app.main import app
from app.core import get_db, Base
from app.core.config import settings
from app.models import UserModel


@pytest.fixture(scope="session")
def engine():
    """Create an in-memory SQLite engine."""
    return create_engine(
        settings.DATABASE_URL,
        echo=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool)


@pytest.fixture(scope="session")
def tables(engine):
    """Create all tables on the test database."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(engine, tables):
    """Provide a transactional scope around tests."""
    connection = engine.connect()
    transaction = connection.begin()
    session = scoped_session(sessionmaker(bind=connection))

    yield session

    session.remove()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
async def client_async(db_session):
    """Create an async test client using the overridden get_db dependency."""
    async def override_get_db():
        try:
            yield db_session
        finally:
            db_session.remove()

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client

    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def client(db_session):
    """Create an async test client using the overridden get_db dependency."""
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.remove()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app=app, base_url="http://test") as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def create_user_in_db(db_session):
    """Fixture to directly insert a user into the database."""
    def _create(username: str, email: str):
        user = UserModel(username=username, email=email)
        db_session.add(user)
        db_session.commit()
        return user
    return _create
