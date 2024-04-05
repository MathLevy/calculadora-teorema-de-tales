print("\nInício do cálculo.\n\n\nPara o cálculo não dar errado, todos os valores devem ser proporcionais\n\n\nParte 1:\n\nDigite x no valor de uma das letras para descobrir o valor da primeira incógnita. Nas demais letras que sobraram digite números.\n")

a1 = input("Digite o valor de a1: ")
b1 = input("Digite o valor de b1: ")
c1 = input("Digite o valor de c1: ")
d1 = input("Digite o valor de d1: ")

incognita_x = "x"

quantidade_incognita_x = 0

if a1 == incognita_x:
    quantidade_incognita_x += 1
if b1 == incognita_x:
    quantidade_incognita_x += 1
if c1 == incognita_x:
    quantidade_incognita_x += 1
if d1 == incognita_x:
    quantidade_incognita_x += 1

if quantidade_incognita_x == 1:
    possivel1 = "então é possível continuar o cálculo."
    print("\nA quantidade de vezes que a incógnita x aparece é: ",
          quantidade_incognita_x, ", ", possivel1)

elif quantidade_incognita_x > 1:
    impossivel1 = "então não é possível continuar o cálculo."
    print("\nA quantidade de vezes que a incógnita x aparece é: ",
          quantidade_incognita_x, ", ", impossivel1)
    print("\nFim do programa 1.\n\n")

if a1 == incognita_x:
    a1 = (float(b1) * float(c1)) / float(d1)
    print("\nResultado da incógnita x = ", a1)
    print()

elif b1 == incognita_x:
    b1 = (float(a1) * float(d1)) / float(c1)
    print("\nResultado da incógnita x = ", b1)
    print()

elif c1 == incognita_x:
    c1 = (float(a1) * float(d1)) / float(b1)
    print("\nResultado da incógnita x = ", c1)
    print()

elif d1 == incognita_x:
    d1 = (float(b1) * float(c1)) / float(a1)
    print("\nResultado da incógnita x = ", d1)
    print()

else:
    incognita_x == 0
    print("\nNão existe nenhuma incógnita x, então não é possível continuar o cálculo.\n")

print("\nFim do programa 1.\n\n\nParte 2:\n\nAgora vamos descobrir o valor da incógnita y.\nO mesmo valor de A e C da incógnita x deve ser atribuído ao A e C da incógnita y para descobrir seu resultado\nprecisamente sem dar nenhum erro, caso contrário o resultado será errado.\nA incógnita da variável de x deve estar posicionada na mesma linha que armazena a variável de y para dar certo o cálculo.\nExemplo: incógnita de x está na linha b1, então incógnita de y deve estar na linha b2.\n")

a2 = input("Digite o valor de a2: ")
b2 = input("Digite o valor de b2: ")
c2 = input("Digite o valor de c2: ")
d2 = input("Digite o valor de d2: ")

incognita_y = "y"

quantidade_incognita_y = 0

if a2 == incognita_y:
    quantidade_incognita_y += 1
if b2 == incognita_y:
    quantidade_incognita_y += 1
if c2 == incognita_y:
    quantidade_incognita_y += 1
if d2 == incognita_y:
    quantidade_incognita_y += 1

if quantidade_incognita_y == 1:
    possivel2 = "então é possível continuar o cálculo."
    print("\nA quantidade de vezes que a incógnita final aparece é: ",
          quantidade_incognita_y, ", ", possivel2)

elif quantidade_incognita_y > 1:
    impossivel2 = "então não é possível continuar o cálculo."
    print("\nA quantidade de vezes que a incógnita y aparece é: ",
          quantidade_incognita_y, ", ", impossivel2)
    print("\nFim do programa 2.\n\n")

if a2 == incognita_y:
    a2 = (float(b2) * float(c2)) / float(d2)
    print("\nResultado da incógnita y = ", a2)
    print()

elif b2 == incognita_y:
    b2 = (float(a2) * float(d2)) / float(c2)
    print("\nResultado da incógnita y = ", b2)
    print()

elif c2 == incognita_y:
    c2 = (float(a2) * float(d2)) / float(b2)
    print("\nResultado da incógnita y = ", c2)
    print()

elif d2 == incognita_y:
    d2 = (float(b2) * float(c2)) / float(a2)
    print("\nResultado da incógnita y = ", d2)
    print()

else:
    incognita_y == 0
    print("\nNão existe nenhuma incógnita y, então não é possível continuar o cálculo.")

print("\nFim do programa 2.\n\n\nTirando a prova dos resultados para ver se foi calculado tudo corretamente:\n")

soma_segmentoXeY = b1 + b2
print("O resultado do segmento x + y é = ", soma_segmentoXeY)

valor1 = float(d1)
valor2 = float(d2)
soma = valor1 + valor2
print("O resultado do segmento d1 + d2 é = ", soma)

print("\nSe o resultado dos valores acima baterem, parabéns, você acertou tudo.\nCaso contrário terá que refazer todo o exercício, boa sorte.\n\n\nFIM DO CÁLCULO TEOREMA DE TALES!\n\n")
