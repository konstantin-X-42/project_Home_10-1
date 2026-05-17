import json
from typing import Any  # специальный тип данных, Any - любой тип

import requests

"""
Задача 1
Напишите программу, которая получает информацию о репозиториях пользователей GitHub.
Программа должна иметь следующую функциональность:
    - Принимает на вход список пользователей GitHub.
    - Для каждого пользователя получает его информацию и список его репозиториев.
    -Составляет список результатов в формате JSON, в котором для каждого пользователя указаны его логин,
     количество публичных репозиториев и список его репозиториев.
Для получения информации о пользователе и его репозиториях должны использоваться открытые API GitHub.
Пример использования программы:
users = ['user1', 'user2', 'user3']
result = get_github_users(users)
print(result)
"""
# import json
# import requests


def get_github_users(users: str) -> str:
    results = []
    for user in users:
        # вызываем ф-ю get_user_info её результат принимаем в переменные: status и user_data
        status, user_data = get_user_info(user)
        if not status:
            continue
        # вызываем ф-ю get_user_repos её результат принимаем в переменные: status и repositories
        status, repositories = get_user_repos(user)
        if not status:
            continue
        result = {"login": user_data["login"], "public_repos": user_data["public_repos"], "repositories": repositories}
        results.append(result)  # добавляем новый элемент в конец существующего списка
    return json.dumps(results)


def get_user_info(user: str) -> tuple[bool, dict[str, Any]]:
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)  # сетевой запрос по адресу repo_url, скачивает оттуда ответ сервера.
    if response.status_code != 200:
        return False, {}  # возвращаем False (статус неудачи) и пустой словарь {} вместо данных
    return True, response.json()  # хорошо, возвращаем True и словарь с данными о пользователе


def get_user_repos(user: str) -> tuple[bool, list[str]]:
    repo_url = f"https://api.github.com/users/{user}/repos"
    repo_response = requests.get(repo_url)  # сетевой запрос по адресу repo_url, скачивает оттуда ответ сервера.
    if repo_response.status_code != 200:
        return False, []  # возвращаем False (статус неудачи) и пустой список [] вместо данных
    return True, [repo["name"] for repo in repo_response.json()]  # хорошо, возвращаем True и список имён репозиториев
