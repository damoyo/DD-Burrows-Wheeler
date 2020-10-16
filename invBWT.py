import quadratic
a = quadratic

def rankBwt(bw):

    tples = dict()
    ranks =	[]
    for	c in bw:
        if c not in	tples:
            tples[c]	= 0
        ranks.append(tples[c])
        tples[c]	+= 1
    return ranks, tples

def firstColumn(tpless):

    start = {}
    tples = 0
    count = 2
    for	c in (tpless):
        start[c] = (tples, tples	+ count)
        tples +=	count
    return	start

def reverseBwt(bw):
    ranks, tples	=	rankBwt(bw)
    first =	firstColumn(tples)
    ithrow = 0
    while	bw[ithrow] != '$':
        c = bw[ithrow]
        t =	c + t
        ithrow = first[c][0] + ranks[ithrow]
    return	t

def readfile(filename):
    """
    @purpose: Reads file Characters, converts them and returns as upperrcase string without spaces or punctuation and writes
    @param: - filename
    @preconditions: Input file must exist
    @postconditions: Reads characters, returns lowercase string without spaces
    @complexity: O(N + N)
    """

    try:
        f = open('originalstring.txt', 'a')
        with open(filename) as file_obj:
            for line in file_obj:
                    f.write(reverseBwt(line))
    except FileNotFoundError:
        print("No such file or directory:", filename)


(reverseBwt('cipher.txt'))