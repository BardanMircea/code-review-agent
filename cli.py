import argparse
from agent.analyzer import CodeAnalyzer

def main():
    parser = argparse.ArgumentParser(description="AI Code Review Agent")
    parser.add_argument("--file", required=True, help="Path to the Python file to analyze")
    parser.add_argument("--mode", required=True, choices=["strict", "mentor", "test_focus"], help="Prompt profile to use")
    parser.add_argument("--provider", required=True, choices=["ollama", "openai", "anthropic"], help="LLM provider to use")
    args = parser.parse_args()

    analyzer = CodeAnalyzer(provider=args.provider, mode=args.mode)
    analysis_result = analyzer.analyze_file(args.file)

    # Write the result to reviews/review_output.md
    with open("reviews/review_output.md", "w") as output_file:
        output_file.write(analysis_result)

    print("Analysis complete. Results saved to reviews/review_output.md")

if __name__ == "__main__":
    main()