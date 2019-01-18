def get_population():

    with open('population.txt', 'r', encoding = 'utf-8') as f:
        for i in f:
            yield i

g = get_population()
kk = g.__next__()
print(eval(kk)['population'])
#s1 = eval(g.__next__())
#print(type(s1))
#print(s1['population'])
#for p in g:
#    pdict = eval(p)
#    print(pdict['population'])

#all_pop = sum(eval(p)['population'] for p in g) 