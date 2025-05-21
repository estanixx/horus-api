# FastAPI + SQLModel + Alembic

Sample FastAPI project that uses async SQLAlchemy, SQLModel, Postgres, Alembic, and Docker.


## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/fastapi-sqlmodel/).

## Want to use this project?
1. Create environment
```sh
$ conda create -n horusapi
$ conda activate horusapi
```
2. Install dependencies
```sh
$ pip install -r project/requirements.txt
```
3. Launch docker.
```sh
$ docker-compose up -d --build
```
4. Launch Migrations
```sh
$ docker-compose exec web alembic upgrade head
```
Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)
# Create Migrations
To generate the first migration file, import the new model to `project/models/main.py` and run:
```sh
$ docker-compose exec web alembic revision --autogenerate -m "init"
```
# To test
bring down the old containers and volumes, rebuild the images, and spin up the new containers:

```sh
$ docker-compose down -v
$ docker-compose up -d --build
```
To view logs:
```sh
$ docker-compose logs web
```
# Add an entity:
```sh
$ curl -d '{"name":"Midnight Fit", "artist":"Mogwai", "year":"2021"}' -H "Content-Type: application/json" -X POST http://localhost:8004/songs
```

Get all songs: [http://localhost:8004/songs](http://localhost:8004/songs)

# Wanna add a new library?
1. Tell me. 


# Add BASIC endpoint.
1. Go to `project/app/main.py`
```python
from app.db import get_session
from app.models import SongCreate

@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
  song = Song(name=song.name, artist=song.artist, year=song.year)
  session.add(song)
  await session.commit()
  await session.refresh(song)
  return song
```