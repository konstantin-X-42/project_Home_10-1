import json

print("  -- 1-3 --")
"""
1. Создайте словарь в Python, который представляет информацию о книге.
2. Словарь должен содержать ключи:
   - title (название книги),
   - author (автор),
   - publication_year (год публикации),
   - genres (жанры в виде списка).
3. Преобразуйте этот словарь в строку JSON с помощью метода dumps библиотеки json.
"""

book_info = {
    "title": "Sherlok Holmes",
    "author": "Arthur Conan Doyle",
    "publication_year": 1887,
    "genres": ["detective", "novel"],
}

book_info_str_1 = json.dumps(book_info)

print(book_info_str_1)
print(type(book_info_str_1))
# >>> <class 'str'>
# >>> {"title": "Sherlok Holmes", "author": "Arthur Conan Doyle",
#      "publication_year": 1887, "genres": ["detective", "novel"]}


# ----------------------------------------------------------
print("  -- 4 --")
""" 4. Используя строку JSON, полученную ранее, преобразуйте ее обратно в объект
       Python с помощью метода loads библиотеки json.
"""
book_info_str_2 = (
    '{"title": "Sherlok Holmes", "author": "Arthur Conan Doyle",'
    ' "publication_year": 1887, "genres": ["detective", "novel"]}'
)

book_info_2 = json.loads(book_info_str_2)

print(book_info_2)
print(type(book_info_2))


# ----------------------------------------------------------
print("  -- 5 --\n" "записан в файл x_12_1_3_data.json")
""" 5. Используйте метод dump для записи исходного словаря в файл в формате JSON.
"""
book_info_3 = {
    "title": "Sherlok Holmes",
    "author": "Arthur Conan Doyle",
    "publication_year": 1887,
    "genres": ["detective", "novel"],
}
with open("x_12_1_3_data.json", "w") as json_file:
    json.dump(book_info_3, json_file)


# ----------------------------------------------------------
print("  -- 6 --")
""" 6. Откройте ранее созданный файл JSON и используйте метод load для чтения данных обратно в объект Python.
"""
with open("x_12_1_3_data.json") as json_file:
    book_info_4 = json.load(json_file)

print(book_info_4)
print(type(book_info_4))
