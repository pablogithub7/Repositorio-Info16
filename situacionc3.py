a = int (input ("Ingrese el primer numero: "))
b = int (input ("Ingrese el segundo numero: "))
c = int (input ("Ingrese el tercer numero: "))
"""if a > b and b > c:
	print "Los numeros en forma ascendente quedan de la siguiente manera: ", a, " , ", b, " y ", c 
	
	
elif a > b and b < c:
	print "Los numeros en forma ascendente quedan de la siguiente manera: ", a, " , ", c, " y ", b                                                             
	
if b > a and a > c:
	print "Los numeros en forma ascendente quedan de la siguiente manera: ", b, " , ", a, " y ", c
	
	
	
elif b > a and a < c:
	print "Los numeros en forma ascendente quedan de la siguiente manera: ", b, " , ", c, " y ", a 
	
	
if c > a and a > b:
	print "Los numeros en forma ascendente quedan de la siguiente manera: ", c, " , ", a, " y ", b 
	
	
elif c > a and a < b:
	print "Los numeros en forma ascendente quedan de la siguiente manera: ", c, " , ", b, " y ", a """
	

if a > b and a > c:
	mayor = a
elif b > a and b > c:
	mayor = b
else:
	mayor = c

if a < b and a < c:
	menor = a
elif b < a and b < c:
	menor = b
else:
	menor = c

medio = (a+b+c) - (mayor + menor)

print "En orden ascendente queda asi: ", mayor, " ,", medio, " y ", menor

