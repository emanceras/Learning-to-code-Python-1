# Dada la siguiente tupla, crear una lista que solo incluya los valores menores de 5

numbers = (13, 1, 8, 3, 2, 5, 8)
x = []

for i in numbers:
    if i < 5:
        x = x + [i]
print(x)

# Otra forma

numbers = (13, 1, 8, 3, 2, 5, 8)
x = []

for i in numbers:
    if i < 5:
        x.append(i)
print(x)
