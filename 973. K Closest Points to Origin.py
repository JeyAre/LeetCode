''' We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].'''

#Solution1(easier to understand) :
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

#Solution2(with using standart method for this task) :
class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
