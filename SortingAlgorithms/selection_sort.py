def selection_sort(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while j >= 0 and val < s[j]:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = val
    return s


ar = [2, 4, 7, 1, 5, 3]
print(selection_sort(ar))

