FROM public.ecr.aws/docker/library/python:3.10-buster

ADD . /app
WORKDIR /app

RUN set -ex \
    && pip install "poetry" \
    && poetry config virtualenvs.create false  \
    && poetry install \
    && chmod 777 entrypoint.sh

EXPOSE 8000

#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "spaceriders_api.wsgi"]


#ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
WORKDIR /app/src

ENTRYPOINT ["gunicorn", "apps.http.__init__:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]

#CMD ["run"]
#RUN gunicorn apps.http.__init__:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
