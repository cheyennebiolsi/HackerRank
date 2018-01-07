#!/bin/python

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "{} {}".format(self.name, self.score)

    def comparator(a, b):
        if a.score == b.score:
            return cmp(a.name, b.name)
        return cmp(-a.score, -b.score)
