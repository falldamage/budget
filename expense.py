#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Expense:
    """Common class for all expenses"""
    expense_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price= price
        Expense.expense_count += 1 # Have to learn how to decrease this too. How to kill in instance?

    @staticmethod
    def amount_of_expenses():
        print("Testa {}".format(Expense.expense_count))

    def __del__(self):
        class_name = self.__class__.__name__ # Test for github
        Expense.expense_count -= 1
        print(class_name, self.name, "destroyed")

