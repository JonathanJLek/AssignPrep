NUCLEOTIDES_DNA = ['A','C','G','T']
NUCLEOTIDES_RNA = ['A','C','G','U']

# TODO Combine isRna and isDNA into one, refactor code so the standard
# becomes DNA = True and RNA = FALSE. In this way any sequence can be identified by a boolean.

def analyzeString(sequence, ignore = ['\n']) -> dict:
    """Analyses any given iterable sequence of characters. Returns its properties as a dict.

    Args:
        sequence (list): A string, list or tuple of a nucleic acid
        ignore (list, optional): A string, list or tuple of characters to ignore when considering nucleic acid type. Ignores '\\n' by default.

    Returns:
        list:  List of sequence information\n
     0 - type specifier: DNA 'D', RNA 'R' or NOT Nucleic Acid ''\n
     1 - Dictionary for keeping track of nucleotide count
    """
    assert hasattr(sequence, '__getitem__'), "sequence argument not subscriptable"
    if ignore: assert hasattr(ignore, '__getitem__'), "ignore argument not subscriptable"
    if not ignore: ignore = []

    # List of sequence information
    # 0 - type specifier: DNA 'D', RNA 'R' or NOT Nucleic Acid ''
    # 1 - Dictionary for keeping track of nucleotide count
    sequence_info = ['',{
        'A' : 0,
        'C' : 0,
        'G' : 0,
        'T' : 0,
        'U' : 0
    }]
    # Iterates each element in the list, adds nucleotides to dict. If any aren't valid return False
    for char in sequence:
        if char in ignore:
            continue
        if char in NUCLEOTIDES_DNA + NUCLEOTIDES_RNA:
            sequence_info[1][char] += 1
            continue
        else:
            return sequence_info
    
    
    # Decide on DNA (D) or RNA (R) based on 'T' and 'U' counts
    if sequence_info[1]['T'] > 0 and sequence_info[1]['U'] <= 0: sequence_info[0] = 'D'
    if sequence_info[1]['U'] > 0 and sequence_info[1]['T'] <= 0: sequence_info[0] = 'R'

    return sequence_info

class Sequence:
    """Central sequence object of DRNA-Utils. 
    """
    def __init__(self) -> None:
        self.type = ''
        self.nucleotides = {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
            'U': 0
        }

    def readFromFile(self, filename, ignore) -> int:
        try:
            with open(filename, 'r') as read_file:
                file_content = read_file.readlines()
                last_type = ''
                for line_number, line in enumerate(file_content):
                    line_info = analyzeString(line, ignore)
                    # See if the nucleic acid type changed since the last line (excluding the first line)
                    # If so exit. TODO: Exit more gracefully I.e not a half filled variable
                    if last_type != line_info[0] and line_number > 0:
                        print("Could not determine nucleic acid type in readFromFile()")
                        return 1
                    self.nucleotides = {k: self.nucleotides.get(k, 0) + line_info[1].get(k, 0) for k in set(self.nucleotides) | set(line_info[1])}
                    last_type = line_info[0]
                # If no nucleic acid type mismatches were found, meaning last_type stayed constant, assign nucleic acid type.
                self.type = last_type
            return 0
        except FileNotFoundError:
            print("No file with name %s was found..." % filename)
            input()
            return 1