FROM python:3.8

RUN useradd --create-home userapi
WORKDIR /films_api

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt

COPY ./ .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 5000
CMD ["python", "./wsgi.py"]
