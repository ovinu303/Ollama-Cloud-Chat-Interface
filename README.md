# Ollama Cloud Interaction Script

This project allows you to interact with Ollama models hosted on the cloud. It fetches the available models and provides a chat interface in the terminal using the `rich` library for nice formatting.

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- An Ollama API Key (if required by your cloud provider setup, or if simply using local Ollama, ensure it is running). *Note: The script is configured to use an API Key from `.env`.*

## Setup

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
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

1.  The script will fetch and list available models.
2.  Enter the number corresponding to the model you want to chat with.
3.  Type your messages in the prompt.
4.  Type `exit` to end the session.
