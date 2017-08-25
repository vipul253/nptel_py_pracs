def freqlist(l):
    freq = []
    for i in range(len(l)):
        count = 0
        for j in range(len(l)):
            if l[j] == l[i]:
                count = count + 1
        freq.append(count)
    return freq


def frequency(l):
    if len(l) < 1:
        return ([], [])
    freq = freqlist(l)
    minm = freq[0]
    maxm = freq[0]
    flist = []
    minl = []
    maxl = []
    for i in range(len(l)):
        if maxm <= freq[i]:
            maxm = freq[i]
        elif minm >= freq[i]:
            minm = freq[i]
    for i in range(len(l)):
        if freq[i] == minm and l[i] not in minl:
            minl.append(l[i])
        if freq[i] == maxm and l[i] not in maxl:
            maxl.append(l[i])
    minl.sort()
    maxl.sort()
    flist.append(minl)
    flist.append(maxl)
    flist = tuple(flist)
    return flist


def onehop(l):
    er = []
    temp = []
    for (i, j) in l:
        for (k, l1) in l:
            if i != k and j != l1:
                if (i == l1 and j != k):
                    if [k, j] not in er:
                        er.append([k, j])
    for i in range(len(er)):
        tem1 = tuple(er[i])
        temp.append(tem1)
    ans = sorted(temp)
    return ans
