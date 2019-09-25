# functions
def make_dough(ingredient1, ingredient2):
   if ((ingredient1, ingredient2) == ('wheat', 'water')) or ((ingredient1, ingredient2) == ('water', 'wheat')):
       return('dough')
   else:
       return('not dough')

def wood_oven(ingredient):
   if (ingredient) == ('dough'):
       return('Naan bread')
   else:
       return('fire')

def run_naan_factory(ingredient1, ingredient2):
    # need to make dough
    doughr = make_dough(ingredient1,ingredient2)
    # needs to send dough to the oven
    result_bread = wood_oven(doughr)
    # I want it to make naan bread
    return result_bread
# Calling of functions