""" 
This module contains a baisc accumulator class
Its purpose is to show how to use the pytest framework fir testing class 
"""
# Class: Accumulator 

class Accumulator:

    def __init__(self):
        self._count = 0

    @property 
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more 
    