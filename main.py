"""
    Данный модуль реализует алгоритм решета Эратосфена
    Пользователь в терминале вводит число n, а программа выводит простые числа от 2 до n
"""
# TODO: сделать функцию Sieve_of_Eratosthenes, которая выводит список простых чисел
# TODO: придумать называние переменной p_max
#  многострочный to_do: нужно всего-лишь сделать отступ в один пробел))


def sieve_of_eratosthenes(max_num: int) -> tuple[list[int], int]:
    """
        Функция принимает один аргумент max_num и возвращает:
            - список простых чисел между 2 и max_num, вычисленный с помощью алгоритма
             решета Эратосфена;
            - наибольшее простое число, кратные которому вычёркивались из списка
             согласно алгоритму Эратосфена.
    """
    list_of_primes: list[int] = list(range(2, max_num+1))
    p_max: int = 0

    for p in list_of_primes:
        if p**2 >= max_num:
            break
        p_max: int = p
        q: int = p
        while q*p <= max_num:
            if q*p in list_of_primes:
                list_of_primes.remove(q*p)
            q = q + 1

    return list_of_primes, p_max


def main():
    """
            Эта функция осуществляет операции ввода и вывода,
            а также вызывает функцию sieve_of_eratosthenes
    """

    print()
    print("Доброго времени суток! Это - первая нормальная полностью мной написанная на Python'e "
          "программа!")
    print("Это программа реализует алгоритм решета Эратосфена по выписыванию всех простых чисел "
          "в диапазоне от 2 до n включительно")
    print("(число n задаётся пользователем)")
    print()

    while True:
        try:
            n: int = int(input("Введите n : "))
            break
        except ValueError:
            print("Нужно ввести целое число, а вы ввели что-то другое. Попробуйте ещё раз")

    list_of_primes, p_max = sieve_of_eratosthenes(n)

    print()
    print(f"Список простых чисел в диапазоне от 2 до {n} : ", *list_of_primes)
    print(f"p_max = {p_max}")
    input()


if __name__ == '__main__':
    main()
