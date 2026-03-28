# Gemini AI Hackathon Starter 🚀

A lightweight, quick-start Python template for connecting to the modern Google Gemini API using the `google-genai` SDK. This project securely loads API keys using environment variables and generates text responses.

## 🌟 What it does
Currently, this script connects to the `gemini-2.5-flash` model and prompts it to "Explain Blockchain like I am 5 years old." It serves as a foundational building block to add more complex AI features to your hackathon project.

## 🛠️ Prerequisites
Before you begin, ensure you have:
* Python 3.9+ installed
* A free Gemini API key from [Google AI Studio](https://aistudio.google.com/)

## 📦 Setup & Installation

**1. Clone the repository (if applicable)**
```bash
git clone <your-repo-url>
cd ai_hack_prep
```

***2. Create and activate a virtual environment)**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

```


***3. Install the required libraries**
```bash
pip install google-genai python-dotenv

```

***4. Set up your environment variables**

Create a .env file in the root directory of your project. Do not commit this file to GitHub!
```bash
GEMINI_API_KEY=your_actual_api_key_here

```

🚀 Usage

Run the main script to see the AI in action:

```bash
python main.py

```

📂 File Structure

    main.py: The core script that initializes the Gemini client and sends the prompt.

    .env: (Local only) Stores your secret API key.

    .gitignore: Ensures secrets and local environments are not pushed to version control.

    README.md: You are reading it!

    ```
Built with aai

