class Solution:
    def flipAndInvertImage(self, A):
        for row in range(len(A)):
            A[row] = A[row][::-1]

            for invert in range(len(A[row])):
                if A[row][invert] == 0:
                    A[row][invert] = 1
                else:
                    A[row][invert] = 0

        return A