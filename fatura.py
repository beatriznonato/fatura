repetir = 's'
fatura = []
total = 0
validPreco = False

while repetir == 's':
    produto = input('Digite o nome do produto: ')

    while validPreco == False:
        preco = input('Digite o preço do produto: ')
        try:
             preco = float(preco)
             
             if preco <= 0:
                print('O preço precisar ser maior do que zero')
             else:
                  validPreco = True
             
        except:
             print("Formato de preço inválido. Use apenas números e separe os centavos '.'.")
             

    fatura.append([produto,preco])
    total += preco
    validPreco = False
    repetir = input('Deseja comprar mais algum produto? (S para sim, N para não) ').lower()

for i in fatura:
    print(i[0],'-',i[1])

print('O total da fatura é:',total)
