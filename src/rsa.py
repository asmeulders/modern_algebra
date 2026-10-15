import numpy as np

def compute_D(n: int, E: int) -> int:
    if not isinstance(n, int) or not isinstance(E, int):
        raise TypeError
    
    if n < 0 or E < 0:
        raise ValueError

    p = q = 0
    for i in range(int(np.sqrt(n))):
        if n % i == 0:
            p = i
            q = n / p

    mod = int((p-1)*(q-1))

    g: int = gcd(mod, n)

    D: int = 

    return D

def gcd(a: int, b: int) -> (int, list[]):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def back_up()

def main():
    ...

if __name__ == '__main__':
    main()