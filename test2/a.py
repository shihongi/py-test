#!/usr/bin/env python

fp = open('/data/iris.csv','r')

count=0
goukei=0
saidai=0
datas=[]
for line in fp:
  data=line.strip().split(',')
  if count>0:
    value=float(data[0])
    goukei+=value
    if saidai<value:
        saidai=value
  count+=1

count-=1
print(goukei)
print(goukei/count)
print(saidai) 

