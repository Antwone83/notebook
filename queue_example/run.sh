#! /usr/bin/env sh

export PYTHONPATH=$PYTHONPATH:$(pwd)
export FLASK_APP=app/routes.py
export FLASK_ENV=development

flask run