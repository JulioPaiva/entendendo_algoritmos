# https://docs.python.org/pt-br/dev/howto/sorting.html

# built-ins
ex_list = [5, 2, 3, 1, 4]
print(sorted(ex_list))

print((ex_list))

ex_list.sort()
print((ex_list))

print(sorted([5, 2, 3, 1, 4], reverse=True))

# A function that returns the 'year' value:


def myFunc(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)


newList = sorted("This is a test string from Andrew".split(), key=str)
print(newList)
newList = sorted("This is a test string from Andrew".split(), key=str.lower)
print(newList)
