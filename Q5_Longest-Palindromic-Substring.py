class Solution(object):
    def longestPalindrome(self, s):
        
        strLength = len(s)
        size = 0
        finalString = ""

        def isPalindrome(s):
            if(s == s[::-1]):
                return True
            else:
                return False

        def isLongest(s):
            if(len(s)>size):
                return True
            else:
                return False


        for i in range(0,strLength+1):
            for j in range(i+1,strLength+1):
                if(isPalindrome(s[i:j]) & isLongest(s[i:j])):
                    size = len(s[i:j])
                    finalString = s[i:j]

        return finalString
                

        

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
