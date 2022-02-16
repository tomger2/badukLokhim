FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python3 api/jesta/manage.py makemigrations
RUN python3 api/jesta/manage.py migrate
CMD ["python3", "api/jesta/manage.py", "runserver", "8080"]