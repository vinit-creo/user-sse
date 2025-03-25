import ollama
from claims import denial_letter


format ={
    "results": [{
        "user_first_name": "",
        "user_last_name": "",
        "user_email_address": ""
    }]    
}


def fetchUserDetails():
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
    
    
    
    

    
if __name__ =="__main__":
    fetchUserDetails()