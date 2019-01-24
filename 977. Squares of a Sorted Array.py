class Solution:
    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = A[i] ** 2
        A.sort()
        print(A)
        return A