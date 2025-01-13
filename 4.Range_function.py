# Range function have 3 steps (Start, end, step)
a= list(range(10)) #By default its start point is 0. It will print 0-9
b= list(range(1,10)) # Start point is 1, ending point is 10. No step point is given so By default step is 1
c= list(range(0,10,2))# Start point is 0, ending point is 10. Step is 2. It will print from 0-10 with a gap of 2
d= list(range(10,0,-1))

print(a)
print(b)
print(c)
print(d)