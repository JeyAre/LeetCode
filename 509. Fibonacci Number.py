class Solution:
    def fib(self,N):
        if N == 0:
            return 0
        last = 0
        now = 1
        for i in range(1,N):
            now = now + last
            last = now - last
        return  now
