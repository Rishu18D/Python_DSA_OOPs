def longest_substring_without_repeating_characters(s):
    if not s:
        return ""

    char_index_map = {}
    max_length = 0
    start = 0
    longest_substring = ""

    for end in range(len(s)):
        if s[end] in char_index_map:
            start = max(start, char_index_map[s[end]] + 1)

        char_index_map[s[end]] = end
        current_length = end - start + 1

        if current_length > max_length:
            max_length = current_length
            longest_substring = s[start:end + 1]

    return longest_substring

# Example usage:
input_string = str(input("enter the string:"))
result = longest_substring_without_repeating_characters(input_string)
print("Longest substring without repeating characters:", result)
