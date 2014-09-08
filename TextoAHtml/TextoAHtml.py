#!/usr/bin/env python2
import sys

Help="ERROR - Wrong Parameters :(\n the way to do it is: TextoAHtml.py -i inputfile.txt -o outputfile.html"
if __name__ == "__main__":
    if (len(sys.argv)==5):
        print len(sys.argv)
        print "Opening " + sys.argv[2]
    else:
        #esta linea va en la parte donde no se encuentre la conicidencia en palabra con el fichero existente
        #print "el fichero",sys.argv[2],"no se encuentra"
        print Help
