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
            candidate = s[i:i+search_length]
            # check if this palindrome is contained in larger contiguous value palindrome
            if candidate[0] == candidate[1] and candidate.count(candidate[0]) == len(candidate):
                contiguous_end = i + len(candidate)
                for j in range(contiguous_end, len(s)):
                    if s[j] == s[i]:
                        contiguous_end += 1
                    else:
                        break
                return s[i:contiguous_end]
            return candidate
    return None


def is_palindrome(s):
    for i in range((len(s) // 2)):
        if s[i] != s[-1 - i]:
            return False
    return True
