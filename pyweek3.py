def ascending(l):
    if len(l) < 2:
        return True
    for i in range(2, len(l)):
        if l[i - 1] > l[i]:
            return False
    return True


def valley(l):
    n = len(l)
    small = l[0]
    vp = 0
    if n < 3:
        return False
    for i in range(n):
        if small > l[i]:
            small = l[i]
            vp = i
    if vp == 0:
        return False
    for i in range(vp):
        if l[i] <= l[i + 1]:
            return False
    for i in range(len(l) - 1, vp, -1):
        if l[i] <= l[i - 1]:
            return False
    return True


def transpose(m):
    temp1 = []
    for i in range(len(m[0])):
        temp2 = []
        for j in range(len(m)):
            temp2.append(m[j][i])
        temp1.append(temp2)
    return temp1