def insertion_sort(s):

    for i in range(len(s) - 1):
        j = i + 1
        while j >= 1 and s[j-1] > s[j]:
            s[j-1], s[j] = s[j], s[j-1]
            j -= 1
    return s


ar = [2, 4, 7, 1, 5, 3]
print(insertion_sort(ar))


