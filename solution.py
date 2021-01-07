class Solution:
    def thousandSeparator(self, n: int) -> str:
        return (str(format(n, ',d')).replace(",","."))
s=Solution()
int1=1234
print(s.thousandSeparator(int1))    
