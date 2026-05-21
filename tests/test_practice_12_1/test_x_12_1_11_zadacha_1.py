import json
from unittest.mock import patch

from practice_12_1.x_12_1_11_zadachi import get_github_users, get_user_info, get_user_repos

"""
КАМАНДА ЗАПУСКАЕТ ТЕСТ в консоль из МОДУЛЯ test_x_12_1_11_zadacha_1.py
pytest tests/test_practice_12_1/test_x_12_1_11_zadacha_1.py

подробный тест
pytest -v tests/test_practice_12_1/test_x_12_1_11_zadacha_1.py
"""


@patch("practice_12_1.x_12_1_11_zadachi.requests.get")
def test_get_user_info(mocked_get):
    """Проверяем успешный сценарий функции при получении данных о пользователе с GitHub"""
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {"login": "test_user", "public_repos": 10}
    result = get_user_info("test_user")
    assert result == (True, {"login": "test_user", "public_repos": 10})


@patch("practice_12_1.x_12_1_11_zadachi.requests.get")
def test_get_user_info_invalid(mocked_get):
    """Проверяем негативный сценарий функции, если запрашиваемого пользователя не существует на GitHub."""
    mocked_get.return_value.json.return_value = {"message": "Not Found"}
    result = get_user_info("non_existent_user")
    assert result == (False, {})


@patch("practice_12_1.x_12_1_11_zadachi.requests.get")
def test_get_user_repos(mocked_get):
    """Проверяем успешный сценарий функции при получении списка репозиториев пользователя с GitHub [?]"""
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
    result = get_user_repos("test_user")
    assert result == (True, ["repo1", "repo2"])


@patch("practice_12_1.x_12_1_11_zadachi.requests.get")
def test_get_user_repos_invalid(mocked_get):
    """Проверяем негативный сценарий функции, если репозитории пользователя не найдены или ошибка на стороне GitHub"""
    mocked_get.return_value.status_code = 404
    mocked_get.return_value.json.return_value = {"message": "Not Found"}
    result = get_user_repos("non_existent_user")
    assert result == (False, [])


@patch("practice_12_1.x_12_1_11_zadachi.get_user_info")
@patch("practice_12_1.x_12_1_11_zadachi.get_user_repos")
def test_get_github_users(mock_get_user_repos, mock_get_user_info):
    """Проверяем интеграционную (совместную) работу всей главной функции в самом успешном сценарии [?]"""
    mock_get_user_info.return_value = (True, {"login": "user1", "public_repos": 2})
    mock_get_user_repos.return_value = (True, ["repo1", "repo2"])
    expected_result = [{"login": "user1", "public_repos": 2, "repositories": ["repo1", "repo2"]}]
    result = get_github_users(["user1"])  # type: ignore
    assert result == json.dumps(expected_result)


@patch("practice_12_1.x_12_1_11_zadachi.get_user_info")
@patch("practice_12_1.x_12_1_11_zadachi.get_user_repos")
def test_get_github_users_negative(mock_get_user_repos, mock_get_user_info):
    """Проверяем негативный сценарий для всей главной функции, если переданный пользователь не существует на GitHub"""
    mock_get_user_info.return_value = (False, {})
    mock_get_user_repos.return_value = (False, [])
    result = get_github_users(["non_existent_user"])  # type: ignore
    assert result == "[]"
