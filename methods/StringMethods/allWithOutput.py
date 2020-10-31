#rpartition: Returns a tuple where the string is parted into three parts
string="abc def ghi jkl"
item, space, quantity = string.rpartition(' ')

print(item)
#abc def ghi
print(space)
# #Only Space
print(quantity)
#jkl

string="abc-def-ghi-jkl"
item, space, quantity = string.rpartition('-')

print(item)
#abc-def-ghi
print(space)
#-
print(quantity)
#jkl

#capitalize()	Converts the first character to upper case
print("capitalize(): ","dheeraj kumar".capitalize())
#capitalize(): Dheeraj kumar

#title()	Converts the first character of each word to upper case
print("title(): ","dheeraj kumar".title())
#title():  Dheeraj Kumar

#casefold()	Converts string into lower case
print("casefold(): ","Dheeraj KUMAR".casefold())
#casefold():  dheeraj kumar

#center()	Returns a centered string
print("center(): ","dheeraj kumar".center(30))
#center():          dheeraj kumar

print("padded center(value): ","dheeraj kumar".center(30,"-"))
#padded center(value):  --------dheeraj kumar---------

#count()	Returns the number of times a specified value occurs in a string
print("count(): ","the then there".count("the"))
#count():  3

#string.count(value, start, end) 
print("count(value,start,end): ","the then there".count("the",4,15))
#count(value,start,end):  2

#encode()	Returns an encoded version of the string
print("encode(): ","dheeraj kumar".encode())
#encode():  b'dheeraj kumar'

#string.encode(encoding=encoding, errors=errors) 
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
#b'My name is St\\xe5le'
print(txt.encode(encoding="ascii",errors="ignore"))
#b'My name is Stle'
print(txt.encode(encoding="ascii",errors="namereplace"))
#b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(txt.encode(encoding="ascii",errors="replace"))
#b'My name is St?le'
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
#b'My name is St&#229;le'
#print(txt.encode(encoding="ascii",errors="strict"))
#Error

#endswith()	Returns true if the string ends with the specified value
print("endswith(): ","dheeraj kumar".endswith("mar."))
#endswith():  False

#string.endswith(value, start, end)
print("endswith(value,start,end): ","dheeraj kumar".endswith("raj",0,7))
#endswith(value,start,end):  True

#expandtabs()	Sets the tab size of the string
print("expandtabs()\t: ","\tdheeraj\t\t\t\t kumar".expandtabs())
#expandtabs()	:          dheeraj                          kumar
#string.expandtabs(tabsize) 
print("expandtabs()\t: ","\tdheeraj\t\t\t\t kumar".expandtabs(3))
#expandtabs()	:     dheeraj            kumar

txt="H\te\tl\tl\to"
print(txt.expandtabs(1))
print(txt.expandtabs(2))
print(txt.expandtabs(3))
print(txt.expandtabs(4))
print(txt.expandtabs(5))
print(txt.expandtabs(6))
print(txt.expandtabs(7))
print(txt.expandtabs(8))
print(txt.expandtabs(9))
print(txt.expandtabs(10))
print(txt.expandtabs(11))
print(txt.expandtabs(12))
print(txt.expandtabs(13))
print(txt.expandtabs(14))
print(txt.expandtabs(15))
print(txt.expandtabs(16))
print(txt.expandtabs(17))
print(txt.expandtabs(18))
print(txt.expandtabs(19))
print(txt.expandtabs(20))

#find()	Searches the string for a specified value and returns the position of where it was found
print("find(): ","the then there".find("the"))
#find():  0

#string.find(value, start, end) 
print("find(value,start,end): ","the then there".find("the",5,15))
#find(value,start,end):  9

#format()	Formats specified values in a string
print("format()","For only {price:.2f}".format(price = 49))
#format() For only 49.00

#string.format(value1, value2...) 
txt1 = "My name is {fname}, I'am {age}".format(fname = "Dheeraj", age = 27)
print(txt1)
#My name is Dheeraj, I'am 27
txt2 = "My name is {0}, I'am {1}".format("Dheeraj",27)
print(txt2)
#My name is Dheeraj, I'am 27
txt3 = "My name is {}, I'am {}".format("Dheeraj",27) 
print(txt3)
#My name is Dheeraj, I'am 27

#:< 		Left aligns the result (within the available space)
#:> 		Right aligns the result (within the available space)
#:^ 		Center aligns the result (within the available space)
#:= 		Places the sign to the left most position
#:+ 		Use a plus sign to indicate if the result is positive or negative
#:- 		Use a minus sign for negative values only
#:  		Use a space to insert an extra space before positive numbers (and a minus sign befor negative numbers)
#:, 		Use a comma as a thousand separator
#:_ 		Use a underscore as a thousand separator
#:b 		Binary format
#:c 		Converts the value into the corresponding unicode character
#:d 		Decimal format
#:e 		Scientific format, with a lower case e
#:E 		Scientific format, with an upper case E
#:f 		Fix point number format
#:F 		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#:g 			General format
#:G 			General format (using a upper case E for scientific notations)
#:o 		Octal format
#:x 		Hex format, lower case
#:X 		Hex format, upper case
#:n 			Number format
#:% 		Percentage format

