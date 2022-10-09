"""
TODO: This solution is slow. Can it be sped up?
"""


def longest_palindrome(s):
    longest = s[0]
    seen_values = {s[0]}
    for i in range(1, len(s)):
        if s[i] in seen_values:
            candidate = find_longest_palindrome_starting_with_last_value(s[s.find(s[i]):i+1])
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
