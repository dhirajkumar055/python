 return sum(1 for i in xrange(n) if a[i]<=t<=b[i])

a = sorted((len(v), i, v.lower()) for i, v in enumerate(text.split(' ')))
        a = [i[-1] for i in a]
    
    
            r = []
        a = map(set, favoriteCompanies)
        for i, v in enumerate(favoriteCompanies):
            if any(all(y in w for y in v)
                   for j, w in enumerate(a)
                   if i != j): continue
            r.append(i)
        return r
    
    
return sorted(points, key=lambda e: e[0]**2+e[1]**2)[0:K]



class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        return next((idx + 1 for idx, w in enumerate(words) if w.startswith(searchWord)), -1)
    
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        value = [0]
        for c in s:
            value.append(value[-1] + int(c in "aeiou"))
        ans = 0
        for i in range(k, len(s) + 1):
            ans = max(ans, value[i] - value[i - k])
        return ans