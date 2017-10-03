FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code



EXPOSE 3078

CMD [ "python", "/code/wsgi/project/manage.py", "runserver", "0.0.0.0:3078", "--insecure" ]