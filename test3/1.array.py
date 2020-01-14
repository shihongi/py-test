#!/usr/bin/env python

fp = open('/data/iris.csv','r')

ds=[]
for line in fp:
  data=line.strip().split(',')
  ds.append(data)



print('ds[0] and [0][0]')
print(ds[0])
print(ds[0][0])

print('ds[-1][0] (last)')
print(ds[-1][0])
