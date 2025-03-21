import requests
from urllib.parse import quote

BASE_URL = "http://localhost:8000"

def get_weather(city):
    try:
        encoded_city = quote(city)
        response = requests.get(f"{BASE_URL}/weather/{encoded_city}")
        response.raise_for_status()
        data = response.json()
        if "message" in data:
            print(f"Ошибка: {data['message']}")
        else:
            print(f"Погода в {city}:")
            print(f"  Температура: {data['temperature']}°C")
            print(f"  Описание: {data['description']}")
    except requests.exceptions.RequestException as e:
        print(f"Не удалось получить погоду: {e}")

def get_exchange_rate():
    try:
        response = requests.get(f"{BASE_URL}/exchange_rate")
        response.raise_for_status()
        data = response.json()
        if "message" in data:
            print(f"Ошибка: {data['message']}")
        else:
            print(f"Курс доллара (USD -> RUB): {data['usd_to_rub']}")
    except requests.exceptions.RequestException as e:
        print(f"Не удалось получить курс: {e}")

def get_news():
    try:
        response = requests.get(f"{BASE_URL}/news")
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            print("Последние новости:")
            for i, article in enumerate(data, 1):
                print(f"  {i}. {article['title']}")
                print(f"     Ссылка: {article['url']}")
        else:
            print(f"Ошибка: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Не удалось получить новости: {e}")

if __name__ == "__main__":
    city = input("Введите город для прогноза погоды: ")
    print("\n--- Результаты ---\n")
    get_weather(city)
    get_exchange_rate()
    get_news()