"""
однозначно назвать самую быструю сортировку нельзя, скорость зависит от входных данных
К примеру, пузырьковая сортировка в некоторых случаях может работать за O(n), но в среднем время работы составляет O(n * n)
Пирамидальная сортировка при любых данных отработает за O(n * log(n))
Наилучшим вариантом я считаю использовать стандарнтный list.sort()
list.sort() сортирует список с помощью стабильного алгоритма Timsort, который в зависимости от входных данных
отработает либо за линейное время, либо за  O(n * log(n))
Реализация состоит из трех главных шагов
    * Разделить входной массив на подмассивы
    * Отсортировать каждый подмассив сортировкой вставками, сортировка вставками эффективна только на небольших массивах
    * Собрать отсортированные подмассивы в единый массив с помощью модифицированной сортировки слиянием
        сортировка слиянием наиболее эффективно работает на подмассивах примерно равного размера.
"""


class Sorter:
    pass