import sys

def main(argv):

    for line in sys.stdin:
        print('{0}'.format(line.split('\t')[0]))

if __name__ == "__main__":
    main(sys.argv)