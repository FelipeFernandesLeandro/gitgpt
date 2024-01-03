import dotenv
import os
import argparse
from gitgpt.modules.git import diff
from gitgpt.modules.inquirer import Inquirer
from gitgpt.modules.commit_name_generator import CommitNameGeneratorPromptTemplate
from gitgpt.modules.ollama import Ollama
from gitgpt.helpers import print_colored

dotenv.load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--model",
        default="dolphin-mistral",
        type=str,
        help="name of the LLM model to use",
    )

    args = parser.parse_args().__dict__
    model_name: str = args.pop("model")

    os.environ["MODEL"] = model_name

    current_directory = os.getcwd()

    ollama = Ollama()
    ollama.serve()

    inquirer = Inquirer()

    commit_name_generator = CommitNameGeneratorPromptTemplate(input_variables=["diff"])
    changes = diff(current_directory)
    print_colored(f"prompting model, please wait...")
    prompt = commit_name_generator.format(diff=changes)

    inquirer.inquire(prompt)
    ollama.disconnect()


if __name__ == "__main__":
    main()
