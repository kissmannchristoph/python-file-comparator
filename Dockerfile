FROM python:3.8-slim-buster

RUN python -m pip install flake8 pytest numpy
RUN python start.py