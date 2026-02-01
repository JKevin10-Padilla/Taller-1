from fastapi import APIRouter
from app.services.news_service import NewsService
from app.models.news_model import News

router = APIRouter()
service = NewsService()

@router.get("/noticia-aleatoria", response_model=News)
def obtener_noticia_aleatoria(pais: str = "us"):
    return service.get_random_news(pais)
