#coding:utf-8

s = 'abcdefghi'

#1
s1 = s[::-1]
print's1 :',s1

#2
lis = list(s)
lis.reverse()
s2 = ''.join(lis)
print 's2 :',s2

#2
from functools import reduce

s3 = reduce(lambda x,y : y+x, s)
print 's3 :',s3
