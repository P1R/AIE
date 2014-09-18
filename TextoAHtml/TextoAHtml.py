#!/usr/bin/env python2 
import sys
from random import randrange

Help="ERROR - Wrong Parameters :(\n\t the way to do it is: TextoAHtml.py -i inputfile.txt -o outputfile.html"
Example="EXAMPLE- ./TextoAHtml.py -i prueba.txt -o prueba.html"
#   se crea una clase para las etiquetas html
class htm:
#   se agregan en el constructor las etiquetas
    def __init__(self):
        self.head="<html>\n<head>\n"
        self.title="<title>"
        self.titlend="</title>\n"
        self.body="</head>\n<body>\n"
        self.bodyend="</body>\n</html>"
#   se utilizan funciones get para regresar cadenas de etiquetas html
    def getHead(self):
        return self.head
    def getTitle(self):
        return self.title
    def getTitlend(self):
        return self.titlend
    def getBody(self):
        return self.body
    def getBodyend(self):
        return self.bodyend
    def HexRand(self):
        return "#%s" % "".join([hex(randrange(0, 255))[2:] for i in range(3)])

if __name__ == "__main__":
#   verificamos que existan los 5 argumentos
    if(len(sys.argv) == 5):
        print "Opening " + sys.argv[2]
        htmtags = htm()
#   Creamos Variable de tipo archivo en modo "universal newline" que da compatibilidad nombre de arg 2
#   Ademas de la variable  con el cuarto argumento que es el nombre a escribir en modo escritura
        InFile = open(sys.argv[2], 'U')
        OuFile = open(sys.argv[4], 'w')
#   Se agrega la cabecera de html y el titulo como la primer linea
        OuFile.writelines(htmtags.getHead())
        line=InFile.readline()
        OuFile.writelines((htmtags.getTitle(),line,htmtags.getTitlend()))
#   Se escribe la variable "line" en el archivo de salida
        OuFile.writelines(htmtags.getBody())
        OuFile.writelines(line)
        OuFile.writelines(htmtags.getBodyend())
        print htmtags.HexRand()
    else:
        print Help
        print Example
        #esta linea va en la parte donde no se encuentre la conicidencia en palabra con el fichero existente
        #print "el fichero",sys.argv[2],"no se encuentra"
