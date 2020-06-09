#numpy.array() is used to convert a list into a NumPy array
import numpy

#Convert an array to numpy array
#np=numpy.array(<list>,<dataType>)
arr=[2,5,1,3,4,6]
np=numpy.array(arr,float)
reverse=np[::-1]
print(np,reverse)
#ReDimension your array
arr=numpy.reshape(arr,(3,2))
print("Changed shape to 3*2\n",arr)
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print("Changed shape to 3*2\n",change_array)

#We can generate the transposition of an array using the tool numpy.transpose. 
print("Transpose\n",change_array.transpose())
#Flatten the array
print("Flatten:",change_array.flatten())

#Concatenate
a1=[1,2,3,4]
a2=[5,6,7,8]
a3=[9,10,11,12]
a4=[[1,2,3,4],[5,6,7,8],[1,2,3,4]]
a5=[[9,10,11,12],[5,6,7,8],[1,2,3,4]]
print("Concatenate",numpy.concatenate((a1,a2,a3)))
print("Concatenate with 1 axis\n",numpy.concatenate((a4,a5),axis=1))

#Fill zeros
print("Fill zeros",numpy.zeros((1,2), dtype = numpy.int))
#Fill ones
print("Fill ones",numpy.ones((1,2), dtype = numpy.int))

#The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere.
#Like Identity matrix k=0
#numpy.set_printoptions(legacy='1.13')

print("Eye \n",numpy.eye(8, 7, k = 1))

a=numpy.array([1,2,3,4],int)
b=numpy.array([5,6,7,8],int)
print("\nOperators on arrays")
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
print("\nOperator functions on arrays")
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.floor_divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))

#floor
#ceil
#rint
#The rint tool rounds to the nearest integer of input element-wise.
numpy.set_printoptions(legacy='1.13')
l=list(map(float,"1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9".split()))
print("floor ceil and nearest round")
print(numpy.floor(numpy.array(l)))
print(numpy.ceil(numpy.array(l)))
print(numpy.rint(numpy.array(l)))