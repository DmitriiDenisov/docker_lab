FROM base_image
# RUN apt-get update -y
# RUN apt-get install -y python-pip python-dev build-essential
COPY here_scripts /app/here_scripts
WORKDIR /app
# RUN pip install -r /app/requirements.txt
# ENTRYPOINT ["python3", "main.py"]
ENTRYPOINT ["gunicorn", "-w", "8", "--bind", "0.0.0.0:80", "--chdir", "here_scripts", "main:app"]
# ENTRYPOINT gunicorn -w 8 --bind 0.0.0.0:80 main:app
# CMD ["--workers=8 --bind=0.0.0.0:80 main:app"]

# ENTRYPOINT ["bash", "-c", ""]
