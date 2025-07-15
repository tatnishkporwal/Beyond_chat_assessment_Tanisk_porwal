import praw
import argparse
import os
import requests
import json

# ---- YOUR API KEYS ----
CLIENT_ID = "aGEoVAoOyH1Hw00kcwGeUA"
CLIENT_SECRET = "-VVPk5X5XC_XX5W_24Kx05JMnKBldA"
USER_AGENT = "script:reddit-persona:v1.0 (by /u/Formal-Statement3695)"
GEMINI_API_KEY = "AIzaSyDKFIYU3KZmlfg7BqsKAnC5oIbBSIjezY4"
# ---------------------


def extract_username(url):
    return url.strip("/").split("/")[-1]


def fetch_user_data(username):
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    user = reddit.redditor(username)

    posts = []
    comments = []

    for submission in user.submissions.new(limit=10):
        posts.append({
            'title': submission.title,
            'selftext': submission.selftext,
            'url': submission.url
        })

    for comment in user.comments.new(limit=20):
        comments.append({
            'body': comment.body,
            'permalink': comment.permalink
        })

    return posts, comments


def ask_gemini_for_persona(all_text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }

    prompt = f"""Analyze the following Reddit user's posts and comments. Write a detailed persona including:
- Interests and Hobbies
- Personality Traits
- Writing Style (formal/informal/sarcastic etc.)
- Online Behavior
- Preferred Communities/Subreddits
Also cite examples where possible.\n\n{all_text}"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()

    try:
        return response_json["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("❌ Error from Gemini API:", response_json)
        return "Failed to generate persona due to API error."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=True, help="Reddit Profile URL")
    args = parser.parse_args()

    username = extract_username(args.url)
    posts, comments = fetch_user_data(username)

    all_text = "\n\n--- POSTS ---\n"
    for p in posts:
        all_text += f"\nTitle: {p['title']}\nText: {p['selftext']}\nURL: {p['url']}\n"

    all_text += "\n\n--- COMMENTS ---\n"
    for c in comments:
        all_text += f"\nComment: {c['body']} (https://reddit.com{c['permalink']})\n"

    persona = ask_gemini_for_persona(all_text)

    os.makedirs("output", exist_ok=True)
    output_file = f"output/{username}_persona.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Gemini AI Persona file generated: {output_file}")
