import random
import os

def obter_pontos(tentativas, nivel):
    if nivel == "facil":
        return 100 - (tentativas * 5)
    elif nivel == "medio":
        return 150 - (tentativas * 8)
    elif nivel == "dificil":
        return 200 - (tentativas * 10)
    else:
        return 0

def adivinhe_o_numero():
    pontuacao_maxima = carregar_pontuacao_maxima()

    print("Bem-vindo ao jogo Adivinhe o Número!")
    nome_jogador = input("Digite seu nome: ")

    nivel = input("Escolha o nível de dificuldade (facil, medio ou dificil): ").lower()
    while nivel not in ["facil", "medio", "dificil"]:
        nivel = input("Escolha um nível válido (facil, medio ou dificil): ").lower()

    minimo, maximo, max_tentativas = 1, 100, 10
    if nivel == "medio":
        minimo, maximo, max_tentativas = 1, 200, 15
    elif nivel == "dificil":
        minimo, maximo, max_tentativas = 1, 300, 20

    numero_secreto = random.randint(minimo, maximo)
    tentativas = 0
    historico = []

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1
        historico.append(palpite)

        if palpite == numero_secreto:
            pontos = obter_pontos(tentativas, nivel)
            print(f"Parabéns, {nome_jogador}! Você acertou em {tentativas} tentativa(s)!")
            print(f"Sua pontuação: {pontos} pontos.")
            if pontos > pontuacao_maxima:
                print("Nova pontuação máxima!")
                salvar_pontuacao_maxima(pontos)
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

        # Dicas numéricas
        if tentativas < max_tentativas:
            if abs(palpite - numero_secreto) <= 10:
                print("Está quente! Você está próximo do número secreto.")
            elif abs(palpite - numero_secreto) <= 20:
                print("Está morno! Você está perto do número secreto.")
            else:
                print("Está frio! Tente novamente.")

    if tentativas >= max_tentativas:
        print(f"Fim de jogo! O número secreto era {numero_secreto}.")
        pontos = obter_pontos(tentativas, nivel)
        print(f"Sua pontuação: {pontos} pontos.")

    print("Histórico de tentativas:")
    for idx, tentativa in enumerate(historico, start=1):
        print(f"Tentativa {idx}: {tentativa}")

    reiniciar = input("Deseja jogar novamente? (sim ou não): ").lower()
    if reiniciar == "sim":
        adivinhe_o_numero()
    else:
        print("Obrigado por jogar! Até a próxima.")

def carregar_pontuacao_maxima():
    if os.path.exists("pontuacao_maxima.txt"):
        with open("pontuacao_maxima.txt", "r") as arquivo:
            return int(arquivo.read())
    else:
        return 0

def salvar_pontuacao_maxima(pontos):
    with open("pontuacao_maxima.txt", "w") as arquivo:
        arquivo.write(str(pontos))

if __name__ == "__main__":
    adivinhe_o_numero()






