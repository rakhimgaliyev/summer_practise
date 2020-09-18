# -*- coding: utf-8 -*-

import math
import random
import matplotlib.pyplot as plt

from config import Config
from spring import Spring
from data import array_of_delta_sp, array_of_i_p_sp


def print_smt(value, description="DATA"):
    print()
    print("------------------------" + description + "------------------------")
    print(value)
    print("------------------------" + description + "------------------------")
    print()


if __name__ == "__main__":
    # Main program starts here
    pop_size = 20
    # max_gen = 921
    max_gen = 921

    # Initialization
    min_x = -55
    max_x = 55
    solution = [min_x + (max_x - min_x) * random.random()
                for i in range(0, pop_size)]
    gen_no = 0

    config = Config()

    springs = []
    for delta_sp in array_of_delta_sp:
        for i_p_sp in array_of_i_p_sp:
            spring = Spring(config, delta_sp, i_p_sp)
            if spring.is_spring_ok():
                springs.append(spring)

    front = []
    if len(springs) > 0:
        front.append(springs[0])

    # generate Pareto-front
    for spring in springs:
        for front_elem in front:
            if spring.dominates_by_pareto(front_elem):
                front = [spring]
            elif not front_elem.dominates_by_pareto(spring) \
                    and not spring.on_array(front):
                front.append(spring)

    for spring in front:
        print(spring)
    print(len(front))

    function1 = [i.n_tau for i in springs]
    function2 = [j.L_szhat for j in springs]
    plt.xlabel('n_tau', fontsize=15)
    plt.ylabel('L_szhat', fontsize=15)
    # plt.gca().invert_yaxis()
    plt.scatter(function1, function2)
    plt.show()
