import utils

data = [{'Country': 'Colombia', 'Population': 500}, {'Country': 'Bolivia', 'Population': 300}]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input('Type country: ')
    result = utils.population_by_country(data, country)
    print(result)

# Esto es un 'entry point'
if __name__ == '__main__':
    run()