class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


def main():
    nums = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    result = sol.twoSum(nums, target)

    print("Indices:", result)


if __name__ == "__main__":
    main()