#!/usr/bin/env python
# -*- coding: utf-8 -*-





fp = open('/data/iris.csv','r')

ds=[]
for line in fp:
    data=line.strip().split(',')
    ds.append(data)


ds.sort()

print(ds)
print('$B%G!<%?$NA0H>$H8eH>$,I=<($5$l$k(B')

print('1$BNsL\$N:G>.CM(B')
print(ds[0][0])

print('1$BNsL\$N:GBgCM(B')
print(ds[-2][0])
