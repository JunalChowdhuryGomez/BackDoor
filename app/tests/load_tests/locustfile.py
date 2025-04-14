from locust import HttpUser, task

class TriviaUser(HttpUser):
    @task
    def play_trivia(self):
        self.client.get("/")

    @task
    def start_game(self):
        self.client.post("/", data={"difficulty": "1"})
