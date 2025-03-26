import ollama
from claims import denial_letter
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests

format ={
    "results": [{
        "user_first_name": "",
        "user_last_name": "",
        "user_email_address": ""
    }]    
}

class Itemexample(BaseModel):
    name: str
    prompt: str
    instruction: str
    is_offer: Union[bool, None] = None

def fetchUserDetails():
    
    Item()
    response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Fetch the following data from the document here {denial_letter}. Fetch and populate the details in json format {format}. Give me response only in json and nothing else.",
        },
    ],
)
    print(response["message"]["content"])
    
    
    
    
app = FastAPI(debug=True)



class Item(BaseModel):
    model: str
    prompt: str

urls =["http://localhost:11434/api/generate"]

headers = {
    "Content-Type": "application/json"
}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat/{llms_name}")
def update_item(llms_name: str, item: Item):
    if llms_name == "llama3.2":
        url = urls[0]
        payload = {
            "model": "llama3.2",
            "prompt": "Why is the sky blue?",
            "stream": False
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return {"data": response.text, "llms_name": llms_name}
        else:
            print("error:", response.status_code, response.text)
            return {"item_name": item.model, "error": response.status_code, "data": response.text}
    return {"item_name": item.model, "llms_name": llms_name}
    

    
if __name__ =="__main__":
    fetchUserDetails()