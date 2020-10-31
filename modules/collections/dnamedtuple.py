#June 10,2020 #Bahadurgarh #DheerajKumarChopra
#namedtuples are easy to create, lightweight object types
#They turn tuples into convenient containers for simple tasks
#With namedtuples, you don’t have to use integer indices for accessing members of a tuple
from collections import namedtuple
Point = namedtuple('Name','x,y')
pt1 = Point(1,2)
pt2 = Point(3,41)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print(dot_product)


Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Class = 'Y', Colour = 'Cyan')
print(xyz)
print(xyz.Class)

#https://docs.python.org/2/library/collections.html
#_make : Class method that makes a new instance from an existing sequence or iterable.
#We use "_make" as it can accept iterables or sequence while populating an entry into the namedtuple object.

#eg. namedtuple was initialized as "Name Marks Grade" Entries: Sam 102 B

#"_make" Will now read the split string as Sam, 102, B and map them to our expected sequence Name=Sam,Marks=102 & Grade=C