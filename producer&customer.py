#def producer():
#    ret  = []
#    for i in range(10000):
#        ret.append('Bread%s' %i)
#
#    return ret
#
#def consumer(res):
#    for index, baozi in enumerate(res):
#        print('The%s comsumer eats%s' %(index,baozi))
#
#s = producer()
#consumer(s)

#send() 也可以触发生成器，和next()不同的是send()可以给yield传送一个值
#def test():
#    print('Begin')
#    first = yield
#    print('First yield', first)
#    yield 2
#    print('Second')
#
#t = test()
#res = t.__next__()
#print(res)
#
#res = t.send('I send value to the first yield')
#print(res)

import time

def consumer(name):
    print('I am [%s], I am ready to eat cake' %name)
    while True:
        cake = yield
        time.sleep(1)
        print('%s eats[%s] cake.'%(name,cake))

def producer():
    c1 = consumer('alex')
    c2 = consumer('zyz')
    c1.__next__()
    c2.__next__()
    for i in range(10):
        time.sleep(1)
        c1.send('cake %s'%i)
        c2.send('cake %s'%i)

producer()
