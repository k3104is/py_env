FROM python:3.10-slim
# USER root
WORKDIR /code
RUN apt-get update
RUN apt-get install -y vim less
# RUN pip install --upgrade pip
# RUN pip install --upgrade setuptools

#RUN python -m pip install jupyterlab
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY ./py_ws ./py_ws