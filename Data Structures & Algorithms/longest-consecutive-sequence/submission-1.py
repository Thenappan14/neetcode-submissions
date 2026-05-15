class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        sorted_nums = sorted(set(nums)) 
        print(sorted_nums)

        count = 1
        longest = 1

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                count += 1
            else:
                count = 1
            
            longest = max(longest, count)

        return longest

        