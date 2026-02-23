import json
from locust import HttpUser, task, between

class CalculatorUser(HttpUser):
    wait_time = between(2, 4)

    @task(2) 
    def add(self):
        payload = {"operation": "add", "operand1": 1, "operand2": 1}
        with self.client.post("/calculate", catch_response=True, name='add', json=payload) as response:
            try:
                response_data = json.loads(response.text)
                if response_data.get('result') != 2:
                    response.failure(f"Expected 2 but got {response_data.get('result')}")
            except json.JSONDecodeError:
                response.failure("Failed to decode response JSON")

    @task(1)
    def subtract(self):
        payload = {"operation": "subtract", "operand1": 10, "operand2": 5}
        self.client.post("/calculate", name='subtract', json=payload)

    @task(1)
    def multiply(self):
        payload = {"operation": "multiply", "operand1": 10, "operand2": 5}
        self.client.post("/calculate", name='multiply', json=payload)

    @task(1)
    def divide(self):
        payload = {"operation": "divide", "operand1": 10, "operand2": 5}
        self.client.post("/calculate", name='divide', json=payload)