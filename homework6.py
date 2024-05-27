# Словари

my_dict = {'Denis': 1985, 'Anton': 1990, 'Sasha': 1992}
print(my_dict)
print(my_dict['Sasha'])
my_dict['Alex'] = 1987
print(my_dict['Alex'])
my_dict.update({'Pasha': 2000,
                'Masha': 2001})
print(my_dict)
a = my_dict.pop('Anton')
print(my_dict)
print(a)

# Множества

my_set = {1, 1, 1, 1, 2, 2, 3, 3, 4, 4}
print(my_set)
my_set.add(5)
my_set.add(6)
print(my_set)
my_set.discard(3)
print(my_set)
