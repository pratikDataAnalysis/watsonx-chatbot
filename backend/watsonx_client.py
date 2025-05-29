import os
import requests
from dotenv import load_dotenv

load_dotenv()

WATSONX_API_URL = "https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-05-29"
BEARER_TOKEN = os.getenv("WATSONX_BEARER_TOKEN")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
MODEL_ID = "ibm/granite-3-8b-instruct"  # You can change this if needed

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

def query_watsonx(user_input: str) -> str:
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "You are Agriculture expert, answer very briefly (10 words max)"
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input
                    }
                ]
            }
        ],
        "project_id": PROJECT_ID,
        "model_id": MODEL_ID,
        "frequency_penalty": 0,
        "max_tokens": 2000,
        "presence_penalty": 0,
        "temperature": 0,
        "top_p": 1,
        "seed": None,
        "stop": []
    }

    response = requests.post(WATSONX_API_URL, headers=HEADERS, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Watsonx API error: {response.text}")
    
    result = response.json()
    return result["results"][0]["generated_text"]
