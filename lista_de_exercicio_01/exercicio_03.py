MB = float(input("Digite o tamanho do arquivo em MB para download:"))
Mbps = float(input("Digite a velociadade da sua internet por Mbps:"))

megabits = MB * 8
tempo_segundos = megabits/Mbps

tempo_min = tempo_segundos/60

print(f"o tempo aproximado de downdload do aquivo é:{tempo_min:.2f} minutos")

