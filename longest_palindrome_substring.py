def longest_palindrome_substring(s):
    if len(s) <= 1 or s == s[::-1]:
        return s

    start = 0
    max_length = 1
    for i in range(1, len(s)):
        odd_String = s[i - max_length - 1: i + 1]
        if i - max_length - 1 >= 0 and odd_String == odd_String[::-1]:
            start = i - max_length - 1
            max_length += 2
            continue

        even_string = s[i - max_length: i + 1]
        if even_string == even_string[::-1]:
            start = i - max_length
            max_length += 1

    return s[start:(start + max_length)]
