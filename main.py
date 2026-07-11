from pydantic import BaseModel
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app=FastAPI()

class TicketRequest(BaseModel):
    message:str
    
@app.post("/classify-ticket")
def create_ticket_request(ticket_request: TicketRequest):
    
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
   messages=[
    {"role": "system", "content": "Classify the urgency of this support ticket. Respond with exactly one word: low, medium, high, or critical.respond in lowercase only. No explanation"},
    {"role": "user", "content": ticket_request.message}

],
   temperature=0
)

    return {"urgency": response.choices[0].message.content.strip().lower()}
