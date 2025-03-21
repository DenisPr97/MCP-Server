from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY_WEATHER = "9014c9405e7316ebb20b86afb39afd55"
NEWS_API_KEY = "bf0ec96dd91d4e46aff4471f420391dc"

async def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_WEATHER}&units=metric"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return {
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "city": city
            }
        except httpx.HTTPError:
            return {"message": f"Не удалось найти погоду для {city}"}

async def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return {"usd_to_rub": data["rates"]["RUB"]}
        except httpx.HTTPError:
            return {"usd_to_rub": "Недоступно"}

async def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return [{"title": article["title"], "url": article["url"]} for article in data["articles"][:5]]
        except httpx.HTTPError:
            return [{"title": "Новости недоступны", "url": "#"}]

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": None})

@app.post("/", response_class=HTMLResponse)
async def get_info(request: Request, city: str = Form(...)):
    weather = await get_weather(city)
    exchange_rate = await get_exchange_rate()
    news = await get_news()
    data = {"weather": weather, "exchange_rate": exchange_rate, "news": news}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/weather/{city}")
async def get_weather_info(city: str):
    return await get_weather(city)

@app.get("/exchange_rate")
async def get_exchange_rate_info():
    return await get_exchange_rate()

@app.get("/news")
async def get_news_info():
    return await get_news()