import sys
import os

# Добавляем родительский каталог в системный путь
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from server import app  # Импортируем приложение FastAPI из server.py

client = TestClient(app)

def test_get_weather():
    """Тестируем получение погоды по городу"""
    city = "Moscow"
    response = client.get(f"/weather/{city}")
    assert response.status_code == 200  # Проверяем, что статус код успешный
    data = response.json()
    assert "temperature" in data  # Проверяем, что температура в ответе
    assert "description" in data  # Проверяем, что описание погоды в ответе

def test_get_news():
    """Тестируем получение новостей"""
    response = client.get("/news")
    assert response.status_code == 200  # Проверяем, что статус код успешный
    data = response.json()
    assert isinstance(data, list)  # Проверяем, что ответ является списком
    assert len(data) > 0  # Проверяем, что в ответе есть хотя бы одна новость

def test_get_exchange_rate():
    """Тестируем получение курса обмена USD/RUB"""
    response = client.get("/exchange_rate")
    assert response.status_code == 200  # Проверяем, что статус код успешный
    data = response.json()
    assert "usd_to_rub" in data  # Проверяем, что курс USD в рублях есть в ответе
    assert isinstance(data['usd_to_rub'], (float, int))  # Проверяем, что курс является числом
