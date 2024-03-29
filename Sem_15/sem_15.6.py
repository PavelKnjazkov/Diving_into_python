# Задание №6
# 📌 Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# 📌 Соберите информацию о содержимом в виде объектов namedtuple.
# 📌 Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# 📌 В процессе сбора сохраните данные в текстовый файл используя
# логирование.


from pathlib import Path
import os
from collections import namedtuple
import logging
import argparse

logging.basicConfig(format='{levelname:<8} {msg}',
                    style='{',
                    filename='info_folder.txt',
                    filemode='w',
                    encoding='utf-8',
                    level=logging.INFO)

logger_val = logging.getLogger(__name__)


def info_folder(folder: str):
    """
    Функция собирает статистику о директории.

    :param folder: Папка о которой нужен отчет
    :return:
    """

    FolderInfo = namedtuple('FolderInfo', ['name_file_or_folder', 'parent_folder', 'type_file',
                                           'flag_folder'], defaults=['', '', '', True])
    list_namedtuple = []
    list_path = []
    for dir_path, *_ in os.walk(Path.cwd() / folder):
        list_path.append(dir_path)
    for path_ in list_path:
        *_, dir_name = path_.split('\\')
        len_dir_name = len(dir_name) + 1
        p_folder = str(path_)[:-len_dir_name]
        list_namedtuple.append(FolderInfo(dir_name, p_folder))

    for path_, _, fl_name in os.walk(Path.cwd() / folder):
        for fl in fl_name:
            try:
                file_mame_, file_type = fl.split('.')
            except ValueError:
                file_mame_ = fl
                file_type = 'no_type'
            list_namedtuple.append(FolderInfo(file_mame_, path_, file_type, False))

    max_len_name_file_or_folder = 0
    max_len_parent_folder = 0
    max_len_type_file = 0
    max_len_flag_folder = 0
    for item in list_namedtuple:
        if max_len_name_file_or_folder < len(item.name_file_or_folder):
            max_len_name_file_or_folder = len(item.name_file_or_folder)
        if max_len_parent_folder < len(item.parent_folder):
            max_len_parent_folder = len(item.parent_folder)
        if max_len_type_file < len(item.type_file):
            max_len_type_file = len(item.type_file)
        if max_len_flag_folder < len(str(item.flag_folder)):
            max_len_flag_folder = len(str(item.flag_folder))

    for item in list_namedtuple:
        logger_val.info(f'parent_folder: {item.parent_folder:<{max_len_parent_folder + 1}}, '
                        f'name: {item.name_file_or_folder:<{max_len_name_file_or_folder + 1}}, '
                        f'folder_flag: {str(item.flag_folder):<{max_len_flag_folder + 1}},'
                        f' type_file: {item.type_file:<{max_len_type_file + 1}}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Функция сохраняет информацию о директории')
    parser.add_argument('-scan_folder', metavar='scan_folder', type=str,
                        help='путь к папке о которой нужен отчет', default=str(Path.cwd()))
    args = parser.parse_args()

    # Создаём отчёты о файлах и каталогах
    info_folder(args.scan_folder)

    # Запуск из командной строки
    # python task_6.py -scan_folder C:\Users\uc201\Desktop\GlonassGpsService ага уверен?)))
    # Описание параметров
    # python task_6.py --help