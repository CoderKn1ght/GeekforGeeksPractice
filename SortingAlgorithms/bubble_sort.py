def bubble_sort(s):
    for i in range(len(s)):
        flag = True
        for j in range(len(s) - i - 1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                flag = False
        if flag:
            break
    return s


ar = [2, 4, 7, 1, 5, 3]
print(bubble_sort(ar))