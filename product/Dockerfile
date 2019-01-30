FROM python:3-onbuild
FROM alpine:3.1
RUN apk add --update python py-pip
RUN pip install Flask redis
COPY . /usr/src/app
CMD ["python", "api.py"]