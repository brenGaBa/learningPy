set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove
set_countries.remove('col')
print(set_countries)

# set_countries.remove('arg') # remove with error
# print(set_countries)

set_countries.discard('arg') # descarta si existe, sino no hace nada
set_countries.remove('ar')
set_countries.add('arg')
print(set_countries)

# clear = elimina todo el set
set_countries.clear()
print(set_countries)
print(len(set_countries))