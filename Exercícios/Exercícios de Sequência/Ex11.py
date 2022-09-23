tamanho = float(input('Digite o tamanho do arquivo (em MB): '))
velocidade = float(input('Digite a velocidade de sua conexão com a internet (em Mbps): '))
download = tamanho / (velocidade / 8)

print(f'O arquivo de tamanho {int(tamanho)} com uma velocidade de {int(velocidade)}'
      f' Mbps pode ser baixado em {int(download)} segundos.')
