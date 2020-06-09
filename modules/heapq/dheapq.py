import heapq
import bisect

#li=[333,433,233,533,833]
#heapq.heapify(li)
#heapq.heappush(li,'a')
#heapq.heappush(li,"asdfs")
#print(list(li))
##,,iterable,key=fun)
##nsmallest(k,iterable,key=fun)
#
#print(heapq.nlargest(3,li))
#print(heapq.nsmallest(4,li))
#print(heapq.heappop(li))
#print(heapq.heappop(li))
#print(heapq.heappushpop(li,344))
#print(heapq.heapreplace(li,"asdf"))
#print(heapq.heappop(li))
#print(heapq.heappop(li))
#print(heapq.heappop(li))
#print(heapq.heappop(li))
#print(len(li))

l=[]
a=heapq.heappush(l,[15,12,1])
a=heapq.heappush(l,[1,12,3])
a=heapq.heappush(l,[11,12,13])
print(heapq.heappop(l))
print(heapq.heappop(l))
print(heapq.heappop(l))


l=[]
bisect.bisect_left(l,[15,12,1])
bisect.bisect_left(l,[1,12,3])
bisect.bisect_left(l,[11,12,13])

print(l)







