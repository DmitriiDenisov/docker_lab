# Налседуемся от нашего base_image:
FROM base_image
# RUN apt-get update -y
# RUN apt-get install -y python-pip python-dev build-essentia
# копируем папку с скриптом:
COPY here_scripts /app/here_scripts
# делаем текущую директорию app
WORKDIR /app
# RUN pip install -r /app/requirements.txt
# запускаем скрипт:
ENTRYPOINT ["python3", "here_scripts/main.py"]
# ENTRYPOINT ["gunicorn", "-w", "8", "--bind", "0.0.0.0:80", "--chdir", "here_scripts", "main:app"]
# ENTRYPOINT gunicorn -w 8 --bind 0.0.0.0:80 main:app
# CMD ["--workers=8 --bind=0.0.0.0:80 main:app"]

# ENTRYPOINT ["bash", "-c", ""]
