import math
from prettytable import PrettyTable

def BellmanFord(adj, start):
    Vsize = len(adj)
    dist = [math.inf] * Vsize
    dist[start] = 0
    for i in range(Vsize - 1):
        for u in range(Vsize):
            for v in range(Vsize):
                if adj[u][v] != 0:
                    if dist[u] != math.inf and dist[u] + adj[u][v] < dist[v]:
                        dist[v] = dist[u] + adj[u][v]
    return dist


check = input('Хотите ввести матрицу вручную(Да/Нет)?: ')
if check == 'Да':
    V = input('Введите названия вершин:\t').split()  # названия вершин
    E = []  # массив рёбер
    eCount = int(input('Введите количество ребер:\t'))  # количество рёбер
    for edge in range(eCount):
        e = input('Введите начало, конец ребра и вес через пробел:\t').split()
        if len(e) != 3:  # проверка ошибок ввода
            print('Неверное количество данных')
            edge -= 1
            continue
        e = {'start': e[0], 'end': e[1], 'weight': int(e[2])}
        E.append(e)
    adjMatrix = [[0 for i in range(len(V))] for i in range(len(V))]
    for edge in E:
        adjMatrix[V.index(edge['start'])][V.index(edge['end'])] = edge['weight']
        adjMatrix[V.index(edge['end'])][V.index(edge['start'])] = edge['weight']

adjTable = PrettyTable(['-'] + [i for i in V])
for i in range(len(adjMatrix)):
    adjTable.add_row([V[i]] + adjMatrix[i])
print(adjTable)

distTable = PrettyTable(['-'] + [i for i in V])
for i in range(len(adjMatrix)):
    distTable.add_row([V[i]] + BellmanFord(adjMatrix, i))
print(distTable)
