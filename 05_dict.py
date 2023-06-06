## llenar un diccionario iterativamente
dict = {}
for i in range(1, 11):
    dict[i] = i*2

print(dict)

## Ahora de forma condensada:
dict_v2 = { i: i*2 for i in range(1, 5)}
print(dict_v2)

## Ahora usando valores numéricos y no numéricos:
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

## La forma condensada es:
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

## Como unir dos listas en un diccionario:
names = ['nico', 'lupe', 'santi']
ages = [12, 56, 98]

  ## forma 1:
print(list(zip(names, ages)))

  ## forma 2, creando el diccionario:
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)