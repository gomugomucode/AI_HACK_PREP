import os
from dotenv import load_dotenv
from google import genai  # <--- Make sure it is exactly this

# Load your .env file
load_dotenv()

# Initialize the client
# It will automatically find GEMINI_API_KEY from your .env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

try:
    # Generate the response
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents="Explain Blockchain like I am 5 years old."
    )

    print(response.text)

except Exception as e:
    print(f"Error: {e}")