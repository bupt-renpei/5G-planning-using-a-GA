import numpy as np
from ..helper_funcs.helper import calculate_probability

def roulette_wheel_selection(population):

    new_mating_pool = []

    calculate_probability(population)

    while(len(new_mating_pool) < len(population)):
        relative_probability = 0.0
        r = np.random.uniform(0, 1)

        for plan in population:
            relative_probability += plan.get_probability()
            if relative_probability >= r:
                new_mating_pool.append(plan)
                break

    print("old")
    for plan in population:
        print(plan.get_fitness())

    print("new")
    for plan in new_mating_pool:
        print(plan.get_fitness())

    return new_mating_pool
