from locust import HttpUser, task, between


class EmployeeUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_employees(self):
        self.client.get("/")