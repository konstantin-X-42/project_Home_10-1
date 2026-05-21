import json
from unittest.mock import mock_open, patch
from src.utils import read_json_file


def test_read_json_file_success():
    """Тест успешного чтения корректного JSON-файла."""
    mock_json_data = [{"id": 1, "state": "EXECUTED"}]
    mock_content = json.dumps(mock_json_data)

    # Патчим проверку файла на диске и сам процесс открытия файла
    with patch("src.utils.Path.is_file", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_content)):
            result = read_json_file("dummy_path.json")
            assert result == mock_json_data
            assert isinstance(result, list)


def test_read_json_file_not_found():
    """Тест поведения функции, если файл отсутствует на диске."""
    with patch("src.utils.Path.is_file", return_value=False):
        result = read_json_file("non_existent.json")
        assert result == []


def test_read_json_file_invalid_json():
    """Тест обработки синтаксической ошибки (битый JSON)."""
    with patch("src.utils.Path.is_file", return_value=True):
        with patch("builtins.open", mock_open(read_data="[{broken json")):
            result = read_json_file("broken.json")
            assert result == []


def test_read_json_file_not_a_list():
    """Тест случая, когда JSON содержит словарь вместо списка."""
    mock_content = json.dumps({"id": 1, "state": "EXECUTED"})
    with patch("src.utils.Path.is_file", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_content)):
            result = read_json_file("dict_only.json")
            assert result == []
