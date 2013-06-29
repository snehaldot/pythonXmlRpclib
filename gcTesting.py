import gc,sys

def make_cycle():
    l = {}
    l[0] = l 

def main():
    collected = gc.collect()
    print "\n\n Garbage collected %d objects." % (collected)
    print "creating cycles..."
    for i in range(10):
        make_cycle()
    collected = gc.collect()
    print " \n\n Garbage collector : collected %d objects.\n" % (collected)

if __name__ == "__main__":
    ret = main()
    sys.exit(ret) 

