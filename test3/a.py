#!/usr/bin/env python

fp = open('/data/iris.csv','r')

ds=[]
for line in fp:
  data=line.strip().split(',')
  ds.append(data)
  
ds.sort()
print(ds[0])
print('last line')
print(ds[-1])
print(ds[-2])

