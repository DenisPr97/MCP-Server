
# MCP Server

## Установка
git clone [[https://github.com/yourusername/mcp_server.git](https://github.com/DenisPr97/MCP-Server)](https://github.com/DenisPr97/MCP-Server)
cd mcp_server


## Установка зависимостей 
pip install -r requirements.txt

## Активируйте ваше виртуальное окружение:
python -m venv venv
.\venv\Scripts\activate


## Дополнительные установки: Убедитесь, что у вас установлены все необходимые зависимости:
pip install jinja2 fastapi httpx


После этого попробуйте снова запустить ваши тесты:
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

Введите название города в форму и получите данные о текущей погоде в выбранном городе 

Вы можете проверить работоспособность API с помощью следующих эндпоинтов:

/weather/{city} — Получить погоду для города.

/news — Получить новости.

/exchange_rate — Получить курс обмена USD/RUB.

