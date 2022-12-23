class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index=-1
        md=float(inf)
        for idx,point in enumerate(points):
            if x==point[0] or y==point[1]:
                if abs(x-point[0])+abs(y-point[1])<md:
                    md=abs(x-point[0])+abs(y-point[1])
                    index=idx
        return index
                
        