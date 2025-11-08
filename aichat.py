import os
import requests
import sys
from dotenv import load_dotenv
def chat(content):
    BASE_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "messages": [
            {
                "role": "user",
                "content": content + " in less than 50 words"
            }
        ],
        "model": "openai/gpt-oss-safeguard-20b:groq"
    }
    
    print("Fetching response...")
    
    try:
        response = requests.post(BASE_URL, headers=headers, json=data)

        # --- THIS IS THE FIX ---
        # Check for failure FIRST and RETURN immediately
        if response.status_code != 200:
            print(f"Error fetching data. Status code: {response.status_code}")
            # Return a friendly error message for the assistant to speak
            return "I'm sorry, I had an error connecting to my brain."

        # If we get here, the status WAS 200 (success)
        response_data = response.json()
        
        # Check if the expected keys exist before trying to access them
        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"]
        else:
            print("Error: API response format is unexpected.")
            print(f"Received data: {response_data}")
            return "I'm sorry, I received a response I couldn't understand."
            
    except requests.exceptions.RequestException as e:
        # Handle network errors (e.g., no internet)
        print(f"Network error: {e}")
        return "I'm sorry, I couldn't reach my servers. Please check your internet."
    
    except Exception as e:
        # Catch any other unexpected error (like a JSON problem)
        print(f"An unexpected error occurred: {e}")
        return "I'm sorry, an unknown error occurred."
# --- 1. Security & Configuration ---
load_dotenv()
API_KEY = os.environ.get("HF_API_KEY")

if API_KEY is None:
    print("FATAL ERROR: The HF_API_KEY was not found. Please check your .env file.")
    sys.exit(1)

if __name__ == "__main__":
    content=""
    while content.lower() != "exit":
        content=input("Enter your prompt:")
        if content.lower() == "exit":
            break
        print(chat(content))



