from urllib.parse import urlparse
from colorama import Fore, Style


def is_url(input: str):
    try:
        result = urlparse(input)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def print_colored(message, color=Fore.LIGHTBLACK_EX, style=Style.NORMAL):
    colored_message = f"{style}{color}{message}{Style.RESET_ALL}"
    print(colored_message)
