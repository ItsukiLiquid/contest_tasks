class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix2 = [matrix[i].copy() for i in range(len(matrix))]
        # for i in range(len(matrix)):
        #     matrix2.append(matrix[i])
        print(f"m: {matrix}")
        print(f"m2: {matrix2}")
            # for j in range(len(matrix)):
            #     matrix[i][j] = matrix2[i][j]
        # we check every ith element of all lists, then put it all in reversed order for ith list
        # 00 01 02, 10 11 12, 20 21 22
        # 20 10 00, 21 11 01, 22 12 02
        # j+++, i+++ (j+n)(i+n)
        # n-1-j, i
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = matrix2[len(matrix) - 1 - j][i]
                print(f"[i, j]: {i, j}, m[i][j]: {matrix[i][j]}, m2[i][j]: {matrix2[i][j]}, changing pos: [{len(matrix) - 1 - j}][{i}]")
                # 00 -> 20, 01 -> 10, 02 -> 00
                # 10 -> 21, 11 -> 11, 12 -> 01
                # 20 -> 22, 21 -> 12, 22 -> 02

s = Solution()
s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])