#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Expense:
    """Common class for all expenses"""
    __expense_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price= price
        self.allocated = 0
        Expense.__expense_count += 1 

    @staticmethod
    def amount_of_expenses():
        print("Testa {}".format(Expense.__expense_count))

    def __del__(self):
        class_name = self.__class__.__name__
        Expense.__expense_count -= 1
        print(class_name, self.name, "destroyed")


