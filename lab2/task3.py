from fastapi import FastAPI
from faker import Faker
import random

app = FastAPI()
fake = Faker()
N = int(1e3)

@app.get("/random_users")
async def get_random_users():
    # Generate 1000 random user records for get API
    users = [{"name": fake.name(), "age": random.randint(20, 60), "location": fake.city()} for _ in range(N)]
    return users



# Run:
# uvicorn task3.py:app --reload

# Available at http://localhost:8000/random_users