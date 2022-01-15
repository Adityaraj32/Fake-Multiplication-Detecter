'''
Author: Adityaraj Yadav 
Date: 15 January 2022
Project Name: Fake Multiplication Detecter
Purpose:For Practising Purpose
'''
import random

mul_add = []


def Fake_Multiplication(a):
    n = 0
    rand = random.randint(2, 8)
    while True:
        n += 1
        if n != 11:
            mul = a * n
            mul_add.append(mul)
        else:
            break
    rand_between = random.randint(mul_add[rand-1], mul_add[rand])
    mul_add[rand] = rand_between
    print(mul_add)


a = int(input("Enter the number: "))

Fake_Multiplication(a)


def Multiplication_Decter(b):
    Add = 0
    Mul_Detect = []
    while True:
        Add += 1
        if Add != 11:
            Tabel = Add * b
            Mul_Detect.append(Tabel)
        else:
            break
    if Mul_Detect == mul_add:
        print("This table is Correct")
    else:
        print("This tabel is incorrect")


Multiplication_Decter(a)