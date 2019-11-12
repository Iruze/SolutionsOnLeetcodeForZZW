class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        if C <= 0 or R <= 0:
            return []
        d = dict()
        for i in range(R):
            for j in range(C):
                distance = abs(i - r0) + abs(j - c0)
                if distance not in d:
                    d[distance] = [[i, j]]
                else:
                    d[distance].append([i, j])
        output = []
        for dist in sorted(d.keys()):
            output.extend(d[dist])
        return output
