# AI Chatbot Assistant

A Python-based AI chatbot application powered by multiple LLM providers (OpenAI, Anthropic, Google Gemini, and Hugging Face) using the LangChain framework.

## Overview

This project provides an interactive conversational AI assistant that maintains conversation history and context. It's built with flexibility in mind, supporting multiple AI models and providers, making it easy to switch between different LLM backends.

## Features

- **Multi-Model Support**: Seamlessly integrate with multiple AI providers:
  - OpenAI (GPT models)
  - Anthropic (Claude)
  - Google Generative AI (Gemini)
  - Hugging Face transformers

- **Conversation History**: Maintains full conversation context for coherent multi-turn interactions
- **LangChain Integration**: Leverages LangChain framework for robust LLM orchestration
- **Environment Configuration**: Uses `.env` files for secure API key management
- **Interactive CLI**: User-friendly command-line interface for chatting with the AI

## Project Structure

```
.
├── main.py                 # Entry point for the application
├── pyproject.toml         # Project metadata and dependencies
├── requiremets.txt        # Direct dependency list
├── README.md              # This file
└── src/
    └── openai/
        ├── __init__.py    # Package initialization and exports
        ├── openai.py      # Core ChatOpenAI assistant logic
        └── const.py       # Configuration constants
```

## Dependencies

### Core LLM & Framework
- `langchain` - LLM orchestration framework
- `langchain-core` - Core LangChain abstractions
- `langchain-openai` - OpenAI integration
- `langchain-anthropic` - Anthropic integration
- `langchain-google-genai` - Google Gemini integration
- `langchain-huggingface` - Hugging Face integration

### AI Models & APIs
- `openai` - OpenAI API client
- `google-generativeai` - Google's generative AI SDK
- `transformers` - Hugging Face transformers
- `huggingface-hub` - Hugging Face model hub

### Utilities
- `python-dotenv` - Environment variable management
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning utilities

## Installation

### Prerequisites
- Python >= 3.14
- Virtual environment (recommended)
- Package manager: `uv` (recommended) or `pip`

### Package Manager: uv

**Why uv?**
- ⚡ Extremely fast - written in Rust
- 🔒 Deterministic dependency resolution
- 🎯 Simpler syntax and better performance than pip
- 📦 Built-in virtual environment management

**Install uv:**
```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows (with PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using Homebrew (macOS)
brew install uv
```

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd /Users/digvijay/WorkSpace/Python
   ```

2. **Create a virtual environment**

   **Using uv (recommended):**
   ```bash
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

   **Or using Python:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**

   **Using uv (recommended):**
   ```bash
   uv pip install -r requiremets.txt
   ```
   Or using `pyproject.toml`:
   ```bash
   uv pip install -e .
   ```

   **Or using pip:**
   ```bash
   pip install -r requiremets.txt
   ```
   Or using `pyproject.toml`:
   ```bash
   pip install -e .
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_key_here
   ANTHROPIC_API_KEY=your_anthropic_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   HUGGINGFACE_API_KEY=your_huggingface_key_here
   ```

## Usage

### Running the Chatbot

```bash
python main.py
```

The application will start an interactive chat session:
```
Human: What is Python?
AI: Python is a high-level, interpreted programming language...
Human: Tell me more
AI: Python was created by Guido van Rossum in 1991...
Human: exit
```

### How It Works

1. **Initialization**: The app loads environment variables and initializes the ChatOpenAI model
2. **Conversation Loop**: 
   - Accepts user input
   - Maintains conversation history with `SystemMessage`, `HumanMessage`, and `AIMessage` objects
   - Sends context-aware queries to the LLM
   - Displays AI responses
3. **Exit**: Type `exit` to end the conversation

## Configuration

### Changing the AI Model

Edit `src/openai/const.py` to switch models:

```python
CHAT_OPEN_AI_MODEL = 'gpt-4'  # or 'gpt-3.5-turbo', etc.
```

### System Prompt Customization

Modify the `SystemMessage` in `src/openai/openai.py`:

```python
chat_history: list[SystemMessage | HumanMessage | AIMessage] = [
    SystemMessage(content='you are a helpful assistant.')
]
```

## API Keys Required

Depending on which provider you use, you'll need API keys from:

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/
- **Google**: https://makersuite.google.com/app/apikey
- **Hugging Face**: https://huggingface.co/settings/tokens

## Architecture

### Main Components

**`ChatOpenAIAssistace(model: str)`**
- Core function that creates an interactive chat interface
- Maintains conversation history for context-aware responses
- Handles multi-turn conversations seamlessly
- Returns conversation history for logging/analysis

**`CHAT_OPEN_AI_MODEL`**
- Configuration constant specifying the LLM model to use
- Easily customizable for different model versions

## Future Enhancements

- [ ] Add conversation logging and persistence
- [ ] Implement message streaming for real-time responses
- [ ] Add support for system-wide configuration files
- [ ] Create web interface (FastAPI/Flask)
- [ ] Add RAG (Retrieval Augmented Generation) capabilities
- [ ] Implement conversation branching and memory management
- [ ] Add multi-language support

## Troubleshooting

### API Key Issues
- Ensure `.env` file is in the project root
- Verify API keys are valid and have appropriate permissions
- Check that environment variables are loaded: `python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('OPENAI_API_KEY'))"`

### Import Errors
- Confirm all dependencies are installed:
  - With uv: `uv pip install -r requiremets.txt`
  - With pip: `pip install -r requiremets.txt`
- Check Python version is >= 3.14

### Connection Issues
- Verify internet connection
- Check API rate limits on provider dashboards
- Ensure firewall allows outbound connections

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Package Manager: uv Commands Reference

### Common uv Commands

```bash
# Create a virtual environment
uv venv

# Install dependencies from requirements.txt
uv pip install -r requiremets.txt

# Install a specific package
uv pip install package_name

# Install in development mode
uv pip install -e .

# Update dependencies
uv pip install --upgrade package_name

# Compile requirements from pyproject.toml
uv pip compile pyproject.toml -o requirements.txt

# Sync environment with requirements
uv pip sync requirements.txt

# Show installed packages
uv pip list

# Remove a package
uv pip uninstall package_name
```

## Notes

- Conversation history is kept in memory during runtime
- Currently uses `gpt-5.4-mini` model (ensure this model exists in your OpenAI account)
- The application is interactive and runs in the terminal
- **Recommended**: Use `uv` package manager for faster dependency resolution and better performance
