class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        lo, hi = 0, len(people) - 1
        ans = 0
        people.sort()
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
            ans += 1
        return ans
