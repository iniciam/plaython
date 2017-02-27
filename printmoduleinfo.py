def showModuleName():
	print __doc__

def getModuleFile():
	return __file__

a = showModuleName()
b = getModuleFile()

print a,b

# function is an object, first class citizen in python

def f():
	"""This function print a message"""
	print "Today is a good day"

print isinstance(f, object)
print id(f)

print f.func_doc
print f.func_name

# passing function as another function input
def a():
	pass

def b():
	pass

def c(a):
	print id(a)

d = (a,b,c)

for i in d:
	print i

c(a)
c(b)

# 3 kinds of functions
from math import sqrt

def cube(x):
	return x * x * x

print abs(-1)
print cube(9)
print sqrt(81)

# return multiple value from function

n = [1, 2, 3, 4, 5]

def stats(x):
	mx = max(x)
	mn = min(x)
	ln = len(x)
	sm = sum(x)
	return mx, mn, ln, sm

mx, mn, ln, sm = stats(n)

print stats(n)

print mx, mn, ln, sm

# power function

def power(x, y=2):
	r = 1
	for i in range(y):
		r = r * x
	
	return r

print power(3)
print power(3, 3)
print power(5, 5)

# arbitrary arguments

def sum(*args):
	'''this sum accept arbitrary arguments'''
	r = 0
	for i in args:
		r += i
	return r

print sum.__doc__
print sum(1,2,3)
print sum(1,2,3,4,5)

# function that accept arbitrary dictionary

def display(**details):
	
	for i in details:
		print "%s : %s" % (i, details[i])

display(name="David", age=36, kelamin="Male", rumah="punggol")

# arguments are passed by reference to function
n = [1, 2, 3, 4, 5]

print "original list:", n

def f(x):
	x.pop()
	x.pop()
	x.insert(0,0)
	x.insert(2,8)
	print "inside f():", x

f(n)
print "After function call:", n

# variable local scope
name = "david"
age = 36

def f():
	name = "vicky"
	print "Within function name=", name
	print "Within function age=", age

print "Outside function name=", name
print "Outside function age=", age
f()

# global var can be read inside function, but to change it we must use global keyword
name = "david"

def f():

	global name
	name = "vicky"
	print "inside function name=", name

print "outside function name=", name
f()
print "outside function name=", name

# anonymous function using lambda function and map
cs = [-10, 0 , 15, 30, 40]

ft = map(lambda t: (9.0/5)*t + 32, cs)
print ft

y = 6
z = lambda x: x * y
print z(8)

































































































