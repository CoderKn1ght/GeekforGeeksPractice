def reverse(n):
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = (reversed_number * 10) + remainder
        n = n//10
    return reversed_number


def check_even(n):
    while n > 0:
        remainder = n % 10
        if remainder % 2 == 0:
            return True
        n = n//10


def solve(n):
    number_of_additions = 0
    reversed_number = reverse(n)
    while check_even(n + reversed_number):
        number_of_additions += 1
        n += reversed_number
        reversed_number = reverse(n)
    return number_of_additions + 1, n + reverse(n)


print(solve(195))
print(solve(265))