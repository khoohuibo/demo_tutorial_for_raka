# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 20:56:06 2021

@author: khoohuibo
"""

# The purpose of the file is to answer multiple math questions in a single run

import Source.ergy
import Source.time

test = Source.ergy.Energy() # 1st variable
test_time = Source.time.Time() # 2nd variable

# energy function testing
print(test.kinetic(100, 100))
print(test_time.days_to_seconds(1))
