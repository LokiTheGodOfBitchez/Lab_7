#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("Enter the elements of the list a:")
    A = list(map(float, input().split()))
    length = len(A)
    print(length)
    print(f"The max element of this list is: {max(A)}")
    i = 0
    for e in A:
        if e >= 0:
            i = A.index(e)
    s = sum([a for a in A if A.index(a) < i])
    print(f"The sum of numbers before the last positive element is: {s}")
    a = int(input("Enter the a number of the border: "))
    b = int(input("Enter the b number of the border: "))
    temp = []
    for e in A:
        if a < abs(e) < b:
            continue
        else:
            temp.append(e)
    if length > len(temp):
        for i in range(length - len(temp)):
            temp.append(0)
    print(temp)
