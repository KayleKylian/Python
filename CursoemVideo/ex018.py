from math import sin, cos, tan, radians
angulo = int(input('Informe o ângulo: '))
angrad = radians(angulo)
sen = sin(angrad)
cs = cos(angrad)
tang = tan(angrad)

print(f'O ângulo de {angulo}° tem o seno de: {sen:.2f}, o cosseno de: {cs:.2f} e a tangente de {tang:.2f}.')
