class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1,comp1=num1.split('+')
        a=int(real1)
        b=int(comp1[:-1])
        real2,comp2=num2.split('+')
        c=int(real2)
        d=int(comp2[:-1])
        real=(a*c)-(b*d)
        comp=(a*d)+(c*b)
        return str(real)+'+'+str(comp)+'i'
        
      
        