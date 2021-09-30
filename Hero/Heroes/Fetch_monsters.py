# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:08:45 2021

@author: Mikołaj
"""
import sys
import csv
from Heroes.Personas import Monster

import os


class Fetch_monsters:
    monster_list = None

    def __init__(self):
        self.monster_list = []

    @staticmethod
    def clean_input(row):
        """
        Clean and sanitize the input so that it does not contain leading and trailing spaces
        """
        return [r.strip() for r in row]

    @staticmethod
    def map_csv_to_class(row):
        """
        Convert the input row into a Student class
        """
        return Monster(*row)

    def fetch_monsters(self):
        with open("Monster_list.csv") as _file:
            reader = csv.reader(
                _file,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
                skipinitialspace=True,
            )
            for i, row in enumerate(reader):
                if i == 0:
                    for item in row:
                        self.headers.append(item)
                else:
                    self.monster_list = self.map_csv_to_class(self.clean_input(row))
        return self.monster_list


if __name__ == "__main__":
    print(os.getcwd())
    
    monsters = Fetch_monsters()
    print(monsters.fetch_monsters())
    

