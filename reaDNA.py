import argparse, os, DRNA_util
parser = argparse.ArgumentParser(
    prog='reaDNA',
    description='Parses DNA files to a user friendly format',
    epilog='Hey :)'
)
DRNA_util.initialize()


# >reaDNA.py filename
# filename should be a .txt file
parser.add_argument('path', nargs='?', default=None)
args = parser.parse_args()



if not args.path:
    print("No file selected, select files from " + DRNA_util.DRNA_SEQUENCES_DIR + ' ?')
    exit(1)

seq1 : DRNA_util.Sequence = DRNA_util.readFromFile(DRNA_util.DRNA_SEQUENCES_DIR + os.path.sep + args.path, ['\n'])
print(seq1.sequence_type)


# Input call to prevent terminal from closing
input("Press RETURN to close...")