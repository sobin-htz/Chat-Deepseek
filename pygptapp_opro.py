import requests
import json
import os
from dotenv import load_dotenv

#API_KEY= "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"
load_dotenv()

API_KEY = os.getenv("API_KEY") 

"""
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "deepseek/deepseek-r1-distill-llama-8b",
    "messages": [
      {
        "role": "user",
        "content": user_input
      }
    ],
    
  })
)
"""

def get_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "deepseek/deepseek-r1-distill-llama-8b",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(payload)
        )
        return response.json()["choices"][0]["message"]["content"]
        
    except Exception as e:
        return f"Error: {str(e)}"


print("Zenyx HTZ Support (Type 'exit' to quit)")
while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == 'exit':
        print("Zenyx: Goodbye!")
        break
        
    print("Zenyx: ", end='', flush=True)
    response = get_response(user_input)
    print(response)