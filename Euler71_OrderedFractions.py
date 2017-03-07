"""
Euler71_Ordered fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
 it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6,
 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
find the numerator of the fraction immediately to the left of 3/7.
"""


import math

def find_closest_to_three_sevenths(highest):
    numer=1000
    min_gap=.01
    while numer<=highest:
        denom=math.ceil(numer*7/3)
        if denom%7!=0: #eliminate situation of multiples such as 30/70 or 30000/70000
            if abs(numer/denom-3/7)<min_gap: #if this come closest yet, make it the 'current' minimum gap
                min_gap=abs(numer/denom-3/7)
                marker=[numer,denom]
        numer+=1
    print("The minimum gap of",min_gap,"occurs with the numer/denom pair:",marker)
    return

find_closest_to_three_sevenths(428571) #--> The minimum gap of 1.4285757138354782e-07 occurs with the numer/denom pair: [428570, 999997] CORRECT
