# Ollama Cloud Chat Interface

This project provides a terminal‑based interface to interact with AI models hosted on Ollama Cloud. It fetches and displays available models, lets you select one, and then chat with it in an iterative session. Responses are rendered with Markdown formatting using the [`rich`](https://github.com/Textualize/rich) library for improved readability.

## Features
- Fetches available Ollama Cloud models dynamically
- Interactive chat loop with chosen model
- Markdown rendering in terminal via `rich`
- Easy configuration with `.env` file

## Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- An Ollama API key (Ollama offers a free tier for cloud access)
- Required Python packages: `requests`, `ollama`, `python-dotenv`, `rich`

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- An Ollama API key. Ollama has a free tier for cloud access. 
  You can generate your free API key from the Ollama website after creating your Ollama account here: https://ollama.com/settings/keys
  *Note: The script is configured to use an API Key from `.env`.*

## Setup

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2.  **Create a virtual environment** (optional):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\Activate.ps1
    # Windows (cmd.exe)
    .\venv\Scripts\activate.bat
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your Ollama API Key:
    ```
    OLLAMA_API_KEY=your_actual_api_key_here
    ```

## Usage

Run the main script:

```bash
python main.py
```

I.  The script will fetch and list all available cloud models hosted by Ollama. As of 06 January, 2026, the supported cloud models are:

1. cogito-2.1:671b
2. glm-4.6
3. glm-4.7
4. kimi-k2:1t
5. kimi-k2-thinking
6. qwen3-coder:480b
7. qwen3-next:80b
8. deepseek-v3.2
9. deepseek-v3.1:671b
10. gpt-oss:120b
11. nemotron-3-nano:30b
12. gpt-oss:20b
13. qwen3-vl:235b-instruct
14. qwen3-vl:235b
15. minimax-m2
16. minimax-m2.1
17. ministral-3:3b
18. ministral-3:8b
19. ministral-3:14b
20. mistral-large-3:675b
21. devstral-2:123b
22. devstral-small-2:24b
23. gemini-3-pro-preview
24. gemini-3-flash-preview
25. gemma3:4b
26. gemma3:12b
27. gemma3:27b
28. rnj-1:8b


II.  Enter the number corresponding to the model you want to chat with.

III. You will now be able to iteratively chat with the model you chose. The LLM responses will be rendered in Markdown format.

IV. Type `exit` to end the session at any time.

## Monitoring your cloud usage

You can keep track of your Ollama cloud usage by logging into your Ollama account and checking it here: https://ollama.com/settings

## Disclaimer
This project uses Ollama Cloud API. The user is responsible for monitoring their own usage and costs.
The author is not liable for any charges incurred from exceeding free tier limits or other usage policies.



