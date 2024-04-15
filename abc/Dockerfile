FROM python:3.9

WORKDIR /ddbms_project

COPY requirements.txt /ddbms_project/
RUN pip install -r requirements.txt

COPY . /ddbms_project/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
