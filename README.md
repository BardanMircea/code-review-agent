# code-review-agent

AI Code Review Agent Project:
A local or prompt-based AI agent that can analyze Python code, detect potential issues, suggest improvements, and act like a code reviewer.

Project Overview
Python-based agent that can:
Accept code files or code snippets
Analyze for bugs, clarity, readability, and standards
Suggest improvements using prompt templates
Generate a review summary in Markdown or terminal output

Will use GenAI tools:
LLM APIs: like OpenAI or Claude (via key-based config)
Local Ollama Models: using models like mistral, phi, etc.

Core Design Principles:
Dual Mode Interface
CLI flag or config setting: --provider openai, --provider ollama, --provider anthropic
Abstracted prompt runner in a llm_interface.py module

Feature:
🔍 Review Targets
Input: one or more Python files
Output: markdown summary of:
Bugs
Style issues
Missing tests
Clarity suggestions

💬 Prompt profiles:
strict
mentor
test_focus

Example CLI Usage:
python cli.py --file examples/buggy_script.py --mode strict --provider ollama
python cli.py --file examples/clean_script.py --mode mentor --provider openai
