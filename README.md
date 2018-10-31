# Aplicação

Criar um programa para registrar uma venda. O programa vai receber do usuário o nome do produto e o preço e vai adicioná-lo à fatura.
Em seguida, perguntar ao usuário se ele quer comprar mais algum produto.

Se a resposta for 's' repetir a operação. Só parar quando a resposta for 'n' e então imprimir a fatura, que deve conter os produtos e os preços. Ao final, apresentar total da fatura.

```
Dica: Considere que só é possivel comprar uma unidade de cada produto por vez.
```

<h1> Estrutura de While e For </h1>

<h4> loop for com range </h4>

```
for i in range(0,10):
    print(10-i)
```

<h4> loop for aninhado </h4>

```
shopping = [['rice','bean','pasta'],['meat','chicken','fish'],['milk','yogurt']]

for i in shopping:
    for item in i:
        print(item)
```

<h4> loop for com dict </h4>

```
colors = {'verde':'green', 'preto':'black', 'azul':'blue'}

for i in colors:
    print(i, ':',colors[i])
```

<h4> loop for com somatório </h4>

```
sales = [1000,450,300,920,600]

total = 0

for i in sales:
    total += i
    print(total)
```

<h4> loop for com lists e strings </h4>

```
shopping = ['rice','bean','pasta','meat']
name = 'joaquim'

for i in name:
    print(i)
```

<h4> While </h4>

```
x = 0
people = 1

while x < 4:
    name = input('What's your name? ')
    ## nome joão não deve ser adicinado á lista
    if name == 'joão':
        break
    people.append(name)
    x += 1
print(people)
```
