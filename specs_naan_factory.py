from naan_functions import*

# As a user I can pass'wheat' and water to the function to make dough, so that I can make dough
                                    # evaluates --> True or False (Boolean)
print('Testing make_dough, with wheat and water --> dough to come out')
print(make_dough('wheat','water') == 'dough')

print("Testing make_dough, with 'sand and cement' --> not dough to come out")
print(make_dough('sand','cement') == 'not dough')

# As a user I can pass 'dough' to the function oven_wood, so that I can make 'bread
print('Testing wood_oven, with dough --> Naan bread to come out')
print(wood_oven('dough') == 'Naan bread')

print('Testing wood_oven, with cement --> Fire')
print(wood_oven('how') == 'fire')