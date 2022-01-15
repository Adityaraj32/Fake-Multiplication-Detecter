'''
Author: Adityaraj Yadav 
Date: 15 January 2022
Project Name: Fake Multiplication Detecter
Purpose:For Practising Purpose
'''
import random


def Fake_Multiplication(m):
    n = 0
    mul_add = []
    rand = random.randint(2, 9)
    while True:
        n += 1
        if n != 11:
            mul = m * n
            mul_add.append(mul)
        else:
            break
    rand_between = random.randint(mul_add[rand-1], mul_add[rand+1])
    mul_add[rand] = rand_between
    print(mul_add)

Fake_Multiplication(6)