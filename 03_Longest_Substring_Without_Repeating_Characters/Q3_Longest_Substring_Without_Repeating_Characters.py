def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    char_index = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # If character is found and is in current window
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        # Update the character index
        char_index[s[right]] = right
        
        # Update max_length
        max_length = max(max_length, right - left + 1)
    
    return max_length


if __name__ == "__main__":
    s = "abcabcbb"
    result = lengthOfLongestSubstring(s)
    
    print(f"Input: {s}")
    print(f"Length of longest substring without repeating characters: {result}")
