### Uso de funciones tipo LAMBDA:
def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

result = increment(10)
print(11)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Full name es: {name.title()} {last_name.title()}'
text = full_name('brenda', 'galan')
print(text)