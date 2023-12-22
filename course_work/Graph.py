from DynamicArray import DynamicArray
from Stack import Stack
from TimSort import timsort


"""Хранение графа в разных вариантах"""

def reading_from_file(path: str = "test.txt"):
    lines = DynamicArray()
    with open(path, encoding="utf-8") as file:
        for line in file:
            lines.add(line.split())
    return lines   

def adjacency_list(): # список смежности
    graph = {}
    variables, *values = reading_from_file()
    for i in range(len(variables)):
        graph[variables[i]] = {}
        for j in range(len(variables)):
            if values[i][j] != '0':
                graph[variables[i]] |= {variables[j]: values[i][j]}
    return graph

def adjacency_matrix(): # матрица смежности
    variables, *values = reading_from_file()
    values = [list(map(int, v)) for v in values]
    graph = values
    return graph

def incidence_matrix(): # матрица инцидентности
    variables, *values = reading_from_file()
    edges = DynamicArray()
    for i in range(len(values)):
        for j in range(i+1, len(values[i])):
            if int(values[i][j]):
                edges.add((i, j, int(values[i][j])))
    graph = [[0] * len(variables) for _ in range (len(edges))]
    for i in range(len(edges)):
        v1, v2, w = edges[i]
        if v1 >= len(variables) or v2 >= len(variables):
            continue
        graph[i][v1] = w
        graph[i][v2] = w
    graph = list(map(list, zip(*graph)))
    print(*graph, sep="\n")

"""Обход графа в ширину и глубину"""

def dfs(visited, answer, graph=adjacency_list(), start="A"): #обход в глубину
    if start not in visited:
        answer.add(start)
        visited.add(start)
        for letter in graph[start]:
            if letter:
                dfs(visited, answer, graph=adjacency_list(), start=letter)
    return answer.array[:answer.length]                

def bfs(visited, answer, graph=adjacency_list(), start="A"): #обход в ширину
    visited.add(start)
    answer.add(start)
    while len(visited) > 0:
        curr_vertex = visited[0]
        visited.remove(0)
        if curr_vertex not in answer:
            answer.add(curr_vertex)
        for v in graph[curr_vertex]:
            if v not in answer:
                visited.add(v)
    return answer.array[:answer.length]
        
"""Алгоритм Крускала"""

X = {}
R = {}

def new_graph(graph=adjacency_list()):
    variables, *values = reading_from_file()
    edges_map = {}
    weights = DynamicArray()
    for i in range(len(values)):
        for j in range(i+1, len(values[i])):
            if int(values[i][j]):
                v1, v2, w = (variables[i], variables[j], int(values[i][j]))
                if w not in edges_map:
                    edges_map[w] = DynamicArray()
                edges_map[w].add((v1, v2, w))
                weights.add(w)
    sorted_weights = timsort(weights[:weights.size()])
    edges = DynamicArray()
    for w in sorted_weights:
        edges.add(edges_map[w][0])
        edges_map[w].remove(0)
    return edges

def make_set(point):
    X[point] = point
    R[point] = 0

def find(point):
    if X[point] != point:
        X[point] = find(X[point])
    return X[point]

def merge(point_1, point_2):
    r_1 = find(point_1)
    r_2 = find(point_2)
    if r_1 != r_2:
        if R[r_1] > R[r_2]:
            X[r_2] = r_1
        else:
            X[r_1] = r_2
            if R[r_1] == R[r_2]:
                R[r_2] += 1

def kruskals_algorithm(vertices=adjacency_list().keys(), edges=new_graph()):
    for v in vertices:
        make_set(v)
    min_tree = DynamicArray()
    summ = 0
    for e in edges:
        vertice_1, vertice_2, weight = e
        if find(vertice_1) != find(vertice_2):
            merge(vertice_1, vertice_2)
            min_tree.add(e[0] + " " + e[1])
            summ += e[2]
    for i in timsort(min_tree):
        print(i)
    print(summ)


#print(adjacency_list())
#print(adjacency_matrix())
#incidence_matrix()
#print(dfs(visited=set(), answer=DynamicArray()))
#print(bfs(visited=DynamicArray(), answer=DynamicArray()))
print("Найдено минимальное остовное дерево:")
kruskals_algorithm(vertices=adjacency_list().keys())