try:
    koll = int(input("Введите кол-во билетов: "))
    summ = 0
    i = 0  #счетчик регистраций
    while i < koll:
        i += 1
        print("введите возраст", i, "посетителя")
        vozrast = int(input('- '))
        if vozrast >= 25 :
            # print("1390")
            summ += 1390
        elif 18 <= vozrast < 25:
            # print("стоит 990")
            summ += 990
        elif vozrast < 0:
            print('возраст не может быть отрицательным')
            break
    if i > 4 or vozrast > 0:  #если регистрирует >3 и вводит все возраста корректно
        summ *= 0.9
        print('Cумма к оплате (со скидкой 10%)-', int(summ), "руб.")
    elif i > 4 and vozrast < 0:  # если регистрирует >3 но вводит возраст НЕ корректно
        summ *= 0.9
        print('сумма к оплате (со скидкой 10%)-', int(summ), "руб.")
    else:   #если регистрирует <3
        print('сумма к оплате', int(summ), "руб.")
except ValueError as e:  # ловим ошибку при введении посторонних символов
    print('Введите только цифры!')