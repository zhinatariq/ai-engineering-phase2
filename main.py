from pydantic import BaseModel
from fastapi import FastAPI

app=FastAPI()

class TicketRequest(BaseModel):
    message:str
    
@app.post("/classify-ticket")
def create_ticket_request(ticket_request: TicketRequest):
    return ticket_request
