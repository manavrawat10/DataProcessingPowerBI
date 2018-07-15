# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 19:49:31 2018

@author: Manav
"""

import os
def delete(raw):
    for filename in os.listdir(raw):
        os.remove(raw+"\\"+str(filename))
    