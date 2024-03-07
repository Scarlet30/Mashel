from locust import HttpUser, task, between


class RickAndMortyApi(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_api_character(self):
        self.client.get("/api/character")
