def solve(a):
    visited = [False for i in range(len(a))]
    count = 0

    for i in range(len(a)):
        if not visited[i]:
            rec_stack = set()
            d_f_s(a, i, visited, rec_stack)
            count = max(count, len(rec_stack))
    return count


def d_f_s(arr, i, visited, rec_stack):
    if i in rec_stack:
        return
    visited[i] = True
    rec_stack.add(i)
    d_f_s(arr, arr[i], visited, rec_stack)


print(solve([2, 1, 3, 0, 5, 6, 4]))
