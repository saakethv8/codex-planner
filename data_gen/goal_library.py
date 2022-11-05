# conditions: [cont, obj1, obj2]

gdict = {}

# Easy one-predicate goals

gdict["pick_and_place_simple"] = \
{
    'pddl' :
    '''
    (define (problem {obj1}_in_{cont}) (:domain cooking)
        {init}

        (:goal (placedon {obj1} {cont})
        )
    )
    ''',
    'templates': ['put the {obj1} in the {cont}',
                   'place some {obj1} on a {cont}'],
    'conditions': [set(), set(), set()]
}

gdict["heat"] = \
{
    'pddl' :
    '''
    (define (problem heat_{obj1}) (:domain cooking)
        {init}

        (:goal (heated {obj1})
        )
    )
    ''',
    'templates': ['heat the {obj1}',
                   'warm up some {obj1}',
                   'produce a heated {obj1}'],
    'conditions': [set(), {'heatable'}, set()]
}

gdict["spread"] = \
{
    'pddl' :
    '''
    (define (problem spread_{obj1}_{obj2}) (:domain cooking)
        {init}

        (:goal (spreadon {obj1} {obj2})
        )
    )
    ''',
    'templates': ['spread some {obj1} on {obj2}',
                    'cover the {obj2} with {obj1}'],
    'conditions': [set(), {'spreadable'}, {'spreadon'}]
}

gdict["pour_serve"] = \
{
    'pddl' :
    '''
    (define (problem pour_{obj1}_serve_{cont}) (:domain cooking)
        {init}

        (:goal (and 
            (placedon {obj1} {cont})
            (served {cont})
        ))
    )
    ''',
    'templates': ['serve a {cont} with {obj1}',
                    'pour {obj1} into a {cont} and serve it'],
    'conditions': [set(), {'pourable'}, set()]
}

# Moderate multi-predicate goals

gdict["pick_clean_then_place_slice"] = \
{
    'pddl' :
    '''
    (define (problem clean_slice_{obj1}_in_{cont}) (:domain cooking)
        {init}

        (:goal (and 
            (washed {obj1})
            (sliced {obj1})
            (placedon {obj1} {cont})
        ))
    )
    ''',
    'templates': ['put clean slices of {obj1} in a {cont}',
                    'clean some sliced {obj1} and put it in a {cont}'],
    'conditions': [set(), {'sliceable'}, set()]
}

gdict["serve_two_hot"] = \
{
    'pddl' :
    '''
    (define (problem serve_{obj1}_and_{obj2}_hot) (:domain cooking)
        {init}

        (:goal (and 
            (heated {obj1})
            (heated {obj2})
            (placedon {obj1} dinner_plate)
            (placedon {obj2} dinner_plate)
            (served dinner_plate)
        ))
    )
    ''',
    'templates': ['heat and serve a {obj1} and {obj2}',
                    'serve the {obj1} and {obj2} with both heated'],
    'conditions': [set(), {'heatable'}, {'heatable'}]
}

gdict["mix_slice"] = \
{
    'pddl' :
    '''
    (define (problem mix_sliced_{obj1}_and_{obj2}) (:domain cooking)
        {init}

        (:goal (and 
            (sliced {obj1})
            (sliced {obj2})
            (mixture_contains mixture {obj1})
            (mixture_contains mixture {obj2})
        ))
    )
    ''',
    'templates': ['mix slices of {obj1} and {obj2}',
                    'slice and mix {obj1} and {obj2}',
                    'create a mixture of sliced {obj1} and {obj2}'],
    'conditions': [set(), {'sliceable'}, {'sliceable'}]
}

gdict["fry_pot"] = \
{
    'pddl' :
    '''
    (define (problem fry_{obj1}_{obj2}_{cont}) (:domain cooking)
        {init}

        (:goal (and 
            (fried {obj1})
            (placedon {obj1} {cont})
            (placedon {obj2} {cont})
        ))
    )
    ''',
    'templates': ['fry {obj1} on a {obj2}ed {cont}',
                    'fry {obj1} using {obj2} on a {cont}',
                    'with a {cont} and {obj2}, fry {obj1}'],
    'conditions': [{'pot'}, {'fryable'}, {'frying'}]
}

gdict["slice_heat"] = \
{
    'pddl' :
    '''
    (define (problem slice_heat_{obj1}) (:domain cooking)
        {init}

        (:goal (and 
            (sliced {obj1})
            (heated {obj1})
        ))
    )
    ''',
    'templates': ['slice a heated {obj1}',
                    'heat slices of {obj1}',
                    'heat and slice the {obj1}'],
    'conditions': [set(), {'sliceable','heatable'}, set()]
}

# Complex opaque goals

gdict["serve_sandwich"] = \
{
    'pddl' :
    '''
    (define (problem serve_toast_sandwich_{obj1}_{obj2}) (:domain cooking)
        {init}

        (:goal (and 
            (toasted bread)
            (spreadon {obj1} bread)
            (spreadon {obj2} bread)
            (placedon bread dinner_plate)
            (served dinner_plate)
        ))
    )
    ''',
    'templates': ['serve a toasted {obj1} and {obj2} sandwich',
                    'serve toast covered with {obj1} and {obj2}'],
    'conditions': [set(), {'spreadable'}, {'spreadable'}]
}