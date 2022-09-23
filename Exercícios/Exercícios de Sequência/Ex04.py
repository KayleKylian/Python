tFah = float(input('Digite a temperatura em Fahrenheit: '))
tCel = float(input('Digite a temperatura em Celsius: '))
convC = (tFah - 32) * 5/9
convF = (tCel * 9 / 5) + 32

print(f'A temperatura em Fahrenheit {tFah:.2f}°F convertida em Celsius é {convC:.2f}°C.')
print(f'A temperatura em Celsius {tCel:.2f}°C convertida em Fahrenheit é {convF:.2f}°F.')
