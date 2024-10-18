from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

# Define the prompt
with open('prompt.txt', 'r') as f:
    prompt = f.read()

# Define the context
with open('context.txt', 'r') as f:
    context = f.read()

# Define the context and prompt for the AI
messages = [
    {"role": "system", "content": f"{context}"}, #Context
    {"role": "user", "content": f"{prompt}"} #Prompt
]

# Generate the response
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Or gpt-4
    messages=messages,
    max_tokens=5
)

print(response.choices[0].message['content'].strip())

