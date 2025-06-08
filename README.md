
# HORUS API

This project provides a robust backend foundation for a modern web application. It features a high-performance GraphQL API built with FastAPI and Strawberry, leveraging SQLModel for an elegant and type-safe database layer. It is configured for asynchronous operations with PostgreSQL, uses Alembic for database migrations, and is **fully containerized with Docker for a streamlined development experience.**

## Tech Stack

  - **Backend:** FastAPI
  - **GraphQL:** Strawberry
  - **Database ORM:** SQLModel (combining Pydantic and SQLAlchemy)
  - **Database:** PostgreSQL
  - **Migrations:** Alembic
  - **Development & Deployment:** Docker & Docker Compose

## Prerequisites

  - Docker
  - Docker Compose

## 1\. Local Development Setup

This project is fully containerized. You do **not** need to install Python or any dependencies on your local machine. All development and commands are run through Docker.

### Step 1: Clone the Repository

```sh
git clone <your-repository-url>
cd <your-project-directory>
```

### Step 2: Build and Start the Services

This single command builds the Docker image for the FastAPI application (which includes installing all Python dependencies from `requirements.txt`) and starts the `web` and `db` services defined in `docker-compose.yml`.

```sh
docker-compose up -d --build
```

### Step 3: Apply Initial Database Migrations

Once the containers are running, create the database tables by applying all existing migrations.

```sh
docker-compose exec web alembic upgrade head
```

### Step 4: Verify Setup

Your API is now running. You can verify it by accessing these URLs in your browser:

  - **Health Check:** [http://localhost:8004/health](https://www.google.com/search?q=http://localhost:8004/health)
  - **GraphQL API & Playground:** [http://localhost:8004/graphql](https://www.google.com/search?q=http://localhost:8004/graphql)

-----

## 2\. Developer's Guide: How to Add a New Entity

This guide will walk you through adding a new `WeatherReading` entity to the project. All `alembic` commands are run inside the `web` container using `docker-compose exec`.

### Step 1: Define the Database Model

Create a new file `app/models/weather_reading.py` to define the table schema.

**`app/models/weather_reading.py`**

```python
from typing import Optional
from sqlmodel import Field
from app.models.base import BaseSQLModel

class WeatherReading(BaseSQLModel, table=True):
    """Represents a weather reading record in the database."""
    temperature: float = Field(description="The recorded temperature in Celsius.")
    humidity: float = Field(description="The recorded relative humidity as a percentage.")
    wind_speed: float = Field(description="The recorded wind speed in km/h.")
    station_id: Optional[int] = Field(default=None, foreign_key="station.id")
```

### Step 2: Create a Database Migration

Alembic needs to know about your new model to create a migration script.

1.  **Expose the new model:** Open `app/models/__init__.py` and add your new model.

    ```python
    # app/models/__init__.py
    # ... existing imports
    from .weather_reading import WeatherReading

    __all__ = [
        # ... existing models
        "WeatherReading",
    ]
    ```

2.  **Generate the migration script:** Run the following command in your terminal.

    ```sh
    docker-compose exec web alembic revision --autogenerate -m "Add WeatherReading model"
    ```

    This will create a new file in the `project/alembic/versions` directory.

### Step 3: Apply the Migration

Run the `upgrade` command to apply the new migration to the database.

```sh
docker-compose exec web alembic upgrade head
```

### Step 4: Create GraphQL Types

Create `app/graphql/types/weather_reading_type.py` to define how your entity will look in the GraphQL schema.

**`app/graphql/types/weather_reading_type.py`**

```python
import strawberry
from typing import Optional

@strawberry.type
class WeatherReadingType:
    id: int
    temperature: float
    # ... other fields

@strawberry.input
class WeatherReadingCreateInput:
    temperature: float
    # ... other fields

@strawberry.input
class WeatherReadingUpdateInput:
    temperature: Optional[float] = None
    # ... other fields
```

### Step 5: Implement the Service Layer

Create `app/services/weather_reading_service.py` to handle the business logic.

**`app/services/weather_reading_service.py`**

```python
from typing import List
from sqlmodel import select
from app.models import WeatherReading
from sqlmodel.ext.asyncio.session import AsyncSession

class WeatherReadingService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[WeatherReading]:
        result = await self.db.exec(select(WeatherReading))
        return result.all()
    
    # ... implement create, update, delete methods ...
```

### Step 6: Create GraphQL Queries & Mutations

Create the files `app/graphql/queries/weather_reading_query.py` and `app/graphql/mutations/weather_reading_mutation.py` and implement the logic, calling your new service.

### Step 7: Integrate into the Schema

Update the `__init__.py` barrel files in each directory to include your new components. This makes them available to the rest of the application.

  - `app/graphql/types/__init__.py`
  - `app/graphql/queries/__init__.py`
  - `app/graphql/mutations/__init__.py`
  - `app/services/__init__.py`

For example, you would add `from .weather_reading_query import WeatherReadingQuery` to `app/graphql/queries/__init__.py` and add `WeatherReadingQuery` to the `class Query(...)` inheritance list.

-----

## 3\. Testing Your Endpoints

The best way to test is using the interactive GraphiQL UI.

  - **Navigate to:** [http://localhost:8004/graphql](https://www.google.com/search?q=http://localhost:8004/graphql)

**Example: Create a new Entity**

```graphql
mutation {
  createWeatherReading(input: {
    temperature: 25.5,
    humidity: 60.2,
    windSpeed: 15.0,
    stationId: 1
  }) {
    id
    temperature
  }
}
```

## 4\. Project Structure Overview

```
/app
├── /core           # Application configuration (settings.py)
├── /database       # Database engine and session management (session.py)
├── /graphql        # Main GraphQL package
│   ├── /mutations  # Mutation logic, separated by entity
│   ├── /queries    # Query logic, separated by entity
│   ├── /types      # GraphQL types (objects, inputs)
│   ├── context.py  # Context getter for DB sessions
│   └── schema.py   # Final schema assembly
├── /models         # SQLModel database models
└── /services       # Business logic and data access layer
/alembic            # Alembic migration scripts and configuration
docker-compose.yml  # Docker service definitions
Dockerfile          # Instructions for building the web service image
requirements.txt    # Python dependencies
...
```

## 5\. Additional Commands

  - **View logs for the web service:**
    ```sh
    docker-compose logs -f web
    ```
  - **Tear down all containers and volumes (deletes all data):**
    ```sh
    docker-compose down -v
    ```