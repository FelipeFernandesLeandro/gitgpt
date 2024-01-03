echo "Installing virtual environment"
python3 -m venv .venv
source .venv/bin/activate

echo "Creating .env file"
touch .env
echo "MODEL=dolphin-mistral" >> .env

echo "Pulling model"
ollama pull dolphin-mistral

echo "Installing dependencies"
pip install -r requirements.txt

echo "Setting environment variables"
export GITGPT_PATH=$(pwd)

echo "Done"
