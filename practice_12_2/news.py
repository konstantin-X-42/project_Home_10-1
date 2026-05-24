# import datetime
import logging
from typing import Any

import requests

from practice_12_2.config import API_KEY, BASE_URL

logger = logging.getLogger("news")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/news.log", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_news(query: str, exclude_words: list[str], api_key: str = API_KEY) -> list[dict[str, Any]]:
    # today = datetime.datetime.today()
    params = {
        "q": query,
        # 'from': today.strftime('%Y-%m-%d'),  # фильтрация новостей с сегодняшнего дня
        "sortBy": "publishedAt",
        "apiKey": api_key,
    }
    try:
        logger.info(f"Выполняем запрос с ключевыми словами: {query}")
        response = requests.get(url=BASE_URL, params=params)

        news_data = response.json()
        if news_data.get("status") != "ok":
            logger.info("Статей не нашлось")
            return []

        articles_list = news_data.get("articles", [])

        articles_result = []
        logger.info(f'Фильтруем новости по словам исключениям: {", ".join(exclude_words)}')
        for article in articles_list:

            content = f'{article.get("title")} {article.get("content")}'.lower()

            if any(word.lower() in content for word in exclude_words):
                continue
            # тоже в одну строку
            # exclude_flag = False
            # for word in exclude_words:
            #     if word in content:
            #         exclude_flag = True
            #
            # if exclude_flag:
            #     continue

            articles_result.append(
                {
                    "title": article.get("title"),
                    "author": article.get("author"),
                    "description": article.get("content"),
                    "url": article.get("url"),
                }
            )

        return articles_result
    except requests.RequestException as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
    except Exception:
        return []
