def inversebwt(bwt):

    invbw = []
    fline = []

    for i in (bwt):
        fline.append(i)


    for i in (bwt):
        invbw.append(i)
    invbw.sort()

    for i in range (len((bwt))):
        a = fline[i] + invbw[i]
        invbw[i] = a
    invbw.sort()

    for c in range((len(bwt)-2)):

        for i in range (len((bwt))):
            a = fline[i] + invbw[i]
            invbw[i] = a
        invbw.sort()

    a = invbw[0]
    return a

print(inversebwt('annb$aa'))

