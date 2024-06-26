for creating a virtual environment for this repo :

for creation -> python3 -m venv .venv
for activation -> source .venv/bin/activate
for demounting the venv -> deactivate

once the venv is mounted , install the fastapi package :

pip install fastapi

after fastapi is installed , start the server with :

fastapi dev main.py (for development server with fastapi watching for changes)

fastapi run main.py (for production server)

