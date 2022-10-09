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
