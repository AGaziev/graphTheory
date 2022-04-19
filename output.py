from graphMatrix import incMatrix, adjMatrix, V, E
from prettytable import PrettyTable

adjTable = PrettyTable(['-']+[i for i in V])
for i in range(len(adjMatrix)):
    adjTable.add_row([V[i]]+adjMatrix[i])
print(adjTable)

incTable = PrettyTable(['-']+[f'a{i+1}' for i in range(len(E))])
for i in range(len(V)):
    incTable.add_row([V[i]]+incMatrix[i])
print(incTable)