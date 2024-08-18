import random
import zipfile
import pyzipper
import os
import time

def pausa(segundos):
    time.sleep(segundos)

def introducao():
    print("Você encontrou um convite misterioso para um jogo enigmático.")
    pausa(2)
    print("Ao aceitá-lo, você se depara com o Anfitrião, um hacker notório com muito tempo livre.")
    pausa(2)
    print("Ele já possui suas informações, mas precisa da sua aprovação pessoal para fazer o que mais gosta: manipular dados e resolver enigmas.")
    pausa(2)
    print("O jogo é simples: você e o Anfitrião apostam números em uma competição.")
    pausa(2)
    print("Seu objetivo é vencer ao máximo de rodadas possíveis para conseguir uma vantagem.")
    pausa(2)
    print("Você não pode deixar que o Anfitrião ganhe. Seus dados estão em jogo!")
    pausa(2)
    print("Prepare-se para um desafio onde sua inteligência e habilidade em apostas serão testadas ao máximo.")
    pausa(2)
    print("Boa sorte!\n")
    pausa(1)

def carta_ascii(numero):
    return f"""
+---------+
|    {numero}   |
|         |
|         |
+---------+
"""

def mensagem_vitoria():
    return """
 ____  ____  ____  ____ 
||V ||||I ||||T ||||O ||
||__||||__||||__||||__||
|/__/||/__/||/__/||/__/ 
    """

def mensagem_derrota():
    return """
 ____  ____  ____  ____ 
||L ||||O ||||S ||||E ||
||__||||__||||__||||__||
|/__/||/__/||/__/||/__/ 
    """

def criar_arquivo_zip(caminho_arquivo, senha):
    with pyzipper.AESZipFile(caminho_arquivo, 'w', compression=zipfile.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(senha.encode())
        zipf.writestr('dados.txt', (
            "Informações do Hacker:\n"
            "Nome: Anfitrião\n"
            "Idade: 32\n"
            "Ocupação: Hacker e Enigmista\n"
            "Especialidades: Criptografia, Engenharia Social, Quebra de Senhas\n"
            "Nota: O Anfitrião adora desafios e sempre busca maneiras de testar suas habilidades."
        ))

def gerar_numeros():
    return [random.randint(1, 10) for _ in range(5)]

def jogar_rodada(player_numeros, anfitriao_numeros):
    print("Seus números são:")
    for numero in player_numeros:
        print(carta_ascii(numero))

    aposta_player = int(input("Aposte um número de 1 a 10: "))
    aposta_anfitriao = random.choice(anfitriao_numeros)

    print(f"\nNúmero do anfitrião: {aposta_anfitriao}")
    print(carta_ascii(aposta_anfitriao))

    if aposta_player > aposta_anfitriao:
        return "player"
    elif aposta_player < aposta_anfitriao:
        return "anfitriao"
    else:
        return "empate"

def main():
    introducao()
    
    # Configuração inicial
    nome_jogador = input("Qual seu nome, desafiador?: ")
    print(f"\nMuito bem, {nome_jogador}! Estou ansioso para ver como você se sai.")
    pausa(1)
    senha_arquivo = 'senha123'
    
    # Caminho para o arquivo .zip na área de trabalho
    caminho_arquivo_zip = os.path.expanduser('~/Área de Trabalho/dadosDoAnfitriao.zip')

    # Criar o arquivo .zip com a senha
    criar_arquivo_zip(caminho_arquivo_zip, senha_arquivo)
    
    print(f"\nVamos começar o jogo, {nome_jogador}!")

    player_pontos = 0
    anfitriao_pontos = 0

    while player_pontos < 2 and anfitriao_pontos < 2:
        # Gerar números para o anfitrião
        anfitriao_numeros = gerar_numeros()

        resultado = jogar_rodada(gerar_numeros(), anfitriao_numeros)

        if resultado == "player":
            print("Você ganhou esta rodada! ᵖᵒʳ ᵉⁿᑫᵘᵃⁿᵗᵒ...")
            player_pontos += 1
        elif resultado == "anfitriao":
            print("O anfitrião ganhou esta rodada!")
            anfitriao_pontos += 1
        else:
            print("Empate ᑫᵘᵉ ᵖᵉⁿᵃ")

        print(f"\nPontuação atual - Você: {player_pontos} | Anfitrião: {anfitriao_pontos}")

        pausa(1)

    # Mensagens finais
    if player_pontos == 2:
        print(mensagem_vitoria())
        print("Você ganhou! Faça bom proveito dos meus dados.")
        print(f"A senha do arquivo é: {senha_arquivo}")
    else:
        print(mensagem_derrota())
        print("Foi um bom jogo. Acho que posso me divertir bastante com seus dados. Até a próxima!")

if __name__ == "__main__":
    main()
