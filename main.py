# import os
# from dotenv import load_dotenv
# from google import genai  # <--- Make sure it is exactly this

# # Load your .env file
# load_dotenv()

# # Initialize the client
# # It will automatically find GEMINI_API_KEY from your .env
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# try:
#     # Generate the response
#     response = client.models.generate_content(
#         model="gemini-2.5-flash", 
#         contents="Explain Blockchain like I am 5 years old."
#     )

#     print(response.text)

# except Exception as e:
#     print(f"Error: {e}")



import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel # New tool for "Schema"

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. DEFINE THE SHAPE: We tell Python what the "Perfect Answer" looks like
class TransactionSummary(BaseModel):
    action: str
    amount: float
    token: str
    human_explanation: str
    risk_level: str # e.g., "Safe", "Medium", "High"

try:
    # 2. THE PROMPT: We give it a "messy" raw transaction string
    raw_tx = "Transfer 12.5 SOL to 7xV... for 'Hackathon Registration Fee'"

    response = client.models.generate_content(
        model="gemini-2.0-flash", # Use 2.0 Flash for best JSON support
        contents=f"Analyze this Solana transaction: {raw_tx}",
        config={
            "response_mime_type": "application/json",
            "response_schema": TransactionSummary, # This is the magic part!
            "system_instruction": "You are a Solana Security Expert. Analyze transactions and return JSON only."
        }
    )

    # 3. USE THE DATA: Now it's a Python Object, not just text!
    data = response.parsed
    print(f"Action: {data.action}")
    print(f"Explanation: {data.human_explanation}")
    print(f"Risk: {data.risk_level}")

except Exception as e:
    print(f"Error: {e}")