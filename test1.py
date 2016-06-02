import sys,os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Please provide a file.'
        sys.exit(0)
    aFile = sys.argv[1]
    if not os.path.exists(aFile):
        print 'Please check if the file', aFile, 'does exist'
        sys.exit(0)
    with open(aFile, 'r') as afile:
        nbLines = len(afile.readlines())
        print 'Nb of lines:', nbLines