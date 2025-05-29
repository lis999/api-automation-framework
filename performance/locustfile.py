import random

from locust import HttpUser, task, between


class MemeUser(HttpUser):
    # Wait time between tasks (in seconds)
    wait_time = between(1, 3)

    def on_start(self):
        # Perform authorization once before tasks begin
        random_user_name = f"user_{random.randint(1000, 9999)}"
        response = self.client.post("/authorize", json={"name": random_user_name})
        self.token = response.json()["token"]
        self.headers = {"Authorization": self.token}

    @task(3)
    def create_object(self):
        # Send POST request to create a new meme object
        payload = {
            "text": "Locust test object",
            "url": "https://example.com/locust.jpg",
            "tags": ["load", "test"],
            "info": {"author": "Locust", "type": "image"}
        }
        self.client.post("/meme", json=payload, headers=self.headers)

    @task(1)
    def get_all_objects(self):
        # Send GET request to retrieve all meme objects
        self.client.get("/meme", headers=self.headers)
