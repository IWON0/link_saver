FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Отключаем создание .pyc файлов и буферизацию stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Ставим необходимые системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    netcat-openbsd \
    tzdata \
    postgresql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip==23.3.1 \
    && pip install --no-cache-dir -r requirements.txt

# Теперь копируем весь проект
COPY . .

# Создаём пользователя для безопасности
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser /app

# Переключаемся на обычного пользователя
USER appuser

# Указываем команду по умолчанию (здесь не надо писать, если в docker-compose указано)
# CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
