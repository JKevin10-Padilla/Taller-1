import random
import requests
from fastapi import HTTPException
from app.core.config import settings

class NewsService:

    def get_random_news(self, pais: str):
        if not settings.NEWS_API_KEY:
            raise HTTPException(status_code=500, detail="API Key no configurada")

        params = {
            "apiKey": settings.NEWS_API_KEY,
            "country": pais,
            "pageSize": 50
        }

        response = requests.get(settings.NEWS_API_URL, params=params)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error en NewsAPI")

        articles = response.json().get("articles", [])
        if not articles:
            raise HTTPException(status_code=404, detail="No hay noticias")

        n = random.choice(articles)

        return {
            "titulo": n["title"],
            "descripcion": n["description"],
            "fuente": n["source"]["name"],
            "autor": n["author"],
            "url": n["url"],
            "imagen": n["urlToImage"],
            "fecha": n["publishedAt"]
        }
