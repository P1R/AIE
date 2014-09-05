#!/usr/bin/env python2
import sys

Help="the way to used it is: TextoAHtml.py -i inputfile.txt -o outputfile.html"
if __name__ == "__main__":
    if (len(sys.argv)==5):
        print len(sys.argv)
        print "Abriendo " + sys.argv[2]
    else:
        print "el fichero",sys.argv[2],"no se encuentra"
        print Help
