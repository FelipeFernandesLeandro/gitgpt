from gitgpt.modules.process import run_command, run_command_then_wait_until


class Ollama:
    def serve(self):
        run_command_then_wait_until(["ollama", "serve"], "Listening on")

    def disconnect(self):
        run_command(["pkill", "ollama"])
