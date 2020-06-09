import re
#re.match: searches in the begining
#re.search: searches in the whole string
#Syntax
#re.match(pattern,string,flags)
#re.search(pattern,string,flags)

print(re.match("c","abcdef"))
print(re.search("c","abcdef"))
print(bool(re.match("c","abcdef")))
print(bool(re.match("a","abcdef")))
print(re.match("a","abcdef").group()) #group() to print match; Error if doesn't match
print(re.search("c","abcdef").group())
print(re.search('n.+',"abcdefnc abcd").group())
print(re.search("c","abdef\nc").start())  #Starting index
print(re.search("c","abdef\nc").end())  #Ending index
print(re.search('asd|bdic|the',"abc the").group())
print(re.findall('asd|bdic|the',"abc the asd"))
print(re.findall('aaa',"aaaaaaaaaa"))


#Index of last occurence of a pattern
#index=string.rindex(pattern)