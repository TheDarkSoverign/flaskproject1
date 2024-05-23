# Используем базовый образ Python
FROM python:3.12

RUN pip install --upgrade pip

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt

# Копируем все файлы в контейнер
COPY . .

COPY Data_testing.csv /app/Data_testing.csv

COPY Data_training.csv /app/Data_training.csv

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Команда для запуска Flask при старте контейнера
CMD ["flask", "run"]
