def sieve_of_eratosthenes(n: int) -> int:
    """
        Функция печатает простые числа в интервале от 2 до n
        и возвращает величину k_max_pereimenovat для которой пока не придумано хорошее название.
    """
    is_prime = [True] * (n+1)
    k_max_pereimenovat = 0
    for k in range(2, n+1):
        if not is_prime[k]:
            continue

        print(k, end=' ')

        for i in range(k, n // k + 1):
            if is_prime[i*k]:
                k_max_pereimenovat = k
                is_prime[i*k] = False

    return k_max_pereimenovat


def sieve_of_eratosthenes_luzin(n: int) -> int:
    """
        Функция печатает простые числа в интервале от 2 до n.
        Реализация А.Лузина.
    """
    not_primes = set()
    for k in range(2, n+1):
        if k in not_primes:
            continue

        print(k, end=' ')

        for i in range(k, n // k + 1):
            not_primes.add(i*k)
    return 0


def main():
    print("\nДоброго времени суток! Это - первая нормальная полностью мной написанная на Python'e программа!")
    print("Это программа реализует алгоритм решета Эратосфена по выписыванию всех простых чисел в диапазане от 2 до n включительно")
    print("(число n задаётся пользователем).\n")

    n = int(input("Введите n: "))
    print(f"\nСписок простых чисел от 2 до {n}:", end=' ')
    k_max_pereimenovat = sieve_of_eratosthenes(n)
    print(f"\nk_max = {k_max_pereimenovat}")

    print('\nАлгоритм Лузина')
    print(f"Список простых чисел от 2 до {n}:", end=' ')
    k_max_pereimenovat = sieve_of_eratosthenes_luzin(n)
    print(f"\nk_max = {k_max_pereimenovat}")

    input()
if __name__ == '__main__':
    main()