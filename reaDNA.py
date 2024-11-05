import argparse, DRNA_util

parser = argparse.ArgumentParser(
    prog='reaDNA',
    description='Parses DNA files to a user friendly format',
    epilog='Hey :)'
)

# >reaDNA.py filename
# filename should be a .txt file
parser.add_argument('filename')
args = parser.parse_args()

# Check to see if file exists, otherwise exist with code 1
file_lines = []
try:
    with open(args.filename, 'r') as read_file:
        file_content = read_file.readlines()
        
        NUCLEIC_TYPE : bool = None
        NUCLEIC_COUNT : dict = {}
        for line in file_content:
            temp = DRNA_util.initializeSequence(line)
            NUCLEIC_TYPE = temp[0]
            NUCLEIC_COUNT= {k: NUCLEIC_COUNT.get(k, 0) + temp[1].get(k,0) for k in set(NUCLEIC_COUNT) | set(temp[1])}
        
            
except FileNotFoundError:
    print("No file with name %s was found..." % args.filename)
    input()
    exit(1)


print(NUCLEIC_COUNT)


# Input call to prevent terminal from closing
input("Press RETURN to close...")