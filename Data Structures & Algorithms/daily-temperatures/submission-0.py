class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force: double for loop, with time O(n^2)
        res = [0] * len(temperatures)
        stack = []

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = idx - stackInd
            stack.append([t, idx])
        return res