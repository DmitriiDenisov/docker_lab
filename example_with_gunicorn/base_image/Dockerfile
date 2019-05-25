FROM python:3
RUN set -ex \
    && apt-get update -y \
    && apt-get install -y python-pip python-dev build-essential

COPY . .
# WORKDIR /reqs
RUN pip install -r requirements.txt
RUN rm requirements.txt && rm Dockerfile
ENTRYPOINT ["python3"]
