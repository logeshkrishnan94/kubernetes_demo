FROM python:3.6-alpine

#ENV CELERY_BROKER_URL amqp://guest:guest@rabbit:5672//
#ENV CELERY_RESULT_BACKEND redis://redis:6379/0
#ENV C_FORCE_ROOT true

#ENV HOST 0.0.0.0
#ENV PORT 5001
#ENV DEBUG true

COPY . /api
WORKDIR /api

# install requirements
RUN pip install -r requirements.txt

# expose the app port
EXPOSE 5001

RUN pip install gunicorn

# run the app server in production with gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:flask_app"]