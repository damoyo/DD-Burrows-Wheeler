import quickSort
a = quickSort


def suffixarray(string):
    sfxsetup =[]
    x = -1
    for i in range (0, len(string)+1):
        x = x + 1
        sfx = (string[i:])
        sfxsetup.append([sfx,(x)])
    sfxsetup = sfxsetup[:-1]
    almost = mmdm_sort(sfxsetup)  # double prefixing
    a.quickSort(almost)   #intitial sort
    return almost


def mmdm_sort(list):
    i = 2
    while (i) <= len(list):
        a = buckets(list,i)
        i = i *2
    return a


def buckets(list, blen):
    buckt = []
    sortedbucket = []
    for i in list:
        fstuple = (i[0][:blen])
        sndtuple = (i[1])
        buckt.append([fstuple,sndtuple])
    a.quickSort(buckt)
    for i in buckt:
        index = i[1]
        sortedbucket.append(list[index])
    return(sortedbucket)



def bwt(t):
    """ Given T, returns BWT(T), by way of the suffix array. """
    bw = []
    for si in suffixarray(t):

        index = si[1]
        bw.append(t[index - 1])
    return ''.join(bw)

def readfile(filename):
    """
    @purpose: Reads file Characters, converts them and returns as upperrcase string without spaces or punctuation and writes
    @param: - filename
    @preconditions: Input file must exist
    @postconditions: Reads characters, returns lowercase string without spaces
    @complexity: O(N + N)
    """

    try:
        f = open('outputbwt.txt', 'a')
        with open(filename) as file_obj:
            for line in file_obj:
                    f.write(bwt(line))
    except FileNotFoundError:
        print("No such file or directory:", filename)


readfile('sample1.txt')

