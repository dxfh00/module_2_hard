while 0 == 0:
    num = (int(input('Введите число от 3 до 20 включительно: ')))
    result = []
    a = 0

    for i in range(2, num + 1):
        a += 1
        b = 1
        for j in range(2, num + 1):
            c = a + b
            if num % c == 0 and b > a:
                result.append(a)
                result.append(b)
                b += 1
            else:
                b += 1
                continue

    print(*result)