#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int n = strlen(s);
    int maxLength = 0;
    int charIndex[256];
    
    // Initialize charIndex array with -1
    for (int i = 0; i < 256; i++) {
        charIndex[i] = -1;
    }
    
    int left = 0;
    
    for (int right = 0; right < n; right++) {
        // If character is found and is in current window
        if (charIndex[(unsigned char)s[right]] >= left) {
            left = charIndex[(unsigned char)s[right]] + 1;
        }
        
        // Update the character index
        charIndex[(unsigned char)s[right]] = right;
        
        // Update maxLength
        int currentLength = right - left + 1;
        if (currentLength > maxLength) {
            maxLength = currentLength;
        }
    }
    
    return maxLength;
}

int main() {
    char s[] = "abcabcbb";
    
    int result = lengthOfLongestSubstring(s);
    
    printf("Input: %s\n", s);
    printf("Length of longest substring without repeating characters: %d\n", result);
    
    return 0;
}
