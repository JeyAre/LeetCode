class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0
        for i in S:
            if (i in J):
                count = count + 1

        return count
