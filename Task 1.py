def radixSort(line):
    #Sorts in (M+N)
    print(line)
    #the setup
    array = list(line)
    lastchrcode = 255
    firstchrcode = 0

    n = lastchrcode - firstchrcode + 2 # creates number of needed buckets
    buckets = [[] for i in range(0, n)]

    for letter in array:
        #print(letter)
        index = 0
        index = ord(letter) - firstchrcode
        buckets[index].append(letter) # push to bucket
    del array[:]

    for bucket in buckets: # do reassembly
        array.extend(bucket)
        del bucket[:]

    print(array)


def decompresstofile():
    # Complexity (N)
    ofile = open("Testfile.txt", "w")
    with open('exam.bz2') as file:
        for line in file:
            #print(line)
            clnup = line.replace('\n', '').split(' ')
            # print(int(clnup[0]) * clnup[1])
            decpt = (int(clnup[0]) * clnup[1])
            #print(decpt)
            ofile.write(decpt)

def invBwt(bw):
    # Complexity (M + N + O + P)
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
            #print(c)
            ender = c + ender
            invrow = first[c][0] + ranks[invrow]
            #print(invrow)
    return fdecompress(ender)

def fdecompress(dewords):
    line = dewords.replace('*' , ' ' ).replace('-', '\n')
    return (line)
    #return(dewords)

def decryptofile():
    decompresstofile()
    file2 = open("Translated", "w")
    with open("Testfile.txt") as file:
        for line in file:
            file2.write(invBwt(line))
            #fdecompress(decompress())
    #print(fdecompress(decompress()))

decryptofile()

#fdecompress("A:*(ten*marks)--B:*(ten*marks)--C:*(ten*marks)--D:*(ten*marks)-$")
#(rankBwt('-****ssss::::nnnn))))---DABC$---mmmmttttrrrr****eeeeaaaakkkk(((('))
