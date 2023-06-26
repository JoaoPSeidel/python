velocidade = 90
local_carro = 102

RADAR_LIM = 60
LOCAL_RAD = 100
RADAR_RANGE = 1

overspeed = velocidade > RADAR_LIM

multa_area = local_carro >= (
    LOCAL_RAD - RADAR_RANGE) and local_carro <= (LOCAL_RAD + RADAR_RANGE)

multado = overspeed and multa_area

if overspeed:
    print('Carro passou do limite do radar')

if multa_area:
    print('Carro passou pela área do radar')

if multado:
    print('Carrou passou acima da velocidade no local do radar *MULTADO*')
