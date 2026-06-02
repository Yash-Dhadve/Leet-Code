class Solution {
    public int lengthOfLongestSubstring(String s) {
        int finalSize = 0;
        StringBuilder temp = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            int index = temp.indexOf(String.valueOf(ch));
            if (index != -1) {
                temp.delete(0, index + 1);
            }

            temp.append(ch);

            finalSize = Math.max(finalSize, temp.length());
        }

        return finalSize;
    }
}

public class Q3_Longest_Substring_Without_Repeating_Characters {
    public static void main(String[] args) {
        Solution sol = new Solution();

        String s = "abcabcbb";

        int result = sol.lengthOfLongestSubstring(s);

        System.out.println("Input: " + s);
        System.out.println("Length of longest substring without repeating characters: " + result);
    }
}