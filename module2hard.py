def password(pairs):
    result = ""

    for i in range(1, 21):
        for j in range(i + 1, 21):
            if pairs % (i + j) == 0:
                result += str(i) + str(j)
    return result

pairs = int(input('Введите число от 3 до 20: '))
result = password(pairs)
print(f'Для числа {pairs} пароль: {result}')
