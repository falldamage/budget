#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Expense:
    """Common class for all expenses"""
    expense_count = 0

    def __init__(self, name, price):
        Expense.expense_count += 1 # Have to learn how to decrease this too. How to kill in instance?

    @staticmethod
    def amount_of_expenses():
        print("Testa {}".format(Expense.expense_count))


