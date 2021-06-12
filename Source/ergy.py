# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:57:50 2021

@author: khoohuibo
"""

class Energy():
    
    def __init__(self):
        self.real=True
    
    def kinetic(self, mass, velocity):
        return 0.5 * mass * velocity ** 2
    
    def gravitational(self, mass , height, a_g=9.81):
        return mass * a_g * height
    
    def electric(self, current, voltage, time):
        return current * voltage * time