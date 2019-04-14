def partition_labels(s):
    last = {c: i for c, i in enumerate(s)}
    j, anchor = 0, 0
    ans = []
    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1


