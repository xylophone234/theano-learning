import theano.tensor as t
from theano import function
x=t.dscalar('x')
y=t.dscalar('y')
z=x+y
f=function ([x,y],z)

print f(2,3)
print f(16.2,4.2)