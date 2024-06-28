"""
Обертка deque
Ограничивает deque, предоставляя минимальный необходимиый интерфейс кольцевого буффера
deque напиан на C, операции в deque производятся очень быстро
основан на внешнем модуле, практически вся реализация скрыта
модифицировать код будет очень сложно
"""

from collections import deque


class DequeRingBuffer:
    def __init__(self, capacity) -> None:
        self.__data = deque(maxlen=capacity)

    def push(self, element):
        self.__data.append(element)

    def getSize(self):
        return len(self.__data)

    def clear(self):
        self.__data.clear()

    def get(self):
        return list(self.__data)
