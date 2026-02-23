import requests
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from calculator_client.client import Client
from calculator_client.models.calculation import Calculation
from calculator_client.api.actions import calculate
from calculator_client.models.opertions import Opertions

def test_api_calculate_manual():
    url = "http://localhost:5001/calculate"
    payload = {"operation": "add", "operand1": 10, "operand2": 5}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json()['result'] == 15.0

def test_api_calculate_with_client():
    client = Client(base_url="http://localhost:5001")
    calc_data = Calculation(operation=Opertions.ADD, operand1=20.0, operand2=20.0)
    response = calculate.sync(client=client, body=calc_data)
    assert response.result == 40.0