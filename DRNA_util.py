from random import choice
import os
NUCLEOTIDES_DNA = ['A','C','G','T']
NUCLEOTIDES_RNA = ['A','C','G','U']

DNA_TYPE = 'D'
RNA_TYPE = 'R'
NON_TYPE = ''

# TODO Combine isRna and isDNA into one, refactor code so the standard
# becomes DNA = True and RNA = FALSE. In this way any sequence can be identified by a boolean.

def analyzeString(target_list, ignore = ['\n']) -> dict:
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
    for char in target_list:
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

class Sequence:
    """Central sequence object of DRNA-Utils. 
    """
    def __init__(self) -> None:
        self.sequence_type = NON_TYPE
        self.nucleotides = {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
            'U': 0
        }
        # Stores file path to the file used to generate this sequence object
        # Sequence can be generated without files therefore can be None.
        self.file_path = None

    def readFromFile(self, file_path, ignore) -> int:
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
                file_content = read_file.readlines()
                # Variable to keep track of nucleic acid type between lines.
                last_type = NON_TYPE
                for line_number, line in enumerate(file_content):
                    line_info = analyzeString(line, ignore)
                    # See if the nucleic acid type changed since the last line (excluding the first line)
                    # If so, exit. TODO: Exit more gracefully I.e not a half filled self.nucleotides
                    if last_type != line_info[0] and line_number > 0:
                        print("Could not determine nucleic acid type in readFromFile(), at line number:" + str(line_number))
                        return 1
                    # Merge dictionaries of nucleotides count with old values and new line_info values. 
                    # line_info[NUCLEIC ACID TYPE, dict]
                    self.nucleotides = {k: self.nucleotides.get(k, 0) + line_info[1].get(k, 0) for k in set(self.nucleotides) | set(line_info[1])}
                    last_type = line_info[0]
                # If no nucleic acid type mismatches were found, meaning last_type stayed constant, assign nucleic acid type.
                self.sequence_type = last_type
            
        except FileNotFoundError:
            print("No file with name %s was found..." % file_path)
            return 1
        
        self.file_path = file_path
        return 0

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

    # Important file paths
    working_directory = os.getcwd()
    target_dir = os.path.join(working_directory, "DRNA_Sequences")

    # Make target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)  

    # Add extension to sequence name and create final path.
    sequence_file = sequence_name + '.txt'       
    sequence_file_path = os.path.join(target_dir, sequence_file)
    
    # No try block because of 'w' flag
    with open(sequence_file_path, 'w') as write_file:
        write_file.write(''.join(nucleotide_list))
        print("Generated file at:"+ sequence_file_path )
    
    # Generate sequence object to return with associated values. TODO: Make constructor to streamlines this process.
    generated_sequence = Sequence()
    generated_sequence.sequence_type = sequence_type
    generated_sequence.file_path = sequence_file_path
   

    return generated_sequence

def convertSequence(sequence: Sequence, conversion_type: str):
    pass

def parseSequence(sequence: Sequence, format: str):
    pass