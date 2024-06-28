from DequeRingBuffer import DequeRingBuffer
from RingBuffer import RingBuffer

# Операций проверки на четность можно реализовать с помощью побитовых операций.
# Последний бит в двоичном представлении четного числа равен нулю, а нечетного — единице

# Операция взятия остатка
# Наиболее понятный и очевидный способ
def isEven(value):
    return value % 2 == 0


# AND
# Быстрее операции взятия остатка
def isEvenAnd(value):
    return ~value & 1


# Побитовый сдвиг
# Производительность cравнима с побитовым И
# Наименее очевидный и читаемый способ
def isEvenShift(value):
    return value == (value >> 1) << 1


def main():
    pass


if __name__ == '__main__':
    main()
