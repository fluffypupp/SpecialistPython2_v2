# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md

graph = [
    # список смежности
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10, 15],  # 14
    [14],  # 15

]

dict1 = {0: 'S-1', 12: 'S-2', 3: 'S-3'}
print(dict1)
# visited = [False] * (len(graph))
start = [0, 3, 12]
final = 14


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


for i in start:
    visited = [False] * (len(graph))
    dfs(i)
    if visited[final]:
        print(f"Из точки {dict1[i]} можно дойти до финиша")
    else:
        print(f"Из точки S-{i % 10} нельзя дойти до финиша")

# Решите задачу и выведите ответ в нужном формате
