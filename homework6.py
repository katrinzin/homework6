my_dict = {'mother':1975, 'father':1974, 'daughter':1994, 'son':1996}
print('my_dict:', my_dict)
print('Existing value:', my_dict.get('daughter'))
print('Not existing value:', my_dict.get('grandma','нет данных'))
my_dict['son-in-law']=1989
my_dict['random']=2024
print('my_dict new:', my_dict)
a = my_dict.pop('random')
print('Deleted value:', a)
print('Modified dictionary', my_dict)
