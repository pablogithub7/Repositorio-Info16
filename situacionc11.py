var1 = input ("Ingrese el Nombre del Empleado ")
var2 = float (input ("Ingrese el Salario del empleado "))
print ("Indique por ''SI'' o ''NO'' si el empleado asisitio todo el mes")
X = input ("")
print ("Indique 1, 2 o 3 segun el rango de horario que trabajo el empleado")
print ("1: entre 3y 5 horas los domingos")
print ("2: entre 6y 10 horas los domingos")
print ("3: entre 3y 10 horas los domingos")
Y = int (input (" "))
if ( X == 'SI') and ( Y == 1):
    Var3 = float (Var2 * 0.03)
    Var2 = float (Var2 + Var3)
    print "El salario del empleado", Var1, " con su correspondiente adicional es de", Var2
elif (X == 'SI') and (Y == 2):
    Var3 = Var2 * 0.10
    Var2 = Var2 + Var3
    print "El salario del empleado", Var1, " con su correspondiente adicional es de", Var2
elif (X == 'NO') and (Y == 3):
    Var3 = Var2 * 0.02
    Var2 = Var2 + Var3
    print "El salario del empleado", Var1, " con su correspondiente adicional es de", Var2
else:
    print "Error los valores ingresados no son validos"