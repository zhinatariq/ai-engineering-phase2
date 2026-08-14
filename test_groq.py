import os
import requests
from dotenv import load_dotenv

load_dotenv()

test_case = {
    "message": "i was charged twice for my last order and i need this fixed today, its really urgent",
    "expected_urgency": "high",
    "expected_department": "billing"
}

response = requests.post("http://127.0.0.1:8000/classify-ticket", json={"message": test_case["message"]})
print(response.json())

if (response.json()["urgency"] == test_case["expected_urgency"] and
        response.json()["department"] == test_case["expected_department"]):
    print("pass")
else:
    print("fail")
    