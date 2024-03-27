compra = float(input('Digite o valor da compra')) 

if compra >= 0.01 and 9.99:
    print('sem desconto', compra)
elif compra >= 100.00 and 499.99:
    valorTotal = 0.10*compra
    desconto = compra - valorTotal
    print('10 porcento de desconto', desconto, valorTotal)
elif compra >= 500.00:
    valorTotal = 0.15*compra
    desconto = compra - valorTotal
    print('15 porcento de desconto', desconto, valorTotal)
