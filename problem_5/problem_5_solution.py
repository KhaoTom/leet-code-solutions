def longest_palindrome(s):
    # easy early out
    if is_palindrome(s):
        return s

    # first character is always a palindrome
    longest = s[0]

    # search for palindromes of increasing lengths up to 1 less the length of input (which we already checked)
    search_length = 2
    while search_length < len(s):
        candidate = search_palindromes(s, search_length)
        if candidate is None:
            search_length += 1
            continue
        search_length = len(candidate) + 1
        longest = candidate

    return longest


def search_palindromes(s, search_length):
    if search_length == 1:
        return s[0]

    for i in range(0, len(s) - search_length + 1):
        if is_palindrome(s[i:i+search_length]):
            return s[i:i+search_length]
    return None


def is_palindrome(s):
    return s == s[::-1]


def first_solution(s) :
    longest = s[0]
    seen_values = {s[0]}
    for i in range(1, len(s)):
        if s[i] in seen_values:
            candidate = find_longest_palindrome_starting_with_last_value(s[s.find(s[i]):i + 1])
            if len(candidate) > len(longest):
                longest = candidate
        else:
            seen_values.add(s[i])

    return longest


def find_longest_palindrome_starting_with_last_value(s):
    last = s[-1]
    longest = ''
    for i in range(len(s)):
        if s[i] == last:
            candidate = s[i:]
            if candidate == candidate[::-1] and len(candidate) > len(longest):
                longest = candidate
    return longest
