#!/usr/bin/env python

fp = open('/data/iris.csv','r')

ds=[]
for line in fp:
  data=line.strip().split(',')
  ds.append(data)
  

ds.sort()
print(ds)

