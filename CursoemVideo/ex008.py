metro = int(input('Digite um valor em metro: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f'{metro} metros em decimetros vale {dm}, centímetros vale {cm}, e em milímetros vale {mm}.'
      f'Já em km vale {km}, em hectômetro {hm} e em decâmetro {dam}.')