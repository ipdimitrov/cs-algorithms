class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while n!=1:
            if d.get(n, None):
                return False
            d[n] = True
            n_new = 0
            while n:
                n_new += (n%10)**2
                n//=10
            n = n_new
        return True