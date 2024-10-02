# Установка Python 3.10 в контейнере
FROM python:3.10

# Открытие каталога для работы приложения
WORKDIR /app

# Копирование библиотеки и файлов приложения в контейнер
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всех файлов Django приложения в контейнер
COPY . .

# Сборка статических файлов
RUN python manage.py collectstatic --noinput

# Создание миграций
RUN python manage.py makemigrations

# Применение миграций
RUN python manage.py migrate

# Запуск приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
