try:
    koll = int(input("Введите кол-во билетов: "))
    summ = 0
    i = 0  #счетчик регистраций
    while i < koll:
        i += 1
        vozrast = int(input(f'введите возраст {i} посетителя- '))
        if vozrast >= 25 :
            # print("1390")
            summ += 1390
        elif 18 <= vozrast < 25:
            # print("стоит 990")
            summ += 990
        elif vozrast < 0:
            print('возраст не может быть отрицательным')
            i -= 1
            break
    if i > 3 and vozrast > 0:  #если регистрирует >3 и вводит все возраста корректно
        summ *= 0.9
        print('Cумма к оплате (со скидкой 10%)-', int(summ), "руб.")
    elif i > 3 and vozrast < 0:  # если регистрирует >3 но вводит возраст НЕ корректно
        summ *= 0.9
        print('сумма к оплате (со скидкой 10%)-', int(summ), "руб.")
    else:   #если регистрирует <3
        print('сумма к оплате', int(summ), "руб.")
except ValueError as e:  # ловим ошибку при введении посторонних символов
    print('Введите только цифры!')
except NameError as e:  # ловим ошибку при введении отрицательных чисел
    print('Используйте положительное число!')