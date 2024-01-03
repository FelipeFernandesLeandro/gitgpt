from gitgpt.modules.process import run_command
from gitgpt.helpers import print_colored


def diff(path: str):
    print_colored(f"retrieving diff for {path.split('/')[-1]}")
    return run_command(
        ["git", f"--git-dir={path}/.git", f"--work-tree={path}", "diff", "--staged"]
    )
