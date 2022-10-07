def length_of_longest_substring(s: str) -> int:
    """Given a string s, find the length of the longest substring without repeating characters."""
    current_substring = ''
    len_longest_substring = 0
    for char in s:
        if char in current_substring:
            len_current_substring = len(current_substring)
            if len_current_substring > len_longest_substring:
                len_longest_substring = len_current_substring
            position_of_duplicate_char = current_substring.find(char)
            current_substring = current_substring[position_of_duplicate_char+1:] + char
        else:
            current_substring += char
    len_current_substring = len(current_substring)
    if len_current_substring > len_longest_substring:
        len_longest_substring = len_current_substring
    return len_longest_substring
