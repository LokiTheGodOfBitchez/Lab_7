#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    A = list(map(float, input().split()))
    if len(A) <= 15:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    counter = 0
    for i in range(len(A)):
        counter = counter + A[i]

    B = len(A)

    print(counter/B)


