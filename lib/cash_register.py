#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.prices = {}
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.prices[title] = price

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100.0)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            last_price = self.prices[last_item]
            last_quantity = self.items.count(last_item) + 1
            self.total -= last_price * last_quantity
            if self.total <= 0:
                self.total = 0.0
        else:
            print("There are no items to void.")