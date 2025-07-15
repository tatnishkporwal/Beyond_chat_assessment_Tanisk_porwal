
# Reddit User Persona Generator  
### Internship Assessment – BeyondChats (AI/LLM Engineer Intern)

---

## 📄 Project Overview  
This project is a Python-based tool that extracts data from a Reddit user's public profile (posts and comments) and generates a detailed **user persona** using **Google Gemini AI (via API)**.  
The generated persona includes inferred interests, personality traits, writing style, and community involvement.

---

## 🛠️ Tech Stack
- Python 3.11+
- `praw` (Reddit API Wrapper)
- `requests` (Google Gemini API Integration)
- Google Gemini 2.0 Flash API (Generative Language Model)

---

## 📂 Project Structure
```
project/
│
├── main.py                # Main executable script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── output/                 # Contains generated persona files
    ├── kojied_persona.txt
    └── Hungry-Move-6603_persona.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repository-link>
cd project/
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 API Keys Required

### Reddit API Credentials (praw)
You need to create a Reddit app and obtain:
- `client_id`
- `client_secret`
- `user_agent`

### Google Gemini API Key
Get your API key from:  
https://makersuite.google.com/app/apikey  

---

### 🔧 Insert API Keys in `main.py`:
```python
CLIENT_ID = "your-reddit-client-id"
CLIENT_SECRET = "your-reddit-client-secret"
USER_AGENT = "your-user-agent"
GEMINI_API_KEY = "your-gemini-api-key"
```

---

## 🚀 How to Run the Script

### Example Commands:
```bash
python main.py --url https://www.reddit.com/user/kojied/
python main.py --url https://www.reddit.com/user/Hungry-Move-6603/
```

---

## 📄 Output
Output persona files will be saved in the `/output/` directory:
```
output/kojied_persona.txt
output/Hungry-Move-6603_persona.txt
```

---

## 📝 Example Reddit Profiles for Testing
These profiles were provided in the official assignment PDF:
```
https://www.reddit.com/user/kojied/
https://www.reddit.com/user/Hungry-Move-6603/
```

---

## 📌 Notes
- Script follows **PEP-8** coding guidelines.
- Outputs are for educational and evaluation purposes only.
- Persona generation is powered by **Google Gemini LLM API** via REST.

---

## 🙋 Author
**Tanishk Porwal**  
Submission for BeyondChats AI/LLM Engineer Internship Assessment.
