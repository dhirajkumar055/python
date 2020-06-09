from collections import deque
d=deque("Hello")
#deque(['H', 'e', 'l', 'l', 'o'])
d.popleft()
#deque(['e', 'l', 'l', 'o'])
d.pop()
#deque(['e', 'l', 'l'])
d.append('Z')
#deque(['e', 'l', 'l', 'Z'])
d.appendleft('A')
#deque(['A', 'e', 'l', 'l', 'Z'])
d.clear()
#deque([])
d.append('abc')
#deque(['abc'])
d.extend('123')
#deque(['abc', '1', '2', '3'])
d.extendleft('456')
#deque(['6', '5', '4', 'abc', '1', '2', '3'])
d.rotate(-1)
#deque(['5', '4', 'abc', '1', '2', '3', '6'])
d.rotate(2)
#deque(['3', '6', '5', '4', 'abc', '1', '2'])
d.clear()
d=deque("hello",maxlen=5)
#deque(['h', 'e', 'l', 'l', 'o'], maxlen=5)
d.append('w')
#deque(['e', 'l', 'l', 'o', 'w'], maxlen=5) Notice h is removed
d.extend([1,2,3])
#deque(['o', 'w', 1, 2, 3], maxlen=5) Notice e l l is removed
print(d.maxlen)
#5
#d.maxlen=7 will give error maxlen is not writable
print(d)