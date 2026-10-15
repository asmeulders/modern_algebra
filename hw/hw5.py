from sage.all import *

def compute_D(n: int, e: int) -> int:
    factors = factor(n)
    assert len(factors) == 2 and all(exp == 1 for _, exp in factors), \
        "n must be a product of two distinct primes"

    p = factors[0][0]
    q = factors[1][0]
    phi = (p - 1) * (q - 1)

    assert gcd(e, phi) == 1

    return inverse_mod(e, phi)
    
def main():
    parts = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    # Question 3
    problems = [(3551,1997,2791), # (n, D, y) y=message
                (5893,81,34),
                (120979,27331,112135),
                (79403,671,129381)]

    for i, (n, d, y) in enumerate(problems):
        m = power_mod(y, d, n)
        print(f"Problem 3{parts[i+1]}: m={m}")

    # Question 4
    problems = [(451,231), (3053, 1921), (37986733, 12371), (16394854313, 34578451)]
    for i, (n, e) in enumerate(problems):
        d = compute_D(n, e)
        print(f"Problem 4{parts[i+1]}: n={n} e={e} -> d={d}")


if __name__ == '__main__':
    main()