txt = "The universe is {:,} years old."
print(txt.format(13800000000))
#The universe is 13,800,000,000 years old.


#format_map()	Formats specified values in a string


#index()	Searches the string for a specified value and returns the position of where it was found
#Same as find but it gives error if not found
print("index(): ","the then there".index("the"))
#index():  0
#string.index(value, start, end) 
print("index(value,start,end): ","the then there".index("the",5,15))
#index(value,start,end):  9

#isalnum()	Returns True if all characters in the string are alphanumeric
print("isalnum(): ","dheeraj kumar".isalnum())
#isalnum():  False
#Above is False because of space
print("isalnum(): ","dheerajkumar345".isalnum())
#isalnum():  True

#isalpha()	Returns True if all characters in the string are in the alphabet
print("isalpha(): ","dheeraj kumar".isalpha())
#isalpha():  False
#Above is False because of space
print("isalpha(): ","dheerajkumar".isalpha())
#isalpha():  True

#isdecimal()	Returns True if all characters in the string are decimals
print("isdecimal(): ","124.567".isdecimal())
#isdecimal():  False
#Above is False because of '.'
print("isdecimal(): ","134567".isdecimal())
#isdecimal():  True
print("isdecimal(): ","\u0030".isdecimal())
#isdecimal():  True

#isdigit()	Returns True if all characters in the string are digits
print("isdigit(): ","124.567".isdigit())
#isdigit():  False
#Above is False because of '.'
print("isdigit(): ","\u00B2".isdigit())
#isdigit():  True
print("isdigit(): ","\u0030".isdigit())
#isdigit():  True
#Exponents, like ², are also considered to be a digit.

#isidentifier()	Returns True if the string is an identifier
#A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
print("isidentifier(): ","1asdf".isidentifier())
#isidentifier():  False
#Above is False because of starts with number
print("isidentifier(): ","D123".isidentifier())
#isidentifier():  True
print("isidentifier(): ","Dheeraj".isidentifier())
#isidentifier():  True

#islower()	Returns True if all characters in the string are lower case
print("islower(): ","123hee123raj123".islower())
#islower():  True
print("islower(): ","dheeraj123".islower())
#islower():  True

#isnumeric()	Returns True if all characters in the string are numeric
print("isnumeric(): ","1234".isnumeric())
#isnumeric():  True
print("isnumeric(): ","dheeraj123".isnumeric())
#isnumeric():  False
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
print(a.isnumeric())
#True
print(b.isnumeric())
#True
print(c.isnumeric()) 
#False

#isprintable()	Returns True if all characters in the string are printable
print("isprintable()","Dheeraj\nkumar".isprintable())
#isprintable() False
print("isprintable()","Dheeraj kumar".isprintable())
#isprintable() True

#isspace()	Returns True if all characters in the string are whitespaces
print("isspace()","Dheeraj kumar".isspace())
#isspace() False
print("isspace()","".isspace())
#isspace() False
print("isspace()","     ".isspace())
#isspace() True

#isupper()	Returns True if all characters in the string are upper case
print("isupper(): ","123DHEE123RAJ123".isupper())
#isupper():  True
print("isupper(): ","DHEERAJ123".isupper())
#isupper():  True

#join()	Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) 
#John#Peter#Vicky

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
#nameTESTcountry

#ljust()	Returns a left justified version of the string
print("ljust()","Dheeraj kumar".ljust(25),"PASS")
#ljust() Dheeraj kumar             PASS
print("ljust()","Dheeraj kumar".ljust(18),"pass")
#ljust() Dheeraj kumar      pass
#string.ljust(length, character) for padding
print("ljust()","Dheeraj kumar".ljust(28,'-'),"pass")
#ljust() Dheeraj kumar--------------- pass
print("ljust()","Dheeraj kumar".ljust(5,'-'),"pass")
#ljust() Dheeraj kumar pass

#lower()	Converts a string into lower case
print("lower(): ","123DHEE123RAJ123".lower())
#lower():  123dhee123raj123
print("lower(): ","DHEERAJ123".lower())
#lower():  dheeraj123

#lstrip()	Returns a left trim version of the string
print("lstrip(): ","      123DHEE123RAJ123    ".lstrip(),"right end")
#lstrip():  123DHEE123RAJ123     right end
print("lstrip(): ","       DHEERAJ123   ".lstrip(),"right end")
#lstrip():  DHEERAJ123    right end

#string.lstrip(characters) Optional. A set of characters to remove as leading characters
txt = ",,,,,ssaawwb.....banana"
x = txt.lstrip(",.asw")
print(x) 
#b.....banana

#maketrans()	Returns a translation table to be used in translations

