FROM python:3.11.5

WORKDIR /likesoft

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install --upgrade pip

COPY requirements.txt /likesoft/
RUN pip install -r requirements.txt
COPY . /likesoft/

RUN python manage.py collectstatic --no-input

COPY . .

