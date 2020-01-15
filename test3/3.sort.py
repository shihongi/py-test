#!/usr/bin/env python
# -*- coding: utf-8 -*-





fp = open('/data/iris.csv','r')

ds=[]
for line in fp:
  data=line.strip().split(',')
  ds.append(data)
  

ds.sort()

print(ds)
print('データの前半と後半が表示される')

print('1列目の最小値')
print(ds[0][0])

print('列目の最大値')
print(ds[-2][0])
