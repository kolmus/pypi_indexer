FROM python:3.8

WORKDIR /usr/app

COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/app
RUN pip install -r requirements.txt

COPY . /usr/app
RUN chmod 777 /usr/app/install.sh /usr/app/get_packages.sh
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]