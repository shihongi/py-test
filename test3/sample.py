#!/usr/bin/env python

fp = open('/data/iris.csv','r')

ds=[]
for line in fp:
  data=line.strip().split(',')
  ds.append(data)

print(ds)

