# 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


def get_file_info(path: str) -> tuple:
    return str(os.path.splitext(path)[0]).split("\\").__getitem__(-1), os.path.abspath(path), os.path.splitext(path)[1]


print(get_file_info("C:\\Users\\OBI.DGZKS\\Desktop\\taskmanager\\10_IT\\02_backend\\05\\hw_back.txt"))
