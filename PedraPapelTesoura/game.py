from random import choice

comp_vitorias = 0
jogador_vitorias = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    if esc_jogador in ["Pedra", "PEDRA","pedra"]:
        esc_jogador = "pedra"
    elif esc_jogador in ["Papel", "PAPEL","papel"]:
        esc_jogador = "papel"
    elif esc_jogador in ["Tesoura", "TESOURA","tesoura"]:
        esc_jogador = "tesoura"
    else:
        print("Opcao invalida. Tente novamente!!")
        esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    return esc_jogador

def Opcao_Computador():
    esc_computador = choice(["pedra","papel","tesoura"])
    return esc_computador

while True:

    print("-----------------------")
    esc_computador = Opcao_Computador()
    esc_jogador = Opcao_Jogador()
    print("-----------------------")
      
    if (esc_jogador == "papel") and (esc_computador == "pedra") or (esc_jogador == "pedra") and (esc_computador == "tesoura") or (esc_jogador == "tesoura") and (esc_computador == "papel"):
        print(f"A escolha do jogador foi {esc_jogador} e a escolha do computador foi {esc_computador}. O JOGADOR VENCEU")
        jogador_vitorias += 1
    elif esc_computador == esc_jogador:
        print(f"A escolha do jogador foi {esc_jogador} e a escolha do computador foi {esc_computador}. EMPATE")
    else:
        print(f"A escolha do jogador foi {esc_jogador} e a escolha do computador foi {esc_computador}. O COMPUTADOR VENCEU")
        comp_vitorias += 1
    
    print("-----------------------")

    print(f"Vitórias do jogador: {jogador_vitorias}")
    print(f"Vitórias do compurador: {comp_vitorias}")

    print("-----------------------")

    esc_jogador = input("Voce deseja jogar novamente? (s/n): ")
    if esc_jogador in ["SIM","Sim","sim","S","s"]:
        pass
    elif esc_jogador in ["NAO","Nao","nao","N","n"]:
        break
    else:
        break





        
        
        