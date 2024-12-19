class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        l, r = 0, int(c**0.5)
        while l < r:
            total = l * l + r * r
            if total > c:
                r -= 1
            elif total < c:
                l -= 1
            else:
                return True

        return False
