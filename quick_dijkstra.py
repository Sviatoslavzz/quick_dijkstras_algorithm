import heapq

option = int(input("Введите 1 для ввода данных из терминала / введите 2 для загрузки из файла\n"))
if option == 1:
    n, k = map(int, input("Введите кол-во городов и дорог через пробел: ").split())

    dist = [-1] * (n + 1)
    matrix = [[] for i in range(n + 1)]

    for i in range(k):
        a, b, l = map(int, input(
            f"Для дороги {i + 1} введите город отправления, город назначения и расстояние через пробел: ").split())
        matrix[a].append((l, b))
        matrix[b].append((l, a))

    s, f = map(int, input("Введите города через пробел для расчета расстояния: ").split())
else:
    path = input("Введите путь к файлу: ")
    with open(path, "r") as file:
        n, k = map(int, file.readline().split())

        dist = [-1] * (n + 1)
        matrix = [[] for i in range(n + 1)]

        for i in range(k):
            a, b, l = map(int, file.readline().split())
            matrix[a].append((l, b))
            matrix[b].append((l, a))

        s, f = map(int, file.readline().split())

dist[s] = 0

heap = []
heapq.heapify(heap)

elem = s
counter = 0
while True:
    for value in matrix[elem]:
        e, v = value[0], value[1]
        if dist[elem] + e < dist[v] or dist[v] == -1:
            dist[v] = dist[elem] + e
            heapq.heappush(heap, value)
            counter += 1
    if counter != 0:
        elem = heapq.heappop(heap)[1]
        counter -= 1
    else:
        break

if dist[f] == -1:
    print(-1)
else:
    print(dist[f])
