FROM python:3
EXPOSE 80
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt update -y && apt install fortune -y
RUN pip install --no-cache-dir -r requirements.txt
COPY fortune.py ./
CMD ["gunicorn", "-b", "0.0.0.0:8080", "fortune:__hug_wsgi__"]
