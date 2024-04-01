FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# RUN python file-parsing

# ENV DJANGO_SETTINGS_MODULE=api.settings

EXPOSE 8100

CMD [ "python", "file_parsing/manage.py", "runserver", "0.0.0.0:8100" ]