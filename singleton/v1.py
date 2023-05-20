from fastapi import FastAPI

class Database:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def connect(self):
        # Connect to the database
        pass

db = Database()

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    db = Database()  # Access the singleton instance
    # Fetch user from the database and return the response
