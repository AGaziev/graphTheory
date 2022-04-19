check = input('Хотите ввести матрицу вручную(Да/Нет)?\t')  # Нет - выбор матрицы смежности из вариант
if check == 'Да':
    V = input('Введите названия вершин:\t').split()  # названия вершин
    E = []  # массив рёбер
    eCount = int(input('Введите количество ребер:\t'))  # количество рёбер
    for i in range(eCount):
        e = input('Введите начало и конец ребра через пробел:\t').split()
        if len(e) != 2:  # проверка ошибок ввода
            print('Неверное количество данных')
            i -= 1
            continue
        if e[0] not in V or e[1] not in V:  # проверка ошибок ввода
            print(f'Вершины с названием {e[0] if e[0] not in V else e[1]} нет в списке')
            i -= 1
            continue
        if {'start': e[1], 'end': e[0], 'oriented': True} in E:
            # если введено ребро обратное уже имеющемуся, то считаем его неориентированным
            E[E.index({'start': e[1], 'end': e[0], 'oriented': True})]['oriented'] = False
        else:
            # добавляем ребро (начало, конец, ориентированность)
            e = {'start': e[0], 'end': e[1], 'oriented': True}
            E.append(e)
