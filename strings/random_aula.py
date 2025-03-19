import random
#
# moeda = ['cara','coroa']
# # escolhe uma opcao aleatoria
# print(random.choice(moeda))
# # ------------------------------
# cartas = ['cartas A','Carta B','Carta C','# AS']
# print(random.shuffle(cartas))
# print(cartas)

opcoes = ['pedra','papel','tesoura']

contadorusuario = 0
contadorplayer2 = 0

while True:
    print("\nEscolha uma opção:")
    print("1 - PEDRA")
    print("2 - PAPEL")
    print("3 - TESOURA")
    print("0 - SAIR")

    player1 = int(input("Digite sua escolha: "))

    if player1 == 0:
        print("Jogo encerrado. Obrigado por jogar!")
        break
    if player1 < 1 or player1 > 3:
        print("Escolha inválida! Tente novamente.")
        continue  # Volta para o início do loop


    opcaojogador = opcoes[player1 - 1].upper()  # Ajustar índice
    playar2 = random.choice(opcoes)  # Escolha do adversário

    print(f"\nVocê escolheu: {opcaojogador}")
    print(f"Computador escolheu: {playar2}")

    # Verifica quem ganhou
    if opcaojogador == playar2:
        print("Empate!")
    elif (opcaojogador == "PEDRA" and playar2.upper() == "TESOURA") or  (opcaojogador == "PAPEL" and playar2.upper() == "PEDRA") or (opcaojogador == "TESOURA" and playar2.upper() == "PAPEL"):
        print("Você venceu! 🎉")
        contadorusuario += 1  # Incrementa pontos do usuário
    else:
        print("Você perdeu! 😢")
        contadorplayer2 += 1  # Incrementa pontos do computador

    print(f"Placar: Você {contadorusuario} x {contadorplayer2} Computador")



