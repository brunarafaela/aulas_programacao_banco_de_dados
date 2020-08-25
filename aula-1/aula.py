nota = int (input ('Digite uma nota'))

if nota >= 6:
    pass
    print("Aprovado")
else:
    print("Reprovado") 


if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("C")
else:
    print("R")

letra = input ("Digite uma letra")

vogais = 'aeiou'

if letra in vogais:
    print("Vc digitou uma vogal")
else:
    print("Vc digitou uma consoante")


for i in range (0, 3):
    print(i)

for i in range(3, 10, 2):
    print(i)    

for i in range (0, 10):
    print(i)
    if i == 5:
        break



for i in range (0, 10):
    if i == 5:
        continue
    print(i)



for i in range(1, 10):
    print(i)
    if i % 3 == 0:
        break
else:
    print("Saindo do for. Valor de i: " + str())   


for i in range(1, 10):
    print(i)
else:
    print("Saindo do for. Valor de i: " + str())

nota = int(input("Digite uma nota"))
while nota != -1:
    if nota >= 6:
        print("Vc está aprovado")
    else:
        print("Vc está reprovado")
    nota = int(input("Digite uma nota"))
else:
    print("Até mais")    