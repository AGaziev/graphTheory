import copy

variantMatrix = [[0, 1, 1, 0, 0],
                 [0, 0, 1, 0, 1],
                 [0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0]]
variantEdgesCount = 7
V = ['x1', 'x2', 'x3', 'x4', 'x5']


def getAdjMatrixFromInput(Vertex, Edges):
    result = [[0 for i in range(len(Vertex))] for i in range(len(Vertex))]
    for i in Edges:
        if not i['oriented']:
            result[Vertex.index(i['end'])][Vertex.index(i['start'])] = 1
        result[Vertex.index(i['start'])][Vertex.index(i['end'])] = 1
    return result


def adjToInc(adj, namesV):  # на вход получаем матрицу смежности, имена вершин
    M = copy.deepcopy(adj)  # копируем исходную матрицу рекурсивно, чтобы не терять данные
    vertexCounter = len(M)
    E = []  # массив рёбер
    # цикл обнаружения всех рёбер
    for i in range(vertexCounter):
        for j in range(vertexCounter):
            if M[i][j] == 1:
                if M[j][i] == 1:
                    # если ребро не направлено, то добавляем неориентированное ребро и удаляем обратную связь из копии
                    E.append({'start': namesV[i], 'end': namesV[j], 'oriented': False})
                    M[j][i] = 0
                else:
                    # если направлено, то просто добавляем ориентированное ребро
                    E.append({'start': namesV[i], 'end': namesV[j], 'oriented': True})
    result = [[0 for i in range(len(E))] for i in range(vertexCounter)]  # матрица nxm
    # цикл заполнения матрицы инцидентности
    for count, edge in enumerate(E):
        if not edge['oriented']:  # если ребро неориентированное, то ставим на обеих строках единицы
            result[namesV.index(edge['end'])][count] = 1
        else:  # если ребро ориентированное, то ставим на начале 1 на конце -1
            result[namesV.index(edge['end'])][count] = -1
        result[namesV.index(edge['start'])][count] = 1
    return result, E


try:
    from input import V, E
except Exception as e:
    adjMatrix = variantMatrix.copy()
    incMatrix, E = adjToInc(variantMatrix, V)
else:
    adjMatrix = getAdjMatrixFromInput(V, E)
    incMatrix, E = adjToInc(adjMatrix, V)
    print(incMatrix)
