# Ollama Cloud Chat Interface

This project provides a terminal-based chat interface for models hosted through the Ollama Cloud API. It fetches the available models from Ollama, lets you choose one, and then starts an interactive conversation session. Responses are rendered in the terminal using Markdown formatting via the Rich library.

## Features
- Fetches available Ollama Cloud models dynamically from the API
- Lets you select a model from the list and start chatting immediately
- Displays assistant responses with Markdown formatting in the terminal
- Uses a local `.env` file for your API key configuration
- Handles unavailable or subscription-restricted models gracefully

## Prerequisites
- Python 3.8 or newer
- pip
- An Ollama API key from your Ollama account
- Internet access to reach the Ollama API endpoint

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Ollama-Cloud-Chat-Interface
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv

   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1

   # Windows (cmd.exe)
   .\.venv\Scripts\activate.bat

   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API key:
   ```env
   OLLAMA_API_KEY=your_actual_api_key_here
   ```

## Usage

Run the application:

```bash
python main.py
```

When the script starts, it will:
1. Load your API key from `.env`
2. Fetch and print the list of available Ollama Cloud models
3. Prompt you to choose a model number
4. Start a chat loop with the selected model

To end the chat session at any time, type:
```text
exit
```

## Notes
- The list of available models is fetched dynamically, so it may change over time.
- If a selected model is unavailable or requires a different access level, the app will notify you and return to the model selection step.
- Usage and billing are managed by your Ollama account and access plan.

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for the full text.

