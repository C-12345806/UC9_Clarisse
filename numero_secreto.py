import random
numero_secreto = random.randint(1, 1000)
print(numero_secreto)
num_tentativas = 0
print("Bem-Vindo ao jogo de adivinhação!\nTente adivinhar um número entre 1 e 1000;")
while True:
    palpite = int (input("\nDigite seu número: "))
    print(type(palpite))
    num_tentativas =+1
    if(palpite == numero_secreto):
        print("👏👏👏👏👏👏👏👏👏👏👏👏👏👏")
        break
    elif (palpite <  numero_secreto):
        print("O número secreto é maior!")  
    else:
        print("O número secreto é menor!")    
