#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('effi').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
