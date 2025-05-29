from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
API_KEY = os.getenv("IBM_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
MODEL_ID = os.getenv("MODEL_ID")

# In-memory store for session messages (for demo only)
user_context = {}

# ✅ Function to get access token using IBM API key
def get_ibm_access_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = f"apikey={api_key}&grant_type=urn:ibm:params:oauth:grant-type:apikey"

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        print("✅ Token fetched successfully")
        return access_token
    else:
        print("❌ Failed to fetch token:", response.text)
        return None

# ✅ Fetch token at startup
ACCESS_TOKEN = get_ibm_access_token(API_KEY)

# Flask setup
app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_id = "default_user"  # You can extend this to real sessions
    user_message = data.get("message", "")

    if user_id not in user_context:
        user_context[user_id] = [
            {
                "role": "system",
                "content": "You are an agriculture expert. Be brief."
            }
        ]

    # Add user message to context
    user_context[user_id].append({
        "role": "user",
        "content": [{"type": "text", "text": user_message}]
    })

    # Prepare messages for WatsonX API (flatten user messages)
    messages_for_api = []
    for entry in user_context[user_id]:
        if entry["role"] == "user":
            messages_for_api.append({
                "role": "user",
                "content": entry["content"]
            })
        else:
            messages_for_api.append({
                "role": entry["role"],
                "content": entry["content"]
            })

    # Send to WatsonX
    response = requests.post(
        "https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-05-29",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "messages": messages_for_api,
            "project_id": os.getenv("PROJECT_ID"),
            "model_id": os.getenv("MODEL_ID"),
            "temperature": 0,
            "top_p": 1
        }
    )

    response_json = response.json()

    # Extract assistant response
    choices = response_json.get("choices")
    if choices and isinstance(choices, list):
        assistant_message = choices[0].get("message", {}).get("content", "No valid response from WatsonX")
    else:
        assistant_message = "No valid response from WatsonX"

    # Append assistant message to context
    user_context[user_id].append({
        "role": "assistant",
        "content": assistant_message
    })

    return jsonify({"response": assistant_message})
if __name__ == '__main__':
    app.run(debug=True)
