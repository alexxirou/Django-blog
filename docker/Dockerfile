FROM python:3.9
RUN apt-get install gcc -y
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /var/www/django/
COPY requirements.txt .
ENV VIRTUAL_ENV django_venv
ENV PATH $VIRTUAL_ENV/bin:$PATH
RUN python3 -m venv $VIRTUAL_ENV
RUN ./$VIRTUAL_ENV/bin/pip3 install --upgrade pip
RUN ./$VIRTUAL_ENV/bin/pip3 install -r requirements.txt
COPY project/django_blog .
CMD ["gunicorn","django_blog.wsgi:application", "-b" ,"0.0.0.0:8000"]
