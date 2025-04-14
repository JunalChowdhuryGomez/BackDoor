from locust import HttpUser, task

class TriviaUser(HttpUser):
    @task
    def play_trivia(self):
        self.client.get("/")
