class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, r = 0, r * c - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // c, m % c
            if target == matrix[row][col]:
                return True
            elif(target < matrix[row][col]):
                r = m - 1
            else:
                l = m + 1
        return False

