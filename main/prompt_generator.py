import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Check if the API key is loaded correctly
if not client.api_key:
    print("Error: OPENAI_API_KEY not found in environment variables.")
    exit(1)

# Read the prompt from a file
with open('prompt.txt', 'r') as f:
    prompt = f.read().strip()  # Using strip() to remove any leading/trailing whitespace
    # print(f"Prompt: {prompt}")

# Read the context from a file
with open('context.txt', 'r') as f:
    context = f.read().strip()  # Using strip() to remove any leading/trailing whitespace
    # print(f"Context: {context}")

# Define the messages for the AI conversation
messages = [
    {"role": "system", "content": context},  # Context
    {"role": "user", "content": prompt}      # Prompt
]

try:
    # Generate the response using the new client
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",  # Or "gpt-4"
        max_tokens=200,         # Adjust this value as needed
    )

    # Print the assistant's response
    assistant_response = chat_completion.choices[0].message.content.strip()
    print(f"Response: {assistant_response}")

    # Write the response to a file
    with open('response.txt', 'w') as f:
        if f is not None:
            if f.tell() != 0:
                f.seek(0)
                f.truncate(0)
        f.write(assistant_response)

except Exception as e:
    print(f"An error occurred: {e}")
