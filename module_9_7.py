def is_prime(func):
    def wrapper(*args):
        result1 = func(*args)
        k = 0
        for i in range(1, result1 + 1):
            if result1 % i == 0:
                k += 1
        if k == 2:
            print('Простое')
        else:
            print('Составное')
        return result1

    return wrapper


@is_prime
def summ_three(a, b, c):
    return a + b + c


result = summ_three(2, 3, 6)
print(result)
