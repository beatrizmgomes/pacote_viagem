# Viagem
# A empresa ofertará descontos progressivos na compra de pacotes dependendo do nº de viajantes que estão no mesmo
# grupo E moram na mesma residência.

# Criar algoritmo que receba o VALOR BRUTO do pacote, CATEGORIA DOS ASSENTOS e QUANTIDADE DE VIAJANTES que moram em
# uma mesma casa E calcule os descontos de acordo.
vbruto = float(input("Bora viajar? Insira o valor do pacote:R$ "))
categoria = int(input("Agora informe a categoria dos assentos, por gentileza: (1) Econômica; (2) Executiva; "
                      "(3) Primeira Classe."))
viajantes = float(input("Por fim, informe a quantidade de viajantes (que morem juntos): "))

if categoria == 1 and viajantes == 2:
    vdesconto = vbruto * 0.97
    print("Você adquiriu 3% OFF, totalizando R${:.2f}".format(vdesconto))  # tudo certo até aqui
elif categoria == 1 and viajantes == 3:
    vdesconto = vbruto * 0.96
    print("Você adquiriu 4% OFF, totalizando R${:.2f}".format(vdesconto))
elif categoria == 1 and viajantes >= 4:
    vdesconto = vbruto * 0.95
    print("Você adquiriu 5% OFF, totalizando R${:.2f}".format(vdesconto))
#############################################################################
elif categoria == 2 and viajantes == 2:
    vdesconto = vbruto * 0.95
    print("Você adquiriu 5% OFF, totalizando R${:.2f}".format(vdesconto))
elif categoria == 2 and viajantes == 3:
    vdesconto = vbruto * 0.93
    print("Você adquiriu 7% OFF, totalizando R${:.2f}".format(vdesconto))
elif categoria == 2 and viajantes >= 4:
    vdesconto = vbruto * 0.92
    print("Você adquiriu 8% OFF, totalizando R${:.2f}".format(vdesconto))
#############################################################################
elif categoria == 3 and viajantes == 2:
    vdesconto = vbruto * 0.90
    print("Você adquiriu 10% OFF, totalizando R${:.2f}".format(vdesconto))
elif categoria == 3 and viajantes == 3:
    vdesconto = vbruto * 0.85
    print("Você adquiriu 15% OFF, totalizando R${:.2f}".format(vdesconto))
else:
    vdesconto = vbruto * 0.80
    print("Você adquiriu 20% OFF, totalizando R${:.2f}".format(vdesconto))
