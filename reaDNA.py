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
try:
    with open(args.filename, 'r') as read_file:
        pass 
except FileNotFoundError:
    print("No file with name %s was found..." % args.filename)
    input()
    exit(1)


print(DRNA_util.FileNucleicAcidType(args.filename))


# Input call to prevent terminal from closing
input("Press RETURN to close...")