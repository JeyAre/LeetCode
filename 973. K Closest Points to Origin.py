class Solution:
    def kClosest(self, points, K):
        rez = dict(); finalList = []

        for i in range(len(points)):
            sqrt = (points[i][0]) ** 2 + (points[i][1]) ** 2
            rez[sqrt] = points[i]
        for j in range(K):
            value = rez.get(min(rez))
            finalList.append(value)
            rez.pop(min(rez))
        return finalList
