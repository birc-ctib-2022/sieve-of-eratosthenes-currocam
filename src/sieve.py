"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    primes, candidates = [], list(range(2, n+1))
    while candidates:
        p = candidates[0]
        candidates = [i for i in candidates if i % p != 0]
        primes.append(p)
    return primes

    while len(primes) != len(candidates):
        p = candidates[i]
        candidates = list(
            filter(lambda x: x not in range(p+p, n+1, p), candidates))
        i += 1
        primes.append(p)

    return primes
