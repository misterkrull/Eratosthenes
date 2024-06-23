# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# class numb:
#    isprime : bool = True

def Sieve_of_Eratosthenes():
    print()
    print("Доброго времени суток! Это - первая нормальная полностью мной написанная на Python'e программа!")
    print("Это программа реализует алгоритм решета Эратосфена по выписыванию всех простых чисел в диапазане от 2 до n включительно")
    print("(число n задаётся пользователем)")
    print()

    n = int(input("Введите n : "))
        # тут ннада сделать try :)

    is_prime = [1 for i in range(n+1)]
    out_str = f"Список простых чисел от 2 до {n} :"
    k_max = 0

    for k in range(2, n+1):
        if (is_prime[k]):
            out_str = out_str + f" {k}"
            i = k
            while (i*k <= n):
                if is_prime[i*k] == 1:
                    k_max = max(k_max, k)
                is_prime[i*k] = 0
                i = i + 1

    print()
    print(out_str)
    print(f"k_max = {k_max}")
    input()

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Sieve_of_Eratosthenes()