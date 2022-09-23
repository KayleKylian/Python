lista = []

for item in range(1, 101):
    if item <= 1:
        continue
    elif item in [2, 3, 5, 7]:
        lista.append(item)
    
    if (item % 2) == 0 or (item % 3) == 0:
        continue
    elif (item % 5) == 0 or (item % 7) == 0:
        continue
    else:
        lista.append(item)

print(lista)