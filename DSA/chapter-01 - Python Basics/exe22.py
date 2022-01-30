"""Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1."""

from typing import List

def dot_product(a: List[int], b: List):
    c = []
    for i in range(len(a)):
        c.append((a[i]*b[i]))
    return c


#test program
if __name__ == "__main__":
    l1 = [1,2,3]
    l2 = [1,2,3]
    print(dot_product(l1, l2))