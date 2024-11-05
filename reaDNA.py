import argparse, DRNA_util

parser = argparse.ArgumentParser(
    prog='reaDNA',
    description='Parses DNA files to a user friendly format',
    epilog='Hey :)'
)

# >reaDNA.py filename
# filename should be a .txt file
parser.add_argument('path')
args = parser.parse_args()

seq1 = DRNA_util.Sequence()
seq1.readFromFile(args.path, ['\n'])
print(seq1.sequence_type)
# Input call to prevent terminal from closing
input("Press RETURN to close...")