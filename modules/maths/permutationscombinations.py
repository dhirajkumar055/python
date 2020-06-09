#How to calculate permutations and combinations?
from itertools import permutations
from itertools import combinations
#from math import comb
import math
p=permutations([1,2,3])
c=combinations([1,2,3],2)
for i in p:
 print(i)

for i in c:
 print(i)


print(comb(3,2))

#Catalan Number
#return (int)(comb(2*n,n)/(n+1))

(int)(ceil(sqrt()))