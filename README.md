HEAD

# MCP Server

## Установка

git clone https://github.com/yourusername/mcp_server.git
cd mcp_server
python3 -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate     # Для Windows
pip install -r requirements.txt

## Запуск сервера
uvicorn server:app --reload   

## Запуск клиента
python client.py

## Запуск тестов
pytest tests/

## Использование
## После установки зависимостей запустите сервер:
uvicorn server:app --reload

## API будет доступен по адресу:
http://127.0.0.1:8000

Вы можете проверить работоспособность API с помощью следующих эндпоинтов:

/weather/{city} — Получить погоду для города.

/news — Получить новости.

/exchange_rate — Получить курс обмена USD/RUB.
e7225d3 (Первый коммит)
