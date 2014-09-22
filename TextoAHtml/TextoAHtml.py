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
        self.divend="</div>\n"
        self.br="<br>"
        self.fontend="</font>"
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
    def getBr(self):
        return self.br
#   generador de numero aleatorios para colores en formato html
    def HexRand(self):
        return "#%s" % "".join([hex(randrange(0, 255))[2:] for i in range(3)])
#   Agregador de etiquetas con llamando a la funcion para colores aleatorios en CSS
    def Divs(self):
        return "<div style='background-color:"+self.HexRand()+";'>"
    def getDivend(self):
        return self.divend
    def Fonts(self):
        return "<font color="+self.HexRand()+">"
    def getFontend(self):
        return self.fontend

if __name__ == "__main__":
#   verificamos que existan los 5 argumentos
    if(len(sys.argv) == 5):
        print "Opening " + sys.argv[2]
#   variable que detecta si estas dentro o fuera de un parrafo
        state = 0
        statef = 0
#   Agregamos contadores de parrafos y de palabras
        countp = 0
        countf = 0
        countw = 0
#creamos el objeto para las etiquetas en html
        htmtags = htm()
#   Creamos Variable de tipo archivo en modo "universal newline" que da compatibilidad nombre de arg 2
#   Ademas de la variable  con el cuarto argumento que es el nombre a escribir en modo escritura
        InFile = open(sys.argv[2], 'U')
        OuFile = open(sys.argv[4], 'w')
#   Se agrega la cabecera de html y el titulo como la primer linea
        OuFile.writelines(htmtags.getHead())
        line=InFile.readline()
        OuFile.writelines((htmtags.getTitle(),line,htmtags.getTitlend()))
        OuFile.writelines(htmtags.getBody())
        OuFile.writelines(line)

#   Inicio de ciclo hasta EOF
        while True:
            line=InFile.readline()
            if not line: break
#   verificamos si estamos dentro de parrafo y en dado caso agregamos div con color y letra
            if state == 1:
                if (line == "\n"):
                    OuFile.writelines(htmtags.getDivend())
                    state=0
#   verificamos si se salio del parrafo y cerramos el div
            if state == 0:  
                if (line == "\n"):
                    OuFile.writelines(htmtags.Divs())
                    state=1
                    countp+=1
#   si ecuentra salto de linea ingresa codigo <br> en html
            if (line == '\n'):
                OuFile.writelines(htmtags.getBr())
#   Agregamos seccion donde detecta y colorea oraciones
#            if (line.find(". ")!=-1):
#                if(countf!=0):
#                    OuFile.writelines(htmtags.getFontend())
#                OuFile.writelines(htmtags.Fonts())
#                countf+=1
#   cuenta palabras
            countw+=len(line.split())
            line=line.split()
            for i in range(len(line)):
                if (line[i].find(".")!=-1):
                    line.insert(i+1,htmtags.getFontend())
                    line.insert(i+2,htmtags.Fonts())
                    countf+=1
                    
            line = " ".join(line)
            OuFile.writelines(line)
        OuFile.writelines(("</div><br><h2> numero de parrafos es:",str(countp+1),"</h2>"))
        OuFile.writelines(("<br><h2> numero de palabras es:",str(countw),"</h2>"))
        OuFile.writelines(("<br><h2> numero de frases es:",str(countf),"</h2>"))
        OuFile.writelines(htmtags.getBodyend())
    else:
        print Help
        print Example
        #esta linea va en la parte donde no se encuentre la conicidencia en palabra con el fichero existente
        #print "el fichero",sys.argv[2],"no se encuentra"
