from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY_WEATHER = "9014c9405e7316ebb20b86afb39afd55"
NEWS_API_KEY = "bf0ec96dd91d4e46aff4471f420391dc"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_WEATHER}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "city": city
        }
    return None

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {"usd_to_rub": data["rates"]["RUB"]}
    return None

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [{"title": article["title"], "url": article["url"]} for article in data["articles"][:5]]
    return None

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": None})

@app.post("/", response_class=HTMLResponse)
async def get_info(request: Request, city: str = Form(...)):
    weather = get_weather(city)
    exchange_rate = get_exchange_rate()
    news = get_news()
    data = {"weather": weather, "exchange_rate": exchange_rate, "news": news}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

# Добавлен маршрут для получения погоды по городу через GET
@app.get("/weather/{city}")
async def get_weather_info(city: str):
    weather = get_weather(city)
    if weather:
        return weather
    return {"message": "City not found"}

@app.get("/exchange_rate")
async def get_exchange_rate_info():
    exchange_rate = get_exchange_rate()
    return exchange_rate

@app.get("/news")
async def get_news_info():
    news = get_news()
    return news

