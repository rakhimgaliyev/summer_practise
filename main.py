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


def show_plot(all_springs, front):
    plt.xlabel("n_tau", fontsize=15)
    plt.ylabel("L_szhat", fontsize=15)

    all_springs_x = [i.n_tau for i in all_springs]
    all_springs_y = [j.L_szhat for j in all_springs]
    plt.scatter(all_springs_x, all_springs_y)

    front_springs_x = [i.n_tau for i in front]
    front_springs_y = [j.L_szhat for j in front]
    plt.scatter(front_springs_x, front_springs_y, c="r")
    plt.show()


if __name__ == "__main__":
    # Main program starts here
    pop_size = 20
    # max_gen = 921
    max_gen = 921

    # Initialization
    min_x = -55
    max_x = 55
    solution = [min_x + (max_x - min_x) * random.random() for i in range(0, pop_size)]
    gen_no = 0

    config = Config()

    springs = []
    for delta_sp in array_of_delta_sp:
        for i_p_sp in array_of_i_p_sp:
            spring = Spring(config, delta_sp, i_p_sp)
            if spring.is_spring_ok():
                springs.append(spring)

    front = []
    if len(springs) == 0:
        print("SPRING DO NOT FIT LIMITS")
        exit(0)

    # generate Pareto-front
    for spring in springs:
        not_dominating = True
        for front_elem in front:
            if spring.dominates_by_pareto(front_elem):
                print(front.index(front_elem))
                print(len(front))
                front = [x for x in front if not x.equals(front_elem)]
                print(len(front))
            if front_elem.dominates_by_pareto(spring):
                not_dominating = False
        if not_dominating and not spring.on_array(front):
            front.append(spring)

    for spring in front:
        print(spring)

    print("ALL SPRINGS ARR LEN: ", len(springs))
    print("FRONT SPRINGS ARR LEN: ", len(front))

    show_plot(springs, front)

    print(front[0])
    print(springs[0])
