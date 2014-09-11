#!/usr/bin/env python2 
import sys

Help="ERROR - Wrong Parameters :(\n the way to do it is: TextoAHtml.py -i inputfile.txt -o outputfile.html"
Example="./TextoAHtml.py -i prueba.txt -o prueba.html"
if __name__ == "__main__":
#   verificamos que existan los 5 argumentos
    if(len(sys.argv) == 5):
        print "Opening " + sys.argv[2]
#   Creamos Variable de tipo archivo en modo "universal newline" que da compatibilidad nombre de arg 2
#   Ademas de la variable  con el cuarto argumento que es el nombre a escribir en modo escritura
        InFile = open(sys.argv[2], 'U')
        OuFile = open(sys.argv[4], 'w')
#   Se lee una linea de archivo de entrada y se almacena en variable "line"
        line=InFile.readline()
#   Se escribe la variable "line" en el archivo de salida
        OuFile.writelines(line)
    else:
        print Help
        print Example
        #esta linea va en la parte donde no se encuentre la conicidencia en palabra con el fichero existente
        #print "el fichero",sys.argv[2],"no se encuentra"

