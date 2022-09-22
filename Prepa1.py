option=int(input('1. Circulo \n2.Cuadrado \n3. Triangulo \nIngrese el numero correspondiente a la figura: '))

if option == 1:
    radio = float(input('Ingrese el radio: '))
    print(f'El area del circulo es: {(3.14)*(radio)**(2)}')
elif option ==2 :
    lado = float(input('Ingrese el lado: '))
    print(f'El area del cuadrado es: {lado**2}')
elif option == 3:
    base = float(input('Ingrese la base: '))
    altura= float(input('Ingrese la altura: '))
    print(f'El area del traingulo es {(base*altura)/2}')
else:
    print('Error')
