Habit Tracker API
Backend для трекера привычек на основе книги "Атомные привычки" Джеймса Клира.
О ПРОЕКТЕ
REST API для создания и отслеживания привычек с функциями:
Регистрация и аутентификация (JWT)
CRUD привычек с правами доступа
Публичные и приватные привычки
Напоминания через Telegram
Отложенные задачи (Celery + Redis)
ТЕХНОЛОГИИ
Python 3.10+
Django 5.0+
Django REST Framework
PostgreSQL
Redis
Celery
SimpleJWT
pytest
УСТАНОВКА
Клонирование:
git clone https://github.com/ВАШ_НИК/habit_tracker.git
cd habit_tracker
Виртуальное окружение:
python -m venv venv
source venv/bin/activate (Linux/macOS)
или venv\Scripts\activate (Windows)
Зависимости:
pip install -r requirements.txt
Переменные окружения:
cp .env.template .env
Отредактируйте .env и укажите свои значения
Миграции:
python manage.py migrate
Запуск сервера:
python manage.py runserver
API ENDPOINTS
Аутентификация:
POST /api/token/ - получение токена
POST /api/token/refresh/ - обновление токена
POST /api/users/register/ - регистрация
Привычки:
GET /api/habits/ - список личных привычек
POST /api/habits/ - создание привычки
GET /api/habits/{id}/ - детальная информация
PUT/PATCH /api/habits/{id}/ - обновление
DELETE /api/habits/{id}/ - удаление
GET /api/habits/public/ - публичные привычки
Уведомления:
PUT /api/notifications/set-telegram-id/ - установка Telegram ID
ТЕСТЫ
Запустить тесты:
pytest
С покрытием:
pytest --cov=. --cov-report=html
ДОКУМЕНТАЦИЯ
После запуска сервера откройте:
http://localhost:8000/api/docs/
СТРУКТУРА ПРОЕКТА
habit_tracker/
├── users/ - Пользователи и аутентификация
├── habits/ - Привычки и бизнес-логика
├── notifications/ - Telegram и Celery задачи
└── habit_tracker/ - Настройки проекта
ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ (.env)
DB_NAME=habit_tracker_db
DB_USER=postgres
DB_PASSWORD=ваш_пароль
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=ваш_secret_key
TELEGRAM_BOT_TOKEN=ваш_токен
CELERY_BROKER_URL=redis://localhost:6379/0
