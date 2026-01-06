import os
import requests
from ollama import Client
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown

# Initialize rich console
console = Console()

# Load environment variables
load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")

# Step 1: Fetch models from Cloud API
url = "https://ollama.com/api/tags"
headers = {"Authorization": f"Bearer {api_key}"}
resp = requests.get(url, headers=headers)
models = resp.json().get("models", [])

print("\n=== Available Models on Ollama Cloud ===\n")
for i, m in enumerate(models, 1):
    print(f"{i}. {m.get('name') or m.get('tag')}")

choice = int(input("\nChoose a model number: "))
selected_model = models[choice-1].get("name") or models[choice-1].get("tag")

# Step 2: Chat with chosen model using ollama client
client = Client(host="https://ollama.com", headers={"Authorization": f"Bearer {api_key}"})
print(f"\nYou are now chatting with {selected_model} in Ollama Cloud.\nType 'Exit' to quit.\n")

while True:
    user_input = input("\nYou> ")
    if user_input.lower() == "exit":
        print("\n *** Ending chat session. Goodbye! ***\n")
        break

    messages = [{"role": "user", "content": user_input}]

    # Buffer the streamed response
    response_text = ""
    for part in client.chat(selected_model, messages=messages, stream=True):
        response_text += part["message"]["content"]

    # Render the full Markdown response once
    print(f"\n{selected_model}>")
    md = Markdown(response_text)
    console.print(md)