/**
 * Find the length of the longest substring without repeating characters.
 * @param {string} s - Input string
 * @return {number} Length of the longest substring without repeating characters
 */
var lengthOfLongestSubstring = function(s) {
    const charIndex = {};
    let maxLength = 0;
    let left = 0;
    
    for (let right = 0; right < s.length; right++) {
        // If character is found and is in current window
        if (s[right] in charIndex && charIndex[s[right]] >= left) {
            left = charIndex[s[right]] + 1;
        }
        
        // Update the character index
        charIndex[s[right]] = right;
        
        // Update maxLength
        maxLength = Math.max(maxLength, right - left + 1);
    }
    
    return maxLength;
};

// Main execution
const s = "abcabcbb";
const result = lengthOfLongestSubstring(s);

console.log("Input: " + s);
console.log("Length of longest substring without repeating characters: " + result);
