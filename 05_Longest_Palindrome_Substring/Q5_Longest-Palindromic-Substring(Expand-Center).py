class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        longest = ""

        for i in range(len(s)):

            # Odd length palindrome
            odd = expand(i, i)

            # Even length palindrome
            even = expand(i, i + 1)

            current = odd if len(odd) > len(even) else even

            if len(current) > len(longest):
                longest = current

        return longest
        

if __name__ == "__main__":
    sol = Solution()

    # Test cases (same style as LeetCode)
    test_cases = [
        "babad",
        "cbbd",
        # "boqylncwfahjzvawrojyhqiymirlkfzkhtvmbjnbfjxzewqqqcfnximdnrxtrbafkimcqvuprgrjetrecqkltforcudmbpofcxqdcirnaciggflvsialdjtjnbrayeguklcbdbkouodxbmhgtaonzqftkebopghypjzfyqutytbcfejhddcrinopynrprohpbllxvhitazsjeyymkqkwuzfenhphqfzlnhenldbigzmriikqkgzvszztmvylzhbfjoksyvfdkvshjzdleeylqwsapapduxrfbwskpnhvmagkolzlhakvfbvcewvdihqceecqhidvwecvbfvkahlzlokgamvhnpkswbfrxudpapaswqlyeeldzjhsvkdfvyskojfbhzlyvmtzzsvzgkqkiirmzgibdlnehnlzfqhphnefzuwkqkmyyejszatihvxllbphorprnyponircddhjefcbtytuqyfzjpyhgpobektfqznoatghmbxdouokbdbclkugeyarbnjtjdlaisvlfggicanricdqxcfopbmducroftlkqcertejrgrpuvqcmikfabrtxrndmixnfcqqqwezxjfbnjbmvthkzfklrimyiqhyjorwavzjhafwcnlyqob"
    ]

    for s in test_cases:
        result = sol.longestPalindrome(s)
        print(f"Input: {s} -> Output: {result}")
