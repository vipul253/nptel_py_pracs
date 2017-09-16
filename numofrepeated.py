def repeated(l):
    n = len(l)
    count = 0
    unq = []
    for i in range(0,n):
        for j in range(i+1, n):
            if (l[i] == l[j]):
                if l[j] not in unq:
                    count += 1
                    unq.append(l[i])
    return count