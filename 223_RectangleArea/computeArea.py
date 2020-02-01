class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (C - A) * (D - B) + (G - E) * (H - F) - max((min(G, C) - max(A, E)), 0) * max((min(D, H) - max(B, F), 0))
