import re
import sys

def main(argv):

    for line in sys.stdin:
        contents = line.split(' ')
        request = ' '.join(contents[4:]).strip()
        search = re.search('(?<=\"GET /)\w+', request)
        operation = search.group(0)
        print("{0}\t1".format(operation))

if __name__ == "__main__":
    main(sys.argv)