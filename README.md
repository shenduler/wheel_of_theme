# wheel_of_theme

wheel_of_topics/
├── app.py              # Flask сервер
├── database.py         # Работа с БД
├── topics.db           # SQLite база (создастся автоматически)
├── requirements.txt    # Зависимости
└── templates/
    └── index.html      # Фронтенд с анимацией


# 1. Создай папку проекта и перейди в неё
mkdir wheel_of_topics
cd wheel_of_topics

# 2. Создай папку templates
mkdir templates

# 3. Сохрани все файлы в соответствующие места

# 4. Установи Flask
pip install flask

# 5. Запусти сервер
python app.py

# 6. Открой в браузере
# http://127.0.0.1:5000