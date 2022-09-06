# Ross Mountjoy Portfolio (portfolio-server)

Welcome to my portfolio website's source code! This repository contains the back end of the site. It is written in Python using FastAPI. To view the source code for the frontend (written using Vue 3 and Quasar) [Click Here](https://github.com/rmountjoy92/portfolio-client)

## To install locally:

## Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Install the dependencies
```bash
pip install --no-cache-dir --upgrade -r /code/requirements.txt
```

### Start the app
```bash
uvicorn main:app --reload
```