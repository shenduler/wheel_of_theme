from flask import Flask, render_template, jsonify
from db import init_db, get_all_topics, get_random_topic, get_topics_count
import random

app = Flask(__name__)

@app.route('/')
def index():
    """Главная страница с барабаном"""
    return render_template('index.html')

@app.route('/api/topics')
def api_topics():
    """API: получить все темы"""
    topics = get_all_topics()
    return jsonify(topics)

@app.route('/api/random')
def api_random():
    """API: получить случайную тему"""
    topic = get_random_topic()
    return jsonify(topic)

@app.route('/api/count')
def api_count():
    """API: количество тем"""
    count = get_topics_count()
    return jsonify({'count': count})

@app.route('/api/spin-result')
def api_spin_result():
    """
    API: возвращает результат вращения.
    Генерирует случайный индекс для анимации на фронтенде.
    """
    topics = get_all_topics()
    count = len(topics)

    # Случайный индекс для финальной позиции
    # Добавляем несколько полных оборотов для эффекта
    target_index = random.randint(0, count - 1)

    return jsonify({
        'target_index': target_index,
        'total_count': count,
        'topic': topics[target_index]
    })

if __name__ == '__main__':
    init_db()
    print(f"База данных готова. Тем в базе: {get_topics_count()}")
    app.run(debug=True, host='127.0.0.1', port=5000)