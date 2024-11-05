import argparse, os, DRNA_util

# Initialize DRNA_util
DRNA_util.initialize()
# Initialize parser
parser = argparse.ArgumentParser(
    prog='reaDNA',
    description='Parses DNA files to a user friendly format',
    epilog='Hey :)'
)
parser.add_argument('path', nargs='?', default=None)
args = parser.parse_args()

# Prepare active sequence variable
active_sequence = None

# This dense peace of logic sets the active file by user input.
if not args.path:
    print("No target file was passed.\nChoose file:")
    for x in os.listdir(DRNA_util.DRNA_SEQUENCES_DIR): print(x)
    selection = input()
    if selection not in os.listdir(DRNA_util.DRNA_SEQUENCES_DIR):
        raise FileNotFoundError("No such file in: %s" % DRNA_util.DRNA_SEQUENCES_DIR)
    active_sequence = DRNA_util.readFromFile(os.path.join(DRNA_util.DRNA_SEQUENCES_DIR, selection))
else:
    active_sequence = DRNA_util.readFromFile(os.path.join(DRNA_util.DRNA_SEQUENCES_DIR, args.path))

# Input call to prevent vscode terminal from closing
input("Press RETURN to close...")