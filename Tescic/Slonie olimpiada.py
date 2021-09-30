# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:15:54 2021

@author: Mikołaj
"""
from sys import stdin
import numpy as np
inf = 1e6


def p(x, current_order, target_order):
    """
    Find next position in a cycle
    """
    return target_order[current_order.index(x)]


def make_int(order):
    """
    Change input from str to int
    """
    return [int(val) for val in order]


def rozklad_na_cykle(slonie_info):
    """
    Divide data into cicles
    """
    num_of_els, _, current_order, target_order = slonie_info
    visited = np.full(num_of_els, False) # False array with len of data
    c = 0
    cycle = []
    for i in range(1, num_of_els + 1): # loop throught elephants
        if not visited[i - 1]:
            c += 1
            x = i
            cycle.append([])
        while not visited[x - 1]:
            visited[x - 1] = True
            cycle[-1].append(x)
            x = p(x, current_order, target_order)
    return cycle


def parametry_cykli(slonie_info):
    """
    Find sum val of movement and min mass in all cycles
    """
    num_of_els, mass_of_els, current_order, target_order = slonie_info
    cycle = rozklad_na_cykle(slonie_info)
    minimum = inf
    cyc_prop = [] # list of lists with mass sum and min mass
    for i in range(len(cycle)):
        sum_cyc = 0
        min_cyc = inf
        for slon in cycle[i]:
            sum_cyc += mass_of_els[slon-1]
            min_cyc = min(min_cyc, mass_of_els[slon-1])
        cyc_prop.append([sum_cyc, min_cyc])
        minimum = min(min_cyc, minimum)
    return cyc_prop, minimum, cycle


def wynik(slonie_info):
    """
    Compute sum of movement for data
    """
    wynik = 0
    cyc_prop, minimum, cycle_list = parametry_cykli(slonie_info)
    for cycle in range(len(cyc_prop)):
        # sum of cycle + len of data -1 * min of cycle
        wynik_metody1 = cyc_prop[cycle][0] + (len(cycle_list[cycle])-2) * cyc_prop[cycle][1]
        wynik_metody2 = cyc_prop[cycle][0] + cyc_prop[cycle][1] + (len(cycle_list[cycle]) + 1) * minimum
        wynik += min(wynik_metody1, wynik_metody2)
    return wynik


def main():
    lines = stdin.readlines()

    num_of_els = int(lines[0].rstrip())
    mass_of_els = make_int(list(lines[1].rstrip().split(" ")))
    current_order = make_int(list(lines[2].rstrip().split(" ")))
    target_order = make_int(list(lines[3].rstrip().split(" ")))
    slonie_info = (num_of_els, mass_of_els, current_order, target_order)

    print(wynik(slonie_info))


if __name__ == "__main__":
    main()
