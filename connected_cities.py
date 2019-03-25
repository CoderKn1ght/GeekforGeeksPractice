def connected_cities(n, g, origin_cities, destination_cities):
    root = [i for i in range(n+1)]
    ids = [1 for i in range(n+1)]
    result = []

    for i in range(g+1, n+1):
        for j in range(2*i, n+1):
            union_find(j, i, root, ids)

    for i in range(len(origin_cities)):
        if get_root(origin_cities[i], root) == get_root(destination_cities[i], root):
            result.append(1)
        else:
            result.append(0)
    return result


def union_find(a, b, root, ids):
    a_root = get_root(a, root)
    b_root = get_root(b, root)
    if a_root == b_root:
        return
    if ids[a_root] < ids[b_root]:
        root[a_root] = root[b_root]
        ids[a_root] += ids[b_root]
    else:
        root[b_root] = root[a_root]
        ids[b_root] += ids[a_root]


def get_root(a, root):
    while a != root[a]:
        a = root[a]
    return a


print(connected_cities(6, 1, [1, 2, 4, 6], [3, 3, 3, 4]))

# if __name__ == "__main__":
#     file = open('input', 'r')
#     n = int(file.readline().strip())
#     g = int(file.readline().strip())
#     originCities_cnt = int(file.readline().strip())
#     originCities = []
#     originCities_i = 0
#     for originCities_i in range(originCities_cnt):
#         originCities_t = int(file.readline().strip())
#         originCities.append(originCities_t)
#     destinationCities_cnt = int(file.readline().strip())
#     destinationCities = []
#     destinationCities_i = 0
#     for destinationCities_i in range(destinationCities_cnt):
#         destinationCities_t = int(file.readline().strip())
#         destinationCities.append(destinationCities_t)
#     res = connected_cities(n, g, originCities, destinationCities)
#     file = open('output', 'w+')
#     file.write("\n".join(map(str, res)))