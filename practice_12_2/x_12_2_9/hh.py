import requests

# 1. Точный адрес API для поиска вакансий
# url = "https://hh.ru"
url = "https://api.hh.ru/vacancies"

# 2. Настройки фильтра поиска
params = {
    "text": "Python",  # Ключевое слово для поиска
    "area": "1",  # Регион (1 — это Москва)
    "per_page": "5",  # Сколько вакансий вернуть в ответе
}

# 3. Обязательный заголовок для идентификации вашего скрипта
headers: dict[str, str] = {"User-Agent": "KonstantinStudyProjectHHParser/1.0 (kostyani4y@yandex.ru)"}

# 4. Отправляем GET-запрос к серверу API
response = requests.get(url, params=params, headers=headers)  # type: ignore

# 5. Проверяем, что сервер ответил успешно (код 200) и прислал JSON
if response.status_code == 200 and "application/json" in response.headers.get("Content-Type", ""):
    data = response.json()  # Превращаем ответ сервера в словарь Python

    print("--- СПИСОК НАЙДЕННЫХ ВАКАНСИЙ ---")
    # 6. Проходим циклом по каждой вакансии в списке и выводим на экран
    for item in data.get("items", []):
        print(f"Вакансия: {item['name']}")
        print(f"Компания: {item['employer']['name']}")
        print(f"Ссылка: {item['alternate_url']}")
        print("-" * 30)
else:
    print(f"Не удалось достучаться. Код ответа сервера: {response.status_code}")
    print(f"Текст ответа: {response.text[:200]}")

#
#
# import requests
#
# # URL для поиска вакансий
# url = "https://hh.ru"
#
# # Параметры запроса
# params = {
#     "text": "Python",  # Ключевое слово
#     "area": "1",       # ID региона (1 — Москва)
#     "per_page": "5"    # Количество вакансий на страницу
# }
#
# # Заголовки (User-Agent обязателен)
# headers = {
#     "User-Agent": "VacancyParser/1.0 (ivanov@mail.ru)"
# }
#
# # Отправка GET-запроса
# response = requests.get(url, params=params, headers=headers)
#
# # Проверка ответа
# # if response.status_code == 200:
# #     data = response.json()
# #     for item in data.get("items", []):
# #         print(f"Вакансия: {item['name']}")
# #         print(f"Компания: {item['employer']['name']}")
# #         print(f"Ссылка: {item['alternate_url']}\n")
# # else:
# #     print(f"Ошибка: {response.status_code}")
#
# if response.status_code == 200 and "application/json" in response.headers.get("Content-Type", ""):
#     data = response.json()
#     # ... далее ваш цикл обработки
# else:
#     print(f"Ошибка {response.status_code}: Сервер вернул не JSON. Текст ответа: {response.text[:200]}")
