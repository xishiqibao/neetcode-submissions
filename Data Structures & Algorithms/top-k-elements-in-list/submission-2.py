class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frequency = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] += 1
        for num, c in count.items():
            frequency[c].append(num)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if(len(res) == k):
                    return res
        return res
