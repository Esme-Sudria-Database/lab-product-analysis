import sys

def main(argv):

    for line in sys.stdin:
        print("{0}\t1".format(line))

if __name__ == "__main__":
    main(sys.argv)