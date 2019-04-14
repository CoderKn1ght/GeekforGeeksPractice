def partition(s, low, high):
    pivot = high
    i = low - 1
    for j in range(low, high):
        if s[j] <= s[pivot]:
            i += 1
            s[i], s[j] = s[j], s[i]
    s[i+1], s[high] = s[high], s[i+1]
    return i + 1


def quick_sort(s, low, high):
    if low < high:
        pivot = partition(s, low, high)
        quick_sort(s, low, pivot)
        quick_sort(s[pivot + 1:])


arr = [7, 2, 1, 6, 8, 5, 3, 4]
quick_sort(arr, 0, len(arr)-1)
print(arr)
