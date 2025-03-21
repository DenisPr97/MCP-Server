
# MCP Server

## Установка
git clone [[https://github.com/yourusername/mcp_server.git](https://github.com/DenisPr97/MCP-Server)](https://github.com/DenisPr97/MCP-Server)

cd MCP-Server-main


## Установка зависимостей 
pip install -r requirements.txt

## Активируйте ваше виртуальное окружение:
python -m venv venv

.\venv\Scripts\activate


## Установка зависимостей (внутри окружения): 
pip install jinja2 

pip install fastapi

pip install httpx

pip install pytest

pip install -r requirements.txt

pip install python-multipart

pip install fastapi[all]

## Запуск тестов
pytest tests/

## После установки зависимостей запустите сервер:
uvicorn server:app --reload

## Запуск клиента (во втором окне PowerShell / Bash)
python client.py


## Использование
## API будет доступен по адресу:
http://127.0.0.1:8000

Введите название города в форму и получите данные о текущей погоде в выбранном городе 

Вы можете проверить работоспособность API с помощью следующих эндпоинтов:

/weather/{city} — Получить погоду для города.

/news — Получить новости.

/exchange_rate — Получить курс обмена USD/RUB.

