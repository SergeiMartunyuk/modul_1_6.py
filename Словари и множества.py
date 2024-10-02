my_dict = {'Sergei': 1999, 'Mary': 2002, 'Nik': 2010}
print(my_dict)
print(my_dict['Mary'])
print(my_dict.get('Anna'))
my_dict.update({'Dima': 1988, 'Lex': 2000})
A = my_dict.pop('Nik')
print(A)
print(my_dict)

my_set = {1,3,5,7,5,3}
print(my_set)
my_set.add(4)
my_set.add(6)
my_set.remove(7)
print(my_set)