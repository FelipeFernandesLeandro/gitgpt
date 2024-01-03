import subprocess
import time

from gitgpt.helpers import print_colored


def run_command(command):
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        raise RuntimeError(f"Command failed: {command}\nError: {result.stderr.strip()}")


def run_command_then_wait_until(command, message, timeout_seconds=60):
    try:
        start_time = time.time()
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        while process.poll() is None:
            output = process.stderr.readline().strip()
            if message in output:
                break

            elapsed_time = time.time() - start_time
            if elapsed_time > timeout_seconds:
                print_colored(
                    f"Timeout ({timeout_seconds} seconds) reached. Forcing break."
                )
                break

    except Exception as e:
        print(f"Error running '{command}': {e}")
        return False
