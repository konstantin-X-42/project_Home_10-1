import logging
import os


def module_logger(file_name='logs.log', logger_name='logs', overwrite=False, log_console=False):
    """Функция для настройки логгера с динамическим именем файла,
    и именными аргументами - тогда все логи в один файл, False - хранить предыдущий лог,
    False - запрет вывода лога в консоль"""

    logger = logging.getLogger(logger_name)  # создаем или возвращаем существующий логгер с установленным именем

    # ПРОВЕРКА: Если у логгера уже есть обработчики, значит логгер настроен
    # возвращаем логгер, чтобы не добавились дублирующие файлы и консоли
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO) # выставляем уровень логирования INFO WARNING ERROR CRITICAL

    path_log = f"logs/{file_name}"          # динамический относительный путь хранения файла лога
    abs_file_path = os.path.abspath(path_log)   # определяем абсолютный путь к файлу логов
    abs_dir_path = os.path.dirname(abs_file_path) # извлекаем путь к ПАПКЕ из абсолютного пути файла
    os.makedirs(abs_dir_path, exist_ok=True)   # если папки logs нет создаём, если есть пропускаем

    # общий формат записи для всех
    file_formater = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - строка: %(lineno)d >>> %(message)s') # шаблон-маска записи в лог

    # РЕЖИМ ЗАПИСИ при запуске logger():
    # True - 'w' (перед записью, удалить старые логи в файле),
    # False - 'a' (продолжить запись не удаляя предыдущие)
    log_mode = 'w' if overwrite else 'a'

    # запись лога в файл
    file_handler = logging.FileHandler(abs_file_path, encoding='utf-8', mode=log_mode) # отправка лога, в кодировке, управление архивом запись
    file_handler.setFormatter(file_formater) # передаём шаблон записи лога на запись в файл
    logger.addHandler(file_handler) # записываем лог в файл

    # вывод лога в консоль
    if log_console: # True — выводить в консоль и файл, False — только в файл
        console_handler = logging.StreamHandler() # создаем обработчик для вывода логов в консоль
        console_handler.setFormatter(file_formater) # передаем ему тот же формат строки
        logger.addHandler(console_handler) # подключаем вывод в консоль к логгеру
    return logger  # возвращаем настроенный логгер

#-------------------------------------------------------
# # Импортируем функцию настройки логгера из файла log_config текущей директории
# from log_config import module_logger
#
# # Инициализируем логгер (задаем имя файлу, имя логгеру, дозапись-False,
# перезапись-True; лог в файл и консоль-True, в файл-False)
# log = module_logger(file_name="logs.log", logger_name='logs', overwrite=False, log_console=False)
#-------------------------------------------------------
#удалить
# log = logging.getLogger('utils') # строка для импорта в другие модули
# В другом модуле импортируем так: from log_config import log
#-------------------------------------------------------
# --- ПРИМЕР ИСПОЛЬЗОВАНИЯ ---
# module_logger.info("Программа успешно запустилась!")
# module_logger.warning("Это предупреждение (появится и в консоли, и в файле).")