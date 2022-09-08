# Imprimiendo titulo
title = "Calculadora de IMC"
center = title.center(37)
print(center)
print()
#---------------- - DATOS PERSONALES - INICIO - --------------------

# pedir al usuario su nombre
name = input("Nombre: ").title()

# el bucle se repite hasta introducir un nombre
while name == '':
	name = input("Campo obligatorio. Intenta de nuevo: ").title()

# pedir apellido al usuario
surname = input('Apellido paterno: ').title()

# el bucle se repite hasta introducir un apellido
while surname == '':
	surname = input("Campo obligatorio. Intenta de nuevo: ").title()

# pedir segundo apellido al usuario
surname2 = input('Apellido materno: ').title()

# el bucle se repite hasta introducir un segundo apellido
while surname2 == '':
	surname2 = input("Campo obligatorio. Intenta de nuevo: ").title()

# pedir edad al usuario
age = int(input('Edad: '))

# el bucle se repite hasta introducir un numero mayor a 2 y menor a 99
while age< 2 or age > 99:
	age = int(input('Introduce una edad valida: '))

# pedir peso al usuario
weight = float(input('Peso (Kg): '))

# el bucle se repite si se introduce un numero negativo o superior a 600kg
while weight <20 or weight > 600:
	weight = int(input('Error. Intenta de nuevo: '))

# pedir estatura al usuario
height = float(input('Estatura (mts): '))

# el bucle se repite si se escribe un numero negativo o mayor a 3 (mts)
while height < 0 or height > 3:
	height = float(input('Introduce una altura valida en metros: '))

#----------------- - CALCULADORA - --------------------

# variable para calcular imc
imc = round(weight / height**2, 1)

# imprimiendo datos personales
print()
print(f'Nombre: {name} {surname} {surname2}')
print(f'Edad: {age}')
print(f'Estatura: {height} mts  -  Peso: {weight} Kg')
print(f'Indice de Masa Corporal: {imc}')

print()

# imprimiendo informacion de acuerdo al IMC obtenido
if imc < 18.5:
	print(f'Su IMC es {imc}, lo que indica que su peso está en la categoría \nde Bajo peso para adultos de su misma estatura')
elif imc == 18.5 or imc < 24.9:
	print(f'Su IMC es 20.4, lo que indica que su peso está en la categoría \nde peso saludable para adultos de su misma estatura.')
elif imc > 25 or imc < 29.9:
	print(f'Su IMC es {imc}, lo que indica que su peso está en la categoría \nde Sobrepeso para adultos de su misma estatura.')
elif imc > 30:
	print(f'Su IMC es {imc}, lo que indica que su peso está en la categoría \nde Obesidad para adultos de su misma estatura.')

