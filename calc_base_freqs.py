def make_count_dict(seq):
    '''
    Uses an input sequece (string of characters) and counts the number of time each character occurs.
    Returns a dictionary of counts.
    '''
    b = dict()
    for base in seq:
        if base not in b:
            b[base] = 1
        else:
            b[base] += 1
    return b

def compute_freqs(count_dict):
    '''
    Computes the relative frequency of every unique character in count_dict and prints them.
    '''
    print('freqs')
    total = float(sum([count_dict[b] for b in count_dict.keys()]))
    for b in count_dict.keys():
        print(b + ':' + str(count_dict[b]/total))

compute_freqs(make_count_dict('ATCTGACGCGCGCCGC'))
