# 🧠 AI Chatbot using IBM WatsonX

## 📌 About the Project

This is an AI-powered chatbot web application that lets users have human-like conversations using IBM WatsonX's Granite large language model (LLM). It features a modern React frontend and a Python Flask backend. 

Key highlights:
- Automatically fetches and refreshes IAM token for authentication.
- Maintains conversational context with the WatsonX model.
- Built with a clean and responsive user interface.
- Designed to be deployed locally or extended for production use.

Ideal for:
- Developers exploring IBM WatsonX
- Students and professionals building custom LLM-powered apps
- Organizations prototyping domain-specific assistants

---

## 📁 Project Structure

chat_bot/
├── backend/ # Python Flask backend
│ ├── app.py
│ └── .env
├── frontend/ # React frontend
│ ├── src/
│ ├── public/
│ └── .env
├── .gitignore
└── README.md



---

## ⚙️ Tech Stack

- **Frontend**: React, TailwindCSS
- **Backend**: Python, Flask
- **AI Model**: IBM WatsonX (Granite)
- **Auth**: IBM IAM Token
- **CORS Handling**: flask-cors

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/chatbot-ui-watsonx.git
cd chatbot-ui-watsonx


🖥️ Backend Setup (Flask + IBM WatsonX)
1. Create a virtual environment
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install Python dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create .env file
Inside backend/.env:

env
Copy
Edit
API_KEY=your_ibm_api_key_here
PROJECT_ID=your_ibm_project_id_here
WATSONX_MODEL_ID=ibm/granite-3-8b-instruct
💡 Use your actual WatsonX API key and project ID.

4. Run the backend server
bash
Copy
Edit
python app.py
API will be live at: http://localhost:5000/api/chat

Frontend Setup (React)
1. Move to frontend folder
bash
Copy
Edit
cd ../frontend
2. Install frontend dependencies
bash
Copy
Edit
npm install
3. Create a .env file
Inside frontend/.env:

env
Copy
Edit
REACT_APP_BACKEND_URL=http://localhost:5000/api
4. Start the frontend server
bash
Copy
Edit
npm start
App will be running at: http://localhost:3000

💬 Features
✅ Chat interface with clean UI

✅ Connects to IBM WatsonX Granite model

✅ Supports context-based chat

✅ Secure IAM token-based authentication

✅ Handles CORS and API errors gracefully

🛠️ Troubleshooting
CORS Errors: Ensure flask-cors is installed and enabled.

401 Errors: Check .env file for a valid IBM API key and project ID.

404 Errors: Ensure the backend is running and /api/chat is defined.

No Response: Confirm backend successfully fetches IAM token and WatsonX response.

📄 License
This project is open-source under the MIT License.

🙋‍♀️ Contributing
Open to feedback, issues, and pull requests!

🧠 Powered by
IBM WatsonX

React.js

Python Flask

yaml
Copy
Edit

---

Let me know if you'd like:
- A `requirements.txt` file
- GitHub repo setup (e.g., `.gitignore`)
- Instructions for deploying on Render/Heroku/Vercel

Want me to generate those too?