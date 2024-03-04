# locust file.py
from locust import HttpUser, task, between


class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def access_api(self):
        self.client.get("https://rickandmortyapi.com/api/character")
