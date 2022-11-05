(define (problem buttered_toast) (:domain cooking)
(:objects 
    bread - food
    butter - food
    peanut_butter - food
    jelly - food
    water - food
    oil - food
    chicken - food

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
    sauce_pan - pan
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


    (isclean butter_knife)
    (isclean chef_knife)
    (isclean cleaver)

    


    
)

(:goal (and
    (toasted bread)
    (spreadon butter bread)
))

)
