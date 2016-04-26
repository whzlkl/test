# -*- coding: utf-8 -*-

print u'%s中文测试%d' %(u'汪慧中',10)
classmates=['aaa','bbb','ccc']
print len(classmates)
print classmates[2]
classmates.append('ddd')
print classmates[3]
classmates.insert(1,'000')
print classmates[2]
a=classmates.pop()
print a
print len(classmates)
tupletest=(a,10,True)
print tupletest
print tupletest[0]
tupletestb=(1,)
print tupletestb

age=19
if age>=18:
     print 'adult'
elif age>=7:
     print 'teenager'
else:
     print 'kid'

for name in classmates:
    print name

sum=0
n=1
while n<=100:
   sum+=n
   n+=1
print sum,n

d={'a':1,'b':2,'c':3}
print d['a']
print 'd' in d
print d.get('b')
print d.get('d')
print d.get('d',-1)

s=set([1,1,2,3,4,5])
print s
s.add(6)
print s
s.remove(5)
print s