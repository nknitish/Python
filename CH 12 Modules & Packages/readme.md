# Create Virtual env

python3 -m venv .venv

# Run it

source .venv/bin/activate

# View list of pips inside new venv

pip list

# Install Env Level Dependecices

% pip install -m requests

# Deacivate

deactivate

# Save app venv dependecites to requirements.txt

pip freeze > requirements.txt

# insall via requirements.txt

pip install -r requirements.txt
