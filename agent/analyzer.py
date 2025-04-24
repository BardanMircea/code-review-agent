import os
from agent.llm_interface import LLMClient
import yaml

class CodeAnalyzer:
    def __init__(self, provider, mode):
        self.provider = provider
        self.mode = mode
        self.llm_client = LLMClient(provider)

        # Load prompt templates
        with open("prompts/templates.yaml", "r") as file:
            self.prompts = yaml.safe_load(file)

    def analyze_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r") as file:
            code = file.read()

        # Generate the prompt based on the mode
        prompt_template = self.prompts.get(self.mode, "")
        prompt = prompt_template.format(code=code)

        # Get the analysis from the LLM
        analysis = self.llm_client.run(prompt)

        # Format the result as Markdown
        result = f"# Code Review for {file_path}\n\n{analysis}"
        return result