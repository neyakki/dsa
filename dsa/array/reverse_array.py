"""
arrays: Task for arrays
Author: Neyakki <neyakki@gmail.com>
=======
Задача: Напишите функцию, которая принимает массив чисел и возвращает
его в обратном порядке без использования встроенных методов для реверса.

Требования:

* Не использовать встроенные методы вроде reverse().
* Изменять массив "на месте" (in-place).
"""

from typing import TypeVar

T = TypeVar("T", int, float)


# TODO: Создать заметку в Obsidian о типизации в Python
# Для версии python >=3.12 можно сделать так
# def reverse_array[T: (int, float)](arr: list[T]) -> None:
# Подробнее:
#   * https://docs.python.org/3.12/library/typing.html#generics
#   * https://docs.python.org/3.12/library/typing.html#typing.TypeVar
#   * https://mypy.readthedocs.io/en/stable/generics.html
#   * Лусиану Рамальо. Python. К вершинам мастерства (Главы 8 и 15)
def reverse_array(arr: list[T]) -> None:
    """
    Reverse array in-place.

    Args:
        arr: List of numbers (int, float).
    """
    arr_size: int = len(arr)
    for index in range(arr_size // 2):
        arr[index], arr[arr_size - 1 - index] = arr[arr_size - 1 - index], arr[index]
