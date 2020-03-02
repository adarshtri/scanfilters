import sys
from src.filter import TemporalFilter, RangeFilter


def run_filter(type_filter, n=None, d=None):

    if type_filter == "range":
        filter_object = RangeFilter()
        loop = True
        scan = []

        output = []

        for i in range(0, n):
            scan_val = int(input())
            scan.append(scan_val)
        output = filter_object.update(scan)
        print 'Final Output {0}'.format(output)

    elif type_filter == "temporal":

        filter_object=TemporalFilter(n,d)
        loop=True
        scan=[]

        output = []

        while(loop):
            for i in range(0,n):
                scan_val = int(input())
                scan.append(scan_val)
            output = filter_object.update(scan)
            scan = []
            response = raw_input('Do you want to enter more data [y]?')
            if response == 'y':
                continue
            else:
                break

        print "Final output {0}".format(output)

    else:
        print "Invalid filter type provided."
        exit(1)


if __name__=="__main__":

    if len(sys.argv) < 2:
        print("Insufficient number of parameters.")
        exit(1)

    filter_type = sys.argv[1]
    n = None
    d = None

    if len(sys.argv) == 3:
        try:
            n = int(sys.argv[2])
        except TypeError:
            print "Invalid value for n or d"
            exit(1)
        run_filter(filter_type, n, d)
    elif len(sys.argv) == 4:
        try:
            n = int(sys.argv[2])
            d = int(sys.argv[3])
        except TypeError:
            print "Invalid value for n or d"
            exit(1)
        run_filter(filter_type, n, d)
