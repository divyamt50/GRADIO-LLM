# Gradio LLM

A simple and lightweight **Gradio** application for interacting with Large Language Models (LLMs). This project provides a clean starting point for building AI-powered chat interfaces with Python.

## Features

- 🚀 Simple Gradio interface
- 🤖 LLM-powered chat
- 🐍 Modern Python project structure
- 📦 Dependency management with `uv`
- ⚙️ Easy to extend and customize

## Project Structure

```text
.
├── .gradio/
├── .gitignore
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Prerequisites

- Python 3.11+ (or the version specified in `.python-version`)
- `uv` installed

Install `uv` if you don't already have it:

```bash
pip install uv
```

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/gradio-llm.git
cd gradio-llm
```

Install dependencies:

```bash
uv sync
```

## Running the Application

Start the Gradio app:

```bash
uv run python main.py
```

Once running, open the local URL displayed in your terminal (typically `http://127.0.0.1:7860`).

## Configuration

Configure your LLM provider or API credentials as required by your application before launching.

## Development

Run the application during development:

```bash
uv run python main.py
```

Update dependencies:

```bash
uv add <package-name>
```

Remove a dependency:

```bash
uv remove <package-name>
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
