def partition(s, low, high):
    pivot = high
    i = low - 1
    for j in range(low, high):
        if s[j] <= s[pivot]:
            i += 1
            s[i], s[j] = s[j], s[i]
    s[i+1], s[high] = s[high], s[i+1]
    return i + 1


def quick_sort(s, low, high, k):
    if low < high:
        pivot = partition(s, low, high)
        if k-1 == pivot:
            return s[k-1], True
        num, decision = quick_sort(s, low, pivot-1, k)
        if decision:
            return num, True
        num, decision = quick_sort(s, pivot + 1, high, k)
        if decision:
            return num, True


arr = [2, 1, 234, 23, 25, 120,22]

num, decision = quick_sort(arr, 0, len(arr)-1, 3)
print(num)
