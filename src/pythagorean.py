"""Module for calculating/approximating pythagorean theorem"""

from math import sqrt

def calc(point: tuple((int, int))):
    """Function for calculating pythagorean theorem"""
    return sqrt(pow(point[0], 2) + pow(point[1], 2))

def approx(point:tuple((int,int))):
    """Function for approximating pythagorean theorem"""
    return 7/8* point[0] + point[1]/2   # 7/8 * cathetus
