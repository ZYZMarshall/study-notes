
#def xiaodan():
#    ret = []
#    for i in range(100):
#        ret.append('鸡蛋%s' %i)
#    return ret

#缺点1：占空间大
#缺点2：效率低 比如需要一万个鸡蛋，需要提前准备好

def xiaodan1():

    for i in range(100):
        yield '鸡蛋{}'.format(i)

alex_lmj = xiaodan1()
jidan = alex_lmj.__next__()
print(jidan)

for i in alex_lmj:

    print(jidan)

#生成器只能遍历一次，也就是无法回溯到最初。