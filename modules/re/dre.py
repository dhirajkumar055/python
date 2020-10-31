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

text='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
0987654321
hello world
this is a text
This is a text

Ha HaHa

MetaCharacters, Which needs to be escaped:
. ^ $ * +? { } [ ] \ | ( )

234-234-678
567.235.456

567-235-456
800-235-456
900-235-456
90000-235-456
9-235-456
url.com

bat
cat
mat
tat
hat

. - Any Character Except newline
\d - Digit(0-9)
\D - Not a Digit (0-9)
\w - Word Character  (a-z,A-Z,0-9,_)
\W - Not a word character
\s - whitespace (space tab newline)
\S - Not a whitespace

Anchors
\b - word boundary
\B - Not a word boundary
^ - Begining of string
$ - End of a string
[] - Matches characters in brackets
[^ ] - Matches Characters NOT in 

Quatifiers
* : 0 or more
+ : 1 or more
? : 0 or 1
{3} : Exact Number
{3,4} : Range of numbers(minimum, maximum)

Mr. Tavid
Mr Dheeraj
Ms Davis
Mrs. Robin
Mr. D

'''


#Index of last occurence of a pattern
#index=string.rindex(pattern)

#Raw string
print(r'\tTab')
#Without raw string
print('\tTab')

#pattern=lambda x,y: x*y
#print(pattern(2,4))

pattern=re.compile(r'abc')
matches=pattern.finditer(text)

for match in matches:
    print(match)
#Check for span
print(text[1:4])

pattern=re.compile(r'\.')
matches=pattern.finditer(text)
for match in matches:
    print(match)

pattern=re.compile(r'url\.com')
matches=pattern.finditer(text)
for match in matches:
    print(match)

pattern=re.compile(r'\d')
matches=pattern.finditer(text)
for match in matches:
    print(match)
    
pattern=re.compile(r'\D')
matches=pattern.finditer(text)
#for match in matches:
#    print(match)

pattern=re.compile(r'\w')
matches=pattern.finditer(text)
#for match in matches:
#    print(match)

pattern=re.compile(r'\W')
matches=pattern.finditer(text)
#for match in matches:
#    print(match)

pattern=re.compile(r'\s')
matches=pattern.finditer(text)
#for match in matches:
#    print(match)

pattern=re.compile(r'\S')
matches=pattern.finditer(text)
#for match in matches:
#    print(match)

pattern=re.compile(r'\bHa')
matches=pattern.finditer(text)
for match in matches:
    print(match)
    
pattern=re.compile(r'\BHa')
matches=pattern.finditer(text)
for match in matches:
    print(match)

newtext="Starting with Start"
pattern=re.compile(r'^Start')
matches=pattern.finditer(newtext)
for match in matches:
    print(match)

pattern=re.compile(r'^NotStart')
matches=pattern.finditer(newtext)
for match in matches:
    print(match)

newtext="Ending with End"
pattern=re.compile(r'End$')
matches=pattern.finditer(newtext)
for match in matches:
    print(match)

newtext="Ending with End"
pattern=re.compile(r'EndNot$')
matches=pattern.finditer(newtext)
for match in matches:
    print(match)
    

pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d')
matches=pattern.finditer(text)
for match in matches:
    print(match)

    
pattern=re.compile(r'[MF],.*@.*.com')

with open('../../files/csv/file.csv','r') as f:
    contents=f.read()
    matches=pattern.finditer(contents)
    for match in matches:
        print(match)
        
pattern=re.compile(r'[98]00-\d\d\d-\d\d\d')
matches=pattern.finditer(text)
for match in matches:
    print(match)

print()
pattern=re.compile(r'\d{0,5}-\d{3}.\d{3}')
matches=pattern.finditer(text)
for match in matches:
    print(match)
    
#In below example ^ works as an negation
pattern=re.compile(r'[^b]at\b')
matches=pattern.finditer(text)
for match in matches:
    print(match)
   
pattern=re.compile(r'Mr\.?\s[A-Z]\w*')
matches=pattern.finditer(text)
for match in matches:
    print(match)
    
print()
pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches=pattern.finditer(text)
for match in matches:
    print(match)
    
#EmailAddress
#pattern=re.compile(r'[a-zA-Z0-9-._+]+@[a-zA-Z0-9-]\.[a-zA-Z0-9-.]')

urls='''
https://www.google.com
http://helloworld.com
http://google.commy
https://www.abc.ode
'''
pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches=pattern.finditer(urls)
for match in matches:
    #print(match.group(0))
    print(match.group(2))

subbed_urls=pattern.sub(r'\2\3',urls)
print(subbed_urls)

pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#findall prints only tuple of group
#if there are no groups it will all the matches
matches=pattern.findall(urls)
for match in matches:
    #print(match.group(0))
    print(match)


sentence='Start a senetence and then bring it to an end'
pattern=re.compile(r'Start')
#Below returns error because match doesn't return iterable like finditer or findall
#matches=pattern.match(sentence)
#match searches only in the begining of the string
print(pattern.match(sentence))

pattern=re.compile(r'and')
print(pattern.match(sentence))

#To search in whole sentence or string
print(pattern.search(sentence))

#Returns None if not found
pattern=re.compile(r'aasdf')
print(pattern.search(sentence))

pattern=re.compile(r'START',re.IGNORECASE)
print(pattern.match(sentence))

pattern=re.compile(r'START',re.I)
print(pattern.match(sentence))

