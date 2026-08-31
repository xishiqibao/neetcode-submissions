class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            diff = target - numbers[i]
            if(numbers[j] == diff):
                return [i + 1, j + 1]
            elif (numbers[j] < diff):
                i += 1
            else:
                j -=1
        return []
