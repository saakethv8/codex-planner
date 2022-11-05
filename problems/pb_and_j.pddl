(define (problem pb_and_j) (:domain cooking)
(:objects 
    bread - bread
    peanut_butter - spreadable
    jelly - spreadable
    knife - knife
)

(:init
    (isclean knife)
)

(:goal (and
    (toasted bread)
    (spreadon peanut_butter bread)
    (spreadon jelly bread)
))

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
