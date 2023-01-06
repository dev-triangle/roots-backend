FROM python:3
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install djangorestframework-simplejwt
RUN pip install -r requirements.txt
COPY . /app/