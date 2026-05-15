class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range (len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) #count the number of occurence, default val of 0
        for n, c in count.items(): # go through each val we counted
            freq[c].append(n)

        res = []
        for i in range (len(freq) -1, 0, -1): # len minus 1, till 0 in the negative order
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        