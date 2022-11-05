OBJECTS = [
    'apple',
    'potato',
    'bread',
    'butter',
    'jelly',
    'water',
    'oil',
    'peanut_butter',
    'chicken',
    'rice',
    'banana',
    'ranch',
    'orange_juice',
    'milk',
]

CONTAINERS = [
    'soup_bowl',
    'salad_bowl',
    'soup_pot',
    'wok',
    'saucier',
    'stock_pot',
    'dutch_oven',
    'skillet',
    'saucepan',
    'frying_pan',
    'saute_pan',
    'saucer',
    'dinner_plate',
]

INIT_STATE = '''
(:objects 
    apple - food
    potato - food
    bread - food
    butter - food
    jelly - food
    water - food
    oil - food
    peanut_butter - food
    chicken - food
    rice - food
    banana - food
    ranch - food
    orange_juice - food
    milk - food

    butter_knife - knife
    chef_knife - knife
    cleaver - knife
    soup_bowl - bowl
    salad_bowl - bowl
    soup_pot - pot
    wok - pot
    saucier - pot
    stock_pot - pot
    dutch_oven - pot
    skillet - pan
    saucepan - pan
    frying_pan - pan
    saute_pan - pan
    saucer - plate
    dinner_plate - plate

    mixture - mixture
)

(:init    
    (toastable bread)
    (sliceable bread)
    (heatable bread)
    (fryable bread)

    (sliceable apple)

    (spreadable butter)
    (sliceable butter)
    (heatable butter)

    (spreadable peanut_butter)
    (pourable peanut_butter)
    (heatable peanut_butter)

    (spreadable jelly)
    (pourable jelly)
    (heatable jelly)

    (pourable water)
    (spreadable water)
    
    (pourable oil)
    (spreadable oil)

    (sliceable chicken)
    (heatable chicken)
    (fryable chicken)

    (sliceable potato)
    (heatable potato)
    (fryable potato)

    (heatable rice)
    (pourable rice)

    (sliceable banana)

    (spreadable ranch)
    (heatable ranch)
    (pourable ranch)

    (pourable orange_juice)
    (spreadable orange_juice)

    (pourable milk)
    (spreadable milk)

    (isclean butter_knife)
    (isclean chef_knife)
    (isclean cleaver)
)
'''

ATTRIBUTES = {
    'apple': {'sliceable', 'spreadon'},
    'potato': {'sliceable', 'heatable', 'fryable', 'spreadon'},
    'bread': {'toastable', 'sliceable', 'heatable', 'fryable', 'spreadon'},
    'butter': {'spreadable', 'sliceable', 'heatable', 'frying'},
    'jelly': {'spreadable', 'pourable', 'heatable'},
    'water': {'pourable'},
    'oil': {'pourable', 'frying'},
    'peanut_butter': {'spreadable', 'pourable', 'heatable'},
    'chicken': {'heatable', 'sliceable', 'fryable', 'spreadon'},
    'rice': {'heatable', 'pourable'},
    'banana': {'sliceable', 'spreadon'},
    'ranch': {'spreadable', 'heatable'},
    'orange_juice': {'pourable'},
    'milk': {'pourable'},

    'soup_bowl': {'bowl'},
    'salad_bowl': {'bowl'},
    'soup_pot': {'pot'},
    'wok': {'pot'},
    'saucier': {'pot'},
    'stock_pot': {'pot'},
    'dutch_oven': {'pot'},
    'skillet': {'pan'},
    'saucepan': {'pan'},
    'frying_pan': {'pan'},
    'saute_pan': {'pan'},
    'saucer': {'plate'},
    'dinner_plate': {'plate'},
}