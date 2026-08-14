import os
import requests
from dotenv import load_dotenv

load_dotenv()

test_cases = [
    {
        "message": "i was charged twice for my last order and i need this fixed today, its really urgent",
        "expected_urgency": "high",
        "expected_department": "billing"
    },
    {
        "message":"my app crashes sometimes when I click settings, not a big deal, whenever you get a chance",
        "expected_urgency": "low",
        "expected_department": "technical"
    },
    {
        "message": "my package was supposed to arrive 3 days ago for a wedding tomorrow and tracking shows nothing, I need this resolved immediately",
        "expected_urgency": "critical",
        "expected_department": "shipping"
    }
]

response = requests.post("http://127.0.0.1:8000/classify-ticket", json={"message": test_case["message"]})
print(response.json())

if (response.json()["urgency"] == test_case["expected_urgency"] and
        response.json()["department"] == test_case["expected_department"]):
    print("pass")
else:
    print("fail")
    