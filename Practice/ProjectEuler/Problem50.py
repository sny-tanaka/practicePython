# coding: utf-8
'''
素数41は6つの連続する素数の和として表せる:
41 = 2 + 3 + 5 + 7 + 11 + 13.
100未満の素数を連続する素数の和で表したときにこれが最長になる.
同様に, 連続する素数の和で1000未満の素数を表したときに最長になるのは953で21項を持つ.
100万未満の素数を連続する素数の和で表したときに最長になるのはどの素数か?
'''


def get_prime_boolean(search_max):
    prime_boolean = [False, False] + [True] * (search_max-1)
    prime_boolean[4::2] = [False] * (len(prime_boolean[4::2]))
    p = 3
    p_max = int(search_max ** 0.5) + 1
    while p <= p_max:
        if prime_boolean[p]:
            prime_boolean[p**2::p] = [False] * (len(prime_boolean[p**2::p]))
        p += 2
    return prime_boolean


def main():
    num = 10**6
    primes = [i for i, b in enumerate(get_prime_boolean(num)) if b]
    cnt, ans = 1, 0
    for n in range(len(primes)):
        if primes[n] > num / cnt:
            break
        for m in range(n + cnt, len(primes) + 1):
            N = sum(primes[n:m])
            if N >= num:
                break
            if m - n > cnt and N in primes:
                cnt, ans = m - n, N
    print(ans)


if __name__ == '__main__':
    main()
