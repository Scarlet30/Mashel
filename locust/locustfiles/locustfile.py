"""from locust import HttpUser, between


class MyApi(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_api(self):
        self.client.get("/api/character/?name=rick")
"""