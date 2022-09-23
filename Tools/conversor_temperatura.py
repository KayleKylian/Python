Celsius = float(input('Informe a temperatura em °C: '))
Fahrenheit = float(input('Informe a temperatura em °F: '))
Kelvin = float(input('Informe a temperatura em K: '))
c_f = (Fahrenheit - 32) / 1.8
c_k = Celsius + 273.15
f_c = (Celsius * 1.8) + 32
f_k = (Fahrenheit + 459.67) / 1.8
k_c = Celsius - 273.15
k_f = (Kelvin * 1.8) - 459.67

print(f'A temperatura em Celsius {Celsius:.2f}°C convertido em Fahrenheit é: {f_c:.2f}°F.')
print(f'A temperatura em Celsius {Celsius:.2f}°C convertido em Kelvin é: {c_k:.2f}°K.')
print(f'A temperatura em Fahrenheit {Fahrenheit:.2f}°F convertido em Celsius é: {c_f:.2f}°C.')
print(f'A temperatura em Fahrenheit {Fahrenheit:.2f}°F convertido em Kelvin é: {f_k:.2f}K.')
print(f'A temperatura em Kelvin {Kelvin:.2f}K convertido em Celsius é: {k_c:.2f}°C.')
print(f'A temperatura em Kelvin {Kelvin:.2f}K convertido em Fahrenheit é: {k_f:.2f}°F.')
