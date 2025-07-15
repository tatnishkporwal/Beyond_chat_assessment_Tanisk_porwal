# 🚀 Reddit User Persona Generator  
### Internship Assessment - BeyondChats (AI/LLM Engineer Intern)

---

## 📄 Project Overview  
This project is a Python-based tool that extracts data from a Reddit user's public profile (posts and comments) and generates a **user persona** using **Google Gemini AI (via API)**.  
The persona includes inferred details like interests, personality traits, writing style, and community involvement.

---

## 🛠️ Tech Stack
- **Python 3.11+**
- `praw` (Reddit API Wrapper)
- `requests` (For Google Gemini API)
- **Google Gemini 2.0 Flash API (Generative Language Model)**

---

## 🎯 How It Works
- Takes a Reddit user profile link as input.
- Fetches recent posts and comments via Reddit API.
- Sends this data to Google Gemini LLM API.
- Outputs a detailed user persona as a `.txt` file.

---

## 📂 Project Structure
project/
│
├── main.py # Main executable script
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── output/ # Contains generated persona files
├── kojied_persona.txt
└── Hungry-Move-6603_persona.txt

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repository-link>
cd project/
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔑 API Keys Required
✅ Reddit API Credentials (praw)
client_id

client_secret

user_agent

✅ Google Gemini API Key
You can get a Google Generative Language API key from:
https://makersuite.google.com/app/apikey

Insert your API keys into main.py:

python
Copy
Edit
CLIENT_ID = "your-reddit-client-id"
CLIENT_SECRET = "your-reddit-client-secret"
USER_AGENT = "your-user-agent"
GEMINI_API_KEY = "your-gemini-api-key"
🚀 How to Run the Script
Example Usage:
bash
Copy
Edit
python main.py --url https://www.reddit.com/user/kojied/
bash
Copy
Edit
python main.py --url https://www.reddit.com/user/Hungry-Move-6603/
📄 Output
The generated persona files will be saved in the /output/ directory. Example:

lua
Copy
Edit
output/kojied_persona.txt
output/Hungry-Move-6603_persona.txt
📝 Example Reddit Profiles for Testing
Provided in the official assignment PDF:

ruby
Copy
Edit
https://www.reddit.com/user/kojied/
https://www.reddit.com/user/Hungry-Move-6603/
📌 Notes
Script follows PEP-8 coding guidelines.

Outputs are purely for educational and evaluation purposes.

Google Gemini LLM is used via REST API for persona generation.

🙋 Author
Tanishk Porwal
Submission for BeyondChats AI/LLM Engineer Internship Assessment.

yaml
Copy
Edit
