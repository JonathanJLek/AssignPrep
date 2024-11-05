NUCLEOTIDES_DNA = ['A','C','G','T']
NUCLEOTIDES_RNA = ['A','C','G','U']

# TODO Combine isRna and isDNA into one, refactor code so the standard
# becomes DNA = True and RNA = FALSE. In this way any sequence can be identified by a boolean.

def initializeSequence(sequence, ignore = ['\n']) -> tuple:
    """Returns both the nucleic acid type; DNA = True, RNA = False. And the counts of each nucleotide store in a dictionary.
    The first element of the tuple is the type boolean and the second is the dictionary.

    Args:
        sequence (list): A string, list or tuple of a nucleic acid
        ignore (list, optional): A string, list or tuple of characters to ignore when considering nucleic acid type. Ignores '\\n' by default.

    Returns:
        tuple: (type boolean DNA or RNA, nucleotide_count dictionary)
    """
    assert hasattr(sequence, '__getitem__'), "sequence argument not subscriptable"
    if ignore: assert hasattr(ignore, '__getitem__'), "ignore argument not subscriptable"
    if not ignore: ignore = []

    # Dictionary for keeping track of nucleotide count
    nucleotide_counts = {
        'A' : 0,
        'C' : 0,
        'G' : 0,
        'T' : 0,
        'U' : 0
    }
    # Iterates each element in the list, adds nucleotides to dict. If any aren't valid return False
    for char in sequence:
        if char in ignore:
            continue
        if char in NUCLEOTIDES_DNA + NUCLEOTIDES_RNA:
            nucleotide_counts[char] += 1
            continue
        else:
            return (None, None)
    
    # The program should not throw an error if it is neither DNA or RNA, but ill figure that out later
    assert nucleotide_counts['T'] * nucleotide_counts['U'] == 0, "Sequence contains both 'T' and 'U'"
    # Decide on DNA (True) or RNA (False) based on 'T' and 'U' counts
    if nucleotide_counts['T'] > 0 and nucleotide_counts['U'] <= 0: return (True, nucleotide_counts)
    if nucleotide_counts['U'] > 0 and nucleotide_counts['T'] <= 0: return (False, nucleotide_counts)

    # Safe guards so that function always returns something
    return (None, None)