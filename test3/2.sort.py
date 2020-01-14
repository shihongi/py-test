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
