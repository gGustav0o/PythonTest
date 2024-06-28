"""
Реализация кольцевого буффера на списке
Реализация проста
Весь код понятен, его легко менять и адаптировать
Все операции контролируются разработчиком
Реализация на основе списка может быть полезна, если вам нужен очень специфичный контроль над поведением буфера
или если вы работаете с очень маленькими буферами, где разница в производительности не будет заметна
"""


class RingBuffer:
    def __init__(self, capacity) -> None:
        self.__currentElement = 0
        self.__size = 0
        self.__capacity = capacity
        self.__data = [None] * capacity

    def push(self, element) -> None:
        if len(self.__data) == self.__capacity:
            if self.__currentElement == self.__capacity:
                self.__currentElement = 0
            self.__data[self.__currentElement] = element
            self.__currentElement += 1
        else:
            self.__data.append(element)
            self.__size += 1

    def clear(self) -> None:
        self.__data = [None] * self.__capacity
        self.__size = 0

    def getSize(self) -> int:
        return self.__size

    def get(self) -> []:
        return self.__data
