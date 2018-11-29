import sys

def main(argv):

    previous_operation = None
    operation_count = 0
    for line in sys.stdin:
        operation, value  = line.split('\t')
        if operation != previous_operation and previous_operation is not None:
            print('{0},{1}'.format(previous_operation, operation_count))
            operation_count = 0

        operation_count += int(value)
        previous_operation = operation

    print('{0},{1}'.format(previous_operation, operation_count))

if __name__ == "__main__":
    main(sys.argv)