#partition()	Returns a tuple where the string is parted into three parts
#string.partition(value) value is compulsory
print("partition()","Dheeraj kumar hello hello world".partition("hello"))
#partition() ('Dheeraj kumar ', 'hello', ' hello world')

#replace()	Returns a string where a specified value is replaced with a specified value
print("replace()","Dheeraj kumar".replace("kumar","chopra"))
#replace() Dheeraj chopra
print("replace()","the there then them".replace("the","he"))
#replace() he here hen hem
#string.replace(oldvalue, newvalue, count) 
print("replace()","the there then them".replace("the","he",2))
#replace() he here then them

#rfind()	Searches the string for a specified value and returns the last position of where it was found
print("rfind(): ","the then there".rfind("the"))
#rfind():  9
#string.find(value, start, end) 
print("rfind(value,start,end): ","the then there".rfind("the",0,8))
#rfind(value,start,end):  4

#rindex()	Searches the string for a specified value and returns the last position of where it was found
print("rindex(): ","the then there".rindex("the"))
#rindex():  9
#string.index(value, start, end) 
print("rindex(value,start,end): ","the then there".rindex("the",0,8))
#rindex(value,start,end):  4

#rjust()	Returns a right justified version of the string
print("rjust()","Dheeraj kumar".rjust(25),"PASS")
#rjust()             Dheeraj kumar PASS
print("rjust()","Dheeraj kumar".rjust(18),"pass")
#rjust()      Dheeraj kumar pass
#string.rjust(length, character) for padding
print("rjust()","Dheeraj kumar".rjust(28,'-'),"pass")
#rjust() ---------------Dheeraj kumar pass
print("rjust()","Dheeraj kumar".rjust(5,'-'),"pass")
#rjust() Dheeraj kumar pass

#rpartition()	Returns a tuple where the string is parted into three parts
print("rpartition()","Dheeraj kumar hello hello world".rpartition("hello"))
#rpartition() ('Dheeraj kumar hello ', 'hello', ' world')

#rsplit()	Splits the string at the specified separator, and returns a 
print("rsplit()","Dheeraj kumar chopra".rsplit())
#rsplit() ['Dheeraj', 'kumar', 'chopra']
#string.rsplit(separator, maxsplit) 
#separator 	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit 	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
print("rsplit()","Dheeraj kumar chopra".rsplit(' ',1))
#rsplit() ['Dheeraj kumar', 'chopra']

#rstrip()	Returns a right trim version of the string
print("rstrip(): ","      123DHEE123RAJ123    ".rstrip(),"right end")
#rstrip():        123DHEE123RAJ123 right end
print("rstrip(): ","       DHEERAJ123   ".rstrip(),"right end")
#rstrip():         DHEERAJ123 right end

#string.rstrip(characters) Optional. A set of characters to remove as leading characters
txt = "banana ,,,,,ssaaww....."
x = txt.rstrip(",.asw")
print(x)
#banana

#split()	Splits the string at the specified separator, and returns a list
print("split()","Dheeraj kumar chopra".split())
#split() ['Dheeraj', 'kumar', 'chopra']
#string.rsplit(separator, maxsplit) 
#separator 	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit 	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
print("split()","Dheeraj kumar chopra".split(' ',1))
#split() ['Dheeraj', 'kumar chopra']

#splitlines()	Splits the string at line breaks and returns a list
print("splitlines()","Dheeraj kumar\nchopra".splitlines())
#splitlines() ['Dheeraj kumar', 'chopra']
print("splitlines()","Dheeraj kumar\nchopra".splitlines(True))
#splitlines() ['Dheeraj kumar\n', 'chopra']

#startswith()	Returns true if the string starts with the specified value
print("startswith()","Dheeraj kumar\nchopra".startswith("Dheeraj"))
#startswith() True
#string.startswith(value, start, end) 
print("startswith()","Dheeraj kumar\nchopra".startswith("kumar",8,15))
#startswith() True

#strip()	Returns a trimmed version of the string
print("strip(): ","      123DHEE123RAJ123    ".strip(),"right end")
#strip():  123DHEE123RAJ123 right end
print("strip(): ","       DHEERAJ123   ".strip(),"right end")
#strip():  DHEERAJ123 right end

#string.rstrip(characters) Optional. A set of characters to remove as leading characters
txt=",,,,,ssaaww.....banana ,,,,,ssaaww....."
x = txt.strip(",.saw")
print(x)
#banana
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x) 
#banana

#swapcase()	Swaps cases, lower case becomes upper case and vice versa
print("swapcase(): "," DHEEraj123   ".swapcase())
#swapcase():   dheeRAJ123   


#translate()	Returns a translated string


#upper()	Converts a string into upper case
print("upper(): "," DHEeraj123   ".upper())
#upper():   DHEERAJ123   

#zfill()	Fills the string with a specified number of 0 values at the beginning
a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))
#00000hello
print(b.zfill(10))
#welcome to the jungle
print(c.zfill(10)) 
#000010.000
