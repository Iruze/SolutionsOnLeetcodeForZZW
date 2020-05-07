class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 1只小猪能够检测的上限是 5桶：如果1h内前4桶没事，则第5桶有毒；
        # 2只小猪上限是 25桶：每5桶混合作为一桶喝下，每个时间段(0-15,15-30,30-45,45-60)两个小猪喝的混合水中只有一桶是来自同一个桶的， 如果中毒，可以判定是哪一桶
        return math.ceil(math.log(buckets, minutesToTest / minutesToDie + 1))
