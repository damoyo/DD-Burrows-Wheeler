def rankBwt(bw):
    #creates rank and occurences
    occurences = dict()
    ranks =	[]
    for	letter in bw:
        if letter not in occurences:
            occurences[letter] = 0
        ranks.append(occurences[letter])
        occurences[letter] += 1
    #print(ranks)
    #print(occurences)

    # first column mapping
    ender = '$'
    invrow = 0
    ender = '$'
    first = {}
    occurences2 = 0
    #count = 0
    for c, count in sorted(occurences.items()):
        first[c] = (occurences2, occurences2 + count)
        occurences2 += count

    #get the string now
    while bw[invrow] is not '$':
            c = bw[invrow]
            print(c)
            ender = c + ender
            invrow = first[c][0] + ranks[invrow]
            #print(invrow)
    fdecompress(ender)

def fdecompress(dewords):
    line = dewords.replace('-' , '\n')
    line = dewords.replace('*' , ' ' )
    print(line)

fdecompress("A:*(ten*marks)--B:*(ten*marks)--C:*(ten*marks)--D:*(ten*marks)-$")



#(rankBwt('-****ssss::::nnnn))))---DABC$---mmmmttttrrrr****eeeeaaaakkkk(((('))