NUCLEOTIDES_DNA = ['A','C','G','T']
NUCLEOTIDES_RNA = ['A','C','G','U']


def isRNA(sequence, ignore = None) -> bool:
    """Verifies if a given list(or string) consists of RNA-Nucleotides.
    Returns False if any character is not a RNA-Nucleotide or in the ignore list.
    Returns True otherwise.

    Args:
        sequence (list): List of char elements to be verified
        ignore (list): List of char elements to be ignored during verification

    Returns:
        bool: True if RNA, False if not
    """
    # Arguments should be iterable
    assert hasattr(sequence, '__getitem__'), "sequence argument not subscriptable"
    if ignore: assert hasattr(ignore, '__getitem__'), "ignore argument not subscriptable"
    if not ignore: ignore = []

    # Iterates each element in the list, if any aren't valid return False
    for char in sequence:
        if char in NUCLEOTIDES_RNA:
            continue
        else:
            return False

    # Iterator didn't return, hence every char is valid 
    return True

def isDNA(sequence, ignore = None) -> bool:
    """Verifies if a given list(or string) consists of DNA-Nucleotides.
    Returns False if any character is not a DNA-Nucleotide or in the ignore list.
    Returns True otherwise.

    Args:
        sequence (list): List of char elements to be verified
        ignore (list): List of char elements to be ignored during verification

    Returns:
        bool: True if DNA, False if not
    """
    # Arguments should be iterable
    assert hasattr(sequence, '__getitem__'), "sequence argument not subscriptable"
    if ignore: assert hasattr(ignore, '__getitem__'), "ignore argument not subscriptable"
    if not ignore: ignore = []

    # Iterates each element in the list, if any aren't valid return False
    for char in sequence:
        if char in NUCLEOTIDES_DNA + ignore:
            continue
        else:
            return False

    # Iterator didn't return, hence every char is valid
    return True

def determineFileNucleicAcidType(file_name, ignore = ['\n']) -> tuple[str, bool, bool]:
    """Opens file and determines it

    Args:
        file_name (string): Name of file to have its type determined
        ignore (list, optional): Optional list of character to be ignored. Ignores '\\n' by default.

    Returns:
        tuple[str, bool, bool]: Returns tuple where index[1] is DNA boolean and index[2] is RNA.
        True being qualifies as the Nucleic Acid type, False meaning it does not qualify.
        Index[0] is the str of the name of the file being tested.
    """
    with open(file_name, 'r') as read_file:
            # Variable containing all of the lines
            file_content_index = read_file.readlines()

            for line in file_content_index:
                # Skip empty lines
                if not line:
                    continue
                # Check if line is DNA, ignore new-line symbols
                if not isDNA(line, ignore):
                    DNA = False
                else:
                    DNA = True


            for line in file_content_index:
                # Skip empty lines
                if not line:
                    continue
                # Check if line is RNA, ignore new-line symbols
                if not isRNA(line, ignore):
                    RNA = False
                else:
                    RNA = True

    return [file_name, DNA, RNA]