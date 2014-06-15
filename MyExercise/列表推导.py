#coding:utf-8

#不好的写法
#性能低
num = range(10)
size = len(num)
evens = []
i = 0
while i < size:
    if i%2 == 0:
        evens.append(i)
    i+=1
print "evens:",evens

#使用列表推导改写
#高效简洁
evens2 = [i for i in range(10) if i%2 ==0]
print "evens2：",evens2


#不好的写法：
i = 0
seq = ["one","two","three"]
for e in seq:
    seq[i] = "%d:%s"%(i,seq[i])
    i+=1
print "seq:",seq

#使用enumerate改写：
seq1 = ["one","two","three"]
for i,e in enumerate(seq):
    seq1[i] = "%d:%s"%(i,seq1[i])
print "seq1",seq1

#使用列表推导重构：
def _treatment(pos,element):
    return "%d:%s"%(pos,element)
seq2 = ["one","two","three"]
seq2 = [_treatment(i,el) for i,el in enumerate(seq2)]
print "seq2:",seq2



>>> ================================ RESTART ================================
>>> 
evens: [0, 2, 4, 6, 8]
evens2： [0, 2, 4, 6, 8]
seq: ['0:one', '1:two', '2:three']
seq1 ['0:one', '1:two', '2:three']
seq2: ['0:one', '1:two', '2:three']
>>> 
