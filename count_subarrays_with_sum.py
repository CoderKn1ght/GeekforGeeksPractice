def arrSum(a, sum):
    start = 0
    n = len(a)
    curr_sum = a[0]
    i = 1
    count = 0
    while i <= n:
        while curr_sum > sum and start < i - 1:
            curr_sum -= a[start]
            start += 1
        if curr_sum == sum:
            print(start, i-1)
            # Count number of continuous sub-arrays
            count += 1
        if i < n:
            curr_sum += a[i]
        i += 1
    return count


array = [1, 32, 20, 3, 10, 5]
number = arrSum(array, 33)
print(number)
