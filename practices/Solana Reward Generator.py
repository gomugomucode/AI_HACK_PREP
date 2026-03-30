import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()

# 1. Initialize the client (Crucial!)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Levelupmessage(BaseModel):
    action: str
    token_name: str 
    amount_rewarded: int # Changed to int for math
    funny_message: str 

# Get user input
user_action = input("What did you do today? (e.g., Bought a coffee, Coded for 5 hours): ")

try:
    # 2. The AI Call
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        # We pass the user_action here so the AI knows what happened
        contents=f"The user did this: {user_action}. Reward them!",
        config={
            "response_mime_type": "application/json",
            "response_schema": Levelupmessage,
            "system_instruction": (
                "You are a cheerful RPG Game Master. "
                "Based on the user's action, decide a funny reward. "
                "Tokens should be 'SOL-Points'. "
                "Amount should be between 1 and 100 based on effort."
            )
        }
    )

    # 3. Accessing the data
    reward = response.parsed
    print(f"\n✨ {reward.funny_message}")
    print(f"💰 You earned: {reward.amount_rewarded} {reward.token_name}!")

except Exception as e:
    print(f"Error: {e}")