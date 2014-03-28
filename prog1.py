import sys

PI = 3.14159265358979323846264338327950288


def aproximacion(n):
  suma = 0
  for i in range (1,n+1):
   b = ((i)/float(n))
   a = b-(1/float(n))
   xi = (i - 0.5)/float(n)
   fxi = (4/(1+xi**2))
   #print "xi %f " % (xi)
   #print "fxi %f " % (fxi)
   #print a
   #print b
   suma = suma + fxi
  pi = suma / float(n)
  #print "pi %.35f" % (pi)
  #print "El numero PI con 35 decimales es %.35f" % (PI)	
  return pi	

if __name__=="__main__":
 if(len(sys.argv)!=3):
  print "faltan los argumentos para el programa"
  n =10
  parametro2 =10
 else:
  n = int(sys.argv[1])
  parametro2 = int(sys.argv[2])
  
 if n>0:
  lista = []
  for i in range (0,parametro2):
   pi = aproximacion(n)
   lista.append(pi)
  print lista
 else:
  print "no se puede hacer el programa porque n no es mayor que 0"
 