def factor(n):
    flist = []
    for i in range(1, n + 1):
        if n % i == 0:
            flist.append(i)
    return flist


def perfect(n):
    if n <= 0:
        return False
    flist = factor(n)
    total = 0
    for i in range(0, len(flist) - 1):
        total = total + flist[i]
    if total == flist[len(flist) - 1]:
        return True
    else:
        return False


def depth(s):
    (dmax, cmax) = (0, 0)
    for i in range(0, len(s)):
        if s[i] == "(":
            cmax = cmax + 1
            if cmax > dmax:
                dmax = cmax
        elif s[i] == ")":
            if cmax > 0:
                cmax = cmax - 1
            else:
                return -1
    if cmax > 0:
        return -1
    return dmax


def psquare(n):
    i = 1
    the_sum = 0
    while the_sum < n:
        the_sum = the_sum + i
        if the_sum == n:
            return True
        i = i + 2
    return False


def sumsquares(l):
    total = 0
    for i in range(0, len(l)):
        if psquare(l[i]):
            total = total + l[i]
    return total