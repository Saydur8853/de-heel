# De Heel

## Create a virtual environment:

python -m venv env

## Activate the virtual environment

env/Scripts/activate

## Install required packages

pip install -r requirements.txt

## Apply migration

python manage.py migrate

## Running server

python manage.py runserver
