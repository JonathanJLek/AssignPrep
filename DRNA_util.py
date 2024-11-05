from random import choice
import os, re

DRNA_SEQUENCES_DIR = (os.getcwd() + "\\DRNA_Sequences")

NUCLEOTIDES_DNA = ['A','C','G','T']
NUCLEOTIDES_RNA = ['A','C','G','U']

DNA_TYPE = 'D'
RNA_TYPE = 'R'
NON_TYPE = ''

def initialize():
    """Create sequence storage folder path if not exists."""
    if not os.path.exists(DRNA_SEQUENCES_DIR):
        os.makedirs(DRNA_SEQUENCES_DIR)  

class Sequence:
    """Central sequence object of DRNA-Utils. Comes with associated .txt file in ${cwd}\\DRNA_Sequences
    """
    def __init__(self, 
                 sequence_type, 
                 nucleotides = {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
            'U': 0
        },
                file_path: str = None
                 ) -> None:
        self.sequence_type = sequence_type
        """Stores nucleic acid type specifier. For DNA, RNA or NON-TYPE
        """
        self.nucleotides = nucleotides
        """Stores nucleotides count in dictionary with one letter nucleotide character as key and count as value.
        """
        self.file_path = file_path
        """Path to associated sequence.txt file."""

def analyzeIterable(target_list, ignore = ['\n']) -> dict:
    """Analyses any given iterable string of characters. Returns its properties as a dict.

    Args:
        target_list (list): A string, list or tuple of a nucleic acid
        ignore (list, optional): A string, list or tuple of characters to ignore when considering nucleic acid type. Ignores '\\n' by default.

    Returns:
        list:  List of sequence information\n
     0 - type specifier: DNA 'D', RNA 'R' or NOT Nucleic Acid ''\n
     1 - Dictionary for keeping track of nucleotide count
    """
    assert hasattr(target_list, '__getitem__'), "sequence argument not subscriptable"
    if ignore: assert hasattr(ignore, '__getitem__'), "ignore argument not subscriptable"
    if not ignore: ignore = []

    # List of sequence information
    # 0 - type specifier: DNA 'D', RNA 'R' or NOT Nucleic Acid ''
    # 1 - Dictionary for keeping track of nucleotide count
    sequence_info = [NON_TYPE,{
        'A' : 0,
        'C' : 0,
        'G' : 0,
        'T' : 0,
        'U' : 0
    }]
    # Iterates each element in the list, adds nucleotides to dict. If any aren't valid return False
    for element in target_list:
        for char in element:
            if char in ignore:
                continue
            if char in NUCLEOTIDES_DNA + NUCLEOTIDES_RNA:
                sequence_info[1][char] += 1
                continue
            else:
                print("Non-valid character found in analyzeString()")
                return sequence_info
    
    
    # Decide on DNA (D) or RNA (R) based on 'T' and 'U' counts
    if sequence_info[1]['T'] > 0 and sequence_info[1]['U'] <= 0: sequence_info[0] = 'D'
    if sequence_info[1]['U'] > 0 and sequence_info[1]['T'] <= 0: sequence_info[0] = 'R'

    return sequence_info

def readFromFile(file_path, ignore) -> Sequence:
        """Reads a .txt file for nucleotides using DRNA_util.analyzeString().

        Args:
            filename (string): File to read.
            ignore (list): A string, list or tuple of characters to ignore when considering nucleic acid type. Ignores '\\n' by default.

        Returns:
            int: exitcode \n
            0 - success,
            1 - failed
        """
        try:
            with open(file_path, 'r') as read_file:
                file_lines = read_file.readlines()
                file_sequence_info = analyzeIterable(file_lines, ignore)
                last_type, nucleotides = file_sequence_info[0], file_sequence_info[1]
            
        except FileNotFoundError:
            print("No file with name %s was found..." % file_path)
            raise FileExistsError("File at "+ file_path + "does not exist...'")
        
        # We can use last_type her as our Sequence type because if it changes at any point verification we don't even reach here.
        # Return Sequence object read from file
        return Sequence(last_type, )

#TODO: Add file formatting. Either here or by a general function that can be called on files read or generated.
#TODO: Pass nucleotide counts to returned Sequence object. PRIORITY HIGH
def generateSequence(sequence_type: str, length: int, sequence_name: str, format: str = None) -> Sequence:  
    """Generates a Sequence object and its associated fle in /DRNA_util directory.\n
    Directory is made if it is not present when function is called. Format is currently useless

    Args:
        sequence_type (str): Sequence type, 'D' for DNA, 'R' for RNA
        length (int): Length of desired sequence.
        sequence_name (str): name of associated sequence file. Without file extension.
        format (str, optional): format flags for writing to file. Defaults to None.

    Raises:
        ValueError: Error raised when sequence_type is has invalid value

    Returns:
        Sequence: Sequence object generated according to specifications
    """
    # Prepare lists for sequence generation
    nucleotides = []
    nucleotide_list = []
  
    if sequence_type == 'D':
        nucleotides = NUCLEOTIDES_DNA
    elif sequence_type == 'R':
        nucleotides = NUCLEOTIDES_RNA
    else:
        raise ValueError("Passed invalid sequence type to generateSequence()...")

    # Generate sequence
    for i in range(0, length):
        nucleotide_list.append(choice(nucleotides))

    # Make target directory if it does not exist
    if not os.path.exists(DRNA_SEQUENCES_DIR):
        raise FileNotFoundError("Target directory does not exist...")

    # Add extension to sequence name and create final path.
    sequence_file = sequence_name + '.txt'       
    sequence_file_path = os.path.join(DRNA_SEQUENCES_DIR, sequence_file)
    
    # No try block because of 'w' flag
    with open(sequence_file_path, 'w') as write_file:
        write_file.write(''.join(nucleotide_list))
        print("Generated file at:"+ sequence_file_path )
    
    generated_sequence = Sequence(sequence_type, file_path=sequence_file_path)

    return generated_sequence

def convertSequence(sequence: Sequence, conversion_type: str):
    pass

def parseSequence(sequence: Sequence, format: str):
    pass

#This should use regex to return count and location
def findNucleotideSequence():
    pass