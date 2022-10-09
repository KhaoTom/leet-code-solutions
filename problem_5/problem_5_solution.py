def longest_palindrome(s):
    if is_palindrome(s):
        return s
    longest = s[0]
    seen_values = {s[0]}
    last_value = s[0]
    last_value_sequence_length = 1
    for i in range(1, len(s)):
        c = s[i]
        if c == last_value:
            last_value_sequence_length += 1
        else:
            # check for long sequence palindrome at boundaries between different values
            if last_value_sequence_length > len(longest):
                longest = s[i-last_value_sequence_length:i]

            if c in seen_values:
                # we've seen this value before and its not part of last value sequence, check for palindromes
                candidate = find_longest_palindrome_starting_with_last_value(s[s.find(c):i+1])
                if len(candidate) > len(longest):
                    longest = candidate
            else:
                # new value, can't be a palindrome longer than the first value in the input
                seen_values.add(c)

            last_value_sequence_length = 1
            last_value = c

    # catch case like 'abbb' where longest is a sequence of repeated values at the end
    if last_value_sequence_length > len(longest):
        longest = s[len(s) - last_value_sequence_length:len(s)]

    return longest


def find_longest_palindrome_starting_with_last_value(s):
    last = s[-1]
    longest = ''
    for i in range(len(s)):
        if s[i] == last:
            candidate = s[i:]
            if is_palindrome(candidate) and len(candidate) > len(longest):
                longest = candidate
    return longest


def is_palindrome(s):
    for i in range((len(s) // 2)):
        if s[i] != s[-1 - i]:
            return False
    return True
