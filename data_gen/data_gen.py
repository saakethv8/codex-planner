import constants
import goal_library as glib
import random
from re import search
import json
# from collections import Counter

def generate_random(str):
    goal = glib.gdict[str]
    invalid = True
    object, container, object2 = '','',''
    while invalid:
        object, object2 = random.sample(constants.OBJECTS, 2)
        container = random.choice(constants.CONTAINERS)
        invalid = False
        for var, cond in zip([container, object, object2], goal['conditions']):
            if not cond.issubset(constants.ATTRIBUTES[var]):
                invalid = True
    template = random.choice(goal['templates'])
    return {
        'goal': template.format(obj1=object.replace('_',' '),cont=container.replace('_',' '),obj2=object2.replace('_',' ')),
        'pddl': goal['pddl'].format(init=constants.INIT_STATE,obj1=object,cont=container,obj2=object2)
    }

if __name__ == '__main__':
    goals = []
    strings = set()
    for action in glib.gdict:
        for _ in range(4000):
            g = generate_random(action)
            if g['goal'] not in strings:
                goals.append(generate_random(action))
                strings.add(g['goal'])
    random.shuffle(goals)
    print(len(goals))
    with open('data_gen/goal_pddl.json', 'w') as f:
        json.dump(goals,f,indent=2)