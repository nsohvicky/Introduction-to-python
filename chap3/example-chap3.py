years_list = [1990, 1991, 1992, 1993, 1994, 1995]
print(years_list)
print(years_list[0])
print(years_list[5])

things = ["mozzarella","cinderella", "salmonella"]
print(things)
print(things[1].upper())
print(things[0].upper())
del things[2]
print(things)

suprise = ["Groucho", "Chico", "Harpo"]
print(suprise)
print(suprise[2].lower())
print(suprise[2].upper())

e2f = {'dog': 'chien', 'cat' : 'chat', 'walrus': 'morse'}
print(e2f ['walrus'])
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
    print(f2e)
    print(f2e['chien'])

print(set(e2f.keys()))

life = {'animals':{'cat':['Henri', 'Grumpy', 'Lucy'], 'octopi':{}, 'emus':{}},

'plants':{},
'others':{}}
print(life.keys())
print(list(life.keys()))
print(list(life['animals'].keys()))
print(life['animals']['cat'])

#ex
years_list = [1990,1991,1992,1993,1994,1995,1996]
print(years_list[3])
print(years_list[6])

things =["mozzarella","cinderella", "salmonella"]
print(things)
print(things[1].upper())
print(things[0].upper())
del things[2]
print(things)


surprise =["Groucho", "Chico", "Harpo"]
print(surprise[2].lower())
print(surprise[2].upper())